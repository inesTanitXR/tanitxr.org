#!/usr/bin/env python3
"""Static site generator for tanitxr.org — replaces the WordPress/Elementor/JetEngine site.

Edit content in this file, then run:  python3 build.py
Output goes to docs/ (GitHub Pages serves main:/docs).

Data sources (scraped from the old WordPress site 2026-09-08):
  wp-data/*.json  — posts, pages, people, opportunities, media, terms
  media/          — downloaded media library (web-sized)
  profiles/       — volunteer profile submissions (JSON), merged into Our People
"""
import json
import os
import posixpath
import re
import shutil
import subprocess
import unicodedata
import urllib.request
import html as htmod

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "docs")
IMG_OUT = os.path.join(DOCS, "assets", "img")
PDF_OUT = os.path.join(DOCS, "assets", "pdf")
MEDIA = os.path.join(HERE, "media")
MEDIA_EXTRA = os.path.join(HERE, "media", "extra")

SITE_NAME = "TANIT XR"
TAGLINE = "Preserving Tunisia's endangered heritage in 3D, AR and VR"
EMAIL = "info@tanitxr.org"
PHONE = "+1 407-562-7793"
DONATE_URL = "https://donors.tuesday.app/campaign/FIHKI"
DONATE_URL_SUPPORT = "https://donors.tuesday.app/campaign/FIHKI"
VOLUNTEER_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSegO7smO5VyQSpSSaamKni4RPD4q_yDytd5TCK3jOH6LTML6w/viewform"
INSTAGRAM = "https://www.instagram.com/tanitxr/"
LINKEDIN = "https://www.linkedin.com/company/tanit-xr/"
SKETCHFAB = "https://sketchfab.com/TanitXR"
FORM_ENDPOINT = "https://formsubmit.co/" + EMAIL
# Profile submissions: FormSubmit (email) by default. After deploying the Cloudflare
# worker (see worker/README.md), set this to the worker URL for instant publishing.
PROFILE_ENDPOINT = FORM_ENDPOINT

# Opportunities board extras
# The featured listing is configured in ref/opportunity_updates.json ("featured": {slug: photo});
# the weekly board-check task curates it. If the configured item has closed, the build
# auto-picks the best open one. Photos fall back by type to these images:
# impact numbers (ref/stats.json, refreshed by the weekly task)
_stats = json.load(open(os.path.join(HERE, "ref", "stats.json")))

def stat(key):
    """Render a stat as an animated count-up target, floored to a friendly number."""
    n = _stats[key]
    if n >= 1000:
        disp, suffix = n // 1000, "k+"
    else:
        disp, suffix = (n // 5) * 5 if n >= 20 else n, "+"
    return f'<span class="cnt" data-n="{disp}" data-s="{suffix}">{disp}{suffix}</span>'


FEATURED_DEFAULT_PHOTOS = {
    "Open Call": "e55b902d5e35430eb6bc4b1d4d477134.jpeg",
    "Award": "e55b902d5e35430eb6bc4b1d4d477134.jpeg",
    "Grant": "acd421bb938b40a798640f0895cb290d.jpeg",
    "Residency": "ac789b797d4e4528aab59e898676a6f3.jpeg",
    "_default": "el-jem.jpg",
}
# Cloudflare worker URL for reactions/click/view counting (see worker/README.md).
# Empty = reactions and counters stay hidden.
REACTIONS_ENDPOINT = ""

# languages: English at the root, French under fr/, Arabic (RTL) under ar/
LANG = "en"
LANG_DIRS = {"en": "", "fr": "fr/", "ar": "ar/"}
LANG_NAMES = {"en": "EN", "fr": "FR", "ar": "ع"}
SITEMAP = []  # pretty page paths collected while building

# ---------------------------------------------------------------- utilities

def fix_mojibake(s):
    """Old site stored UTF-8 read as Mac Roman ('‚Äì' etc.). Undo where possible."""
    if not s:
        return s
    repl = {
        "‚Äì": "–", "‚Äì": "–", "‚Äî": "—", "‚Ä¶": "…",
        "‚Äú": "“", "‚Äù": "”", "‚Äô": "’", "‚Äò": "‘",
        "Salammb√´": "Salammbô", "Salammb‚àö¬¥": "Salammbô",
        " ‚ ": " – ",
    }
    for k, v in repl.items():
        s = s.replace(k, v)
    if any(ch in s for ch in ("‚", "Ä", "√", "‚àö")):
        try:
            s = s.encode("mac_roman").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    return s


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:60]


def esc(s):
    return htmod.escape(s or "", quote=True)


def load(name):
    with open(os.path.join(HERE, "wp-data", name)) as f:
        return json.load(f)


# ---------------------------------------------------------------- images

_media_files = {}
for fn in os.listdir(MEDIA):
    _media_files[fn.lower()] = os.path.join(MEDIA, fn)
for _sub in ("extra", "drive"):
    _d = os.path.join(MEDIA, _sub)
    if os.path.isdir(_d):
        for fn in os.listdir(_d):
            _media_files.setdefault(fn.lower(), os.path.join(_d, fn))

_img_cache = {}

# basenames that exist more than once in the old media library (flat downloads clobbered
# each other) — for these, a dated copy is fetched from the exact URL instead
_dupe_names = set()
_seen_names = set()
for _m in json.load(open(os.path.join(HERE, "wp-data", "media.json"))):
    _b = os.path.basename(_m.get("source_url", "")).lower()
    (_dupe_names if _b in _seen_names else _seen_names).add(_b)


def _source_for(url):
    """Local file for a wp-content URL (downloads once into media/extra if missing)."""
    base = os.path.basename(url.split("?")[0])
    dated = re.search(r"/uploads/(\d{4})/(\d{2})/([^/?]+)$", url.split("?")[0])
    if dated and dated.group(3).lower() in _dupe_names:
        base = f"{dated.group(1)}-{dated.group(2)}-{dated.group(3)}"
    if base.lower() in _media_files:
        return _media_files[base.lower()]
    os.makedirs(MEDIA_EXTRA, exist_ok=True)
    dest = os.path.join(MEDIA_EXTRA, base)
    if not os.path.exists(dest):
        clean = url.replace("&amp;", "&")
        if clean.startswith("https://i0.wp.com/"):
            clean = "https://" + clean[len("https://i0.wp.com/"):].split("?")[0]
        print(f"  fetching missing image {base}")
        req = urllib.request.Request(clean, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
            f.write(r.read())
    _media_files[base.lower()] = dest
    return dest


def img(url_or_name, max_px=1600, as_jpeg=None, quality=72):
    """Process an image into docs/assets/img, return relative site path."""
    key = (url_or_name, max_px, as_jpeg)
    if key in _img_cache:
        return _img_cache[key]
    src = _source_for(url_or_name)
    base = os.path.basename(src)
    stem, ext = os.path.splitext(base)
    ext = ext.lower()
    if as_jpeg is None:
        as_jpeg = ext in (".jpg", ".jpeg", ".webp")
    out_ext = ".jpg" if as_jpeg else (ext if ext in (".png", ".svg", ".gif") else ".jpg")
    out_name = f"{slugify(stem)}-{max_px}{out_ext}"
    out_path = os.path.join(IMG_OUT, out_name)
    rel = f"assets/img/{out_name}"
    if not os.path.exists(out_path):
        if ext == ".svg":
            shutil.copy(src, out_path)
        else:
            cmd = ["sips", "-Z", str(max_px)]
            if as_jpeg:
                cmd += ["-s", "format", "jpeg", "-s", "formatOptions", str(quality)]
            cmd += [src, "--out", out_path]
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode != 0:
                print(f"  !! sips failed for {base}: {r.stderr.strip()[:120]}")
                shutil.copy(src, out_path)
    _img_cache[key] = rel
    return rel


# ---------------------------------------------------------------- css

CSS = """
:root{
  --gold:#ffcd05; --gold-dark:#f7b500; --ink:#111518; --ink-soft:#1b2126;
  --gray:#687279; --mist:#edeff2; --cloud:#f9fafb; --paper:#ffffff;
  --serif:'Yeseva One',Georgia,serif; --sans:'Roboto',-apple-system,'Helvetica Neue',Arial,sans-serif;
  --slab:'Roboto Slab',Georgia,serif;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:var(--sans);color:var(--ink);background:var(--paper);line-height:1.7;font-size:17px}
img{max-width:100%;height:auto;display:block}
a{color:inherit}
h1,h2,h3{font-family:var(--serif);font-weight:400;line-height:1.15}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.btn{display:inline-block;padding:13px 30px;border-radius:4px;font-family:var(--sans);font-weight:500;
  font-size:15px;text-decoration:none;letter-spacing:.02em;transition:.2s;border:none;cursor:pointer}
.btn-gold{background:var(--gold);color:var(--ink)}
.btn-gold:hover{background:var(--gold-dark)}
.btn-dark{background:var(--ink-soft);color:#fff;border:1px solid #3a4249}
.btn-dark:hover{background:#2a3138}
.btn-line{background:transparent;color:var(--ink);border:2px solid var(--ink)}
.btn-line:hover{background:var(--ink);color:#fff}
.btn-line-light{background:transparent;color:#fff;border:2px solid rgba(255,255,255,.7)}
.btn-line-light:hover{background:#fff;color:var(--ink)}
.eyebrow{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-dark);font-weight:700;margin-bottom:14px}
.center{text-align:center}

/* header — nav split around a centered logo, like the original site */
header.site{position:fixed;top:0;left:0;right:0;z-index:60;transition:background .25s,box-shadow .25s;padding:0}
header.site .bar{position:relative;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;
  gap:26px;padding:10px 28px}
header.site .logo{display:flex;justify-content:center;text-decoration:none}
header.site .logo img{height:64px;width:auto;transition:height .25s}
header.site.scrolled .logo img,header.site.solid .logo img{height:52px}
.hside{display:flex;align-items:center;gap:26px;width:100%}
.hl{justify-content:space-between}
.hr{justify-content:space-between}
.hcta{display:flex;align-items:center;gap:16px}
.hlinks{display:flex;align-items:center;gap:34px}
.hlinks a{color:rgba(255,255,255,.92);text-decoration:none;font-size:16px;font-weight:500;white-space:nowrap}
.hlinks a:hover,.hlinks a.on{color:var(--gold)}
header.site .socials{display:flex;gap:12px}
header.site .socials a{color:rgba(255,255,255,.8)}
header.site .socials svg{width:17px;height:17px;fill:currentColor}
header.site .donate{background:var(--gold);color:var(--ink)!important;padding:9px 20px;border-radius:4px;
  font-weight:700;text-decoration:none;font-size:15px;white-space:nowrap}
header.site .donate:hover{background:var(--gold-dark);color:var(--ink)}
header.site.solid,header.site.scrolled{background:#fff;box-shadow:0 1px 14px rgba(17,21,24,.09)}
header.site.solid .hlinks a,header.site.scrolled .hlinks a{color:var(--ink)}
header.site.solid .hlinks a:hover,header.site.scrolled .hlinks a:hover,
header.site.solid .hlinks a.on,header.site.scrolled .hlinks a.on{color:var(--gold-dark)}
header.site.solid .socials a,header.site.scrolled .socials a{color:var(--gray)}
@media(max-width:1470px){header.site .socials{display:none}}
#mobnav{display:none}
.drop{position:relative}
.drop>a::after{content:" ▾";font-size:11px}
.drop .menu{position:absolute;top:100%;left:-14px;background:#fff;min-width:250px;border-radius:6px;
  box-shadow:0 10px 34px rgba(17,21,24,.16);padding:10px 0;display:none}
.drop:hover .menu,.drop:focus-within .menu{display:block}
.drop .menu a{display:block;padding:9px 20px;color:var(--ink)!important;font-size:14.5px}
.drop .menu a:hover{background:var(--cloud);color:var(--gold-dark)!important}
.langs{display:flex;gap:4px;font-size:12.5px;font-weight:700;align-items:center}
.langs a{color:inherit;text-decoration:none;opacity:.75;padding:3px 7px;border-radius:4px}
.langs a:hover{opacity:1}
.langs a.on{background:var(--gold);color:var(--ink)!important;opacity:1}
header.site.solid .langs a,header.site.scrolled .langs a{color:var(--ink)}
[dir=rtl] .quote{border-left:none;border-right:4px solid var(--gold)}
[dir=rtl] .drop .menu{left:auto;right:-14px}
[dir=rtl] .faq summary::after{right:auto;left:22px}
[dir=rtl] .page-hero .crumb a{margin-left:0}
#nav-toggle{display:none;background:none;border:none;cursor:pointer;padding:6px}
#nav-toggle span{display:block;width:24px;height:2px;margin:5px 0;background:#fff;transition:.2s}
header.site.solid #nav-toggle span,header.site.scrolled #nav-toggle span{background:var(--ink)}
@media(max-width:1120px){
  .hside{display:none}
  header.site .bar{grid-template-columns:auto 1fr auto;padding:10px 18px}
  header.site .logo{justify-content:flex-start}
  header.site .logo img{height:50px}
  #mobnav{display:flex;position:fixed;top:0;right:-320px;width:300px;height:100vh;background:var(--ink);
    flex-direction:column;align-items:flex-start;padding:80px 30px 30px;gap:4px;transition:right .25s;overflow-y:auto}
  #mobnav.open{right:0}
  [dir=rtl] #mobnav{right:auto;left:-320px;transition:left .25s}
  [dir=rtl] #mobnav.open{left:0}
  #mobnav .langs{margin-top:10px}
  #mobnav .langs a{color:#fff!important}
  #mobnav .langs a.on{color:var(--ink)!important}
  #mobnav a{color:#fff!important;padding:9px 0;font-size:17px;text-decoration:none}
  #mobnav .donate{padding:10px 22px;margin-top:12px}
  #mobnav .drop .menu{position:static;display:block;background:none;box-shadow:none;padding:0 0 0 16px;min-width:0}
  #mobnav .drop .menu a{color:rgba(255,255,255,.75)!important;padding:7px 0}
  #mobnav .drop>a::after{content:""}
  #nav-toggle{display:block;z-index:70;position:relative;grid-column:3;justify-self:end}
}

/* hero */
.hero{position:relative;min-height:92vh;display:flex;align-items:center;justify-content:center;
  text-align:center;color:#fff;background:var(--ink)}
.hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.55}
.hero .in{position:relative;max-width:880px;padding:140px 24px 90px}
.hero h1{font-size:clamp(44px,7.5vw,84px);margin-bottom:26px}
.hero p{font-size:17px;color:rgba(255,255,255,.88);max-width:720px;margin:0 auto 34px}
.hero .ctas{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}

/* page hero */
.page-hero{background:var(--ink);color:#fff;padding:150px 0 56px;position:relative}
.page-hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.28}
.page-hero .wrap{position:relative}
.page-hero h1{font-size:clamp(34px,5vw,54px)}
.page-hero .crumb{margin-top:12px;font-size:14px;color:rgba(255,255,255,.65)}
.page-hero .crumb a{color:var(--gold);text-decoration:none}

section.pad{padding:80px 0}
section.pad-sm{padding:56px 0}
.sec-title{font-size:clamp(28px,4vw,42px);margin-bottom:16px}
.sec-sub{color:var(--gray);max-width:760px;margin:0 auto 40px}

/* pillars */
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:26px}
.pillar{background:var(--cloud);border:1px solid var(--mist);border-radius:10px;padding:34px 30px;
  display:flex;flex-direction:column;transition:.2s}
.pillar:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgba(17,21,24,.10)}
.pillar img{width:86px;height:86px;object-fit:contain;margin-bottom:20px}
.pillar h3{font-size:22px;margin-bottom:12px}
.pillar p{color:var(--gray);font-size:15.5px;flex:1}
.pillar a{margin-top:18px;color:var(--gold-dark);font-weight:700;text-decoration:none;font-size:15px}
.pillar a:hover{text-decoration:underline}

/* cards */
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:26px}
.card{background:#fff;border:1px solid var(--mist);border-radius:10px;overflow:hidden;
  text-decoration:none;display:flex;flex-direction:column;transition:.2s}
.card:hover{transform:translateY(-4px);box-shadow:0 16px 36px rgba(17,21,24,.12)}
.card .ph{aspect-ratio:4/3;overflow:hidden;background:var(--mist)}
.card .ph img{width:100%;height:100%;object-fit:cover;transition:.35s}
.card:hover .ph img{transform:scale(1.05)}
.card .tx{padding:20px 22px 22px}
.card h3{font-size:19px;margin-bottom:8px}
.card .meta{font-size:13px;color:var(--gray)}
.chip{display:inline-block;background:var(--mist);border-radius:20px;padding:3px 12px;font-size:12.5px;
  color:var(--ink);margin:0 6px 6px 0}
.chip.gold{background:var(--gold);font-weight:700}

/* dark band */
.band{background:var(--ink);color:#fff;position:relative}
.band .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.22}
.band .wrap{position:relative}
.band h2{color:#fff}
.band p{color:rgba(255,255,255,.82)}

/* stats */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:30px;text-align:center}
.stats b{display:block;font-family:var(--serif);font-size:52px;color:var(--gold);font-weight:400}
.stats span{font-size:15px;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.75)}

/* team */
.team{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:28px}
.member{text-align:center;text-decoration:none}
.member .ph{width:150px;height:150px;border-radius:50%;overflow:hidden;margin:0 auto 14px;
  background:var(--mist);border:4px solid var(--gold)}
.member .ph img{width:100%;height:100%;object-fit:cover}
.member .ph.blank{display:flex;align-items:center;justify-content:center;font-family:var(--serif);
  font-size:42px;color:var(--gray)}
.member h3{font-size:19px}
.member .role{color:var(--gold-dark);font-size:14px;font-weight:700;margin:4px 0 8px}
.member .more{font-size:13.5px;color:var(--gray)}
.member:hover .more{color:var(--gold-dark)}

/* quotes */
.quotes{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:26px}
.quote{background:var(--cloud);border-left:4px solid var(--gold);border-radius:8px;padding:28px}
.quote p{font-family:var(--slab);font-size:15.5px;color:#333b41;font-style:italic}
.quote b{display:block;margin-top:16px;font-family:var(--sans);color:var(--ink)}

/* filters + board */
.filters{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:34px}
.fbtn{background:var(--mist);border:none;border-radius:20px;padding:8px 18px;font-size:14px;
  cursor:pointer;font-family:var(--sans);transition:.15s}
.fbtn:hover{background:#dfe3e8}
.fbtn.on{background:var(--ink);color:var(--gold);font-weight:700}
.board-tools{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:26px;align-items:center}
.board-tools select,.board-tools input[type=search]{padding:10px 14px;border:1px solid var(--mist);
  border-radius:6px;font-family:var(--sans);font-size:14.5px;background:#fff;color:var(--ink)}
#featured .opp{grid-column:1/-1;display:grid;grid-template-columns:1.5fr 1fr;gap:0;padding:0;
  border:2px solid var(--gold);overflow:hidden;margin-bottom:22px;background:#fffdf4}
#featured .opp .fx{padding:30px 34px;display:flex;flex-direction:column}
#featured .opp .fp{min-height:260px;background-size:cover;background-position:center}
#featured .opp h3{font-size:26px}
#featured .opp .desc{-webkit-line-clamp:unset}
.chip.feat{background:var(--ink);color:var(--gold);font-weight:700}
@media(max-width:760px){#featured .opp{grid-template-columns:1fr}#featured .opp .fp{min-height:180px}}
.reacts{display:flex;gap:10px;margin-top:14px;flex-wrap:wrap}
.reacts button{background:var(--mist);border:none;border-radius:20px;padding:6px 14px;font-size:13px;
  cursor:pointer;font-family:var(--sans);transition:.15s}
.reacts button:hover{background:#dfe3e8}
.reacts button.on{background:var(--gold);font-weight:700}
#board{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:20px;align-items:stretch}
.opp{border:1px solid var(--mist);border-radius:12px;padding:24px 26px;background:#fff;
  display:flex;flex-direction:column}
.opp:hover{box-shadow:0 8px 26px rgba(17,21,24,.08)}
.opp .top{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:8px}
.opp h3{font-size:20px;margin:4px 0 8px}
.opp .desc{color:#3c454c;font-size:15px;display:-webkit-box;-webkit-line-clamp:5;
  -webkit-box-orient:vertical;overflow:hidden}
.opp.x .desc{-webkit-line-clamp:unset}
.opp .more{background:none;border:none;color:var(--gold-dark);font-weight:700;font-size:13.5px;
  cursor:pointer;padding:6px 0 0;text-align:left;font-family:var(--sans);width:max-content}
.opp .dl{font-weight:700;font-size:13.5px;color:var(--ink)}
.opp .dl.soon{color:#c0392b}
.opp .dl.closed{color:var(--gray)}
.opp .btn{margin-top:auto;align-self:flex-start}
.opp.closed{opacity:.55}
@media(max-width:760px){#board{grid-template-columns:1fr}}

/* prose pages */
.prose{max-width:820px;margin:0 auto}
.prose h2{font-size:30px;margin:44px 0 16px}
.prose h3{font-size:23px;margin:34px 0 12px}
.prose h4{font-size:18px;margin:26px 0 10px;font-family:var(--sans);font-weight:700}
.prose p{margin-bottom:18px}
.prose ul,.prose ol{margin:0 0 18px 26px}
.prose li{margin-bottom:8px}
.prose img{border-radius:10px;margin:26px 0}
.prose a{color:var(--gold-dark)}
.prose blockquote{border-left:4px solid var(--gold);padding:6px 22px;margin:22px 0;color:var(--gray);font-style:italic}
.prose iframe{width:100%;aspect-ratio:16/9;border:0;border-radius:10px;margin:26px 0}

/* embed */
.embed{width:100%;aspect-ratio:16/10;border:0;border-radius:12px;background:var(--ink)}

/* forms */
form.nice{max-width:680px}
form.nice label{display:block;font-weight:700;font-size:14.5px;margin:20px 0 7px}
form.nice input,form.nice textarea,form.nice select{width:100%;padding:12px 14px;border:1px solid #d5dade;
  border-radius:6px;font-family:var(--sans);font-size:15.5px;background:#fff;color:var(--ink)}
form.nice input:focus,form.nice textarea:focus{outline:2px solid var(--gold)}
form.nice textarea{min-height:130px;resize:vertical}
form.nice .req::after{content:" *";color:#c0392b}
form.nice button{margin-top:26px}
form.nice .hint{font-size:13px;color:var(--gray);margin-top:5px}

/* faq */
.faq details{border:1px solid var(--mist);border-radius:8px;margin-bottom:12px;background:#fff}
.faq summary{padding:18px 22px;font-weight:700;cursor:pointer;font-size:16.5px;list-style:none;position:relative}
.faq summary::after{content:"+";position:absolute;right:22px;font-size:22px;color:var(--gold-dark)}
.faq details[open] summary::after{content:"–"}
.faq .a{padding:0 22px 20px;color:#3c454c}

/* tiers */
.tiers{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px}
.tier{border:1px solid var(--mist);border-radius:12px;padding:30px 26px;background:var(--cloud)}
.tier b.amt{font-family:var(--serif);font-size:38px;display:block;color:var(--ink);font-weight:400}
.tier p{color:var(--gray);font-size:15px;margin-top:12px}

/* trending */
.trend{background:var(--cloud);border-top:1px solid var(--mist)}
.trend h3{font-size:22px;margin-bottom:22px}
.trend .row{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px}
.trend a{display:flex;gap:12px;align-items:center;text-decoration:none;font-size:14.5px;font-weight:500}
.trend a img{width:56px;height:56px;border-radius:8px;object-fit:cover;flex:none}
.trend a:hover{color:var(--gold-dark)}

/* partners */
.partners{display:flex;flex-wrap:wrap;gap:38px;align-items:center;justify-content:center}
.partners img{height:64px;width:auto;object-fit:contain;filter:grayscale(1);opacity:.7;transition:.2s}
.partners img:hover{filter:none;opacity:1}

/* footer */
footer.site{background:var(--ink);color:rgba(255,255,255,.78);padding:70px 0 30px;font-size:15px}
footer.site .cols{display:grid;grid-template-columns:2fr 1fr 1fr 1.3fr;gap:44px}
footer.site h4{color:#fff;font-family:var(--serif);font-size:19px;margin-bottom:16px;font-weight:400}
footer.site a{color:rgba(255,255,255,.78);text-decoration:none;display:block;margin-bottom:9px}
footer.site a:hover{color:var(--gold)}
footer.site .fsoc{display:flex;gap:14px;margin-top:16px}
footer.site .fsoc a{margin:0}
footer.site .fsoc svg{width:20px;height:20px;fill:currentColor}
footer.site .base{border-top:1px solid rgba(255,255,255,.14);margin-top:52px;padding-top:24px;
  display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:13.5px;color:rgba(255,255,255,.5)}
footer.site .base a{display:inline;color:rgba(255,255,255,.5)}
@media(max-width:900px){footer.site .cols{grid-template-columns:1fr 1fr}}
@media(max-width:560px){footer.site .cols{grid-template-columns:1fr}}
.notice{background:#fff8e1;border:1px solid var(--gold);border-radius:8px;padding:14px 18px;font-size:14.5px;margin:18px 0}
"""

JS = """
const hd=document.querySelector('header.site');
addEventListener('scroll',()=>{hd.classList.toggle('scrolled',scrollY>40)},{passive:true});
const nt=document.getElementById('nav-toggle');
if(nt){nt.addEventListener('click',()=>{document.getElementById('mobnav').classList.toggle('open')})}
// count-up animation on impact numbers
(function(){
  const els=document.querySelectorAll('.cnt');
  if(!els.length)return;
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  const io=new IntersectionObserver(entries=>{
    entries.forEach(en=>{
      if(!en.isIntersecting)return;
      io.unobserve(en.target);
      const el=en.target,n=+el.dataset.n,s=el.dataset.s||'+',t0=performance.now(),dur=1400;
      function tick(t){
        const p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);
        el.textContent=Math.round(n*e)+s;
        if(p<1)requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  },{threshold:.4});
  els.forEach(e=>io.observe(e));
})();
"""

# ---------------------------------------------------------------- svg icons

ICO_IG = '<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2m0 3.6a6.2 6.2 0 1 0 0 12.4 6.2 6.2 0 0 0 0-12.4m0 10.2a4 4 0 1 1 0-8 4 4 0 0 1 0 8m6.4-10.4a1.4 1.4 0 1 1-2.9 0 1.4 1.4 0 0 1 2.9 0"/></svg>'
ICO_LI = '<svg viewBox="0 0 24 24"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5M.2 8h4.6v14.8H.2zm7.6 0h4.4v2h.1c.6-1.2 2.1-2.4 4.4-2.4 4.7 0 5.5 3.1 5.5 7.1v8.1h-4.6v-7.2c0-1.7 0-3.9-2.4-3.9s-2.8 1.9-2.8 3.8v7.3H7.8z"/></svg>'

# ---------------------------------------------------------------- shell

NAV = [
    ("Home", "index.html"),
    ("Archive", "archive.html"),
    ("Opportunities", "opportunities.html"),
    ("News", "news.html"),
    ("Get Involved", "volunteer.html", [
        ("Volunteer", "volunteer.html"),
        ("Create Your Profile", "create-profile.html"),
        ("Scanning Guide", "scanning-guide.html"),
        ("Splats With Phones", "splats-with-phones.html"),
    ]),
    ("About", "about.html", [
        ("About", "about.html"),
        ("Our People", "people.html"),
        ("El Jem Conference", "el-jem-conference.html"),
        ("ImmerseGT 2026", "immersegt-2026.html"),
        ("TanitXR &amp; the Unique Mappers", "unique-mappers.html"),
    ]),
    ("Contact", "contact.html"),
]


def lang_switcher(fname):
    """EN / FR / ع links pointing at this page's siblings in the other languages."""
    if fname == "404.html":  # no localized 404 pages — send to the homepages
        fname = "index.html"
    out = []
    for code, d in LANG_DIRS.items():
        if code == LANG:
            href, cls = "#", ' class="on"'
        else:
            up = "../" if LANG != "en" else ""
            href, cls = f"{up}{d}{fname}", ""
        out.append(f'<a href="{href}"{cls} lang="{code}">{LANG_NAMES[code]}</a>')
    return f'<div class="langs">{"".join(out)}</div>'


def _nav_items(entries, active):
    items = []
    for entry in entries:
        name, href, sub = entry[0], entry[1], (entry[2] if len(entry) > 2 else None)
        on = ' class="on"' if href == active else ""
        if sub:
            menu = "".join(f'<a href="{h}">{n}</a>' for n, h in sub)
            items.append(f'<div class="drop"><a href="{href}"{on}>{name}</a><div class="menu">{menu}</div></div>')
        else:
            items.append(f'<a href="{href}"{on}>{name}</a>')
    return "".join(items)


def header_html(active, transparent, fname="index.html"):
    logo = img("tanitxr-logo_red_vertical.png", 160, as_jpeg=False)
    left = _nav_items(NAV[:4], active)     # Home, Archive, Opportunities, News
    right = _nav_items(NAV[4:], active)    # Get Involved, About, Contact
    socials = f"""<div class="socials">
<a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{ICO_IG}</a>
<a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICO_LI}</a>
</div>"""
    donate = f'<a class="donate" href="{DONATE_URL}" target="_blank" rel="noopener">Donate</a>'
    cls = "site" if transparent else "site solid"
    return f"""<header class="{cls}"><div class="bar">
<div class="hside hl">{socials}<div class="hlinks">{left}</div></div>
<a class="logo" href="index.html"><img src="{logo}" alt="Tanit XR"></a>
<div class="hside hr"><div class="hlinks">{right}</div><div class="hcta">{donate}{lang_switcher(fname)}</div></div>
<button id="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
</div>
<nav id="mobnav">{_nav_items(NAV, active)}
{donate}
{lang_switcher(fname)}
</nav></header>"""


def trending_html():
    rows = []
    for title, href, thumb in TRENDING:
        t = img(thumb, 300) if thumb else None
        timg = f'<img src="{t}" alt="">' if t else ""
        rows.append(f'<a href="{href}">{timg}<span>{esc(title)}</span></a>')
    return f"""<section class="trend pad-sm"><div class="wrap">
<h3>Trending now</h3><div class="row">{''.join(rows)}</div></div></section>"""


def footer_html():
    return f"""<footer class="site"><div class="wrap"><div class="cols">
<div><h4>About Tanit XR</h4>
<p>Tanit XR is a nonprofit initiative working to digitally preserve Tunisia’s cultural heritage before it
disappears to time, weather, or neglect. Through 3D scanning, an open digital archive, and immersive AR/VR
experiences, we make mosaics, statues, and historic sites accessible to students, researchers, and the
public everywhere.</p>
<div class="fsoc">
<a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{ICO_IG}</a>
<a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICO_LI}</a>
</div></div>
<div><h4>Explore</h4>
<a href="archive.html">Archive</a>
<a href="coming-soon.html">AR/VR Experiences</a>
<a href="news.html">News</a>
<a href="opportunities.html">Opportunities</a></div>
<div><h4>Get Involved</h4>
<a href="volunteer.html" style="color:var(--gold);font-weight:700">Volunteer →</a>
<a href="splats-with-phones.html">Workshops</a>
<a href="{DONATE_URL}" target="_blank" rel="noopener">Donate</a>
<a href="contact.html">Contact</a></div>
<div><h4>Contact</h4>
<a href="mailto:{EMAIL}">Email: {EMAIL}</a>
<a href="tel:{PHONE.replace(' ','')}">Phone: {PHONE}</a>
<p style="margin-top:14px;font-size:13.5px">Fiscally sponsored by Florida Community Innovation, a U.S. 501(c)(3) nonprofit.</p></div>
</div><div class="base">
<span>© 2026 Tanit XR. All rights reserved.</span>
<span><a href="privacy.html">Privacy Policy</a></span>
</div></div></footer>"""


_tr_cache = {}

def _tr_patterns(lang):
    """Compiled (pattern, replacement) pairs, longest key first, whitespace-tolerant."""
    if lang not in _tr_cache:
        import translations
        table = translations.FR if lang == "fr" else translations.AR
        pats = []
        for k in sorted(table, key=len, reverse=True):
            pat = re.compile(r"\s+".join(re.escape(w) for w in k.split()))
            pats.append((pat, table[k]))
        _tr_cache[lang] = pats
    return _tr_cache[lang]


def _translate(doc):
    """Apply the current language's string table to everything outside <script> blocks."""
    if LANG == "en":
        return doc
    parts = re.split(r"(<script.*?</script>)", doc, flags=re.S)
    for i, part in enumerate(parts):
        if part.startswith("<script"):
            continue
        for pat, repl in _tr_patterns(LANG):
            part = pat.sub(lambda m, v=repl: v, part)
        parts[i] = part
    return "".join(parts)


FONTS_LATIN = ("https://fonts.googleapis.com/css2?family=Yeseva+One&family=Roboto:ital,wght@0,400;0,500;"
               "0,700;1,400&family=Roboto+Slab:wght@400;500&display=swap")
FONTS_ARABIC = ("https://fonts.googleapis.com/css2?family=El+Messiri:wght@400;600&family=Tajawal:wght@400;"
                "500;700&display=swap")


def page(fname, title, body, active=None, transparent=False, desc=TAGLINE, trending=True):
    if LANG == "ar":
        html_attrs = 'lang="ar" dir="rtl"'
        fonts = FONTS_ARABIC
        font_fix = ("<style>:root{--serif:'El Messiri',serif;--sans:'Tajawal',-apple-system,sans-serif;"
                    "--slab:'Tajawal',sans-serif}body{font-size:17.5px}"
                    "header.site .logo span{letter-spacing:.05em}</style>")
    else:
        html_attrs = f'lang="{LANG}"'
        fonts = FONTS_LATIN
        font_fix = ""
    doc = f"""<!DOCTYPE html>
<html {html_attrs}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} – TANIT XR</title>
<meta name="description" content="{esc(desc)}">
<link rel="icon" href="{img('tanitxr-logo_red_vertical.png', 120, as_jpeg=False)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">{font_fix}
</head>
<body>
{header_html(active or fname, transparent, fname)}
{body}
{trending_html() if trending else ''}
{footer_html()}
<script src="assets/site.js"></script>
</body>
</html>"""
    doc = _translate(doc)

    # ---- pretty URLs: every page (except the homepage and 404) lives in its own
    # directory, so links are tanitxr.org/archive/ instead of /archive.html
    is_index = fname == "index.html"
    is_404 = fname == "404.html"
    out_dir_rel = LANG_DIRS[LANG] + ("" if (is_index or is_404) else fname[:-5] + "/")
    P = "../" * out_dir_rel.count("/")

    def _pretty_root(root_html):
        d, b = posixpath.split(root_html)
        stem = b[:-5]
        return (d + "/" if d else "") + ("" if stem == "index" else stem + "/")

    def _link_repl(m):
        attr, ups, sub, stem, anchor = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5) or ""
        old = posixpath.normpath(posixpath.join(LANG_DIRS[LANG], ups + sub + stem + ".html"))
        href = P + _pretty_root(old) + anchor
        return f'{attr}="{href or "./"}"'

    doc = re.sub(r'(href|src)="((?:\.\./)*)((?:fr/|ar/)?)([A-Za-z0-9_-]+)\.html(#[^"]*)?"', _link_repl, doc)
    doc = re.sub(r'(href|src)="(?:\.\./)*(assets/[^"]*)"', lambda m: f'{m.group(1)}="{P}{m.group(2)}"', doc)
    doc = re.sub(r'url\((?:\.\./)*(assets/[^)]*)\)', lambda m: f"url({P}{m.group(1)})", doc)
    doc = re.sub(r"fetch\('(?:\.\./)*profiles-live\.json'\)", f"fetch('{P}profiles-live.json')", doc)

    out_dir = os.path.join(DOCS, out_dir_rel)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html" if not (is_index or is_404) else fname), "w") as f:
        f.write(doc)
    if not is_404:
        SITEMAP.append(out_dir_rel)
    if not (is_index or is_404):
        # flat alias (archive.html -> archive/) so links shared before the rename keep working
        stem = fname[:-5]
        with open(os.path.join(DOCS, LANG_DIRS[LANG], fname), "w") as f:
            f.write(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
                    f'<link rel="canonical" href="https://tanitxr.org/{LANG_DIRS[LANG]}{stem}/">'
                    f'<meta http-equiv="refresh" content="0;url={stem}/">'
                    f'<script>location.replace("{stem}/"+location.hash);</script></head>'
                    f'<body><a href="{stem}/">Continue</a></body></html>')


def page_hero(title, crumb=None, bg=None, pos="center"):
    bgd = (f'<div class="bg" style="background-image:url({img(bg, 1800)});'
           f'background-position:{pos}"></div>') if bg else ""
    return f"""<div class="page-hero">{bgd}<div class="wrap">
<h1>{title}</h1>
<div class="crumb"><a href="index.html">Home</a> &nbsp;›&nbsp; {crumb or title}</div>
</div></div>"""


# ---------------------------------------------------------------- data prep

def _clean_wp_content(c):
    """Turn WordPress post HTML into clean prose HTML with local images."""
    c = re.sub(r"<!--.*?-->", "", c, flags=re.S)
    c = re.sub(r"<div id=['\"]jp-relatedposts.*", "", c, flags=re.S)
    c = re.sub(r"<div class=['\"]sharedaddy.*", "", c, flags=re.S)
    # localize images: replace <img ...> with local processed copy
    def fix_img(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        if not src:
            return ""
        u = src.group(1)
        if "wp-content" not in u:
            return ""
        try:
            local = img(u, 1400)
        except Exception as e:
            print(f"  !! post image {u.split('/')[-1][:50]}: {e}")
            return ""
        alt = re.search(r'alt="([^"]*)"', tag)
        return f'<img src="{local}" alt="{alt.group(1) if alt else ""}" loading="lazy">'
    c = re.sub(r"<img[^>]*>", fix_img, c)
    # strip srcset/sizes remnants and wp class soup on common tags
    c = re.sub(r'\s(?:class|style|id|data-[a-z-]+|srcset|sizes|width|height|decoding|fetchpriority|loading)="[^"]*"',
               "", c)
    c = re.sub(r"<(/?)figure[^>]*>", r"", c)
    c = re.sub(r"<figcaption[^>]*>(.*?)</figcaption>",
               r'<p style="font-size:13.5px;color:var(--gray);margin-top:-12px">\1</p>', c, flags=re.S)
    # keep sketchfab/youtube iframes, restore lazy attr
    c = c.replace("<img ", '<img loading="lazy" ')
    c = re.sub(r"<iframe", '<iframe loading="lazy" allow="autoplay; fullscreen; xr-spatial-tracking"', c)
    c = fix_mojibake(c)
    return c


MODELS = json.load(open(os.path.join(HERE, "ref", "models.json")))
NEWS = json.load(open(os.path.join(HERE, "ref", "news.json")))

# titles that were stored truncated on the old site
TITLE_FIXES = {
    "Roman Mosaic with Bird and Vine Motifs – Villas…":
        "Roman Mosaic with Bird and Vine Motifs – Roman Villas of Carthage",
    "Decorated Bust Fragment – Roman Villas of Carth…":
        "Decorated Bust Fragment – Roman Villas of Carthage",
    "Inscribed Architectural Fragment – Byrsa Hill, …":
        "Inscribed Architectural Fragment – Byrsa Hill, Carthage",
}

for m in MODELS + NEWS:
    m["title"] = fix_mojibake(m["title"]).strip().rstrip(".")
    m["title"] = TITLE_FIXES.get(m["title"], m["title"])
    m["text"] = fix_mojibake(m["text"])
    m["clean_slug"] = slugify(m["title"])

def _site_of(m):
    t = m["title"] + " " + " ".join(m["cats"])
    if "Byrsa" in t: return "Byrsa Hill"
    if "Villas" in t: return "Roman Villas"
    if "Tophet" in t: return "Tophet of Salammbô"
    if "Baths of Antoninus" in t: return "Baths of Antoninus"
    if "Sidi" in t or "Kairouan" in t: return "Kairouan"
    return "Carthage"

for m in MODELS:
    m["href"] = f"model-{m['clean_slug']}.html"
    m["site"] = _site_of(m)
    tail = re.search(r"[–—-]\s*([^–—]+)$", m["title"])
    m["place"] = tail.group(1).strip() if tail else m["site"]
    # strip trailing GPS pin + scaniverse link (mojibake'd on the old site)
    m["text"] = re.sub(r"\s*(?:📍|üìç|\bü\S*|�\S*)?\s*\[[\d.,\s-]+\]\s*\(\s*https?://scaniver\.se\S*\s*\)\s*$",
                       "", m["text"])
    m["text"] = re.sub(r"[�]+\S*", "", m["text"]).strip()
for n in NEWS:
    n["href"] = f"post-{n['clean_slug']}.html"

PEOPLE_EXTRA = load("person_extra.json")
PEOPLE_PHOTOS = load("people_photos.json")

CORE_TEAM = [
    ("Ines Said", "Founder"),
    ("Julia Moreno-Molen", "Project Manager"),
    ("Melek Said", "Regional Manager"),
    ("Dr. Caroline Nickerson", "Partnerships & Community"),
    ("Margarita Johnson", "Research and Writing"),
    ("Fatma Slama", "Community Liaison"),
    ("Dr. Laura Harrison", "Chief Scientist"),
]
CONTRIBUTORS = [
    ("Ana Beatriz Vega González", "XR Development"),
    ("Oussema Ghattassi", "Volunteer"),
    ("Nick Reno", "XR Developer"),
    ("Rachel West", "2D Design & 3D Generalist"),
    ("Phil Chacko", "XR Advisor"),
    ("Ryan George", "3D Modeler & Web Contributor"),
    ("Patrick Molen", "3D Generalist"),
    ("Nick Kaufmann", "Photogrammetry, Grants and Opportunities"),
    ("Kristina Reyes", "3D Generalist"),
    ("Brianne Lehan", "Strategy & Creative Support"),
]


def person_record(name, role):
    slug = slugify(name)
    extra = PEOPLE_EXTRA.get(slug) or next(
        (v for k, v in PEOPLE_EXTRA.items() if v["name"] == name), None) or {}
    body = extra.get("body", "")
    # body starts with "Name Role bio..." — strip name/role prefix and icon junk
    bio = body
    for pre in (name, role, extra.get("name", "")):
        if pre and bio.lower().startswith(pre.lower()):
            bio = bio[len(pre):].lstrip(" ,–-")
    bio = re.sub(r"email \[#\d+\] Created with Sketch\.?", "", bio).strip()
    bio = re.sub(r"\s+", " ", bio)
    bio = bio.replace("Awardpresented", "Award presented")
    if bio and bio[0].islower():
        bio = f"{name} {bio}"
    photo = PEOPLE_PHOTOS.get(name)
    return {
        "name": name, "role": role, "slug": slug, "bio": bio,
        "photo": photo, "links": extra.get("links", []),
        "href": f"person-{slug}.html",
    }


TEAM = [person_record(n, r) for n, r in CORE_TEAM]
COMMUNITY = [person_record(n, r) for n, r in CONTRIBUTORS]

# volunteer profiles submitted through the new site (profiles/*.json)
PROFILE_DIR = os.path.join(HERE, "profiles")
if os.path.isdir(PROFILE_DIR):
    for fn in sorted(os.listdir(PROFILE_DIR)):
        if fn.endswith(".json"):
            with open(os.path.join(PROFILE_DIR, fn)) as f:
                d = json.load(f)
            if not d.get("approved", True):
                continue
            slug = slugify(d["name"])
            COMMUNITY.append({
                "name": d["name"], "role": d.get("role", "Volunteer"), "slug": slug,
                "bio": d.get("bio", ""), "photo": d.get("photo"),
                "links": [d[k] for k in ("linkedin", "instagram", "website") if d.get(k)],
                "href": f"person-{slug}.html",
            })

# opportunities
TERMS = load("terms.json")
OPP_RAW = load("opportunity.json")
OPPS = []
for o in OPP_RAW:
    txt = fix_mojibake(htmod.unescape(re.sub(r"<[^>]+>", " ", o["content"]["rendered"])))
    txt = re.sub(r"\s+", " ", txt).strip()
    terms = {}
    for grp in o.get("_embedded", {}).get("wp:term", []):
        for t in grp:
            terms.setdefault(t["taxonomy"], []).append(t["name"])
    dl = None
    mdl = re.search(r"(?:deadline|due|closes?|apply by|submit(?:ted)? by|applications? close[sd]?)[^.]{0,60}?"
                    r"([A-Z][a-z]+ \d{1,2}, \d{4})", txt, re.I)
    if mdl:
        dl = mdl.group(1)
    OPPS.append({
        "slug": o["slug"],
        "title": fix_mojibake(htmod.unescape(o["title"]["rendered"])),
        "desc": txt,
        "type": (terms.get("opportunity_type") or [""])[0],
        "eligibility": terms.get("eligibility", []),
        "region": (terms.get("region") or [""])[0],
        "country": (terms.get("country") or [""])[0],
        "mode": (terms.get("participation-mode") or [""])[0],
        "deadline_type": (terms.get("deadline_type") or [""])[0],
        "deadline_date": dl,
        "url": None,
        "published": o["date"][:10],
    })

# merge deadline dates / apply links / new entries harvested from the LinkedIn
# newsletter (ref/opportunity_updates.json)
_upd_path = os.path.join(HERE, "ref", "opportunity_updates.json")
if os.path.exists(_upd_path):
    _upd = json.load(open(_upd_path))
    for n in _upd.get("new", []):
        OPPS.append({
            "slug": slugify(n["title"]),
            "title": n["title"],
            "desc": n["desc"],
            "type": n.get("type", ""),
            "eligibility": n.get("eligibility", []),
            "region": n.get("region", ""),
            "country": "",
            "mode": n.get("mode", ""),
            "deadline_type": n.get("deadline_type", "Fixed" if n.get("deadline_date") else "Rolling"),
            "deadline_date": n.get("deadline_date"),
            "url": n.get("url"),
            "published": n.get("published", "2026-06-29"),
        })
    for key, patch in _upd.get("matches", {}).items():
        for o in OPPS:
            if o["slug"] == key or o["slug"].startswith(key) or key.startswith(o["slug"]):
                for field in ("deadline_date", "url", "deadline_type", "desc"):
                    if patch.get(field):
                        o[field] = patch[field]
                break
        else:
            print(f"  !! opportunity update matched nothing: {key}")

# a "Fixed" deadline with no recoverable date on a months-old posting is long past —
# mark it closed rather than showing a dateless "Deadline: Fixed"
import datetime as _dt
_stale = (_dt.date.today() - _dt.timedelta(days=60)).isoformat()
for o in OPPS:
    if not o["deadline_date"] and o["deadline_type"] in ("Fixed", "TBA", "") and o["published"] < _stale:
        o["deadline_type"] = "Closed"


def _dl_date(o):
    try:
        return _dt.datetime.strptime(o["deadline_date"], "%B %d, %Y").date()
    except (TypeError, ValueError):
        return None


def _is_open(o):
    if o["deadline_type"] == "Closed":
        return False
    d = _dl_date(o)
    return d is None or d >= _dt.date.today()


# featured listing: configured slug if still open, else the best open fallback
FEATURED_ACTIVE = {}
_feat_cfg = _upd.get("featured", {}) if os.path.exists(_upd_path) else {}
for slug, photo in _feat_cfg.items():
    o = next((x for x in OPPS if x["slug"] == slug), None)
    if o and _is_open(o):
        FEATURED_ACTIVE[slug] = photo or FEATURED_DEFAULT_PHOTOS.get(
            o["type"], FEATURED_DEFAULT_PHOTOS["_default"])
if not FEATURED_ACTIVE:
    candidates = [o for o in OPPS if _is_open(o) and o.get("url")]
    dated = sorted([o for o in candidates if _dl_date(o) and (_dl_date(o) - _dt.date.today()).days >= 5],
                   key=_dl_date)
    pick = (dated or sorted(candidates, key=lambda o: o["published"], reverse=True) or [None])[0]
    if pick:
        FEATURED_ACTIVE[pick["slug"]] = FEATURED_DEFAULT_PHOTOS.get(
            pick["type"], FEATURED_DEFAULT_PHOTOS["_default"])
        print(f"  featured (auto-picked): {pick['title']}")

FEATURED_BASENAMES = ["e55b902d5e35430eb6bc4b1d4d477134.jpeg",
                      "ac789b797d4e4528aab59e898676a6f3.jpeg",
                      "acd421bb938b40a798640f0895cb290d.jpeg"]

def _find_featured():
    out = []
    for b in FEATURED_BASENAMES:
        for m in MODELS:
            if m["img"] and os.path.basename(m["img"]).lower() == b.lower():
                out.append(m)
                break
    return out or MODELS[:3]

FEATURED = _find_featured()
TRENDING = []  # (title, href, thumb-url) — filled after models/news known
_tr_models = [m for m in MODELS if "Punic Stela" in m["title"] or "Corinthian Capital" in m["title"]][:2]
for m in _tr_models:
    TRENDING.append((m["title"], m["href"], m["img"]))
for n in sorted(NEWS, key=lambda x: x["date"]):
    TRENDING.append((n["title"], n["href"], n["img"]))
TRENDING = TRENDING[:4]


# ---------------------------------------------------------------- pages

def build_home():
    pillars = [
        ("research-1.png", "Digital Scanning",
         "Recording mosaics, statues, and ruins at risk before time, weather, and climate erase them.",
         "See how we scan", "scanning-guide.html"),
        ("archive.png", "Open Archive",
         "A free, growing online library where anyone can explore Tunisia’s heritage. Perfect for teachers, students, and the public.",
         "Explore the Archive", "archive.html"),
        ("education.png", "Education &amp; Workshops",
         "Hands-on training for students and volunteers in scanning, model cleanup, and storytelling. Programs in Tunisia and online.",
         "Attend a workshop", "splats-with-phones.html"),
        ("ARVR.png", "AR/VR Experiences",
         "Immersive learning: place mosaics in your space with AR or walk inside a Roman villa in VR. Designed for schools and museums.",
         "Try a demo", "coming-soon.html"),
        ("research.png", "Partnerships &amp; Research",
         "Working with institutions and experts to document sites, enhance accuracy, and share context so history is preserved and understood.",
         "Learn &amp; participate", "el-jem-conference.html"),
        ("volunteer.png", "Global Volunteer Network",
         "Join from Tunisia or abroad. Scan on site, help classify models, write context, or build apps that bring heritage to life.",
         "Volunteer with us", "volunteer.html"),
    ]
    pillar_html = "".join(
        f'<div class="pillar"><img src="{img(p[0], 400, as_jpeg=False)}" alt="">'
        f'<h3>{p[1]}</h3><p>{p[2]}</p><a href="{p[4]}">{p[3]} →</a></div>'
        for p in pillars)

    feat = "".join(
        f'<a class="card" href="{m["href"]}"><div class="ph"><img src="{img(m["img"], 800)}" alt="{esc(m["title"])}" loading="lazy"></div>'
        f'<div class="tx"><h3>{esc(m["title"])}</h3><div class="meta">{esc(m["place"])}</div></div></a>'
        for m in FEATURED)

    team = "".join(
        f'<a class="member" href="{p["href"]}">'
        + (f'<div class="ph"><img src="{img(p["photo"], 400)}" alt="{esc(p["name"])}" loading="lazy"></div>'
           if p["photo"] else f'<div class="ph blank">{esc(p["name"][0])}</div>')
        + f'<h3>{esc(p["name"])}</h3><div class="role">{esc(p["role"])}</div>'
          f'<div class="more">Read More →</div></a>'
        for p in TEAM)

    quotes = [
        ("I joined Tanit XR because I didn’t want to see our history disappear. When you walk through ruins in "
         "Carthage or Dougga, you can already see the erosion and damage from weather and time. Volunteering with "
         "Tanit XR gave me a way to fight back against that loss. Every scan I help with feels like I’m protecting "
         "a piece of Tunisia for future generations.", "Melek Said"),
        ("I joined Tanit XR because of the community. I love the people involved, and I am so grateful that we get "
         "to work together to celebrate our shared global, human heritage and shine a world spotlight on one of the "
         "most beautiful countries out there: Tunisia.", "Caroline Nickerson, PhD"),
        ("I started Tanit XR by simply walking around Carthage with my phone, scanning ruins because I couldn’t "
         "stand the idea of them being lost forever. Over time I realized this was bigger than me: people in "
         "Tunisia and abroad wanted to help, and it became a movement. Climate change, erosion, and neglect are "
         "real threats, but every scan is a way to push back, to make sure our heritage is preserved and "
         "celebrated.", "Ines Said"),
    ]
    quote_html = "".join(f'<div class="quote"><p>“{q}”</p><b>— {a}</b></div>' for q, a in quotes)

    partners = "".join(
        f'<img src="{img(fn, 300, as_jpeg=False)}" alt="{alt}" loading="lazy">'
        for fn, alt in [("FCI.webp", "Florida Community Innovation"), ("aaas-1.jpg", "AAAS"),
                        ("sketchfab.png", "Sketchfab"), ("FTAV.jpeg", "FTAV"),
                        ("Logon-logo.jpg", "Logon")])

    body = f"""
<div class="hero"><div class="bg" style="opacity:1;background-position:right center;background-image:linear-gradient(97deg,#0b0e11 0%,#0b0e11 32%,rgba(11,14,17,.82) 50%,rgba(11,14,17,.18) 82%,rgba(11,14,17,.5) 100%),linear-gradient(180deg,rgba(11,14,17,.55),rgba(11,14,17,0) 30%,rgba(11,14,17,0) 55%,rgba(11,14,17,.85)),url({img('hero-baths-flipped.jpg', 1920)})"></div>
<div class="in">
<h1>Preserving Heritage</h1>
<p>Preserving Tunisia’s endangered heritage. Climate change, erosion, and neglect threaten our ruins.
We capture them in 3D and bring them to life in AR and VR so they are never forgotten.</p>
<div class="ctas"><a class="btn btn-gold" href="volunteer.html">Join the Mission</a>
<a class="btn btn-dark" href="archive.html">Explore the Archive</a></div>
</div></div>

<section class="pad"><div class="wrap">
<div class="pillars">{pillar_html}</div>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap center">
<div class="eyebrow">Featured Scans</div>
<h2 class="sec-title">Highlights from the Tanit XR Archive</h2>
<div class="cards" style="text-align:left">{feat}</div>
<p style="margin-top:34px"><a class="btn btn-line" href="archive.html">Open the Full Archive</a></p>
</div></section>

<section class="band pad"><div class="bg" style="background-image:url({img('el-jem.jpg', 1800)})"></div>
<div class="wrap">
<div class="eyebrow">Why It Matters</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:44px">
<div><h2 class="sec-title">Heritage on the Brink</h2>
<p>Tunisia’s ruins are vanishing faster than they can be protected. Climate change brings floods, storms,
and heat that accelerate erosion. Without urgent action, pieces of world history could disappear.</p></div>
<div><h2 class="sec-title">A Lasting Record</h2>
<p>With every scan, Tanit XR creates a permanent archive. Even if the physical site is lost, the digital
memory survives – for schools, museums, and future generations.</p></div>
</div>
<div style="margin-top:36px;display:flex;gap:14px;flex-wrap:wrap">
<a class="btn btn-gold" href="{DONATE_URL}" target="_blank" rel="noopener">Donate Now</a>
<a class="btn btn-line-light" href="about.html">Learn More</a></div>
</div></section>

<section class="pad"><div class="wrap center">
<div class="eyebrow">Our Team</div>
<h2 class="sec-title">Powered by our people</h2>
<p class="sec-sub">Tanit XR is led by a dedicated core team and powered by a growing network of volunteers
across Tunisia and the world.</p>
<div class="team">{team}</div>
<p style="margin-top:36px"><a class="btn btn-line" href="people.html">Meet Everyone</a></p>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap center">
<div class="eyebrow">Testimonials</div>
<h2 class="sec-title">Hear from the volunteers and mentors shaping Tanit XR</h2>
<div class="quotes" style="text-align:left;margin-top:40px">{quote_html}</div>
</div></section>

<section class="band pad"><div class="wrap">
<div class="stats">
<div><b>{stat('artifacts')}</b><span>Artifacts Scanned</span></div>
<div><b>{stat('sites')}</b><span>Sites Documented</span></div>
<div><b>{stat('volunteers')}</b><span>Volunteers</span></div>
<div><b>{stat('reach')}</b><span>Global Reach</span></div>
</div></div></section>

<section class="pad-sm"><div class="wrap center">
<div class="eyebrow">Partners &amp; Supporters</div>
<div class="partners" style="margin-top:22px">{partners}</div>
</div></section>
"""
    page("index.html", "Home", body, transparent=True)


def build_archive():
    sites = sorted({m["site"] for m in MODELS})
    fbtns = '<button class="fbtn on" data-f="*">All ({})</button>'.format(len(MODELS)) + "".join(
        f'<button class="fbtn" data-f="{esc(s)}">{esc(s)} ({sum(1 for m in MODELS if m["site"] == s)})</button>'
        for s in sites)
    cards = "".join(
        f'<a class="card arch" data-site="{esc(m["site"])}" href="{m["href"]}">'
        f'<div class="ph"><img src="{img(m["img"], 800)}" alt="{esc(m["title"])}" loading="lazy"></div>'
        f'<div class="tx"><h3>{esc(m["title"])}</h3><div class="meta">{esc(m["place"])}</div></div></a>'
        for m in MODELS)
    body = f"""
{page_hero("Explore the Tanit XR Archive", "Archive")}
<section class="pad"><div class="wrap">
<p class="sec-sub" style="margin:0 0 30px">A free, growing library of 3D scans of Tunisia’s endangered
heritage — mosaics, statues, stelae, and ruins captured by our volunteers. Every model can be explored
interactively, and viewed in augmented reality on your phone.</p>
<div class="filters">{fbtns}</div>
<div class="cards" id="grid">{cards}</div>
</div></section>
<script>
document.addEventListener('DOMContentLoaded',()=>{{
document.querySelectorAll('.fbtn').forEach(b=>b.addEventListener('click',()=>{{
  document.querySelectorAll('.fbtn').forEach(x=>x.classList.remove('on'));b.classList.add('on');
  const f=b.dataset.f;
  document.querySelectorAll('.card.arch').forEach(c=>{{c.style.display=(f==='*'||c.dataset.site===f)?'':'none'}});
}}));
}});
</script>
<section class="band pad"><div class="bg" style="background-image:url({img('aug-20260813_124249.jpg', 1800)})"></div>
<div class="wrap center">
<div class="eyebrow">Become a volunteer</div>
<h2 class="sec-title">Every scan here was made by a volunteer</h2>
<p class="sec-sub" style="color:rgba(255,255,255,.85)">You don’t need to be an archaeologist or a
technologist to make an impact. Our first scans were made with a phone. Whether on the ground in Tunisia or
helping remotely, every volunteer contributes to preserving history.</p>
<a class="btn btn-gold" href="volunteer.html">Volunteer</a>
</div></section>"""
    page("archive.html", "Archive", body)


def build_model_pages():
    for i, m in enumerate(MODELS):
        prev_m = MODELS[i - 1] if i > 0 else MODELS[-1]
        next_m = MODELS[(i + 1) % len(MODELS)]
        sk = m["sketchfab"]
        sk_id = re.search(r"models/([a-f0-9]+)", sk).group(1) if sk else None
        embed = (f'<iframe class="embed" src="{sk}?ui_theme=dark" title="{esc(m["title"])} 3D model" '
                 f'allow="autoplay; fullscreen; xr-spatial-tracking" allowfullscreen '
                 f'loading="lazy"></iframe>') if sk else \
            f'<img src="{img(m["img"], 1400)}" alt="{esc(m["title"])}" style="border-radius:12px">'
        sk_link = (f'<a class="btn btn-line" href="https://sketchfab.com/3d-models/{sk_id}" target="_blank" '
                   f'rel="noopener">View on Sketchfab</a>') if sk_id else ""
        chips = "".join(f'<span class="chip">{esc(c)}</span>'
                        for c in m["cats"] if c != "Models" and c != m["place"])
        text = esc(m["text"])[:4000]
        body = f"""
{page_hero(esc(m["title"]), f'<a href="archive.html">Archive</a> &nbsp;›&nbsp; {esc(m["title"])}')}
<section class="pad"><div class="wrap" style="max-width:960px">
{embed}
<div style="margin:26px 0 10px">{chips}<span class="chip gold">{esc(m["place"])}</span></div>
<p style="color:#3c454c">{text}</p>
<div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:30px">
{sk_link}
<a class="btn btn-gold" href="archive.html">← Back to Archive</a>
</div>
<p style="margin-top:26px;padding:16px 20px;background:var(--cloud);border-radius:10px;font-size:14.5px;color:var(--gray)">
🤝 This scan exists because of volunteers — from scanning on site to cleanup and research.
<a href="volunteer.html" style="color:var(--gold-dark);font-weight:700">Join us →</a></p>
<div style="display:flex;justify-content:space-between;margin-top:44px;padding-top:22px;border-top:1px solid var(--mist);font-size:14.5px">
<a href="{prev_m['href']}" style="text-decoration:none;color:var(--gray)">← {esc(prev_m['title'][:40])}</a>
<a href="{next_m['href']}" style="text-decoration:none;color:var(--gray);text-align:right">{esc(next_m['title'][:40])} →</a>
</div>
</div></section>"""
        page(m["href"], m["title"], body, active="archive.html",
             desc=m["text"][:150])


def build_news():
    cards = ""
    for n in sorted(NEWS, key=lambda x: x["date"], reverse=True):
        date = n["date"]
        excerpt = esc(n["text"][:220]) + "…"
        cards += f"""<a class="card" href="{n['href']}">
<div class="ph"><img src="{img(n['img'], 800)}" alt="" loading="lazy"></div>
<div class="tx"><div class="meta">{date}</div><h3>{esc(n['title'])}</h3>
<p style="color:var(--gray);font-size:14.5px;margin-top:8px">{excerpt}</p></div></a>"""
    body = f"""
{page_hero("News", "News")}
<section class="pad"><div class="wrap">
<div class="cards">{cards}</div>
</div></section>"""
    page("news.html", "News", body)

    for n in NEWS:
        content = _clean_wp_content(n["content"])
        body = f"""
{page_hero(esc(n["title"]), f'<a href="news.html">News</a> &nbsp;›&nbsp; {esc(n["title"][:50])}')}
<section class="pad"><div class="wrap"><div class="prose">
<p style="color:var(--gray);font-size:14px">Published {n['date']}</p>
{content}
<p style="margin-top:40px"><a class="btn btn-line" href="news.html">← All News</a></p>
</div></div></section>"""
        page(n["href"], n["title"], body, active="news.html", desc=n["text"][:150])


def build_people():
    def grid(people):
        return "".join(
            f'<a class="member" href="{p["href"]}">'
            + (f'<div class="ph"><img src="{img(p["photo"], 400)}" alt="{esc(p["name"])}" loading="lazy"></div>'
               if p["photo"] else f'<div class="ph blank">{esc(p["name"][0])}</div>')
            + f'<h3>{esc(p["name"])}</h3><div class="role">{esc(p["role"])}</div>'
              f'<div class="more">Read More →</div></a>'
            for p in people)
    body = f"""
{page_hero("Our People", "Our People")}
<section class="pad"><div class="wrap center">
<div class="eyebrow">Meet the team</div>
<h2 class="sec-title">Core Team</h2>
<div class="team" style="margin-top:38px">{grid(TEAM)}</div>
<h2 class="sec-title" style="margin-top:70px">Community Contributors</h2>
<div class="team" style="margin-top:38px">{grid(COMMUNITY)}</div>
<div class="notice" style="text-align:left;max-width:720px;margin:56px auto 0">
<b>Are you a Tanit XR volunteer?</b> <a href="create-profile.html" style="color:var(--gold-dark)">Create your
profile</a> and it will appear here once approved.</div>
</div></section>
<script>
// live profiles submitted since the last build (see profiles/README.md)
fetch('profiles-live.json').then(r=>r.ok?r.json():[]).then(list=>{{
  const grid=document.querySelectorAll('.team')[1];
  if(!grid||!Array.isArray(list))return;
  const baked=new Set([...document.querySelectorAll('.member h3')].map(h=>h.textContent.trim().toLowerCase()));
  list.filter(p=>p&&p.name&&p.approved!==false&&!baked.has(p.name.trim().toLowerCase())).forEach(p=>{{
    const a=document.createElement('a');a.className='member';
    a.href=p.linkedin||p.website||p.instagram||'#';
    if(a.href!=='#')a.target='_blank';
    const ph=p.photo?'<div class="ph"><img src="'+p.photo.replace(/"/g,'')+'" alt="" loading="lazy"></div>'
      :'<div class="ph blank">'+p.name[0]+'</div>';
    const escT=s=>{{const d=document.createElement('span');d.textContent=s||'';return d.innerHTML}};
    a.innerHTML=ph+'<h3>'+escT(p.name)+'</h3><div class="role">'+escT(p.role||'Volunteer')+'</div>';
    grid.appendChild(a);
  }});
}}).catch(()=>{{}});
</script>"""
    page("people.html", "Our People", body)

    def link_label(u):
        return re.sub(r"^https?://(www\.)?", "", u).split("/")[0]

    for p in TEAM + COMMUNITY:
        links = "".join(
            f'<a class="btn btn-line" style="margin:0 10px 10px 0" href="{esc(u)}" target="_blank" rel="noopener">'
            f'{esc(link_label(u))}</a>'
            for u in p["links"])
        photo = (f'<img src="{img(p["photo"], 700)}" alt="{esc(p["name"])}" '
                 f'style="border-radius:14px;max-width:340px;width:100%">') if p["photo"] else ""
        bio = esc(p["bio"]) if p["bio"] else "Part of the Tanit XR volunteer network."
        body = f"""
{page_hero(esc(p["name"]), f'<a href="people.html">Our People</a> &nbsp;›&nbsp; {esc(p["name"])}')}
<section class="pad"><div class="wrap" style="max-width:960px">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:44px;align-items:start">
<div>{photo}</div>
<div>
<div class="eyebrow">{esc(p["role"])}</div>
<p style="font-size:17px;color:#2c343b">{bio}</p>
<div style="margin-top:26px">{links}</div>
<p style="margin-top:34px"><a class="btn btn-gold" href="people.html">← Back to Our People</a></p>
</div></div></div></section>"""
        page(p["href"], p["name"], body, active="people.html", desc=p["bio"][:150])


def build_opportunities():
    LBL = {
        "en": {"dl": "Deadline: ", "closed": "Closed", "days": " days left", "day": " day left",
               "none": "No opportunities match those filters.", "det": "See details",
               "apply": "Apply / Info →", "more": "▾ More", "less": "▴ Less",
               "feat": "★ Featured", "helpful": "👍 Helpful", "applied": "✅ I applied",
               "vol": "Volunteer with us →", "terms": {}},
        "fr": {"dl": "Date limite : ", "closed": "Clôturé", "days": " jours restants", "day": " jour restant",
               "none": "Aucune opportunité ne correspond à ces filtres.", "det": "Voir les détails",
               "apply": "Postuler / Infos →", "more": "▾ Plus", "less": "▴ Moins",
               "feat": "★ À la une", "helpful": "👍 Utile", "applied": "✅ J’ai postulé",
               "vol": "Devenez bénévole →",
               "terms": {"Rolling": "Continu", "Fixed": "Date fixe", "Open": "Ouvert", "TBA": "À annoncer"}},
        "ar": {"dl": "الموعد النهائي: ", "closed": "مغلق", "days": " أيام متبقية", "day": " يوم متبقٍ",
               "none": "لا توجد فرص مطابقة لهذه المرشحات.", "det": "انظر التفاصيل",
               "apply": "قدّم / التفاصيل ←", "more": "▾ المزيد", "less": "▴ أقل",
               "feat": "★ مميّزة", "helpful": "👍 مفيدة", "applied": "✅ لقد قدّمت",
               "vol": "تطوّع معنا ←",
               "terms": {"Rolling": "مستمر", "Fixed": "تاريخ محدد", "Open": "مفتوح", "TBA": "سيُعلن لاحقًا"}},
    }[LANG]
    data = []
    for o in OPPS:
        rec = {
            "id": o["slug"],
            "t": o["title"], "d": o["desc"], "ty": o["type"], "el": o["eligibility"],
            "rg": o["region"], "co": o["country"], "md": o["mode"],
            "dt": o["deadline_type"], "dd": o["deadline_date"], "pub": o["published"],
            "u": o.get("url"),
        }
        if o["slug"] in FEATURED_ACTIVE:
            rec["f"] = 1
            rec["ph"] = img(FEATURED_ACTIVE[o["slug"]], 1000)
        data.append(rec)
    # permanent house listing: volunteering with Tanit XR is always open
    data.insert(0, {
        "id": "volunteer-with-tanit-xr", "tx": 1,
        "t": "Volunteer with Tanit XR — Preserve Heritage in 3D & XR",
        "d": "Tanit XR is powered by volunteers: 3D scanning, model cleanup, XR development, "
             "historical research, writing, translation, and storytelling. Join from Tunisia or "
             "anywhere in the world — all experience levels welcome, fully remote friendly.",
        "ty": "Volunteer", "el": ["Open to all"], "rg": "Global", "co": "", "md": "Remote",
        "dt": "Rolling", "dd": None, "pub": _dt.date.today().isoformat(), "u": "../volunteer/",
    })
    types = sorted({o["type"] for o in OPPS if o["type"]})
    eligs = sorted({e for o in OPPS for e in o["eligibility"]})
    modes = sorted({o["mode"] for o in OPPS if o["mode"]})
    def opts(vals):
        return "".join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in vals)
    body = f"""
{page_hero("Art, XR &amp; Impact Opportunities", "Art, XR &amp; Impact Opportunities")}
<section class="pad"><div class="wrap">
<p class="sec-sub" style="margin:0 0 26px;max-width:860px">A curated board of grants, residencies, fellowships, open calls,
and events for artists, XR creators, educators, students, and changemakers — updated regularly by the
Tanit XR team. Also published as our
<a href="https://www.linkedin.com/newsletters/art-xr-impact-opportunities-7370189407523454976/"
target="_blank" rel="noopener" style="color:var(--gold-dark)">LinkedIn newsletter</a>.</p>
<div class="board-tools">
<input type="search" id="q" placeholder="Search…" style="flex:1;min-width:170px">
<select id="f-type"><option value="">Type</option>{opts(types)}</select>
<select id="f-elig"><option value="">Eligibility</option>{opts(eligs)}</select>
<select id="f-mode"><option value="">Mode</option>{opts(modes)}</select>
<select id="sort">
<option value="soon">Deadline soonest</option>
<option value="new">Newest</option>
</select>
</div>
<div id="featured"></div>
<div id="board"></div>

<div class="band" style="margin-top:64px;border-radius:14px;padding:44px 38px">
<div style="max-width:640px">
<div class="eyebrow">Newsletter</div>
<h2 class="sec-title" style="font-size:30px">Never miss a deadline</h2>
<p style="margin-bottom:22px">Get new grants, residencies, and open calls for art, XR &amp; impact in your
inbox — free, from the Tanit XR team. You'll also be first to hear how our heritage-preservation work is
going.</p>
<form class="nice" action="{FORM_ENDPOINT}" method="POST" style="display:flex;gap:12px;flex-wrap:wrap;max-width:none">
<input type="hidden" name="_subject" value="Newsletter subscription — tanitxr.org">
<input type="hidden" name="_captcha" value="true">
<input type="text" name="_honey" style="display:none">
<input name="email" type="email" placeholder="you@example.com" required
  style="flex:1;min-width:220px;padding:13px 16px;border:none;border-radius:6px;font-size:15.5px">
<button class="btn btn-gold" type="submit" style="margin-top:0">Subscribe Free</button>
</form>
<p style="font-size:13px;color:rgba(255,255,255,.6);margin-top:12px">No spam — opportunities and Tanit XR
news only. Also published on
<a href="https://www.linkedin.com/newsletters/art-xr-impact-opportunities-7370189407523454976/"
target="_blank" rel="noopener" style="color:var(--gold)">LinkedIn</a>.</p>
</div>
</div>

<div style="margin-top:26px;background:var(--cloud);border:1px solid var(--mist);border-radius:12px;padding:36px 34px">
<h2 class="sec-title" style="font-size:28px">Know an opportunity we should feature?</h2>
<p style="color:var(--gray);margin-bottom:6px">Send it our way — if it's a fit, it will appear on this board
and in the newsletter.</p>
<form class="nice" action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Opportunity submission — tanitxr.org">
<input type="hidden" name="_captcha" value="true">
<input type="text" name="_honey" style="display:none">
<label class="req" for="oname">Opportunity name</label>
<input id="oname" name="opportunity" required>
<label class="req" for="olink">Link</label>
<input id="olink" name="link" type="url" placeholder="https://…" required>
<label for="odl">Deadline (if you know it)</label>
<input id="odl" name="deadline">
<label for="odesc">Who is it for / anything we should know</label>
<textarea id="odesc" name="details" style="min-height:90px"></textarea>
<label for="osub">Your name or email (optional, so we can credit or thank you)</label>
<input id="osub" name="submitted_by">
<button class="btn btn-gold" type="submit">Submit Opportunity</button>
</form>
</div>
</div></section>
<script>
const OPPS={json.dumps(data)};
const LBL={json.dumps(LBL, ensure_ascii=False)};
const RX={json.dumps(REACTIONS_ENDPOINT)};
let STATS={{}};
const board=document.getElementById('board');
const featBox=document.getElementById('featured');
const lsGet=k=>{{try{{return localStorage.getItem(k)}}catch(e){{return null}}}};
const lsSet=(k,v)=>{{try{{localStorage.setItem(k,v)}}catch(e){{}}}};
function track(type,id){{
  if(!RX)return;
  try{{navigator.sendBeacon(RX+'/track',new Blob([JSON.stringify({{type,id}})],{{type:'application/json'}}))}}catch(e){{}}
}}
function reactsHtml(o){{
  if(!RX||o._closed)return '';
  const s=STATS[o.id]||{{}};
  const mk=(type,label)=>{{
    const n=(s[type]||0)+(lsGet('rx:'+type+':'+o.id)?0:0);
    const on=lsGet('rx:'+type+':'+o.id)?' class="on"':'';
    return '<button'+on+' data-rx="'+type+'" data-id="'+o.id+'">'+label+(n?' · '+n:'')+'</button>';
  }};
  return '<div class="reacts">'+mk('thumbs',LBL.helpful)+mk('applied',LBL.applied)+'</div>';
}}
function parseDate(s){{return s?new Date(s):null}}
function render(){{
  const q=document.getElementById('q').value.toLowerCase();
  const ft=document.getElementById('f-type').value;
  const fe=document.getElementById('f-elig').value;
  const fm=document.getElementById('f-mode').value;
  const sort=document.getElementById('sort').value;
  const now=new Date();
  let list=OPPS.filter(o=>
    (!q||(o.t+' '+o.d).toLowerCase().includes(q)) &&
    (!ft||o.ty===ft) && (!fe||o.el.includes(fe)) && (!fm||o.md===fm));
  list.forEach(o=>{{
    o._d=parseDate(o.dd);
    o._closed = !!(o.dt==='Closed' || (o._d && o._d < now));
  }});
  if(sort==='new'){{ list.sort((a,b)=>b.pub.localeCompare(a.pub)); }}
  else {{
    list.sort((a,b)=>{{
      if(a._closed!==b._closed) return a._closed?1:-1;
      if(a._d&&b._d) return a._d-b._d;
      if(a._d) return -1; if(b._d) return 1;
      return b.pub.localeCompare(a.pub);
    }});
  }}
  function dlOf(o){{
    if(o._closed)return [LBL.closed,'closed'];
    if(o._d){{
      const days=Math.ceil((o._d-now)/864e5);
      return [LBL.dl+o.dd+(days<=14?' · '+days+(days===1?LBL.day:LBL.days):''), days<=14?'soon':''];
    }}
    if(o.dt&&o.dt!=='Fixed')return [LBL.dl+(LBL.terms[o.dt]||o.dt),''];
    return [LBL.dl+LBL.det,''];
  }}
  function chipsOf(o){{
    return (o.tx?'<span class="chip feat">🏺 Tanit XR</span>':'')
      + [o.ty,o.md,o.rg||o.co].filter(Boolean).map(c=>'<span class="chip">'+c+'</span>').join('')
      + o.el.map(c=>'<span class="chip gold">'+c+'</span>').join('');
  }}
  function btnOf(o){{
    if(!o.u||o._closed)return '';
    if(o.tx)return '<a class="btn btn-gold" style="padding:8px 20px;font-size:13.5px;margin-top:14px" href="'+o.u+'">'+LBL.vol+'</a>';
    return '<a class="btn btn-gold apply" data-id="'+o.id+'" style="padding:8px 20px;font-size:13.5px;margin-top:14px" href="'+o.u+'" target="_blank" rel="noopener">'+LBL.apply+'</a>';
  }}
  const feats=list.filter(o=>o.f&&!o._closed);
  let rest=list.filter(o=>!feats.includes(o));
  rest=[...rest.filter(o=>o.tx),...rest.filter(o=>!o.tx)];
  featBox.innerHTML=feats.map(o=>{{
    const [dl,cls]=dlOf(o);
    return '<div class="opp" id="opp-'+o.id+'"><div class="fx">'+
      '<div class="top"><span class="chip feat">'+LBL.feat+'</span>'+chipsOf(o)+'</div>'+
      '<h3>'+o.t+'</h3><div class="dl '+cls+'">'+dl+'</div>'+
      '<p class="desc">'+o.d+'</p>'+btnOf(o)+reactsHtml(o)+'</div>'+
      '<div class="fp" style="background-image:url('+o.ph+')"></div></div>';
  }}).join('');
  board.innerHTML=rest.map(o=>{{
    const [dl,cls]=dlOf(o);
    const more=o.d.length>260?'<button class="more" type="button">'+LBL.more+'</button>':'';
    return '<div class="opp'+(o._closed?' closed':'')+'" id="opp-'+o.id+'"><div class="top">'+chipsOf(o)+'</div>'+
      '<h3>'+o.t+'</h3><div class="dl '+cls+'">'+dl+'</div>'+
      '<p class="desc">'+o.d+'</p>'+more+btnOf(o)+reactsHtml(o)+'</div>';
  }}).join('')||'<p style="color:var(--gray)">'+LBL.none+'</p>';
  document.querySelectorAll('#board .more').forEach(b=>b.addEventListener('click',()=>{{
    const card=b.closest('.opp');card.classList.toggle('x');
    b.textContent=card.classList.contains('x')?LBL.less:LBL.more;
  }}));
  document.querySelectorAll('.apply').forEach(a=>a.addEventListener('click',()=>track('click',a.dataset.id)));
  document.querySelectorAll('.reacts button').forEach(b=>b.addEventListener('click',()=>{{
    const type=b.dataset.rx,id=b.dataset.id;
    if(lsGet('rx:'+type+':'+id))return;
    lsSet('rx:'+type+':'+id,'1');
    track(type,id);
    b.classList.add('on');
    const s=STATS[id]=STATS[id]||{{}};s[type]=(s[type]||0)+1;
    b.textContent=(type==='thumbs'?LBL.helpful:LBL.applied)+' · '+s[type];
  }}));
}}
['q','f-type','f-elig','f-mode','sort'].forEach(id=>{{
  document.getElementById(id).addEventListener('input',render);
}});
render();
if(location.hash&&location.hash.startsWith('#opp-')){{
  try{{const el=document.querySelector(location.hash);
    if(el){{el.scrollIntoView({{block:'center'}});el.style.boxShadow='0 0 0 3px var(--gold)';}}
  }}catch(e){{}}
}}
if(RX){{
  track('view','board');
  fetch(RX+'/stats').then(r=>r.json()).then(s=>{{STATS=s&&typeof s==='object'?s:{{}};render();}}).catch(()=>{{}});
}}
</script>"""
    page("opportunities.html", "Art, XR & Impact Opportunities", body, active="opportunities.html")


def build_volunteer():
    faqs = [
        ("How can I become a volunteer?",
         "We’re so excited that you’re interested in volunteering! Please fill out our "
         f"<a href='{VOLUNTEER_FORM_URL}' target='_blank' rel='noopener'>volunteer form</a> "
         "and we’ll get back to you via email."),
        ("What should I know before applying?",
         "Our volunteer positions are currently unpaid and remote. We work with volunteers digitally all over "
         "the globe. We have some mentorship and networking opportunities available to our volunteers based on "
         "your chosen area of focus. Areas of focus we’re currently seeking are: grant writing, XR/VR "
         "development, business development, social media management, graphic design, and general interest. "
         "All levels of experience and expertise are welcome to volunteer."),
        ("How does your team work together?",
         "As a global, virtual team, it’s important for us to communicate asynchronously. The majority of our "
         "communication is done via Slack. Once a week, we meet virtually and discuss ongoing, upcoming, and "
         "blocked tasks to keep our mission moving forward."),
        ("Are there different ways to volunteer?",
         "As one of our goals is to engage the public in preservation work, the ability to volunteer will "
         "eventually expand and become tiered. While we build our foundation, we hold only one tier. Keep "
         "checking back to see how you can get involved!"),
        ("Do you work with organizations and external partners?",
         "Preservation, cultural conservation, and climate work is done best in community. We are open to all "
         "forms of partnership that help move our mission forward. If you are an archaeologist, non-profit, "
         "government agency, or any other organization aligned in the mission of conservation or preservation, "
         f"please reach out to us at <a href='mailto:{EMAIL}'>{EMAIL}</a>."),
        ("How much time do I need to dedicate if I become a volunteer?",
         "Volunteer tasks are project and task based. After expressing your interests via the volunteer form, a "
         "member of our leadership team will reach out to you with questions about your capacity for available "
         "work that aligns with your interests and expertise. You set the expectation on how much you can "
         "commit to and what time you have."),
    ]
    faq_html = "".join(
        f"<details><summary>{q}</summary><div class='a'>{a}</div></details>" for q, a in faqs)
    body = f"""
{page_hero("Volunteer", "Volunteer", bg="sv-IMG_8547.jpg", pos="center 22%")}
<section class="pad"><div class="wrap" style="max-width:880px">
<div class="center">
<h2 class="sec-title">Want to join our team of volunteers?</h2>
<p class="sec-sub">Fill out our volunteer interest form and we will connect with you about available
opportunities.</p>
<a class="btn btn-gold" href="{VOLUNTEER_FORM_URL}" target="_blank" rel="noopener">Volunteer Interest Form</a>
&nbsp; <a class="btn btn-line" href="scanning-guide.html">Read the Scanning Guide</a>
</div>
<h2 class="sec-title" style="margin-top:70px">Frequently Asked Questions</h2>
<div class="faq" style="margin-top:28px">{faq_html}</div>
</div></section>
<section class="band pad"><div class="wrap center">
<div class="eyebrow">Become a volunteer</div>
<h2 class="sec-title">Join us in preserving Tunisia’s cultural heritage</h2>
<p class="sec-sub" style="color:rgba(255,255,255,.82)">We rely on our international volunteer support to bring
TanitXR to life. We greatly appreciate any time you are willing to share with us as we work toward the digital
preservation of Tunisia’s historically and culturally rich heritage sites.</p>
<a class="btn btn-gold" href="{VOLUNTEER_FORM_URL}" target="_blank" rel="noopener">Volunteer</a>
&nbsp; <a class="btn btn-line-light" href="create-profile.html">Create Your Volunteer Profile</a>
</div></section>"""
    page("volunteer.html", "Volunteer", body)


def build_create_profile():
    body = f"""
{page_hero("Create Your Profile", '<a href="volunteer.html">Volunteer</a> &nbsp;›&nbsp; Create Your Profile')}
<section class="pad"><div class="wrap" style="max-width:760px">
<p class="sec-sub" style="margin:0 0 8px">Already volunteering with Tanit XR? Submit your profile and, once
approved by the team, it will appear on our <a href="people.html" style="color:var(--gold-dark)">Our People</a>
page.</p>
<form class="nice" action="{PROFILE_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="New volunteer profile submission — tanitxr.org">
<input type="hidden" name="_captcha" value="true">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" style="display:none">
<label class="req" for="pname">Your Name</label>
<input id="pname" name="name" required>
<label class="req" for="prole">Your Role / What you do</label>
<input id="prole" name="role" placeholder="e.g. 3D Generalist, XR Developer, Researcher" required>
<label class="req" for="pbio">Short Bio</label>
<textarea id="pbio" name="bio" placeholder="A few sentences about you and what you do with Tanit XR." required></textarea>
<label for="pphoto">Photo (link)</label>
<input id="pphoto" name="photo_url" type="url" placeholder="Link to a headshot (Google Drive, Dropbox, LinkedIn photo…)">
<div class="hint">Or simply reply with a photo attached when we email you back.</div>
<label for="plink1">LinkedIn</label>
<input id="plink1" name="linkedin" type="url" placeholder="https://www.linkedin.com/in/…">
<label for="plink2">Instagram</label>
<input id="plink2" name="instagram" type="url" placeholder="https://www.instagram.com/…">
<label for="plink3">Website / Portfolio</label>
<input id="plink3" name="website" type="url">
<label class="req" for="pemail">Email</label>
<input id="pemail" name="email" type="email" required>
<div class="hint">Used only to contact you about your profile — it is not published.</div>
<button class="btn btn-gold" type="submit">Submit Profile</button>
</form>
</div></section>"""
    page("create-profile.html", "Create Your Profile", body, active="volunteer.html")


def build_scanning_guide():
    body = f"""
{page_hero("Tanit XR Scanning Guide", "Scanning Guide", bg="sv-IMG_4213.jpg")}
<section class="pad"><div class="wrap"><div class="prose">
<h2>Using Scaniverse to Preserve Heritage</h2>
<h3>📲 Getting Started</h3>
<ul>
<li><b>App:</b> Download Scaniverse from the iOS App Store (iPhone 12 Pro or newer recommended for LiDAR support).</li>
<li><b>Goal:</b> Create detailed 3D scans of historical landmarks, ruins, pottery, architecture, and cultural
artifacts for a global digital heritage archive.</li>
</ul>
<img src="{img('https://tanitxr.org/wp-content/uploads/2025/09/image.png', 1200)}" alt="Scaniverse scanning example">
<h2>🧭 Choosing What to Scan</h2>
<p>Not sure where to start? Look for objects, places, and details that carry cultural, historical, artistic,
or community meaning.</p>
<p><b>Good things to scan include:</b></p>
<ul>
<li><b>Architecture and ruins</b> — doors, arches, columns, facades, walls, courtyards, tombs, monuments, and historic homes</li>
<li><b>Objects and artifacts</b> — pottery, tools, carvings, statues, tiles, jewelry, textiles, inscriptions, and household items</li>
<li><b>Small details</b> — patterns, textures, symbols, damage, repairs, maker’s marks, or decorative elements</li>
<li><b>Everyday heritage</b> — bakeries, workshops, markets, gathering places, family heirlooms, gardens, and community spaces</li>
<li><b>At-risk heritage</b> — places or objects threatened by weather, neglect, development, conflict, theft, or loss of memory</li>
</ul>
<p><b>Before scanning, ask:</b></p>
<ul>
<li>What story does this object or place tell?</li>
<li>Who uses it, remembers it, or cares about it?</li>
<li>Is it connected to a tradition, craft, family, neighborhood, or historic event?</li>
<li>Is it changing, disappearing, or at risk?</li>
</ul>
<p><b>Please do not scan sacred, private, restricted, or sensitive objects without permission.</b> When in
doubt, ask a local caretaker, community member, owner, or cultural authority first.</p>
<h2>🕯️ Scanning Intangible Heritage</h2>
<p>Some heritage is not just a building or object. It lives in stories, songs, rituals, recipes, crafts,
dances, languages, memories, and everyday practices. This is called <b>intangible heritage</b>.</p>
<p>You cannot always 3D scan intangible heritage directly, but you can document the objects, spaces, and
people connected to it. Examples:</p>
<ul>
<li>A traditional bread recipe → scan the oven, tools, table, or bakery space</li>
<li>A weaving practice → scan the loom, textile patterns, tools, or finished pieces</li>
<li>A family story → scan the home, courtyard, photograph, object, or place connected to the memory</li>
<li>A festival or ritual → scan decorations, costumes, instruments, gathering spaces, or symbolic objects</li>
<li>A disappearing craft → scan the tools, workshop, materials, and finished work</li>
</ul>
<p>When documenting intangible heritage, include context with your upload: what the tradition is called, who
practices it, where it happens, how you learned about it, why it matters, and any story, memory, or quote
that should go with the scan.</p>
<p><b>Always get permission</b> before recording people, private spaces, ceremonies, sacred practices, or
personal stories. Tanit XR is not just preserving objects — we are preserving the worlds, memories, and
meanings around them.</p>
<h3>🧱 Step-by-Step Scanning Instructions</h3>
<h4>1. Open Scaniverse</h4>
<ul>
<li>Tap the “+” button to start a new scan.</li>
<li>Choose <b>“Mesh”</b> (not “Splat”) — this is what we need for Tanit XR.</li>
<li>Select the size of your object: <b>Small Object</b> (pottery, carvings, statues), <b>Medium Object</b>
(doors, columns, mosaics), or <b>Large Area</b> (facades, walls, monuments).</li>
</ul>
<h4>2. Begin the Scan</h4>
<ul>
<li>Move slowly around the object while recording a video.</li>
<li>Get multiple angles: walk around, crouch down, raise your phone, etc.</li>
<li>Avoid fast movements and make sure to capture all sides.</li>
<li>In bright sun, try to scan in partial shade or overcast light.</li>
</ul>
<h4>3. Save Without Processing (Important!)</h4>
<ul>
<li>If you’re outside and don’t have strong Wi-Fi or data, tap <b>“Save to process later.”</b></li>
<li>Processing uses a lot of data — it’s best to wait until you’re home with Wi-Fi.</li>
</ul>
<h3>🗂️ Processing and Exporting</h3>
<h4>4. Back at Home: Process Your Scan</h4>
<ul>
<li>Open the Scaniverse Library (bottom menu).</li>
<li>Tap your saved scan, tap the name, and give it a clear title (e.g., “Ksar Ouled Soltane – Main Door”).</li>
<li>Tap “Process” and wait for the app to complete the 3D model.</li>
</ul>
<h4>5. Export the Model</h4>
<ul>
<li>Once processed, tap “Share” &gt; “Export Model.”</li>
<li>Select <b>FBX</b> format and keep <b>textures enabled</b>.</li>
<li>Name it “Scan Title_Location”.</li>
</ul>
<h4>6. Share Your Model</h4>
<p>Email your exported file (or a link to it) along with a short description of the model, any historical
info you know, and your name to <a href="mailto:{EMAIL}?subject=New%20scan%20submission">{EMAIL}</a>.
For large files, share a Google Drive, Dropbox, or WeTransfer link.</p>
<h3>✅ Tips for Great Scans</h3>
<ul>
<li>Scan slowly and steadily</li>
<li>Avoid people or shadows in your scan</li>
<li>Focus on texture and angles — walk around the object fully</li>
<li>Natural daylight is good, but harsh sun causes glare — avoid scanning at noon</li>
</ul>
</div></div></section>"""
    page("scanning-guide.html", "Tanit XR Scanning Guide", body, active="volunteer.html")


def build_splats():
    body = f"""
{page_hero("Splats With Phones", "Splats With Phones", bg="Screenshot-2025-12-10-at-8.17.41-PM.png")}
<section class="pad"><div class="wrap"><div class="prose">
<p>This 6-week online course introduces splats using smartphones, taught by <b>Mark Jeffcock</b>.</p>
<p>Participants will learn how to capture real-world objects using a phone, turn them into 3D models and
Gaussian splats, and review scans together in an immersive learning environment.</p>
<p>The cohort meets once a week at 7PM Tunisia Time (2PM Eastern) for 1 hour, for 6 weeks. No prior
experience is required. Attendance and engagement matter more than technical background.</p>
<p>Due to limited spots, we review applications holistically based on availability, background, and
motivation. More details are shared with accepted participants.</p>
<div class="notice"><b>Want to join the next cohort?</b> Email
<a href="mailto:{EMAIL}?subject=Splats%20With%20Phones%20application" style="color:var(--gold-dark)">{EMAIL}</a>
with your name, time zone, a short bio, why you want to join, and whether you can attend at least 5 of the
6 live sessions.</div>
</div></div></section>"""
    page("splats-with-phones.html", "Splats With Phones", body, active="volunteer.html")


def build_el_jem():
    pdfs = {
        "English": "El-Jem-2026-Paper_English.pdf",
        "Français": "El-Jem-2026-Paper_French.pdf",
        "دارجة تونسية": "El-Jem-2026-Paper_Arabic.pdf",
    }
    btns = "".join(
        f'<a class="btn btn-gold" style="margin:0 12px 12px 0" href="assets/pdf/{f}" target="_blank">{lang}</a>'
        for lang, f in pdfs.items())
    body = f"""
{page_hero("El Jem Conference", "El Jem Conference", bg="el-jem.jpg")}
<section class="pad"><div class="wrap"><div class="prose">
<div class="eyebrow">English</div>
<p>This paper was presented at the El Jem Conference in April 2026 and explores how digital documentation,
extended reality (XR), and citizen science can support scalable, community-driven heritage preservation in
Tunisia and beyond. Using Tanit XR as a case study, the paper highlights how accessible technologies and
volunteer training can expand documentation efforts, reach underrepresented sites, and connect global
audiences to Tunisian heritage.</p>
<div class="eyebrow" style="margin-top:34px">Français</div>
<p>Cet article a été présenté à la conférence d’El Jem en avril 2026. Il explore comment la documentation
numérique, la réalité étendue (XR) et la science participative peuvent soutenir une préservation du
patrimoine évolutive et portée par les communautés, en Tunisie et au-delà. À travers l’exemple de Tanit XR,
l’article montre comment des technologies accessibles et la formation de bénévoles permettent d’élargir les
efforts de documentation, d’inclure des sites sous-représentés et de connecter des publics du monde entier
au patrimoine tunisien.</p>
<div class="eyebrow" style="margin-top:34px">دارجة تونسية</div>
<p dir="rtl" lang="ar">الورقة هاذي تقدمت في مؤتمر الجم في أفريل 2026 وتتحدث كيفاش التوثيق الرقمي والواقع
الممتد (XR) والعلوم التشاركية ينجموا يدعموا حفظ التراث بطريقة مجتمعية وقابلة للتوسع في تونس وخارجها.</p>
<h2>Download the full paper</h2>
<p>{btns}</p>
</div></div></section>"""
    page("el-jem-conference.html", "El Jem Conference", body, active="about.html")


def build_unique_mappers():
    body = f"""
{page_hero("TanitXR &amp; the Unique Mappers", "TanitXR &amp; the Unique Mappers")}
<section class="pad"><div class="wrap"><div class="prose">
<p>TanitXR is a project, fiscally sponsored by Florida Community Innovation, that empowers volunteers and
students to scan at-risk heritage sites. The goal is not only to digitally preserve these places, but also
to increase appreciation for them by bringing them into XR environments and experiences.</p>
<p><b>The pilot country is Tunisia, and now we are excited to expand to Nigeria with the help of the Unique
Mappers!</b></p>
<p><a href="assets/pdf/TanitXR_One-Pager_English-French-Arabic.pdf" target="_blank">Linked here is a PDF with
background on TanitXR’s mission</a>. Read on to learn about the Unique Mappers and the scope of the TanitXR
collaboration.</p>
<img src="{img('164961718_137972651589064_4119697293414013034_n.jpg', 1200)}" alt="Unique Mappers Network">
<h2>About the Unique Mappers</h2>
<p>The Unique Mappers Network was founded in 2017 by Victor Sunday during his PhD studies at the University
of Nigeria, Enugu. Initially, the network focused on geographic information systems (GIS) and crowdsourcing
through <a href="https://scistarter.org/openstreetmap" target="_blank" rel="noopener">OpenStreetMap</a>,
with a goal of mapping streets and buildings.</p>
<p>Over time, it grew into a diverse community of more than 500 citizen scientists across Nigeria. They
engage in participatory mapping projects for disaster response, humanitarian action, and research, with a
specific focus on Sustainable Development Goals (SDGs).</p>
<p>What sets the Unique Mappers apart is their ability to mobilize volunteers from diverse
backgrounds—including students, women, and youth—for impactful mapping projects.</p>
<p>They’ve expanded their scope to include efforts like mapping flood-affected regions, monitoring oil
spills, and even mapping stalled blood vessels in the brain to support Alzheimer’s research through the
<a href="https://scistarter.org/stall-catchers-by-eyesonalz" target="_blank" rel="noopener">Stall
Catchers</a> project.
<a href="https://pages.scistarter.org/unique-mappers-of-nigeria-and-scistarter-a-collaborative-journey-in-citizen-science/"
target="_blank" rel="noopener">Learn more about their citizen science work</a>.</p>
<h2>Unique Mappers &amp; TanitXR Collaboration</h2>
<p>Unique Mappers volunteers are receiving a $500 mini-grant from Florida Community Innovation, TanitXR’s
fiscal sponsor. Before the end of 2026, they will make at least 50 scans of heritage sites and help optimize
them, optionally joining weekly stand-up meetings on Thursdays at 5 PM WAT (emailing
<a href="mailto:info@floridainnovation.org">info@floridainnovation.org</a> to receive the Zoom link).</p>
<p>The volunteers will:</p>
<ul>
<li>Capture 3D scans of heritage sites using photogrammetry (<a href="scanning-guide.html">full scanning
guide</a>). We plan to email the team behind <a href="http://museum.ng" target="_blank"
rel="noopener">museum.ng</a> and see what heritage sites they’re okay with us scanning, or if we need to do
non-restricted heritage sites that are closer to the Unique Mappers’ homes. There are also potential
partners like the <a href="https://www.instagram.com/discoverymuseum.ng/" target="_blank"
rel="noopener">Discovery Museum</a> that we hope to speak with.</li>
<li>Engage in 3D modeling, cultural preservation, and storytelling for an online gallery of Nigerian heritage</li>
<li>Present their work in a global December 2026 webinar</li>
</ul>
<p><b>We are excited and the best is yet to come!</b></p>
</div></div></section>"""
    page("unique-mappers.html", "TanitXR & the Unique Mappers", body, active="about.html")


def build_immersegt():
    body = f"""
{page_hero("ImmerseGT 2026", "ImmerseGT 2026", bg="IMG_9631.jpg")}
<section class="pad"><div class="wrap"><div class="prose">
<p>TanitXR is a project, fiscally sponsored by Florida Community Innovation, that empowers volunteers and
students to scan at-risk heritage sites. The goal is not only to digitally preserve these places, but also
to increase appreciation for them by bringing them into XR environments and experiences.</p>
<p>The pilot country for scanning is Tunisia, and contributors from around the world help turn these scans
into immersive experiences.
<a href="assets/pdf/TanitXR_One-Pager_English-French-Arabic.pdf" target="_blank">The one-pager summarizing
our mission is here</a>.</p>
<p><b>TanitXR sponsored a track at <a href="https://www.immersegt.org/" target="_blank"
rel="noopener">Immerse GT</a> from April 10–12!</b> Immerse GT was a 36-hour XR hackathon at Georgia Tech
that brought together designers, developers, and storytellers to build immersive experiences. We gave a $300
prize to the winning team for our track.</p>
<p>For our track, we invited participants to work with real TanitXR 3D models
(<a href="{SKETCHFAB}" target="_blank" rel="noopener">sketchfab.com/TanitXR</a> and the models we have
optimized so far: <a href="https://skfb.ly/pIxPR" target="_blank" rel="noopener">https://skfb.ly/pIxPR</a>).
We wanted them to create creative experiences that deepen appreciation for Tunisian heritage, which has been
overlooked and misrepresented on the global stage.</p>
<p>We are interested in projects that help people explore, understand, or care about heritage in new ways.
That might mean immersion, storytelling, education, interaction, public contribution, or something none of
us has thought of yet.</p>
<h2>Background</h2>
<p>Named for Tanit, the goddess of protection in ancient Carthage (where modern-day Tunisia now is), TanitXR
was founded in 2025 by <a href="person-ines-said.html">Ines Said</a>, a Tunisian XR developer, to preserve
the historic ruins she grew up loving.</p>
<p>The project focuses on places that are slowly deteriorating due to climate exposure, rising seas, extreme
weather, development, and lack of preservation resources. After local volunteers scan objects and landscapes
with photogrammetry and publish them as interactive models, the global community helps create a permanent
digital record that can be explored online and increase appreciation of shared human heritage in Tunisia.</p>
<p>Fundamentally, this work involves teaching people how to document heritage themselves. Tunisian and other
students, artists, and volunteers learn to use accessible tools such as smartphone scanning to capture
objects and spaces in their communities. The result is both a growing archive of Tunisian heritage and a
participatory process that connects people – both locally in Tunisia and on the global stage – with
historical sites.</p>
<h2>Dr. Caroline Nickerson’s Workshop at Immerse GT</h2>
<p>As part of the event, <a href="person-dr-caroline-nickerson.html">Caroline Nickerson, PhD</a>, led a
workshop connected to the TanitXR track on Saturday, April 11, at 2 PM ET in ISyE Main 228.</p>
<p>The workshop focused on citizen science, public participation, and XR. TanitXR’s model focuses on
community empowerment, and Caroline shared best practices and lessons learned from all her involvements.</p>
<img src="{img('IMG_6884.jpg', 1200)}" alt="ImmerseGT 2026" loading="lazy">
<h2>ImmerseGT 2026 Results</h2>
<p>We were thrilled to see so many creative submissions for the TanitXR track at ImmerseGT 2026. All
participants had a chance to explore powerful ways to use immersive technology to preserve, interpret, and
share Tunisian heritage with global audiences.</p>
<p><b>Track Winner: <a href="https://devpost.com/software/iamnotia-from-ruin-to-memory" target="_blank"
rel="noopener">From Mystery to History</a></b></p>
<p>From Mystery to History was selected as the winner of the TanitXR track for its innovative use of XR,
generative AI, and photogrammetry to reimagine cultural heritage preservation.</p>
<p>The project stood out for its creativity, strong execution, and meaningful alignment with TanitXR’s
mission to preserve and share Tunisia’s historical legacy through immersive experiences. We are incredibly
proud of the team and excited to see how this project continues to evolve!</p>
<p>Other projects from the TanitXR Track also demonstrated XR’s incredible potential to bring heritage
preservation to life. We are deeply grateful to every participant who contributed ideas, creativity, and
passion to this challenge.
<a href="https://immersegt-2026.devpost.com/submissions/search?prize_filter%5Bprizes%5D%5B%5D=100446"
target="_blank" rel="noopener">Review submissions here</a>.</p>
<img src="{img('IMG_6912.jpg', 1200)}" alt="ImmerseGT participants" loading="lazy">
<h2>Stay Involved After the Hackathon</h2>
<p>TanitXR is not just a hackathon prompt. It is an active and growing project, and we would love to stay
connected with participants who want to keep building with us after ImmerseGT.</p>
<p>There are many ways to contribute. Some volunteers help with photogrammetry and scanning. Others help
with research, writing, interpretation, outreach, or immersive development. If you are interested in staying
involved, sign up through our <a href="volunteer.html">volunteer page</a>.</p>
<p>We are always excited to work with people who care about heritage, storytelling, participation, and the
future of immersive technology.</p>
</div></div></section>"""
    page("immersegt-2026.html", "ImmerseGT 2026", body, active="immersegt-2026.html")


def build_about():
    body = f"""
{page_hero("About", "About", bg="sv-IMG_0511.jpg")}
<section class="pad"><div class="wrap center">
<h2 class="sec-title">Our Impact So Far</h2>
<p class="sec-sub">Tanit XR is a community effort to save Tunisia’s heritage from climate change, erosion,
and neglect. Together, we’re building a digital archive to protect it for generations.</p>
<div class="stats" style="margin-top:14px">
<div><b style="color:var(--gold-dark)">{stat('artifacts')}</b><span style="color:var(--gray)">Artifacts Scanned</span></div>
<div><b style="color:var(--gold-dark)">{stat('sites')}</b><span style="color:var(--gray)">Sites Documented</span></div>
<div><b style="color:var(--gold-dark)">{stat('volunteers')}</b><span style="color:var(--gray)">Volunteers</span></div>
<div><b style="color:var(--gold-dark)">{stat('reach')}</b><span style="color:var(--gray)">Global Reach</span></div>
</div>
</div></section>
<section class="pad" style="background:var(--cloud)"><div class="wrap"><div class="prose">
<h2 style="margin-top:0">We Are A Non-Profit Organization</h2>
<p>Tanit XR operates under fiscal sponsorship with Florida Community Innovation (FCI), a U.S. 501(c)(3)
nonprofit. This partnership allows us to accept tax-deductible donations while we grow toward becoming a
fully independent nonprofit organization.</p>
<p>Our mission is to preserve Tunisia’s endangered heritage through digital scans, immersive technology, and
education. With every artifact we scan and every volunteer we train, we are proving that heritage can be
safeguarded for future generations — no matter the threats of climate change and neglect.</p>
<p>Tanit XR advances <b>Sustainable Development Goal 11.4</b>, which focuses on safeguarding cultural and
natural heritage. We view the Sustainable Development Goals as an important shared framework for linking
local action to global impact.</p>
</div></div></section>
<section class="pad"><div class="wrap">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:50px;align-items:center">
<div>
<h2 class="sec-title">Why I Started Tanit XR</h2>
<p>I grew up walking past the ruins of Carthage every day. To me, they were just there – a backdrop of my
childhood. But slowly I began to notice how pieces were missing, how mosaics cracked and crumbled, how
nothing was truly protected. Tunisia’s history is not kept in vaults or guarded museums. It is left in the
open air, vulnerable to time, weather, and neglect. And every year, more of it disappears.</p>
<p>Tanit XR was born from the fear of losing this history forever and the belief that technology can change
the story. With 3D scanning, digital archiving, and immersive storytelling, we can preserve what remains and
share it with the world. Each scan is more than just data; it is a memory, a voice from the past, a way of
saying: we were here, and we matter.</p>
<p><b>– <a href="https://www.inessaid.com" target="_blank" rel="noopener"
style="color:var(--gold-dark)">Ines Said</a>, Founder</b></p>
</div>
<img src="{img('img_4196.jpg', 1000)}" alt="Ines scanning at Carthage" style="border-radius:14px" loading="lazy">
</div>
</div></section>
<section class="band pad"><div class="bg" style="background-image:url({img('img_4615-copy.jpg', 1800)})"></div>
<div class="wrap center">
<div class="eyebrow">Become a volunteer</div>
<h2 class="sec-title">Join us to protect Tunisia’s Heritage</h2>
<p class="sec-sub" style="color:rgba(255,255,255,.85)">You don’t need to be an archaeologist or a
technologist to make an impact. Our first scans were made with a phone. Whether on the ground in Tunisia or
helping remotely, every volunteer contributes to preserving history.</p>
<a class="btn btn-gold" href="volunteer.html">Volunteer</a>
</div></section>"""
    page("about.html", "About", body)


def build_contact():
    body = f"""
{page_hero("Contact", "Contact")}
<section class="pad"><div class="wrap">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:56px">
<div>
<h2 class="sec-title">Send us your Questions/Feedback</h2>
<p style="color:var(--gray)">We’ll get back to you as soon as we can.</p>
<form class="nice" action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Contact form — tanitxr.org">
<input type="hidden" name="_captcha" value="true">
<input type="text" name="_honey" style="display:none">
<label class="req" for="cname">Full Name</label>
<input id="cname" name="name" required>
<label class="req" for="cemail">Email Address</label>
<input id="cemail" name="email" type="email" required>
<label class="req" for="csub">Subject</label>
<input id="csub" name="_subject_line" required>
<label class="req" for="cmsg">Message</label>
<textarea id="cmsg" name="message" required></textarea>
<button class="btn btn-gold" type="submit">Send Message</button>
</form>
</div>
<div>
<img src="{img('aug-PXL_0811_174938.jpg', 900)}" alt="Sidi Bou Said, Tunisia"
style="border-radius:14px" loading="lazy">
<p style="margin-top:26px"><b>Email:</b> <a href="mailto:{EMAIL}" style="color:var(--gold-dark)">{EMAIL}</a><br>
<b>Phone:</b> {PHONE}</p>
</div></div>
</div></section>
<section class="band pad"><div class="wrap center">
<div class="eyebrow">Become a volunteer</div>
<h2 class="sec-title">Join us to protect Tunisia’s Heritage</h2>
<p class="sec-sub" style="color:rgba(255,255,255,.85)">You don’t need to be an archaeologist or a
technologist to make an impact. Our first scans were made with a phone. Whether on the ground in Tunisia or
helping remotely, every volunteer contributes to preserving history.</p>
<a class="btn btn-gold" href="volunteer.html">Apply Now</a>
</div></section>"""
    page("contact.html", "Contact", body)


def build_support():
    tiers = [
        ("$25", "Help cover basic costs for scanning a site: like transportation, mobile data for uploads, "
                "and backup storage."),
        ("$50", "Support detailed documentation of a site, enabling multiple 3D captures, archival research, "
                "and creating educational content to go with it."),
        ("$500", "Sponsor a field day with collaborators, covering travel, meals, and shared equipment to scan "
                 "and document endangered ruins. It also helps us start compensating local contributors for "
                 "their time and expertise."),
        ("$1,000", "Fund a full digital storytelling package for one site, including high-quality 3D scans, "
                   "animated walk-throughs, historical research, and immersive media production. This tier also "
                   "supports the purchase of better scanning tools so we can scale beyond just a phone."),
    ]
    tier_html = "".join(f'<div class="tier"><b class="amt">{a}</b><p>{d}</p></div>' for a, d in tiers)
    body = f"""
{page_hero("Support", "Support", bg="img_7396-copy.jpg")}
<section class="pad"><div class="wrap"><div class="prose">
<p>As climate change, conflict, and neglect threaten historic sites like ancient ruins, our shared global
heritage is at risk.</p>
<p>XR—a term that includes augmented and virtual reality—offers powerful tools to help. XR offers a way to
preserve disappearing heritage—by capturing sites in 3D, enriching visits with storytelling, and making
global history accessible from anywhere.</p>
<p>Named for the ancient Carthaginian goddess of protection and the moon, if we can protect heritage in
Tunisia—using immersive technology, community storytelling, and local leadership—we can build a model to
safeguard cultural sites around the world.</p>
<p class="center" style="margin:34px 0">
<a class="btn btn-gold" style="font-size:17px;padding:16px 44px" href="{DONATE_URL_SUPPORT}"
target="_blank" rel="noopener">DONATE HERE</a></p>
</div>
<div class="tiers" style="margin-top:30px">{tier_html}</div>
<p class="center" style="margin-top:34px;color:var(--gray);font-size:14px">Donations are tax-deductible
through our fiscal sponsor, Florida Community Innovation, a U.S. 501(c)(3) nonprofit.</p>
</div></section>"""
    page("support.html", "Support", body)


def build_misc():
    # coming soon
    body = f"""
{page_hero("Coming Soon", "Coming Soon")}
<section class="pad"><div class="wrap center" style="max-width:640px">
<h2 class="sec-title">👀 Something exciting is on the way.</h2>
<p class="sec-sub">This page will be live soon! In the meantime, explore our archive of 3D scans or join the
volunteer network helping to preserve Tunisia’s heritage.</p>
<a class="btn btn-gold" href="archive.html">Explore the Archive</a> &nbsp;
<a class="btn btn-line" href="index.html">Back Home</a>
</div></section>"""
    page("coming-soon.html", "Coming Soon", body, trending=False)

    # privacy (the old site's page was placeholder text — this is a real minimal policy)
    body = f"""
{page_hero("Privacy Policy", "Privacy Policy")}
<section class="pad"><div class="wrap"><div class="prose">
<p>Tanit XR (“we”) runs tanitxr.org to share our heritage-preservation work. We collect as little personal
information as possible.</p>
<h3>What we collect</h3>
<ul>
<li><b>Contact &amp; volunteer forms:</b> the name, email address, and message details you choose to send us.
We use them only to reply to you and to coordinate volunteer work, and we don’t sell or share them.</li>
<li><b>Volunteer profiles:</b> if you submit a profile for our Our People page, the name, role, bio, photo,
and links you provide are published on this website after review. Email us at
<a href="mailto:{EMAIL}">{EMAIL}</a> any time to update or remove your profile.</li>
</ul>
<h3>What we don’t do</h3>
<ul>
<li>No advertising or tracking cookies.</li>
<li>No sale of personal data.</li>
</ul>
<h3>Third parties</h3>
<p>This site is hosted on GitHub Pages, forms are delivered by FormSubmit, 3D models are embedded from
Sketchfab, and donations are processed by Tuesday (on behalf of our fiscal sponsor, Florida Community
Innovation). Each of these services has its own privacy policy.</p>
<p>Questions? Contact <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></div></section>"""
    page("privacy.html", "Privacy Policy", body, trending=False)

    # 404 with redirects from old WordPress URLs (root/English only)
    if LANG != "en":
        return
    redirects = {"/archive": "archive.html", "/about": "about.html", "/our-people": "people.html",
                 "/art-xr-impact-opportunities": "opportunities.html", "/news": "news.html",
                 "/volunteer": "volunteer.html", "/volunteer-with-us": "volunteer.html",
                 "/submit-volunteer-profile": "create-profile.html",
                 "/tanit-xr-scanning-guide": "scanning-guide.html",
                 "/photogrammetry-with-phones-by-mark-jeffcock": "splats-with-phones.html",
                 "/el-jem-conference": "el-jem-conference.html", "/uniquemappers": "unique-mappers.html",
                 "/immersegt-2026": "immersegt-2026.html", "/contact": "contact.html",
                 "/contact-2": "contact.html", "/donate": "support.html", "/support": "support.html"}
    for m in MODELS:
        redirects[f"/2025/09/14/{m['slug']}"] = m["href"]
    for n in NEWS:
        d = n["date"].replace("-", "/")
        redirects[f"/{d[:4]}/{d[5:7]}/{d[8:10]}/{n['slug']}"] = n["href"]
    redirects = {k: (v[:-5] + "/" if v.endswith(".html") else v) for k, v in redirects.items()}
    body = f"""
{page_hero("Page Not Found", "404")}
<section class="pad"><div class="wrap center" style="max-width:640px">
<img src="{img('sv-IMG_9612.jpg', 900)}" alt="A cat resting on a Roman column at Carthage"
style="border-radius:14px;margin:0 auto 30px">
<h2 class="sec-title">We couldn’t find that page.</h2>
<p class="sec-sub">Even our archive cat couldn’t dig it up. It may have moved when we rebuilt the site.</p>
<a class="btn btn-gold" href="index.html">Back Home</a> &nbsp;
<a class="btn btn-line" href="archive.html">Explore the Archive</a>
</div></section>
<script>
const R={json.dumps(redirects)};
const base=location.pathname.toLowerCase().includes('/tanitxr.org/')?'/tanitxr.org/':'/';
const p=location.pathname.replace(/\\/$/,'').toLowerCase();
for(const k in R){{ if(p===k||p.endsWith(k)){{location.replace(base+R[k]);break}} }}
</script>"""
    page("404.html", "Page Not Found", body, trending=False)


def build_redirects():
    """Emit a stub at every URL path of the old WordPress site so no shared link
    ever breaks after the domain cutover. Paths come from the scraped WP data."""
    CANON = "https://tanitxr.org"
    targets = {}  # old path (no leading/trailing slash) -> new target (root-relative file)

    page_map = {
        "home": "index.html", "home-2": "index.html", "archive": "archive.html",
        "about": "about.html", "news": "news.html", "our-people": "people.html",
        "art-xr-impact-opportunities": "opportunities.html",
        "volunteer": "volunteer.html", "volunteer-with-us": "volunteer.html",
        "submit-volunteer-profile": "create-profile.html",
        "tanit-xr-scanning-guide": "scanning-guide.html",
        "photogrammetry-with-phones-by-mark-jeffcock": "splats-with-phones.html",
        "el-jem-conference": "el-jem-conference.html",
        "uniquemappers": "unique-mappers.html", "immersegt-2026": "immersegt-2026.html",
        "contact": "contact.html", "contact-2": "contact.html",
        "donate": "support.html", "support": "support.html",
        "privacy-policy-2": "privacy.html", "coming-soon": "coming-soon.html",
        "opportunity": "opportunities.html", "person": "people.html",
    }

    def path_of(link):
        p = re.sub(r"^https?://[^/]+", "", link).strip("/")
        return p

    for p in load("pages.json"):
        slug = p["slug"]
        if slug in page_map:
            targets[path_of(p["link"])] = page_map[slug]
    for extra in ("home", "coming-soon", "donate", "support", "opportunity", "person"):
        targets.setdefault(extra if extra != "coming-soon" else "home/coming-soon",
                           page_map.get(extra, "index.html"))

    by_slug = {m["slug"]: m["href"] for m in MODELS}
    by_slug.update({n["slug"]: n["href"] for n in NEWS})
    for p in load("posts.json"):
        if p["slug"] in by_slug:
            targets[path_of(p["link"])] = by_slug[p["slug"]]

    people_files = {p["href"] for p in TEAM + COMMUNITY}
    for p in load("person.json"):
        href = f"person-{slugify(htmod.unescape(p['title']['rendered']))}.html"
        targets[path_of(p["link"])] = href if href in people_files else "people.html"

    for o in load("opportunity.json"):
        targets[path_of(o["link"])] = f"opportunities.html#opp-{o['slug']}"

    for c in load("categories.json"):
        if "link" in c:
            targets[path_of(c["link"])] = "news.html" if c["name"] == "News" else "archive.html"

    def pv(t):
        f, _, anchor = t.partition("#")
        stem = f[:-5]
        return ("" if stem == "index" else stem + "/") + (("#" + anchor) if anchor else "")

    n = 0
    for path, target in targets.items():
        if not path:
            continue
        target = pv(target)
        depth = len(path.split("/"))
        rel = "../" * depth + target
        canon_file = target.split("#")[0]
        out_dir = os.path.join(DOCS, path)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w") as f:
            f.write(f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Tanit XR</title>
<link rel="canonical" href="{CANON}/{canon_file}">
<meta http-equiv="refresh" content="0;url={rel}">
<script>location.replace("{rel}");</script>
</head><body><p><a href="{rel}">Continue to Tanit XR</a></p></body></html>""")
        n += 1
    print(f"  {n} legacy-URL redirects written")

    # sitemap of canonical pages (all three languages)
    urls = [f"{CANON}/{p}" for p in sorted(set(SITEMAP))]
    with open(os.path.join(DOCS, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"<url><loc>{esc(u)}</loc></url>\n" for u in urls)
                + "</urlset>\n")
    with open(os.path.join(DOCS, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {CANON}/sitemap.xml\n")


# ---------------------------------------------------------------- main

def main():
    os.makedirs(IMG_OUT, exist_ok=True)
    os.makedirs(PDF_OUT, exist_ok=True)
    # static assets
    with open(os.path.join(DOCS, "assets", "style.css"), "w") as f:
        f.write(CSS)
    with open(os.path.join(DOCS, "assets", "site.js"), "w") as f:
        f.write(JS)
    for pdf in ["El-Jem-2026-Paper_English.pdf", "El-Jem-2026-Paper_French.pdf",
                "El-Jem-2026-Paper_Arabic.pdf", "TanitXR_One-Pager_English-French-Arabic.pdf"]:
        src = os.path.join(MEDIA, pdf)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(PDF_OUT, pdf))
    with open(os.path.join(DOCS, ".nojekyll"), "w") as f:
        f.write("")
    # live-profile queue: emptied at build (everything in profiles/ is baked in now)
    with open(os.path.join(DOCS, "profiles-live.json"), "w") as f:
        f.write("[]")
    with open(os.path.join(DOCS, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n")

    global LANG
    for LANG in LANG_DIRS:
        build_home()
        build_archive()
        build_model_pages()
        build_news()
        build_people()
        build_opportunities()
        build_volunteer()
        build_create_profile()
        build_scanning_guide()
        build_splats()
        build_el_jem()
        build_unique_mappers()
        build_immersegt()
        build_about()
        build_contact()
        build_support()
        build_misc()
        print(f"  {LANG}: done")
    LANG = "en"
    build_redirects()

    n_pages = len([f for f in os.listdir(DOCS) if f.endswith(".html")])
    n_fr = len([f for f in os.listdir(os.path.join(DOCS, "fr")) if f.endswith(".html")])
    n_ar = len([f for f in os.listdir(os.path.join(DOCS, "ar")) if f.endswith(".html")])
    size = subprocess.run(["du", "-sh", DOCS], capture_output=True, text=True).stdout.split()[0]
    print(f"\nBuilt {n_pages} en + {n_fr} fr + {n_ar} ar pages -> docs/ ({size})")


if __name__ == "__main__":
    main()
