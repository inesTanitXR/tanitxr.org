#!/usr/bin/env python3
"""Static site generator for tanitxr.org, replaces the WordPress/Elementor/JetEngine site.

Edit content in this file, then run:  python3 build.py
Output goes to docs/ (GitHub Pages serves main:/docs).

Data sources (scraped from the old WordPress site 2026-09-08):
  wp-data/*.json , posts, pages, people, opportunities, media, terms
  media/         , downloaded media library (web-sized)
  profiles/      , volunteer profile submissions (JSON), merged into Our People
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
# Kit (newsletter), account tanit-xr.kit.com, form "tanitxr.org sign-up" (uid f2587d8800). Tag IDs: fill in once
# Ines creates the tags in Kit (Subscribers → Tags; the id is in the tag's URL). Empty = checkbox hidden.
KIT_FORM_ID = "9912073"
KIT_TAGS = {"opportunities": "23332230", "news": "23332232"}
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
        "üîé": "", "üìç": "", "üè∫": "", "‚ú®": "", "ü§ù": "",
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
# each other), for these, a dated copy is fetched from the exact URL instead
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

/* header, nav split around a centered logo, like the original site */
header.site{position:fixed;top:0;left:0;right:0;z-index:60;transition:background .25s,box-shadow .25s;padding:0}
header.site .bar{position:relative;display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;
  gap:54px;padding:12px 32px}
header.site .logo{display:flex;justify-content:center;text-decoration:none}
header.site .logo img{height:92px;width:auto;transition:height .25s}
header.site.scrolled .logo img,header.site.solid .logo img{height:68px}
.hside{display:flex;align-items:center;gap:26px;width:100%;min-width:0}
/* both link groups sit the same distance from the logo; socials pin to the far left, donate/langs to the far right */
.hl{justify-content:flex-end}
.hl .socials{margin-inline-end:auto}
.hr{justify-content:flex-start}
.hcta{display:flex;align-items:center;gap:16px;margin-inline-start:auto}
.hlinks{display:flex;align-items:center;gap:44px}
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
@media(max-width:1320px){.hlinks{gap:24px}.hlinks a{font-size:15px}.hcta{gap:10px}header.site .bar{gap:34px}
  header.site .donate{padding:8px 16px}header.site .logo img{height:80px}
  header.site.scrolled .logo img,header.site.solid .logo img{height:62px}}
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
@media(max-width:1240px){
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
/* homepage hero: side-lit on wide screens, evenly darkened + centered when narrower */
/* the photo url() must stay in the page's inline style: a url() inside a custom property resolves
   relative to this stylesheet (assets/), so only the scrim gradients live here */
.hero .bg.hero-photo{opacity:1;background-position:right center;
  --scrim:linear-gradient(97deg,#0b0e11 0%,#0b0e11 32%,rgba(11,14,17,.82) 52%,rgba(11,14,17,.22) 82%,rgba(11,14,17,.55) 100%),
    linear-gradient(180deg,rgba(11,14,17,.55),rgba(11,14,17,0) 30%,rgba(11,14,17,0) 55%,rgba(11,14,17,.85))}
@media(max-width:1450px){
  .hero .bg.hero-photo{background-position:center;
    --scrim:linear-gradient(rgba(11,14,17,.8),rgba(11,14,17,.62) 55%,rgba(11,14,17,.86))}
}
.hero h1{font-size:clamp(44px,7.5vw,84px);margin-bottom:26px}
.hero p{font-size:17px;color:rgba(255,255,255,.88);max-width:720px;margin:0 auto 34px}
.hero .ctas{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}

/* page hero */
.page-hero{background:var(--ink);color:#fff;padding:190px 0 66px;position:relative}
.page-hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.34}
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
.card h3 a{color:inherit;text-decoration:none}
.card h3 a:hover{color:var(--gold-dark)}
.card .meta{font-size:13px;color:var(--gray)}
/* in-place 3D viewer: the ▶ button swaps the thumbnail for the Sketchfab iframe (site.js) */
.card .ph{position:relative}
.card .ph a{display:block;height:100%}
.card .ph.blank{display:flex;align-items:center;justify-content:center;background:var(--ink)}
.card .play{position:absolute;right:12px;bottom:12px;background:var(--gold);color:var(--ink);border:0;border-radius:4px;
  padding:8px 13px;font:700 13px var(--sans);cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.25)}
.card .play:hover{background:var(--gold-dark)}
.card .ph.live{aspect-ratio:4/3;background:#000}
.card .ph.live iframe{width:100%;height:100%;border:0;display:block}
.card:hover .ph.live{transform:none}
.prose .btn-gold,.prose .btn-gold:hover{color:var(--ink)}

/* homepage v2: recognition strip, community mosaic, press cards, funding transparency */
.strip{display:flex;flex-wrap:wrap;justify-content:center;gap:12px 14px;align-items:center}
.strip .badge{display:inline-flex;align-items:center;gap:9px;font-size:14px;font-weight:700;color:var(--ink);text-decoration:none;
  border:1px solid var(--mist);border-radius:30px;padding:9px 16px;background:#fff;transition:.2s}
.strip .badge:hover{border-color:var(--gold);box-shadow:0 6px 18px rgba(17,21,24,.08)}
.strip .badge span{color:var(--gray);font-weight:400}
.logos{display:flex;flex-wrap:wrap;justify-content:center;gap:26px 22px;align-items:flex-start;margin-top:26px}
.logos a{display:flex;flex-direction:column;align-items:center;gap:10px;text-decoration:none;color:var(--gray);font-size:12.5px;width:148px;text-align:center}
.logos img,.logos .wordmark{height:44px;display:flex;align-items:center;justify-content:center}
.logos img{width:auto;max-width:148px;object-fit:contain;filter:grayscale(1) brightness(.25);opacity:.8;transition:.25s}
.logos .wordmark{font-family:var(--serif);font-size:17px;line-height:1.15;color:#2c343b;opacity:.85;text-align:center;max-width:148px}
.logos a:hover img{filter:none;opacity:1}
.logos a:hover .cap{color:var(--ink)}
.cream{background:#fbf6ed}
.stats.light b{color:var(--gold-dark)}.stats.light>div>span{color:var(--gray)}
/* the original site's impact band: big gold serif numbers over a site photo */
.band.photo .bg{opacity:.55;background-position:center 35%}
.band.photo::after{content:"";position:absolute;inset:0;background:rgba(11,14,17,.42)}
.band.photo .wrap{z-index:1}
.statsband{padding:110px 0}
.stats.big{gap:30px 20px}
.stats.big b{font-size:clamp(56px,6.5vw,96px);line-height:1;margin-bottom:14px}
.stats.big>div>span{font-family:var(--serif);font-size:clamp(20px,2vw,28px);text-transform:none;letter-spacing:0;color:#fff}
@media(max-width:700px){.statsband{padding:70px 0}}
.plinks{display:flex;flex-wrap:wrap;gap:12px}
.plinks a{width:44px;height:44px;border:1px solid var(--mist);border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--ink);transition:.2s}
.plinks a:hover{background:var(--gold);border-color:var(--gold)}
.plinks svg{width:19px;height:19px;fill:currentColor}
.mosaic{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:170px;gap:12px}
.mosaic img{width:100%;height:100%;object-fit:cover;border-radius:10px;display:block}
.mosaic img:first-child{grid-column:span 2;grid-row:span 2}
@media(max-width:700px){.mosaic{grid-template-columns:1fr 1fr;grid-auto-rows:140px}}
.acts{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-top:30px}
.act{background:#fff;border:1px solid var(--mist);border-radius:10px;padding:22px 22px 20px}
.act .ic{font-size:26px;margin-bottom:10px}
.act b{display:block;font-size:17px;margin-bottom:6px;font-family:var(--serif);font-weight:400}
.act p{color:var(--gray);font-size:14.5px}
.press{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}
.press a,.press div.item{display:block;background:#fff;border:1px solid var(--mist);border-radius:10px;padding:22px;text-decoration:none;color:var(--ink);transition:.2s}
.press a:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(17,21,24,.1)}
.press .k{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold-dark);font-weight:700}
.press h3{font-size:18px;margin:8px 0 6px}
.press p{color:var(--gray);font-size:14.5px}
.vid{width:100%;border-radius:12px;background:#000;display:block;aspect-ratio:16/9}
.shots.museum img{aspect-ratio:16/9}
.timeline{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;margin-top:26px}
.timeline div{background:#fff;border:1px solid var(--mist);border-radius:10px;overflow:hidden}
.timeline img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.timeline b{display:block;padding:14px 16px 4px;font-family:var(--serif);font-weight:400;font-size:17px}
.timeline p{padding:0 16px 16px;color:var(--gray);font-size:14px}
.embed16{position:relative;padding-top:56.25%;border-radius:12px;overflow:hidden;background:#000}
.embed16 iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.money{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-top:28px}
.money div{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:10px;padding:18px 20px}
.money b{display:block;font-family:var(--serif);font-size:30px;color:var(--gold);font-weight:400;margin-bottom:4px}
.money span{font-size:14.5px;color:rgba(255,255,255,.8)}
.steps{counter-reset:s;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;margin-top:26px}
.steps div{background:var(--cloud);border-radius:10px;padding:22px;position:relative}
.steps div::before{counter-increment:s;content:counter(s);font-family:var(--serif);font-size:34px;color:var(--gold-dark);display:block;margin-bottom:6px}
/* split section (photo | cream panel), like the original "Why It Matters" */
.split{display:grid;grid-template-columns:1fr 1fr;min-height:560px}
.split .simg{background-size:cover;background-position:center;min-height:360px}
.split .stx{background:#fbf6ed;padding:96px 8vw 96px 64px}
.split .stx h3{font-size:26px;margin:34px 0 12px}
.split .stx p{color:var(--gray);font-size:16.5px;max-width:620px}
@media(max-width:900px){.split{grid-template-columns:1fr}.split .stx{padding:60px 24px}}
.infographic{margin:60px auto 0;max-width:1000px;border-radius:14px;overflow:hidden;box-shadow:0 14px 44px rgba(17,21,24,.12);background:#fff}
.infographic img{display:block;width:100%}
.stats.icons img{height:54px;width:auto;display:block;margin:0 auto 12px}
.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:36px 0}
.shots img{width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:10px}
/* archive index tiles */
.arch-index{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px;margin:0 0 34px}
.ix{display:flex;gap:20px;align-items:center;padding:22px 26px;border-radius:12px;background:#fff;
  border:1px solid var(--mist);text-decoration:none;color:var(--ink);transition:.2s}
.ix:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(17,21,24,.12)}
.ix b{font-family:var(--serif);font-size:44px;line-height:1;color:var(--gold-dark);min-width:74px}
.ix span{font-size:14px;color:var(--gray);line-height:1.45}
.ix span strong{display:block;color:var(--ink);font-size:17px;margin-bottom:3px}
.ix.gold{background:var(--ink);color:#fff;border-color:var(--ink)}
.ix.gold span{color:rgba(255,255,255,.72)}.ix.gold span strong{color:#fff}.ix.gold b{color:var(--gold)}
.filters a.fbtn{text-decoration:none;display:inline-block}
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
.stats>div>span{font-size:15px;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.75)}

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
.board-tools[hidden]{display:none}
/* modern toolbar: search + segmented sort, then pill filters */
.toolbar{display:flex;flex-wrap:wrap;gap:14px 24px;align-items:center;justify-content:space-between;margin-bottom:14px}
.search{position:relative;flex:1;min-width:260px;display:block}
.search .ico{position:absolute;left:14px;top:50%;transform:translateY(-50%);width:18px;height:18px;color:var(--gray)}
.search .ico svg{width:18px;height:18px;fill:currentColor}
.search input{width:100%;padding:13px 16px 13px 42px;border:1px solid var(--mist);border-radius:30px;font-size:15px;background:#fff}
.search input:focus{outline:2px solid var(--gold)}
.sortwrap{display:flex;align-items:center;gap:10px}
.seg{display:inline-flex;border:1px solid var(--mist);border-radius:30px;padding:4px;background:#fff}
.seg button{border:0;background:none;padding:8px 16px;border-radius:24px;font:600 13.5px var(--sans);color:var(--gray);cursor:pointer}
.seg button.on{background:var(--ink);color:#fff}
.fgroups{display:flex;flex-wrap:wrap;gap:12px 28px;align-items:center;margin:0 0 26px}
.fgroup{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.flabel{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gray);font-weight:700;margin-right:2px}
.pills{display:flex;flex-wrap:wrap;gap:6px}
.pill{border:1px solid var(--mist);background:#fff;border-radius:30px;padding:6px 13px;font:500 13px var(--sans);color:var(--ink);cursor:pointer;transition:.15s}
.pill:hover{border-color:var(--gold)}
.pill.on{background:var(--gold);border-color:var(--gold);font-weight:700}
.clearf{border:0;background:none;color:var(--gold-dark);font:700 13px var(--sans);cursor:pointer;text-decoration:underline}
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
#board,#closed{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:20px;align-items:stretch}
#closed .opp.hid{display:none}
.closed-h{margin:44px 0 16px;font-size:20px;color:var(--gray);font-weight:400}
.subtop{background:var(--cloud);border:1px solid var(--mist);border-radius:12px;padding:18px 22px;margin:0 0 24px;display:grid;grid-template-columns:minmax(200px,.8fr) 1.6fr;gap:22px;align-items:center}
.subtop form.nice{max-width:none}
@media(max-width:760px){.subtop{grid-template-columns:1fr}}
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
form.nice input[type=checkbox]{width:auto;padding:0;margin:0;accent-color:var(--gold-dark);transform:scale(1.15)}
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
// "View in 3D": swap a card thumbnail for the live Sketchfab viewer
document.addEventListener('click',e=>{
  const b=e.target.closest('[data-embed]');if(!b)return;
  e.preventDefault();
  const ph=b.closest('.ph');if(!ph)return;
  const f=document.createElement('iframe');
  f.src='https://sketchfab.com/models/'+b.dataset.embed+'/embed?autostart=1&ui_theme=dark&ui_infos=0&ui_watermark=0';
  f.allow='autoplay; fullscreen; xr-spatial-tracking';f.allowFullscreen=true;f.title='3D model';
  ph.innerHTML='';ph.classList.add('live');ph.appendChild(f);
});
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
ICO_WEB = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20m6.9 6h-3a15.6 15.6 0 0 0-1.4-3.6A8 8 0 0 1 18.9 8M12 4a14 14 0 0 1 1.9 4h-3.8A14 14 0 0 1 12 4M4.3 14a8 8 0 0 1 0-4h3.4a16.5 16.5 0 0 0 0 4zm.8 2h3a15.6 15.6 0 0 0 1.4 3.6A8 8 0 0 1 5.1 16m3-8h-3a8 8 0 0 1 4.4-3.6A15.6 15.6 0 0 0 8.1 8M12 20a14 14 0 0 1-1.9-4h3.8A14 14 0 0 1 12 20m2.3-6H9.7a14.7 14.7 0 0 1 0-4h4.6a14.7 14.7 0 0 1 0 4m.3 5.6a15.6 15.6 0 0 0 1.4-3.6h3a8 8 0 0 1-4.4 3.6m1.7-5.6a16.5 16.5 0 0 0 0-4h3.4a8 8 0 0 1 0 4z"/></svg>'
ICO_MAIL = '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2m0 4-8 5-8-5V6l8 5 8-5z"/></svg>'
ICO_GH = '<svg viewBox="0 0 24 24"><path d="M12 .5A12 12 0 0 0 8.2 23.9c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.4-1.8-1.4-1.8-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1.1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.8-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0c2.3-1.5 3.3-1.2 3.3-1.2.7 1.7.3 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5"/></svg>'
ICO_SF = '<svg viewBox="0 0 24 24"><path d="M12 2 2 7v10l10 5 10-5V7zm0 2.2 7.5 3.8L12 11.8 4.5 8zM4 9.6l7 3.5v6.7l-7-3.5zm9 10.2v-6.7l7-3.5v6.7z"/></svg>'
ICO_YT = '<svg viewBox="0 0 24 24"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8M9.6 15.6V8.4l6.2 3.6z"/></svg>'


def link_icon(u):
    """(icon svg, label) for a profile link, only the platforms a volunteer actually provided are shown."""
    if u.startswith("mailto:"):
        return ICO_MAIL, "Email"
    h = re.sub(r"^https?://(www\.)?", "", u).split("/")[0].lower()
    for k, ico, lab in (("linkedin.com", ICO_LI, "LinkedIn"), ("instagram.com", ICO_IG, "Instagram"),
                        ("github.com", ICO_GH, "GitHub"), ("sketchfab.com", ICO_SF, "Sketchfab"),
                        ("youtube.com", ICO_YT, "YouTube")):
        if k in h:
            return ico, lab
    return ICO_WEB, h


ICO_SEARCH = '<svg viewBox="0 0 24 24"><path d="M15.5 14h-.8l-.3-.3A6.5 6.5 0 1 0 14 15.5l.3.3v.8l5 5 1.5-1.5-5-5zm-6 0a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9"/></svg>'
ICO_LI = '<svg viewBox="0 0 24 24"><path d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5M.2 8h4.6v14.8H.2zm7.6 0h4.4v2h.1c.6-1.2 2.1-2.4 4.4-2.4 4.7 0 5.5 3.1 5.5 7.1v8.1h-4.6v-7.2c0-1.7 0-3.9-2.4-3.9s-2.8 1.9-2.8 3.8v7.3H7.8z"/></svg>'

# ---------------------------------------------------------------- shell

NAV = [
    ("Home", "index.html"),
    ("Archive", "archive.html"),
    ("Opportunities", "opportunities.html"),
    ("News", "news.html"),
    ("Get Involved", "volunteer.html", [
        ("Community", "community.html"),
        ("Volunteer", "volunteer.html"),
        ("Volunteer Profile (members)", "create-profile.html"),
        ("Scanning Guide", "scanning-guide.html"),
        ("Splats With Phones", "splats-with-phones.html"),
    ]),
    ("About", "about.html", [
        ("About", "about.html"),
        ("Our People", "team.html"),
        ("El Jem Conference", "el-jem-conference.html"),
        ("ImmerseGT 2026", "immersegt-2026.html"),
        ("TanitXR &amp; the Unique Mappers", "unique-mappers.html"),
        ("Virtual Museum", "museum.html"),
        ("Services", "services.html"),
        ("Press &amp; Recognition", "press.html"),
    ]),
    ("Contact", "contact.html"),
]


def lang_switcher(fname):
    """EN / FR / ع links pointing at this page's siblings in the other languages."""
    if fname == "404.html":  # no localized 404 pages, send to the homepages
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
    logo = img("tanitxr-logo_red_vertical.png", 300, as_jpeg=False)
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
<a href="community.html">Community</a>
<a href="museum.html">Virtual Museum</a>
<a href="news.html">News</a>
<a href="opportunities.html">Opportunities</a></div>
<div><h4>Get Involved</h4>
<a href="volunteer.html" style="color:var(--gold);font-weight:700">Volunteer →</a>
<a href="services.html">Services</a>
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
    # like the original site, the menu floats over the page hero photo wherever there is one
    transparent = transparent or 'class="page-hero"' in body
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

    doc = re.sub(r'(href|src)="((?:\.\./)*)((?:[A-Za-z0-9_-]+/)*)([A-Za-z0-9_-]+)\.html(#[^"]*)?"', _link_repl, doc)
    doc = re.sub(r'(href|src|poster)="(?:\.\./)*(assets/[^"]*)"', lambda m: f'{m.group(1)}="{P}{m.group(2)}"', doc)
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
        alias_path = os.path.join(DOCS, LANG_DIRS[LANG], fname)
        os.makedirs(os.path.dirname(alias_path), exist_ok=True)
        rel_target = posixpath.basename(stem) + "/"
        with open(alias_path, "w") as f:
            f.write(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
                    f'<link rel="canonical" href="https://tanitxr.org/{LANG_DIRS[LANG]}{stem}/">'
                    f'<meta http-equiv="refresh" content="0;url={rel_target}">'
                    f'<script>location.replace("{rel_target}"+location.hash);</script></head>'
                    f'<body><a href="{rel_target}">Continue</a></body></html>')


def page_hero(title, crumb=None, bg=None, pos="center"):
    bg = bg or "aug-PXL_0811_151718.jpg"
    bgd = (f'<div class="bg" style="background-image:url({img(bg, 1800, as_jpeg=True)});'
           f'background-position:{pos}"></div>')
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
        # wp-content URLs are localized; a bare filename is a file we already keep in media/
        if "wp-content" not in u and "/" in u:
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


NEWS = json.load(open(os.path.join(HERE, "ref", "news.json")))
_WP_MODELS = json.load(open(os.path.join(HERE, "ref", "models.json")))

# known full location strings, used to complete titles that Sketchfab stored truncated
_PLACES = ["Byrsa Hill, Carthage", "Roman Villas of Carthage", "Tophet of Salammbo, Carthage",
           "Tophet of Salammbo (Carthage)", "Baths of Antoninus", "Water Temple of Zaghouan",
           "Water Temple, Zaghouan", "Medina of Tunis", "Zawiya of Sidi Sahbi",
           "Mausoleum of Sidi Sahbi, Kairouan", "Madrasa Al-Bachia, Medina of Tunis",
           "Medersa Slimanya"]


def _complete_title(t):
    t = t.replace("Mausolegt", "Mausoleum").rstrip(" –—-")
    for full in _PLACES:
        if t.endswith(full):
            return t
        for cut in range(len(full) - 1, 3, -1):
            if t.endswith(full[:cut]):
                return t[: len(t) - cut] + full
    return t


def _clean_model_text(txt):
    txt = fix_mojibake(txt or "")
    txt = re.sub(r"\s*(?:📍|üìç|\bü\S*|�\S*)?\s*\[[\d.,\s-]+\]\s*\(\s*https?://scaniver\.se\S*\s*\)\s*$", "", txt)
    txt = re.sub(r"[�]+\S*", "", txt)
    txt = re.sub(r"https?://scaniver\.se\S*", "", txt)
    txt = re.sub(r"\[([^\]]*)\]\(\s*[^)]*\s*\)", "", txt)  # markdown tag-links from Sketchfab
    txt = re.sub(r"ü\S{1,3}", "", txt)  # residual emoji mojibake
    return re.sub(r"\s+", " ", txt).strip(" .|-–—") + "."


for n in NEWS:
    n["title"] = fix_mojibake(n["title"]).strip().rstrip(".")
    n["text"] = fix_mojibake(n["text"])
    n["clean_slug"] = slugify(n["title"])
    n["href"] = f"news/{n['clean_slug']}.html"

# ---- the archive: built from the Sketchfab ORG inventory (ref/archive-data.json,
# regenerated by compile_archive.py). Each artifact pairs the raw photogrammetry scan
# (preservation record) with its optimized game-ready twin when a public one exists.
_ARCH_ALL = json.load(open(os.path.join(HERE, "ref", "archive-data.json")))
_ARCH = _ARCH_ALL["artifacts"]
VOLUNTEER_MADE = _ARCH_ALL.get("volunteer_made", [])
CREATORS = json.load(open(os.path.join(HERE, "ref", "creators-map.json")))


def member_slug(sketchfab_user):
    return CREATORS.get("sketchfab", {}).get(sketchfab_user)


def author_slug(name):
    return CREATORS.get("authors", {}).get(name)


def creator_credit(sketchfab_user):
    """(display name, profile href or None) for a Sketchfab creator, None if unknown/org account.
    Volunteers without a profile yet are credited by name from CREATORS['pending']."""
    slug = member_slug(sketchfab_user)
    if slug and slug in TEAM_BY_SLUG:
        return TEAM_BY_SLUG[slug]["name"], TEAM_BY_SLUG[slug]["href"]
    name = CREATORS.get("pending", {}).get(sketchfab_user)
    return (name, None) if name else (None, None)


def credit_link(name, href):
    return (f'<a href="{href}" style="color:var(--gold-dark);font-weight:700">{esc(name)}</a>' if href
            else f'<b>{esc(name)}</b>')


# contributions accumulated per member slug, rendered on their profile
CONTRIB = {}

def _add_contrib(slug, kind, label, href, uid=None, thumb=None):
    if not slug:
        return
    CONTRIB.setdefault(slug, {"scanned": [], "optimized": [], "made": [], "wrote": [], "built": []})
    CONTRIB[slug][kind].append({"label": label, "href": href, "uid": uid, "thumb": thumb})


def model_card(title, thumb, href, meta="", uid=None, external=False, cls=""):
    """Card with a thumbnail that swaps to the live Sketchfab viewer on click (data-embed → site.js).
    Uses a <div>, not <a>, so the credit inside can be its own link."""
    tgt = ' target="_blank" rel="noopener"' if external else ""
    play = (f'<button class="play" data-embed="{uid}" aria-label="View in 3D">▶ View in 3D</button>' if uid else "")
    if thumb:
        ph = (f'<div class="ph"><a href="{href}"{tgt}><img src="{img(thumb, 800)}" alt="{esc(title)}" loading="lazy"></a>'
              f'{play}</div>')
    else:
        ph = f'<div class="ph blank">{play}</div>'
    return (f'<div class="card {cls}">{ph}<div class="tx"><h3><a href="{href}"{tgt}>{esc(title)}</a></h3>'
            f'{f"<div class=meta>{meta}</div>" if meta else ""}</div></div>')
_wp_by_slug = {w["slug"]: w for w in _WP_MODELS}
MODELS = []
_matched_wp = set()
for a in _ARCH:
    title = _complete_title(fix_mojibake(a["title"]).strip().rstrip("."))
    wpm = _wp_by_slug.get(a.get("wp_slug"))
    if wpm:
        _matched_wp.add(wpm["slug"])
    img_src = (wpm or {}).get("img") or a.get("thumb") or ""
    MODELS.append({
        "title": title,
        "slug": (wpm or {}).get("slug") or slugify(title),
        "clean_slug": slugify(title),
        "href": f"archive/{slugify(title)}.html",
        "site": a["site"],
        "place": fix_mojibake(a["place"]),
        "cats": [a["site"]],
        "date": a["date"],
        "sketchfab": f"https://sketchfab.com/models/{a['preservation']}/embed" if a["preservation"] else None,
        "gameready": a.get("gameready"),
        "scanned_by": a.get("scanned_by", ""),
        "optimized_by": a.get("optimized_by", ""),
        "text": _clean_model_text(a["desc"]),
        "img": img_src,
    })
for w in _WP_MODELS:  # old-site scans with no org counterpart keep their original embeds
    if w["slug"] in _matched_wp:
        continue
    title = fix_mojibake(w["title"]).strip().rstrip(".")
    uid = re.search(r"models/([a-f0-9]+)", w["sketchfab"] or "")
    MODELS.append({
        "title": title, "slug": w["slug"], "clean_slug": slugify(title),
        "href": f"archive/{slugify(title)}.html",
        "site": "Kairouan" if "Sidi" in title else "Carthage",
        "place": "Carthage", "cats": w["cats"], "date": w["date"],
        "sketchfab": w["sketchfab"], "gameready": None,
        "text": _clean_model_text(w["text"]), "img": w["img"],
    })
MODELS.sort(key=lambda m: (m["site"], m["place"], m["title"]))
for n in NEWS:
    n["href"] = f"news/{n['clean_slug']}.html"

PEOPLE_EXTRA = load("person_extra.json")
PEOPLE_PHOTOS = load("people_photos.json")
# WP had two uploads named headshot.png / Headshot.png (Rachel's + "Charity Headshot"); on a
# case-insensitive disk they collided, so Rachel's is stored under its own name.
PHOTO_OVERRIDES = {"Rachel West": "rachel-west-headshot.png"}

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
    # body starts with "Name Role bio...", strip name/role prefix and icon junk
    bio = body
    for pre in (name, role, extra.get("name", "")):
        if pre and bio.lower().startswith(pre.lower()):
            bio = bio[len(pre):].lstrip(" ,–-")
    bio = re.sub(r"email \[#\d+\] Created with Sketch\.?", "", bio).strip()
    bio = re.sub(r"\s+", " ", bio)
    bio = bio.replace("Awardpresented", "Award presented")
    if bio and bio[0].islower():
        bio = f"{name} {bio}"
    photo = PHOTO_OVERRIDES.get(name) or PEOPLE_PHOTOS.get(name)
    return {
        "name": name, "role": role, "slug": slug, "bio": bio,
        "photo": photo, "links": extra.get("links", []),
        "href": f"team/{slug}.html",
    }


TEAM = [person_record(n, r) for n, r in CORE_TEAM]
COMMUNITY = [person_record(n, r) for n, r in CONTRIBUTORS]
TEAM_BY_SLUG = {p["slug"]: p for p in TEAM + COMMUNITY}

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
                "links": [d[k] for k in ("linkedin", "instagram", "website", "github", "sketchfab", "other_link") if d.get(k)] + ([f"mailto:{d['public_email']}"] if d.get("public_email") else []),
                "href": f"team/{slug}.html",
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

# ref/opportunity_updates.json records deadlines as "YYYY-MM-DD"; the older scraped
# entries carry "September 14, 2026". Normalise to the display form so _dl_date below
# can read every entry, an unparseable date reads as "no deadline", which would keep
# a closed call on the board forever and print the raw ISO string on its card.
import datetime as _dt


def _parse_any_date(s):
    for fmt in ("%Y-%m-%d", "%B %d, %Y", "%b %d, %Y"):
        try:
            return _dt.datetime.strptime(s, fmt).date()
        except (TypeError, ValueError):
            continue
    return None


for o in OPPS:
    _d = _parse_any_date(o["deadline_date"])
    if _d:
        o["deadline_date"] = _d.strftime("%B %-d, %Y")

# a "Fixed" deadline with no recoverable date on a months-old posting is long past —
# mark it closed rather than showing a dateless "Deadline: Fixed"
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
TRENDING = []  # (title, href, thumb-url), filled after models/news known
_tr_models = [m for m in MODELS if "Punic Stela" in m["title"] or "Corinthian Capital" in m["title"]][:2]
for m in _tr_models:
    TRENDING.append((m["title"], m["href"], m["img"]))
for n in sorted(NEWS, key=lambda x: x["date"]):
    TRENDING.append((n["title"], n["href"], n["img"]))
TRENDING = TRENDING[:4]


# ---------------------------------------------------------------- pages

# ---- recognition & press facts (verified 2026-09-12) ------------------------
PRESS = [
    {"k": "Award", "t": "Auggie Awards 2026, Finalist, Best Societal Impact",
     "d": "Tanit XR was a finalist in the Best Societal Impact category at Augmented World Expo USA 2026, the XR industry's main awards, selected by public vote and expert review.",
     "u": "https://www.awexr.com/blog/1382-2026-auggie-awards-finalists-announced", "date": "June 2026", "anchor": "auggie"},
    {"k": "Podcast", "t": "Voices of VR #1728, Preserving Tunisian Cultural Heritage with Tanit XR",
     "d": "Kent Bye interviewed Ines Said at AWE USA 2026 about phone-based reality capture, volunteers and heritage at risk.",
     "u": "https://voicesofvr.com/1728-preserving-tunisian-cultural-heritage-with-tanit-xr-reality-capture", "date": "July 2, 2026", "anchor": "voices"},
    {"k": "Talk", "t": "AWE USA 2026, Speaker",
     "d": "Ines Said spoke at Augmented World Expo USA 2026 in Long Beach, California, on XR for social impact and heritage.",
     "u": "https://www.awexr.com/usa-2026/speakers/2677-ines-said", "date": "June 2026", "anchor": "awe"},
    {"k": "Video", "t": "Niantic Spatial, video interview with Nathan Bowser",
     "d": "Nathan Bowser interviewed Ines Said for Niantic Spatial about Tanit XR and the Scaniverse capture of the amphitheatre of El Jem; Niantic published the video on its channels.",
     "u": "press.html#niantic", "date": "2026", "anchor": "niantic"},
    {"k": "Paper", "t": "El Jem Conference 2026, Paper in English, French and Tunisian Arabic",
     "d": "Our paper on digital documentation, XR and citizen science for community-driven heritage preservation, presented in April 2026.",
     "u": "el-jem-conference.html", "date": "April 2026", "anchor": "eljem"},
    {"k": "Press", "t": "Al Jazeera, \"Tanit XR\": a non-profit platform documenting Tunisian heritage digitally (Arabic)",
     "d": "Al Jazeera's culture desk profiled Tanit XR in Arabic: a non-profit building a precise digital library of Tunisia's sites and artifacts with photogrammetry and Gaussian splats, before time and neglect erase them.",
     "u": "https://www.aljazeera.net/culture/2025/10/12/%D8%AA%D8%A7%D9%86%D9%8A%D8%AA-%D8%A5%D9%83%D8%B3-%D8%A2%D8%B1-%D9%85%D9%86%D8%B5%D8%A9-%D8%BA%D9%8A%D8%B1-%D8%B1%D8%A8%D8%AD%D9%8A%D8%A9-%D8%AA%D9%88%D8%AB%D9%82", "date": "October 12, 2025", "anchor": "aljazeera"},
    {"k": "Exhibition", "t": "XR Women Museum, two exhibitions in FrameVR, curated by Paige Dansinger",
     "d": "Tanit XR's work was shown in the XR Women Museum, including its \"Garden: In Full Bloom\" exhibition, an immersive museum of 30+ gallery worlds directed by Paige Dansinger.",
     "u": "https://framevr.io/xrwomenmuseum", "date": "2026", "anchor": "xrwomen"},
    {"k": "Article", "t": "Carthage Magazine, Preserving Tunisia's Heritage Through Immersive Technology",
     "d": "Feature on how Tanit XR uses photogrammetry, Scaniverse and Gaussian splatting to build an open archive of Tunisian heritage.",
     "u": "https://carthagemagazine.com/tanit-xr-preserving-tunisias-heritage-through-immersive-technology/", "date": "2026", "anchor": "carthage"},
    {"k": "Article", "t": "Medium / Women Write, Tanit XR: Preserving Tunisia's Heritage Through Immersive Technology",
     "d": "Ines Said on why Tanit XR exists and where it is going, published in the Women Write collection.",
     "u": "https://medium.com/women-write/tanit-xr-preserving-tunisias-heritage-through-immersive-technology-c9238dab7675", "date": "2026", "anchor": "medium"},
    {"k": "Event", "t": "ImmerseGT 2026, Sponsored track at Georgia Tech's XR hackathon",
     "d": "We sponsored a heritage track and a $300 prize; Dr. Caroline Nickerson led a workshop on citizen science and XR.",
     "u": "immersegt-2026.html", "date": "April 10–12, 2026", "anchor": "immersegt"},
    {"k": "Partnership", "t": "TanitXR & the Unique Mappers, expanding to Nigeria",
     "d": "The Unique Mappers Network (500+ citizen scientists) is replicating the Tanit XR model in Nigeria with a mini-grant from our fiscal sponsor.",
     "u": "unique-mappers.html", "date": "2026", "anchor": "nigeria"},
]
NIANTIC_EMBED = "https://www.linkedin.com/embed/feed/update/urn:li:activity:7488488682652495873"

COMMUNITY_ACTS = [
    ("📅", "Weekly community call, Thursdays, 12 pm Eastern", "Volunteers from Tunisia, the US, Europe and Nigeria meet every Thursday at 12 pm Eastern (5 pm Tunisia) to review scans, plan trips and help each other."),
    ("🏛", "History lessons", "Short sessions on the sites and objects we scan, Carthage, the Tophet, the medina of Tunis, so every model comes with its story."),
    ("📱", "Splats With Phones workshop", "A 6-week course with Mark Jeffcock on capturing 3D models and Gaussian splats with a phone."),
    ("🤝", "Mentoring & interview prep", "Portfolio reviews, mock interviews and career advice for students and early-career volunteers."),
    ("🎤", "Events & conferences", "We speak, exhibit and sponsor: AWE, the El Jem conference, ImmerseGT at Georgia Tech, and more."),
    ("🌍", "Cultural exchange", "Volunteers who have never been to Tunisia learn its history while modeling lamps, pottery and plants for our virtual museum, and we learn about theirs."),
]
COMMUNITY_PHOTOS = ["sv-IMG_1315.jpg", "aug-PXL_0814_112926.jpg", "sv-IMG_4213.jpg",
                    "aug-PXL_0809_170720.jpg", "sv-IMG_8547.jpg"]



def subscribe_form(dark=True):
    """Kit sign-up form. Two interest checkboxes appear once KIT_TAGS has the tag ids."""
    inp = ("flex:1;min-width:220px;padding:13px 16px;border:none;border-radius:6px;font-size:15.5px" if dark
           else "flex:1;min-width:220px;padding:13px 16px;border:1px solid var(--mist);border-radius:6px;font-size:15.5px")
    lab = "rgba(255,255,255,.85)" if dark else "var(--ink)"
    boxes = ""
    if KIT_TAGS.get("opportunities") and KIT_TAGS.get("news"):
        boxes = (f'<div style="display:flex;gap:22px;flex-wrap:wrap;margin:12px 0 0;font-size:14.5px;color:{lab}">'
                 f'<label style="display:flex;gap:8px;align-items:center;font-weight:400;margin:0"><input type="checkbox" name="tags[]" value="{KIT_TAGS["opportunities"]}" checked> Opportunities (every 1–2 weeks)</label>'
                 f'<label style="display:flex;gap:8px;align-items:center;font-weight:400;margin:0"><input type="checkbox" name="tags[]" value="{KIT_TAGS["news"]}" checked> Tanit XR news (occasional)</label></div>')
    return (f'<form class="nice" action="https://app.kit.com/forms/{KIT_FORM_ID}/subscriptions" method="post" '
            f'data-sv-form="{KIT_FORM_ID}" style="max-width:none">'
            f'<div style="display:flex;gap:12px;flex-wrap:wrap">'
            f'<input name="email_address" type="email" placeholder="you@example.com" required aria-label="Email" style="{inp}">'
            f'<button class="btn btn-gold" type="submit" style="margin-top:0">Subscribe Free</button></div>{boxes}</form>')

def recognition_strip():
    """Press/recognition logo row (grayscale, colour on hover), like the original site's partner strip."""
    items = [
        ("awe.svg", "AWE · Auggie Awards 2026", "Finalist, Best Societal Impact", PRESS[0]["u"]),
        ("voicesofvr.png", "Voices of VR", "Episode #1728", PRESS[1]["u"]),
        (None, "Niantic Spatial", "Video interview", "press.html#niantic"),
        ("aljazeera.svg", "Al Jazeera", "Al Jazeera · Culture feature", next(x["u"] for x in PRESS if x["anchor"] == "aljazeera")),
        (None, "XR Women Museum", "Two exhibitions", "https://framevr.io/xrwomenmuseum"),
        ("georgiatech.svg", "Georgia Tech · ImmerseGT", "Track sponsor 2026", "immersegt-2026.html"),
    ]
    out = ""
    for fn, name, sub, u in items:
        ext = ' target="_blank" rel="noopener"' if u.startswith("http") else ""
        mark = (f'<img src="{img(fn, 400, as_jpeg=False)}" alt="{esc(name)}" loading="lazy">' if fn
                else f'<span class="wordmark">{esc(name)}</span>')
        out += f'<a href="{u}"{ext} title="{esc(name)}, {esc(sub)}">{mark}<span class="cap">{sub}</span></a>'
    return f'<div class="logos">{out}</div>'


def community_mosaic():
    return '<div class="mosaic">' + "".join(
        f'<img src="{img(f, 1200 if i == 0 else 700)}" alt="Tanit XR volunteers" loading="lazy">'
        for i, f in enumerate(COMMUNITY_PHOTOS)) + '</div>'


def community_acts(limit=None):
    return '<div class="acts">' + "".join(
        f'<div class="act"><div class="ic">{ic}</div><b>{t}</b><p>{d}</p></div>'
        for ic, t, d in COMMUNITY_ACTS[:limit]) + '</div>'


def press_cards(items):
    out = ""
    for x in items:
        ext = ' target="_blank" rel="noopener"' if x["u"].startswith("http") else ""
        out += (f'<a href="{x["u"]}"{ext}><div class="k">{x["k"]} · {x["date"]}</div><h3>{esc(x["t"])}</h3>'
                f'<p>{esc(x["d"])}</p></a>')
    return f'<div class="press">{out}</div>'


def funding_band():
    return f"""
<section class="band pad" id="funding"><div class="wrap">
<div class="eyebrow">How we're funded</div>
<h2 class="sec-title">Honest numbers</h2>
<p class="sec-sub" style="margin:0;max-width:760px">Tanit XR is run entirely by volunteers. So far most costs, travel to
sites, tools, hosting, hackathon prizes, have been paid out of pocket by our founders, plus a few individual donations
through our fiscal sponsor, the Florida Community Innovation Foundation (a US 501(c)(3), so donations are tax-deductible).
We are applying for grants and building partnerships to change that. Donations keep the community running: hosting,
volunteer hours, optimizing and publishing models, the virtual museum, scanning and site clean-up days, our free course
and workshops, and better equipment. Here is what a donation does:</p>
<div class="money">
<div><b>$25</b><span>A scanning day for a volunteer: transport, mobile data for uploads, backups.</span></div>
<div><b>$50</b><span>A month of hosting and tools for the archive and the volunteers who optimize models.</span></div>
<div><b>$250</b><span>A free workshop or course session for the community, Splats With Phones, history lessons, mentoring.</span></div>
<div><b>$1,000</b><span>Toward the virtual museum and, one day, a professional scanner like the XGRIDS PortalCam.</span></div>
</div>
<div style="margin-top:32px;display:flex;gap:14px;flex-wrap:wrap">
<a class="btn btn-gold" href="{DONATE_URL}" target="_blank" rel="noopener">Donate</a>
<a class="btn btn-line-light" href="services.html">Work with us</a>
<a class="btn btn-line-light" href="support.html">See the full breakdown</a></div>
</div></section>"""



def build_home():
    pillars = [
        ("archive.png", "Scan &amp; Preserve",
         "Volunteers capture statues, mosaics and ruins with their phones. Every scan becomes a permanent, open record.",
         "Explore the Archive", "archive.html"),
        ("ARVR.png", "Optimize &amp; Build",
         "Remote volunteers turn raw scans into game-ready models, AR lessons and our virtual museum.",
         "Visit the virtual museum", "museum.html"),
        ("education.png", "Learn Together",
         "Weekly community calls, history lessons on the sites we scan, and the Splats With Phones workshop.",
         "Join the community", "community.html"),
        ("volunteer.png", "Mentor &amp; Grow",
         "Interview prep, portfolio reviews and mentoring for students and early-career volunteers, across four continents.",
         "Volunteer with us", "volunteer.html"),
        ("research.png", "Research &amp; Share",
         "Papers, conference talks, podcasts and hackathon tracks. We publish what we learn.",
         "Press &amp; recognition", "press.html"),
        ("research-1.png", "Extend Beyond Tunisia",
         "With the Unique Mappers in Nigeria we are testing the model in a second country. Under-represented heritage everywhere is the goal.",
         "TanitXR &amp; the Unique Mappers", "unique-mappers.html"),
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
<div class="hero"><div class="bg hero-photo" style="background-image:var(--scrim),url({img('hero-baths-flipped.jpg', 1920)})"></div>
<div class="in">
<h1>Preserving Heritage</h1>
<p>A volunteer community from Tunisia and around the world, scanning endangered heritage in 3D and bringing it to
life in AR and VR, and learning from each other along the way.</p>
<div class="ctas"><a class="btn btn-gold" href="community.html">Join the Community</a>
<a class="btn btn-dark" href="archive.html">Explore the Archive</a></div>
</div></div>

<section class="pad"><div class="wrap center" style="max-width:860px">
<div class="eyebrow">More than an archive</div>
<h2 class="sec-title">One phone, the ruins of Carthage, and now a community</h2>
<p class="sec-sub" style="margin:0;font-size:18px">Tanit XR started with a phone and the ruins Ines grew up next to.
Today, volunteers in Tunisia, the US, Europe and Nigeria meet every week to scan, optimize, teach each other history,
mentor students and publish research, building a free 3D archive of Tunisia’s heritage, and a model for other
under-represented regions.</p>
</div></section>

<section class="band photo statsband"><div class="bg" style="background-image:url({img('sv-IMG_0511.jpg', 1800)})"></div>
<div class="wrap">
<div class="stats big">
<div><b>{stat('artifacts')}</b><span>Artifacts scanned by volunteers</span></div>
<div><b>{stat('sites')}</b><span>Heritage sites documented</span></div>
<div><b>{stat('volunteers')}</b><span>Volunteers on four continents</span></div>
<div><b>{stat('reach')}</b><span>People reached online</span></div>
</div></div></section>

<section class="pad-sm cream"><div class="wrap center">
<div class="eyebrow">Recognized by</div>
{recognition_strip()}
</div></section>

<section class="pad"><div class="wrap">
<div class="center" style="max-width:820px;margin:0 auto 40px">
<div class="eyebrow">What we do</div>
<h2 class="sec-title">Six ways the community works</h2></div>
<div class="pillars">{pillar_html}</div>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:44px;align-items:center">
{community_mosaic()}
<div>
<div class="eyebrow">Community</div>
<h2 class="sec-title">We meet every week</h2>
<p class="sec-sub" style="margin:0 0 18px">Tanit XR is a weekly call across time zones as much as it is an archive. We
review each other’s scans, learn the history behind them, run workshops, prepare students for interviews, share
Tunisian culture, and celebrate wins together.</p>
<ul style="color:var(--gray);line-height:1.9;padding-left:20px;margin-bottom:26px">
<li>Weekly community call, Thursdays, 12 pm Eastern</li><li>History lessons on the sites we scan</li><li>Splats With Phones workshop</li>
<li>Mentoring &amp; interview prep</li><li>Events, talks &amp; hackathons</li><li>Cultural exchange</li></ul>
<a class="btn btn-gold" href="community.html">See how the community works</a>
&nbsp; <a class="btn btn-line" href="volunteer.html">Volunteer</a>
</div></div></div></section>

<section class="pad"><div class="wrap center">
<div class="eyebrow">Featured Scans</div>
<h2 class="sec-title">Highlights from the Tanit XR Archive</h2>
<div class="cards" style="text-align:left">{feat}</div>
<p style="margin-top:34px"><a class="btn btn-line" href="archive.html">Open the Full Archive</a></p>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap center">
<div class="eyebrow">🏺 Made by our volunteers</div>
<h2 class="sec-title">Recreated by hand, for VR &amp; learning</h2>
<p class="sec-sub">Beyond scanning, our volunteers model Tunisian lamps, pottery and plants from scratch for our
virtual museum. Press <b>View in 3D</b> to spin one around right here.</p>
<div class="cards" style="text-align:left">{volunteer_made_cards(4)}</div>
<p style="margin-top:34px"><a class="btn btn-line" href="archive.html#volunteer-made">See all {len(VOLUNTEER_MADE)} volunteer-made models</a>
&nbsp; <a class="btn btn-gold" href="volunteer.html">Make one with us</a></p>
</div></section>

<section class="split">
<div class="simg" style="background-image:url({img('aug-20260813_124249.jpg', 1400)})" role="img" aria-label="Ruins on the Tunisian coast"></div>
<div class="stx">
<h2 class="sec-title">Climate is rewriting the coastline</h2>
<h3>Storm Harry, January 2026</h3>
<p>The storm stripped sediment off the coast at Nabeul and exposed parts of Neapolis, an ancient city lost to a
tsunami in the 4th century. Within days our volunteers captured the newly revealed ruins in 3D, a record that
exists no matter what the sea does next.</p>
<h3>A lasting record</h3>
<p>Floods, storms and heat are accelerating erosion across Tunisia’s sites. Every scan is a permanent, open record:
even if the physical site is lost, the digital memory survives, for schools, museums and future generations.</p>
<div style="margin-top:36px;display:flex;gap:14px;flex-wrap:wrap">
<a class="btn btn-gold" href="news/storm-harry-neapolis-and-a-digital-moment-of-preservation.html">Read the Neapolis story</a>
<a class="btn btn-line" href="{DONATE_URL}" target="_blank" rel="noopener">Donate</a></div>
</div></section>

<section class="pad"><div class="wrap center">
<div class="eyebrow">Press &amp; Recognition</div>
<h2 class="sec-title">What people are saying</h2>
<div style="text-align:left;margin-top:36px">{press_cards(PRESS[:6])}</div>
<p style="margin-top:34px"><a class="btn btn-line" href="press.html">All press, talks &amp; papers</a></p>
</div></section>

<section class="band pad"><div class="bg" style="background-image:url({img('sv-IMG_0511.jpg', 1800)})"></div>
<div class="wrap">
<div class="eyebrow">Where we’re going</div>
<h2 class="sec-title">Tunisia is the pilot</h2>
<p class="sec-sub" style="margin:0;max-width:760px">The method, phones, volunteers, open data, works anywhere heritage is
under-documented. In 2026 the Unique Mappers Network began scanning in Nigeria with a mini-grant from our fiscal
sponsor. If you want to bring this to your region, talk to us.</p>
<div style="margin-top:32px;display:flex;gap:14px;flex-wrap:wrap">
<a class="btn btn-gold" href="contact.html">Bring Tanit XR to your region</a>
<a class="btn btn-line-light" href="unique-mappers.html">The Nigeria pilot</a></div>
</div></section>

<section class="pad"><div class="wrap center">
<div class="eyebrow">Our Team</div>
<h2 class="sec-title">Powered by our people</h2>
<p class="sec-sub">Tanit XR is led by a dedicated core team and powered by a growing network of volunteers
across Tunisia and the world.</p>
<div class="team">{team}</div>
<p style="margin-top:36px"><a class="btn btn-line" href="team.html">Meet Everyone</a></p>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap center">
<div class="eyebrow">Testimonials</div>
<h2 class="sec-title">Hear from the volunteers and mentors shaping Tanit XR</h2>
<div class="quotes" style="text-align:left;margin-top:40px">{quote_html}</div>
</div></section>

{funding_band()}

<section class="pad" style="background:var(--cloud)"><div class="wrap" style="max-width:760px">
<div class="eyebrow">Newsletter</div>
<h2 class="sec-title" style="font-size:30px">Opportunities and news, in your inbox</h2>
<p class="sec-sub" style="margin:0 0 20px">Grants, residencies and open calls for artists and XR creators every one to two
weeks, only things we’d apply to ourselves, plus occasional Tanit XR news. Free, unsubscribe any time.</p>
{subscribe_form(dark=False)}
</div></section>

<section class="pad-sm"><div class="wrap center">
<div class="eyebrow">Partners &amp; Supporters</div>
<div class="partners" style="margin-top:22px">{partners}</div>
</div></section>
"""
    page("index.html", "Home", body, transparent=True)


def build_community():
    steps = [
        ("Fill the volunteer form", "Tell us what you like doing, scanning, 3D, writing, design, research, teaching."),
        ("Join Slack and the Thursday call", "A member of the team welcomes you, and you meet everyone on the next call, Thursdays at 12 pm Eastern."),
        ("Pick a first task", "Optimize a scan, write the history of an object, model something Tunisian, or plan a scanning trip."),
        ("Once accepted, create your profile", "Accepted volunteers get their own page here: your scans, models and articles are credited to you."),
    ]
    steps_html = "".join(f'<div><b>{t}</b><p style="color:var(--gray);font-size:14.5px;margin-top:6px">{d}</p></div>' for t, d in steps)
    body = f"""
{page_hero("Community", '<a href="volunteer.html">Get Involved</a> &nbsp;›&nbsp; Community', bg="sv-IMG_1315.jpg", pos="center 35%")}
<section class="pad"><div class="wrap">
<div class="center" style="max-width:820px;margin:0 auto 40px">
<div class="eyebrow">More than an archive</div>
<h2 class="sec-title">We started as an archive. We became a community.</h2>
<p class="sec-sub" style="margin:0">Tanit XR is volunteers in Tunisia, the United States, Europe and Nigeria who meet
every week. We scan on the ground and optimize remotely, learn the history behind every object, run workshops,
mentor students, attend events together, and share Tunisian culture with people who had never heard of Carthage.
Everything we make is free and open.</p></div>
{community_mosaic()}
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap">
<div class="center"><div class="eyebrow">What we do together</div>
<h2 class="sec-title">A week at Tanit XR</h2></div>
{community_acts()}
<div style="max-width:820px;margin:40px auto 0;background:#fff;border:1px solid var(--mist);border-radius:10px;padding:24px 28px">
<b style="font-family:var(--serif);font-size:19px;font-weight:400">Recorded history lessons</b>
<p style="color:var(--gray);font-size:14.5px;margin:6px 0 12px">Julia records a short lesson each week so volunteers in any time zone can follow along and pick a task.</p>
<ul style="padding-left:20px;line-height:1.9;color:var(--ink)">{"".join(f'<li><a href="{u}" target="_blank" rel="noopener" style="color:var(--gold-dark)">{esc(t)}</a> <span style="color:var(--gray);font-size:13px">· {d}</span></li>' for t, d, u in HISTORY_LESSONS)}</ul>
</div>
</div></section>

<section class="pad"><div class="wrap">
<div class="center"><div class="eyebrow">Join</div>
<h2 class="sec-title">How to get in</h2>
<p class="sec-sub">No archaeology or 3D background needed. Our first scans were made with a phone.</p></div>
<div class="steps">{steps_html}</div>
<p class="center" style="margin-top:34px">
<a class="btn btn-gold" href="{VOLUNTEER_FORM_URL}" target="_blank" rel="noopener">Volunteer Interest Form</a>
&nbsp; <a class="btn btn-line" href="team.html">Meet the community</a></p>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap center">
<div class="eyebrow">🏺 Made by our volunteers</div>
<h2 class="sec-title">What comes out of the weekly calls</h2>
<div class="cards" style="text-align:left">{volunteer_made_cards(3)}</div>
<p style="margin-top:30px"><a class="btn btn-line" href="archive.html#volunteer-made">See all {len(VOLUNTEER_MADE)} volunteer-made models</a></p>
</div></section>

<section class="band pad"><div class="bg" style="background-image:url({img('sv-IMG_1232.jpg', 1800)})"></div>
<div class="wrap center">
<div class="eyebrow">Where we’re going</div>
<h2 class="sec-title">Bring the model to your region</h2>
<p class="sec-sub" style="color:rgba(255,255,255,.85)">Tunisia is the pilot. The Unique Mappers are replicating it in
Nigeria. If your community’s heritage is under-documented, we want to hear from you.</p>
<a class="btn btn-gold" href="contact.html">Contact us</a>
&nbsp; <a class="btn btn-line-light" href="unique-mappers.html">The Nigeria pilot</a>
</div></section>"""
    page("community.html", "Community", body, active="volunteer.html",
         desc="Tanit XR is a weekly community of volunteers in Tunisia, the US, Europe and Nigeria, scanning, learning history, mentoring and building a free 3D archive.")


# volunteers building the virtual museum (from Slack #vr-app / #volunteer-updates, Sept 2026) and Julia's recorded lessons
MUSEUM_BUILDERS = "Patrick Molen (the original room and the modular building kit every new room is assembled from), Ala (a wing inspired by the Roman baths of Dougga), Kristina Reyes (a furnished room), Cam K. (narrative and thematic brief), Claire Natanek, Rachel West, Nick Kaufmann, Ana Beatriz Vega and Ray (models and optimization)"
HISTORY_LESSONS = [
    ("First Phoenicians and Tyrian Purple Origins", "July 31, 2026", "https://www.loom.com/share/e4717da8892544bca7b7aff597e27407"),
    ("Mini history lesson 2, Carthage's craft quarters", "August 6, 2026", "https://www.loom.com/share/53d0a3afb9b14734a9c4b643d4f15b6e"),
    ("Mini history lesson 3", "August 18, 2026", "https://www.loom.com/share/27ad26874ff84c1d95be7a2a2f42bedd"),
]


def vid(name):
    """Copy a pre-encoded web video from media/video/web into docs/assets/video and return its site path."""
    src = os.path.join(HERE, "media", "video", "web", name)
    out_dir = os.path.join(DOCS, "assets", "video")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, name)
    if not os.path.exists(out) and os.path.exists(src):
        shutil.copy(src, out)
    return f"assets/video/{name}"


def build_museum():
    body = f"""
{page_hero("Virtual Museum", '<a href="archive.html">Archive</a> &nbsp;›&nbsp; Virtual Museum', bg="museum-courtyard-pool.jpg", pos="center 45%")}
<section class="pad"><div class="wrap">
<div class="center" style="max-width:820px;margin:0 auto 40px">
<div class="eyebrow">In progress</div>
<h2 class="sec-title">A museum built by volunteers, from real scans</h2>
<p class="sec-sub" style="margin:0">The first community-led virtual museum of Tunisian heritage. Every artifact inside was
scanned in Tunisia by our volunteers and optimized by volunteers around the world; the rooms are modeled by hand so
anyone in the community can build a new one. Built in Unity with photogrammetry and Gaussian splats. Still in
progress, this is what it looks like today.</p>
<p style="color:var(--gray);font-size:14.5px;margin-top:14px">Built so far by {MUSEUM_BUILDERS}, coordinated on the Thursday call.</p></div>
<video class="vid" controls preload="none" playsinline poster="{img('museum-domed-hall-fountain.jpg', 1400)}"
src="{vid('museum-walkthrough-06.mp4')}"></video>
<p class="center" style="color:var(--gray);font-size:14px;margin-top:10px">Walkthrough recorded in the Unity editor, March 2026.</p>
<div class="shots museum" style="margin-top:34px">
<img src="{img('museum-hall-arches.jpg', 900)}" alt="Domed hall with striped arches" loading="lazy">
<img src="{img('museum-statue-niche.jpg', 900)}" alt="Scanned Roman statue in a niche" loading="lazy">
<img src="{img('museum-tiled-corridor.jpg', 900)}" alt="Tiled corridor with a scanned artifact" loading="lazy">
</div>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap">
<div class="center"><div class="eyebrow">How it works</div>
<h2 class="sec-title">Rooms you can walk through, objects you can get close to</h2></div>
<div class="acts">
<div class="act"><div class="ic">🏛</div><b>Real artifacts</b><p>Punic stelae, Roman statues and mosaics, doors and tilework from the medina, the same scans you find in our open archive, placed life-size.</p></div>
<div class="act"><div class="ic">🧩</div><b>Modular rooms</b><p>Walls, arches and courtyards are built from a kit of pre-made pieces designed by Patrick Molen, so volunteers can puzzle together a new gallery without starting from scratch.</p></div>
<div class="act"><div class="ic">🎧</div><b>Sound from the sites</b><p>Ambient sound recorded at the real places, wind, footsteps, echoes, so each gallery feels different.</p></div>
<div class="act"><div class="ic">🧭</div><b>A guide</b><p>Nura, a guide character modeled in Blender, walks with you and tells the story behind each object. Her narrated tour, “Before It’s Gone,” is being written now.</p></div>
<div class="act"><div class="ic">🕶</div><b>Headset, browser, phone</b><p>Planned for Viverse so it runs cross-platform, in VR, and as a scroll-to-walk version in any browser for classrooms.</p></div>
<div class="act"><div class="ic">🏺</div><b>Made by the community</b><p>Lamps, pottery and plants modeled by volunteers furnish the rooms. Optimized scans keep it light enough for phones.</p></div>
</div>
</div></section>

<section class="pad"><div class="wrap">
<div class="center"><div class="eyebrow">Progress</div>
<h2 class="sec-title">From greybox to galleries</h2></div>
<div class="timeline">
<div><img src="{img('museum-progress-jan-2026.jpg', 800)}" alt="" loading="lazy"><b>January 2026</b><p>First courtyard and corridor blocked out; scanned statues placed.</p></div>
<div><img src="{img('museum-hall-arches.jpg', 800)}" alt="" loading="lazy"><b>March 2026</b><p>Domed hall with striped arches, tiled floors, fountain and lighting.</p></div>
<div><img src="{img('museum-courtyard-pool.jpg', 800)}" alt="" loading="lazy"><b>March 2026</b><p>Courtyard with pool, terraces and the sculpted canopy.</p></div>
<div><img src="{img('museum-second-room-greybox.jpg', 800)}" alt="" loading="lazy"><b>August 2026</b><p>Second wing under construction, colonnade and galleries in greybox.</p></div>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:22px;margin-top:34px">
<div><video class="vid" controls preload="none" playsinline poster="{img('museum-hall-arches.jpg', 1000)}" src="{vid('museum-walkthrough-03.mp4')}"></video>
<p style="color:var(--gray);font-size:14px;margin-top:8px">The domed hall, March 2026.</p></div>
<div><video class="vid" controls preload="none" playsinline muted poster="{img('museum-second-room-greybox.jpg', 1000)}" src="{vid('museum-second-room.mp4')}"></video>
<p style="color:var(--gray);font-size:14px;margin-top:8px">The second wing in greybox, August 2026.</p></div>
</div>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap center">
<div class="eyebrow">🏺 Inside the museum</div>
<h2 class="sec-title">Objects made by our volunteers</h2>
<div class="cards" style="text-align:left">{volunteer_made_cards(3)}</div>
<p style="margin-top:30px"><a class="btn btn-line" href="archive.html#volunteer-made">See all {len(VOLUNTEER_MADE)} volunteer-made models</a>
&nbsp; <a class="btn btn-line" href="archive.html">Browse the scans on display</a></p>
</div></section>

<section class="band pad"><div class="bg" style="background-image:url({img('museum-tiled-corridor.jpg', 1800)})"></div>
<div class="wrap center">
<div class="eyebrow">Help finish it</div>
<h2 class="sec-title">Build a room. Fund a room.</h2>
<p class="sec-sub" style="color:rgba(255,255,255,.85)">Unity developers, 3D artists, sound designers and writers are
building this on Thursday calls. Donations pay for the tools and hosting that get it onto headsets and into classrooms.</p>
<a class="btn btn-gold" href="volunteer.html">Volunteer</a>
&nbsp; <a class="btn btn-line-light" href="{DONATE_URL}" target="_blank" rel="noopener">Donate</a>
</div></section>"""
    page("museum.html", "Virtual Museum", body, active="archive.html",
         desc="The first community-led virtual museum of Tunisian heritage, real scans placed in rooms built by volunteers in Unity. Walkthroughs, progress and how to help.")


def build_services():
    # Principle (Ines, 2026-09-12): volunteer work is NEVER sold. Only what the leadership team delivers itself.
    services = [
        ("🎓", "Workshops & training",
         "Phone-scanning workshops and sessions on XR for heritage and community-driven documentation, delivered by "
         "our leadership team, in person in Tunisia and the US, or online.",
         "For schools, universities, museums, NGOs and companies; from a two-hour intro to a multi-day program. We "
         "have been asked to train groups of 200.",
         "Free for student groups and grassroots organizations · contracted delivery for institutions"),
        ("🎤", "Talks & consulting",
         "Keynotes, panels and workshops on XR for heritage, phone-based reality capture and building a volunteer "
         "community, and help for organizations that want to replicate the Tanit XR model in their region.",
         "For conferences, universities, companies and heritage organizations. Our founder has spoken at AWE USA "
         "2026 and the El Jem conference; our method is being replicated in Nigeria.",
         "Speaking fees and consulting rates on request"),
        ("📣", "Sharing opportunities",
         "Reach artists, XR developers and changemakers through the Art, XR & Impact Opportunities newsletter and the "
         "opportunities board on this site.",
         "For funders, festivals, residencies and programs looking for strong applicants from under-represented "
         "regions. Featured placement on the board and in the newsletter; we only share calls that fit our readers.",
         "Free for grassroots calls · sponsored placement for institutions"),
        ("💻", "Hackathon & challenge tracks",
         "We design and judge heritage tracks for hackathons and student challenges, bringing our open 3D archive and "
         "a real problem to your participants.",
         "For universities, hackathon organizers and companies. We sponsored a track at ImmerseGT 2026 at Georgia "
         "Tech and are planning one for CityCamp Gainesville.",
         "Co-sponsored"),
    ]
    cards = "".join(
        f'<div class="act" style="display:flex;flex-direction:column"><div class="ic">{ic}</div><b>{t}</b><p>{d}</p>'
        f'<p style="margin-top:10px">{who}</p>'
        f'<p style="margin-top:auto;padding-top:14px;color:var(--gold-dark);font-weight:700;font-size:13.5px">{price}</p></div>'
        for ic, t, d, who, price in services)
    body = f"""
{page_hero("Services", '<a href="about.html">About</a> &nbsp;›&nbsp; Services', bg="sv-IMG_4299.jpg", pos="center 40%")}
<section class="pad"><div class="wrap">
<div class="center" style="max-width:820px;margin:0 auto 40px">
<div class="eyebrow">Work with us</div>
<h2 class="sec-title">Work with the Tanit XR team</h2>
<p class="sec-sub" style="margin:0">A few things our leadership team can do for organizations, never our
volunteers’ work, which is not for sale. Grassroots heritage and community groups get our help for free; institutions,
companies and funders pay a low rate that goes straight back into the community, hosting, tools, training and
scanning days.</p></div>
<div class="acts" style="margin-top:0">{cards}</div>
</div></section>

<section class="pad" style="background:var(--cloud)"><div class="wrap">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:44px;align-items:start">
<div>
<div class="eyebrow">How it works</div>
<h2 class="sec-title">Three steps</h2>
<div class="steps" style="grid-template-columns:1fr">
<div><b>Tell us what you need</b><p style="color:var(--gray);font-size:14.5px;margin-top:6px">A few lines about your objects, audience or event, your timeline and where you are.</p></div>
<div><b>We scope it together</b><p style="color:var(--gray);font-size:14.5px;margin-top:6px">A short call with our team. We tell you what is free, what has a rate, and what our volunteers can realistically deliver.</p></div>
<div><b>You get the work, and the community gets funded</b><p style="color:var(--gray);font-size:14.5px;margin-top:6px">Invoices go through our fiscal sponsor, the Florida Community Innovation Foundation (a US 501(c)(3)).</p></div>
</div>
</div>
<div>
<div class="eyebrow">Get in touch</div>
<h2 class="sec-title">Partner with us</h2>
<form class="nice" action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Services inquiry, tanitxr.org">
<input type="hidden" name="_captcha" value="true">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" style="display:none">
<label class="req" for="sv-name">Name</label><input id="sv-name" type="text" name="name" required>
<label class="req" for="sv-org">Organization</label><input id="sv-org" type="text" name="organization" required>
<label class="req" for="sv-email">Email</label><input id="sv-email" type="email" name="email" required>
<label class="req" for="sv-type">What are you interested in?</label>
<select id="sv-type" name="service" required><option value="">Pick one</option>
<option>Workshops &amp; training</option><option>Talks &amp; consulting</option><option>Sharing opportunities</option>
<option>Hackathon &amp; challenge tracks</option><option>Something else</option></select>
<label for="sv-msg">Tell us more</label><textarea id="sv-msg" name="message" rows="4" placeholder="Objects, audience, dates, location, budget if you have one."></textarea>
<button class="btn btn-gold" type="submit">Send</button>
</form>
<p style="color:var(--gray);font-size:13.5px;margin-top:12px">Or email <a href="mailto:{EMAIL}" style="color:var(--gold-dark)">{EMAIL}</a>.</p>
</div></div></div></section>

<section class="band pad"><div class="wrap center">
<div class="eyebrow">Prefer to give?</div>
<h2 class="sec-title">Every service funds the community, so does every donation</h2>
<a class="btn btn-gold" href="{DONATE_URL}" target="_blank" rel="noopener">Donate</a>
&nbsp; <a class="btn btn-line-light" href="index.html#funding">How we’re funded</a>
</div></section>"""
    page("services.html", "Services", body, active="about.html",
         desc="Work with the Tanit XR team: workshops and training, talks and consulting, sharing opportunities and hackathon tracks, free for grassroots groups, low rates for institutions. Our volunteers’ work is never for sale.")


def build_press():
    groups = [("Awards", ["auggie"]), ("Exhibitions", ["xrwomen"]), ("Talks & events", ["awe", "eljem", "immersegt"]),
              ("Podcasts & video", ["voices", "niantic"]), ("Articles", ["aljazeera", "carthage", "medium"]),
              ("Partnerships", ["nigeria"])]
    by = {x["anchor"]: x for x in PRESS}
    sections = ""
    for title, keys in groups:
        sections += f'<h2 class="sec-title" style="font-size:30px;margin:46px 0 18px">{title}</h2>' + press_cards([by[k] for k in keys])
    body = f"""
{page_hero("Press &amp; Recognition", '<a href="about.html">About</a> &nbsp;›&nbsp; Press &amp; Recognition', bg="sv-IMG_1232.jpg", pos="center 30%")}
<section class="pad"><div class="wrap">
<p class="sec-sub" style="margin:0 0 10px;max-width:800px">Where Tanit XR has been recognized, featured and heard. For
interviews, talks or media requests write to <a href="mailto:{EMAIL}" style="color:var(--gold-dark)">{EMAIL}</a>.</p>
{sections}
<h2 class="sec-title" id="niantic" style="font-size:30px;margin:46px 0 18px">Featured by Niantic Spatial</h2>
<p class="sec-sub" style="margin:0 0 18px;max-width:800px">Nathan Bowser interviewed Ines Said for Niantic Spatial about Tanit XR and our Scaniverse capture of the amphitheatre of El Jem.</p>
<div class="embed16" style="max-width:820px"><iframe src="{NIANTIC_EMBED}" title="Niantic Spatial feature on Tanit XR" allowfullscreen loading="lazy"></iframe></div>
<p style="margin-top:12px"><a class="btn btn-line" href="https://www.linkedin.com/feed/update/urn:li:activity:7488488682652495873" target="_blank" rel="noopener">Watch the post on LinkedIn</a></p>
<h2 class="sec-title" style="font-size:30px;margin:46px 0 18px">Publications</h2>
<div class="press">
<a href="assets/pdf/El-Jem-2026-Paper_English.pdf" target="_blank" rel="noopener"><div class="k">Paper · English</div><h3>El Jem Conference 2026 paper</h3><p>Digital documentation, XR and citizen science for community-driven heritage preservation.</p></a>
<a href="assets/pdf/El-Jem-2026-Paper_French.pdf" target="_blank" rel="noopener"><div class="k">Paper · Français</div><h3>Article de la conférence d’El Jem 2026</h3><p>Documentation numérique, XR et science participative.</p></a>
<a href="assets/pdf/El-Jem-2026-Paper_Arabic.pdf" target="_blank" rel="noopener"><div class="k">Paper · دارجة تونسية</div><h3>ورقة مؤتمر الجم 2026</h3><p>التوثيق الرقمي والواقع الممتد والعلوم التشاركية.</p></a>
</div>
<h2 class="sec-title" style="font-size:30px;margin:46px 0 18px">Media kit</h2>
<div class="press">
<a href="assets/pdf/TanitXR_One-Pager_English-French-Arabic.pdf" target="_blank" rel="noopener"><div class="k">PDF</div><h3>One-pager (EN / FR / AR)</h3><p>Who we are, what we do, how to help, one page in three languages.</p></a>
<a href="{img('tanitxr-logo_red_vertical.png', 1200, as_jpeg=False)}" target="_blank" rel="noopener"><div class="k">PNG</div><h3>Logo, vertical</h3><p>Transparent background, red mark.</p></a>
<a href="{img('tanitxr-logo_red_horizontal.png', 1600, as_jpeg=False)}" target="_blank" rel="noopener"><div class="k">PNG</div><h3>Logo, horizontal</h3><p>Transparent background, red mark.</p></a>
</div>
</div></section>
<section class="band pad"><div class="wrap center">
<div class="eyebrow">Support the work</div>
<h2 class="sec-title">Volunteer-run, founder-funded, so far</h2>
<p class="sec-sub" style="color:rgba(255,255,255,.85)">Our recognition came before our funding. Help us change that.</p>
<a class="btn btn-gold" href="{DONATE_URL}" target="_blank" rel="noopener">Donate</a>
&nbsp; <a class="btn btn-line-light" href="index.html#funding">How we’re funded</a>
</div></section>"""
    page("press.html", "Press & Recognition", body, active="about.html",
         desc="Awards, talks, podcasts, articles and papers about Tanit XR, including the Auggie Awards 2026 finalist nomination and the Voices of VR interview.")



def build_archive():
    sites = sorted({m["site"] for m in MODELS})
    fbtns = '<button class="fbtn on" data-f="*">All ({})</button>'.format(len(MODELS)) + "".join(
        f'<button class="fbtn" data-f="{esc(s)}">{esc(s)} ({sum(1 for m in MODELS if m["site"] == s)})</button>'
        for s in sites)
    cards = "".join(
        f'<a class="card arch" data-site="{esc(m["site"])}" href="{m["href"]}">'
        f'<div class="ph"><img src="{img(m["img"], 800)}" alt="{esc(m["title"])}" loading="lazy"></div>'
        f'<div class="tx"><h3>{esc(m["title"])}</h3><div class="meta">{esc(m["place"])}'
        + ('&nbsp; <span class="chip" style="font-size:11.5px">🎮 Game-ready</span>' if m.get("gameready") else '')
        + '</div></div></a>'
        for m in MODELS)
    body = f"""
{page_hero("Explore the Tanit XR Archive", "Archive", bg="aug-20260813_124249.jpg")}
<section class="pad"><div class="wrap">
<p class="sec-sub" style="margin:0 0 30px">A free, growing library of 3D scans of Tunisia’s endangered
heritage, mosaics, statues, stelae, and ruins captured by our volunteers. Every model can be explored
interactively, and viewed in augmented reality on your phone.</p>
<div class="arch-index">
<a class="ix" href="#grid"><b>{len(MODELS)}</b><span><strong>heritage scans</strong>
Photogrammetry records of statues, mosaics, stelae and ruins, preservation quality, with game-ready twins.</span></a>
<a class="ix gold" href="#volunteer-made"><b>{len(VOLUNTEER_MADE)}</b><span><strong>models made by our volunteers</strong>
Lamps, pottery, plants and everyday objects modeled by hand for our virtual museum. Click to explore in 3D.</span></a>
</div>
<div class="filters">{fbtns}<a class="fbtn" href="#volunteer-made">🏺 Made by volunteers ({len(VOLUNTEER_MADE)})</a></div>
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
{_volunteer_made_section()}
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


def volunteer_made_cards(limit=None):
    cards = ""
    for vm in VOLUNTEER_MADE[:limit]:
        byname, byhref = creator_credit(vm.get("by"))
        credit = ("by " + (f'<a href="{byhref}" style="color:var(--gold-dark);font-weight:700">{esc(byname)}</a>'
                  if byhref else esc(byname))) if byname else ""
        cards += model_card(vm["title"], vm.get("thumb"), f"https://sketchfab.com/models/{vm['uid']}",
                            meta=credit, uid=vm["uid"], external=True)
    return cards


def _volunteer_made_section():
    if not VOLUNTEER_MADE:
        return ""
    cards = volunteer_made_cards()
    return f"""
<section class="pad" style="background:var(--cloud)" id="volunteer-made"><div class="wrap">
<div class="center"><div class="eyebrow">🏺 Made by our volunteers</div>
<h2 class="sec-title">Recreated by hand, for VR &amp; learning</h2>
<p class="sec-sub">Beyond photogrammetry scans, our volunteers model Tunisian objects, pottery, lamps,
tilework, everyday heritage, from scratch, for our virtual museum and community projects.</p></div>
<div class="cards">{cards}</div></div></section>"""


MANUAL_CONTRIB = {  # work Sketchfab can't record, confirmed by Ines
    "ana-beatriz-vega-gonzalez": [  # "Bety" on Slack
        ("built", "Scanning & optimization guide for volunteers (with Rachel West and Nick Kaufmann)", "scanning-guide.html", None, "sv-IMG_4213.jpg"),
        ("built", "Social media videos for Tanit XR", "community.html", None, "aug-PXL_0814_112926.jpg"),
    ],
    "patrick-molen": [
        ("built", "Virtual museum, the original room and the modular building kit", "museum.html", None, "museum-progress-jan-2026.jpg"),
        ("built", "Tutorial videos for volunteers", "community.html", None, "museum-hall-arches.jpg"),
        ("built", "Mentoring students", "community.html", None, "sv-IMG_1315.jpg"),
    ],
}


def build_model_pages():
    CONTRIB.clear()  # rebuilt each language pass
    for slug, items in MANUAL_CONTRIB.items():
        for kind, label, href, uid, thumb in items:
            _add_contrib(slug, kind, label, href, uid=uid, thumb=thumb)
    for vm in VOLUNTEER_MADE:  # decorative props → "made" contribution
        _add_contrib(member_slug(vm.get("by")), "made", vm["title"],
                     f"https://sketchfab.com/models/{vm['uid']}", uid=vm["uid"], thumb=vm.get("thumb"))
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
        gr = m.get("gameready")
        gr_html = f"""
<div style="margin-top:56px;padding-top:34px;border-top:2px solid var(--gold)">
<div class="eyebrow">🎮 Game-ready version</div>
<p style="color:#3c454c;max-width:760px">The scan above is our full-detail <b>preservation record</b>.
This optimized version is light enough for real-time use, game engines, WebXR, VR, and community
projects. Build something with it.</p>
<iframe class="embed" src="https://sketchfab.com/models/{gr}/embed?ui_theme=dark"
title="{esc(m["title"])}, game-ready 3D model" allow="autoplay; fullscreen; xr-spatial-tracking"
allowfullscreen loading="lazy"></iframe>
<p style="margin-top:16px"><a class="btn btn-gold" href="https://sketchfab.com/3d-models/{gr}"
target="_blank" rel="noopener">Open the game-ready model on Sketchfab</a></p>
</div>""" if gr else ""
        # creator attribution (records the contribution onto the member's profile)
        credits = []
        s_slug = member_slug(m.get("scanned_by"))
        o_slug = member_slug(m.get("optimized_by"))
        s_name, s_href = creator_credit(m.get("scanned_by"))
        o_name, o_href = creator_credit(m.get("optimized_by"))
        # Sketchfab only records the uploader; Ines can reassign credit per model in creators-map.json
        ov = next((v for k, v in CREATORS.get("model_overrides", {}).items()
                   if k.lower() in m["title"].lower()), {})
        if ov.get("scanned") in TEAM_BY_SLUG:
            s_slug = ov["scanned"]; s_name, s_href = TEAM_BY_SLUG[s_slug]["name"], TEAM_BY_SLUG[s_slug]["href"]
        if ov.get("optimized") in TEAM_BY_SLUG:
            o_slug = ov["optimized"]; o_name, o_href = TEAM_BY_SLUG[o_slug]["name"], TEAM_BY_SLUG[o_slug]["href"]
        if s_slug:
            _add_contrib(s_slug, "scanned", m["title"], m["href"], uid=sk_id, thumb=m["img"])
        if s_name:
            credits.append(f'3D scan by {credit_link(s_name, s_href)}')
        if o_slug and o_slug != s_slug:
            _add_contrib(o_slug, "optimized", m["title"], m["href"], uid=gr, thumb=m["img"])
        if o_name:
            credits.append(f'game-ready optimization by {credit_link(o_name, o_href)}')
        credit_html = (f'<p style="color:var(--gray);font-size:14.5px;margin-top:6px">👐 ' +
                       " · ".join(credits) + "</p>") if credits else ""
        text = esc(m["text"])[:4000]
        body = f"""
{page_hero(esc(m["title"]), f'<a href="archive.html">Archive</a> &nbsp;›&nbsp; {esc(m["title"])}')}
<section class="pad"><div class="wrap" style="max-width:960px">
{embed}
<div style="margin:26px 0 10px"><span class="chip">{esc(m["site"])}</span><span class="chip gold">{esc(m["place"])}</span>{'<span class="chip">🎮 Game-ready available</span>' if gr else ''}</div>
{credit_html}
<p style="color:#3c454c">{text}</p>
<div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:30px">
{sk_link}
<a class="btn btn-gold" href="archive.html">← Back to Archive</a>
</div>
{gr_html}
<p style="margin-top:26px;padding:16px 20px;background:var(--cloud);border-radius:10px;font-size:14.5px;color:var(--gray)">
🤝 This scan exists because of volunteers, from scanning on site to cleanup and research.
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
{page_hero("News", "News", bg="aug-PXL_0811_150055.jpg")}
<section class="pad"><div class="wrap">
<div class="cards">{cards}</div>
</div></section>"""
    page("news.html", "News", body)

    NEWS_AUTHOR = {
        "storm-harry-neapolis-and-a-digital-moment-of-preservation": "Margarita Johnson",
        "material-and-meaning-marble-identity-and-cultural-exchange-in-ancient-carthage": "Margarita Johnson",
        "a-beginning-why-tanit-xr-exists": "Ines Said",
        "a-2-000-year-old-ghost-town-on-cape-bon": "Laura Harrison",
    }
    for n in NEWS:
        content = _clean_wp_content(n["content"])
        author = NEWS_AUTHOR.get(n["clean_slug"])
        a_slug = author_slug(author) if author else None
        if a_slug:
            _add_contrib(a_slug, "wrote", n["title"], n["href"], thumb=n.get("img"))
            byline = (f'By <a href="{TEAM_BY_SLUG[a_slug]["href"]}" '
                      f'style="color:var(--gold-dark);font-weight:700">{esc(author)}</a> · ') \
                if a_slug in TEAM_BY_SLUG else f"By {esc(author)} · "
        else:
            byline = f"By {esc(author)} · " if author else ""
        body = f"""
{page_hero(esc(n["title"]), f'<a href="news.html">News</a> &nbsp;›&nbsp; {esc(n["title"][:50])}')}
<section class="pad"><div class="wrap"><div class="prose">
<p style="color:var(--gray);font-size:14px">{byline}Published {n['date']}</p>
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
{page_hero("Our People", "Our People", bg="sv-IMG_1315.jpg", pos="center 30%")}
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
    page("team.html", "Our People", body)

    def link_label(u):
        if u.startswith("mailto:"):
            return "Email"
        host = re.sub(r"^https?://(www\.)?", "", u).split("/")[0]
        for k, lab in (("linkedin.com", "LinkedIn"), ("instagram.com", "Instagram"), ("github.com", "GitHub"),
                       ("x.com", "X"), ("twitter.com", "X"), ("youtube.com", "YouTube"), ("sketchfab.com", "Sketchfab")):
            if k in host:
                return lab
        return host

    for p in TEAM + COMMUNITY:
        links = ('<div class="plinks">' + "".join(
            f'<a href="{esc(u)}" target="_blank" rel="noopener" title="{esc(link_icon(u)[1])}" aria-label="{esc(link_icon(u)[1])}">'
            f'{link_icon(u)[0]}</a>' for u in p["links"]) + '</div>') if p["links"] else ""
        photo = (f'<img src="{img(p["photo"], 700)}" alt="{esc(p["name"])}" '
                 f'style="border-radius:14px;max-width:340px;width:100%">') if p["photo"] else ""
        bio = esc(p["bio"]) if p["bio"] else "Part of the Tanit XR volunteer network."
        # contributions this person made (scans, optimizations, models, articles)
        c = CONTRIB.get(p["slug"], {})
        blocks = []
        total = 0
        for kind, heading, meta in (("built", "🏗 Built for the community", "Community"),
                                    ("scanned", "🏛 3D scans captured", "Photogrammetry scan"),
                                    ("optimized", "🎮 Models optimized for game/VR", "Game-ready optimization"),
                                    ("made", "🏺 Models made by hand", "Modeled for the virtual museum"),
                                    ("wrote", "✍️ Articles written", "Article")):
            seen, cards = set(), ""
            for it in c.get(kind, []):
                if it["label"] in seen:
                    continue
                seen.add(it["label"])
                cards += model_card(it["label"], it["thumb"], it["href"], meta=meta, uid=it["uid"],
                                    external=it["href"].startswith("http"))
            if cards:
                total += len(seen)
                blocks.append(f'<h3 style="margin:38px 0 18px;font-size:22px">{heading}</h3>'
                              f'<div class="cards">{cards}</div>')
        contrib_html = (f'<section class="pad" style="background:var(--cloud);padding-top:56px"><div class="wrap">'
                        f'<div class="eyebrow">Contributions to Tanit XR</div>'
                        f'<h2 class="sec-title" style="font-size:32px">What {esc(p["name"].split()[0])} has made with us</h2>'
                        f'<p class="sec-sub" style="margin:0">Press <b>View in 3D</b> on any model to explore it right here.</p>'
                        f'{"".join(blocks)}</div></section>') if blocks else ""
        body = f"""
{page_hero(esc(p["name"]), f'<a href="team.html">Our People</a> &nbsp;›&nbsp; {esc(p["name"])}')}
<section class="pad"><div class="wrap" style="max-width:960px">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:44px;align-items:start">
<div>{photo}</div>
<div>
<div class="eyebrow">{esc(p["role"])}</div>
<p style="font-size:17px;color:#2c343b">{bio}</p>
<div style="margin-top:26px">{links}</div>
</div></div>
</div></section>
{contrib_html}
<section class="pad-sm"><div class="wrap" style="max-width:960px">
<p><a class="btn btn-gold" href="team.html">← Back to Our People</a></p>
</div></section>"""
        page(p["href"], p["name"], body, active="team.html", desc=p["bio"][:150])


def build_opportunities():
    LBL = {
        "en": {"dl": "Deadline: ", "closed": "Closed", "days": " days left", "day": " day left",
               "none": "No opportunities match those filters.", "det": "See details",
               "apply": "Apply / Info →", "more": "▾ More", "less": "▴ Less",
               "feat": "★ Featured", "helpful": "👍 Helpful", "applied": "✅ I applied",
               "vol": "Volunteer with us →", "closedh": "Closed opportunities", "showall": "Show all {n} closed opportunities", "showless": "Show fewer", "terms": {}},
        "fr": {"dl": "Date limite : ", "closed": "Clôturé", "days": " jours restants", "day": " jour restant",
               "none": "Aucune opportunité ne correspond à ces filtres.", "det": "Voir les détails",
               "apply": "Postuler / Infos →", "more": "▾ Plus", "less": "▴ Moins",
               "feat": "★ À la une", "helpful": "👍 Utile", "applied": "✅ J’ai postulé",
               "vol": "Devenez bénévole →", "closedh": "Opportunités clôturées", "showall": "Voir les {n} opportunités clôturées", "showless": "Voir moins",
               "terms": {"Rolling": "Continu", "Fixed": "Date fixe", "Open": "Ouvert", "TBA": "À annoncer"}},
        "ar": {"dl": "الموعد النهائي: ", "closed": "مغلق", "days": " أيام متبقية", "day": " يوم متبقٍ",
               "none": "لا توجد فرص مطابقة لهذه المرشحات.", "det": "انظر التفاصيل",
               "apply": "قدّم / التفاصيل ←", "more": "▾ المزيد", "less": "▴ أقل",
               "feat": "★ مميّزة", "helpful": "👍 مفيدة", "applied": "✅ لقد قدّمت",
               "vol": "تطوّع معنا ←", "closedh": "فرص انتهت", "showall": "عرض كل الفرص المنتهية ({n})", "showless": "عرض أقل",
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
        "t": "Volunteer with Tanit XR, Preserve Heritage in 3D & XR",
        "d": "Tanit XR is powered by volunteers: 3D scanning, model cleanup, XR development, "
             "historical research, writing, translation, and storytelling. Join from Tunisia or "
             "anywhere in the world, all experience levels welcome, fully remote friendly.",
        "ty": "Volunteer", "el": ["Open to all"], "rg": "Global", "co": "", "md": "Remote",
        "dt": "Rolling", "dd": None, "pub": _dt.date.today().isoformat(), "u": "../volunteer/",
    })
    types = sorted({o["type"] for o in OPPS if o["type"]})
    eligs = sorted({e for o in OPPS for e in o["eligibility"]})
    modes = sorted({o["mode"] for o in OPPS if o["mode"]})
    def pills(sel, values):
        return ('<div class="pills" data-for="' + sel + '"><button type="button" class="pill on" data-v="">All</button>'
                + "".join(f'<button type="button" class="pill" data-v="{esc(v)}">{esc(v)}</button>' for v in values) + '</div>')
    def opts(vals):
        return "".join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in vals)
    body = f"""
{page_hero("Art, XR &amp; Impact Opportunities", "Art, XR &amp; Impact Opportunities", bg="aug-PXL_0811_150245.jpg")}
<section class="pad"><div class="wrap">
<p class="sec-sub" style="margin:0 0 26px;max-width:860px">A curated board of grants, residencies, fellowships, open calls,
and events for artists, XR creators, educators, students, and changemakers, updated regularly by the
Tanit XR team. Also published as our
<a href="https://www.linkedin.com/newsletters/art-xr-impact-opportunities-7370189407523454976/"
target="_blank" rel="noopener" style="color:var(--gold-dark)">LinkedIn newsletter</a>.</p>
<div class="subtop">
<div><b style="font-family:var(--serif);font-size:20px;font-weight:400;display:block">Get these in your inbox</b>
<span style="color:var(--gray);font-size:14px">New opportunities every one to two weeks. Free.</span></div>
{subscribe_form(dark=False)}
</div>
<div class="toolbar">
<label class="search"><span class="ico">{ICO_SEARCH}</span><input type="search" id="q" placeholder="Search opportunities…"></label>
<div class="sortwrap"><span class="flabel">Sort</span>
<div class="seg" role="group" aria-label="Sort">
<button type="button" class="on" data-sort="soon">Deadline soonest</button><button type="button" data-sort="new">Newest</button></div></div>
</div>
<div class="fgroups">
<div class="fgroup"><span class="flabel">Type</span>{pills("f-type", types)}</div>
<div class="fgroup"><span class="flabel">Eligibility</span>{pills("f-elig", eligs)}</div>
<div class="fgroup"><span class="flabel">Mode</span>{pills("f-mode", modes)}</div>
<button type="button" id="clearf" class="clearf" hidden>Clear filters</button>
</div>
<div class="board-tools" hidden>
<select id="f-type"><option value="">Type</option>{opts(types)}</select>
<select id="f-elig"><option value="">Eligibility</option>{opts(eligs)}</select>
<select id="f-mode"><option value="">Mode</option>{opts(modes)}</select>
<select id="sort"><option value="soon">Deadline soonest</option><option value="new">Newest</option></select>
</div>
<div id="featured"></div>
<div id="board"></div>
<div id="closedwrap" hidden><h3 class="closed-h"></h3><div id="closed"></div>
<p style="margin-top:18px"><button id="moreclosed" class="btn btn-line" type="button"></button></p></div>

<div class="band" style="margin-top:64px;border-radius:14px;padding:44px 38px">
<div style="max-width:640px">
<div class="eyebrow">Newsletter</div>
<h2 class="sec-title" style="font-size:30px">Never miss a deadline</h2>
<p style="margin-bottom:22px">Get new grants, residencies, and open calls for art, XR &amp; impact in your
inbox, free, from the Tanit XR team. You'll also be first to hear how our heritage-preservation work is
going.</p>
{subscribe_form()}
<p style="font-size:13px;color:rgba(255,255,255,.6);margin-top:12px">No spam, opportunities and Tanit XR
news only. Also published on
<a href="https://www.linkedin.com/newsletters/art-xr-impact-opportunities-7370189407523454976/"
target="_blank" rel="noopener" style="color:var(--gold)">LinkedIn</a>.</p>
</div>
</div>

<div style="margin-top:26px;background:var(--cloud);border:1px solid var(--mist);border-radius:12px;padding:36px 34px">
<h2 class="sec-title" style="font-size:28px">Know an opportunity we should feature?</h2>
<p style="color:var(--gray);margin-bottom:6px">Send it our way, if it's a fit, it will appear on this board
and in the newsletter.</p>
<form class="nice" action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Opportunity submission, tanitxr.org">
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
document.querySelectorAll('.pills').forEach(g=>g.addEventListener('click',e=>{{
  const b=e.target.closest('.pill');if(!b)return;
  g.querySelectorAll('.pill').forEach(x=>x.classList.remove('on'));b.classList.add('on');
  document.getElementById(g.dataset.for).value=b.dataset.v;
  document.getElementById('clearf').hidden=![...document.querySelectorAll('.pills .pill.on')].some(x=>x.dataset.v);
  render();
}}));
document.querySelector('.seg').addEventListener('click',e=>{{
  const b=e.target.closest('button');if(!b)return;
  document.querySelectorAll('.seg button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
  document.getElementById('sort').value=b.dataset.sort;render();
}});
document.getElementById('clearf').addEventListener('click',()=>{{
  document.querySelectorAll('.pills').forEach(g=>{{g.querySelectorAll('.pill').forEach((x,i)=>x.classList.toggle('on',i===0));document.getElementById(g.dataset.for).value='';}});
  document.getElementById('q').value='';document.getElementById('clearf').hidden=true;render();
}});
let showAllClosed=false;
document.getElementById('moreclosed').addEventListener('click',()=>{{showAllClosed=!showAllClosed;render();if(!showAllClosed)document.getElementById('closedwrap').scrollIntoView({{behavior:'smooth',block:'start'}});}});
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
  const card=(o,extra)=>{{
    const [dl,cls]=dlOf(o);
    const more=o.d.length>260?'<button class="more" type="button">'+LBL.more+'</button>':'';
    return '<div class="opp'+(o._closed?' closed':'')+(extra||'')+'" id="opp-'+o.id+'"><div class="top">'+chipsOf(o)+'</div>'+
      '<h3>'+o.t+'</h3><div class="dl '+cls+'">'+dl+'</div>'+
      '<p class="desc">'+o.d+'</p>'+more+btnOf(o)+reactsHtml(o)+'</div>';
  }};
  const openList=rest.filter(o=>!o._closed), closedList=rest.filter(o=>o._closed);
  board.innerHTML=openList.map(o=>card(o)).join('')||(closedList.length?'':'<p style="color:var(--gray)">'+LBL.none+'</p>');
  const cw=document.getElementById('closedwrap'), cb=document.getElementById('closed'), mb=document.getElementById('moreclosed');
  if(closedList.length){{
    cw.hidden=false;
    cw.querySelector('.closed-h').textContent=LBL.closedh+' ('+closedList.length+')';
    cb.innerHTML=closedList.map((o,i)=>card(o,(i>=3&&!showAllClosed)?' hid':'')).join('');
    mb.hidden=closedList.length<=3;
    mb.textContent=showAllClosed?LBL.showless:LBL.showall.replace('{{n}}',closedList.length);
  }} else {{ cw.hidden=true; }}
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
<figure class="infographic"><img src="{img('Volunteer-Page-English-2.png', 1600, as_jpeg=False)}"
alt="Tanit XR, Volunteer to help protect global heritage. Cultural memory powered by volunteers and digital technology." loading="lazy"></figure>
<div class="center" style="margin-top:80px"><div class="eyebrow">🏺 What our volunteers create</div>
<h2 class="sec-title">From a phone scan to a museum-ready model</h2>
<p class="sec-sub">Volunteers scan sites on the ground, optimize models for VR, write articles, and model heritage
objects by hand, like these.</p></div>
<div class="cards" style="grid-template-columns:repeat(auto-fill,minmax(240px,1fr))">{volunteer_made_cards(3)}</div>
<p class="center" style="margin-top:26px"><a class="btn btn-line" href="archive.html#volunteer-made">See all {len(VOLUNTEER_MADE)} volunteer-made models</a></p>
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
</div></section>"""
    page("volunteer.html", "Volunteer", body)


def build_create_profile():
    body = f"""
{page_hero("Create Your Profile", '<a href="volunteer.html">Volunteer</a> &nbsp;›&nbsp; Create Your Profile', bg="sv-IMG_8034.jpg")}
<section class="pad"><div class="wrap" style="max-width:760px">
<div class="notice" style="margin:0 0 22px"><b>For accepted Tanit XR volunteers only.</b> Not a volunteer yet? Start with the
<a href="volunteer.html" style="color:var(--gold-dark)">volunteer interest form</a>, profiles are created after you join.</div>
<p class="sec-sub" style="margin:0 0 8px">Already volunteering with Tanit XR? Submit your profile and, once
approved by the team, it will appear on our <a href="team.html" style="color:var(--gold-dark)">Our People</a>
page.</p>
<form class="nice" action="{PROFILE_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="New volunteer profile submission, tanitxr.org">
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
<div class="hint" style="margin-top:22px"><b>Links, all optional.</b> Only the ones you add appear on your profile, as icons.</div>
<label for="plink1">LinkedIn</label>
<input id="plink1" name="linkedin" type="url" placeholder="https://www.linkedin.com/in/…">
<label for="plink2">Instagram</label>
<input id="plink2" name="instagram" type="url" placeholder="https://www.instagram.com/…">
<label for="plink3">Website / Portfolio</label>
<input id="plink3" name="website" type="url">
<label for="plink4">GitHub</label>
<input id="plink4" name="github" type="url" placeholder="https://github.com/…">
<label for="plink5">Sketchfab</label>
<input id="plink5" name="sketchfab" type="url" placeholder="https://sketchfab.com/…">
<label for="plink6">Other (YouTube, X, Behance…)</label>
<input id="plink6" name="other_link" type="url">
<label for="pshowmail">Show a public email icon on your profile? (optional)</label>
<input id="pshowmail" name="public_email" type="email" placeholder="Leave empty to keep your email private">
<label class="req" for="pemail">Email</label>
<input id="pemail" name="email" type="email" required>
<div class="hint">Used only to contact you about your profile, it is not published.</div>
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
<li><b>Architecture and ruins</b>, doors, arches, columns, facades, walls, courtyards, tombs, monuments, and historic homes</li>
<li><b>Objects and artifacts</b>, pottery, tools, carvings, statues, tiles, jewelry, textiles, inscriptions, and household items</li>
<li><b>Small details</b>, patterns, textures, symbols, damage, repairs, maker’s marks, or decorative elements</li>
<li><b>Everyday heritage</b>, bakeries, workshops, markets, gathering places, family heirlooms, gardens, and community spaces</li>
<li><b>At-risk heritage</b>, places or objects threatened by weather, neglect, development, conflict, theft, or loss of memory</li>
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
personal stories. Tanit XR is not just preserving objects, we are preserving the worlds, memories, and
meanings around them.</p>
<h3>🧱 Step-by-Step Scanning Instructions</h3>
<h4>1. Open Scaniverse</h4>
<ul>
<li>Tap the “+” button to start a new scan.</li>
<li>Choose <b>“Mesh”</b> (not “Splat”), this is what we need for Tanit XR.</li>
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
<li>Processing uses a lot of data, it’s best to wait until you’re home with Wi-Fi.</li>
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
<li>Focus on texture and angles, walk around the object fully</li>
<li>Natural daylight is good, but harsh sun causes glare, avoid scanning at noon</li>
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
</div>
<div class="shots">
<img src="{img('Screenshot-2025-12-10-at-8.18.55-PM.png', 900)}" alt="Gaussian splat captured with a phone" loading="lazy">
<img src="{img('Screenshot-2025-12-10-at-8.21.21-PM.png', 900)}" alt="Reviewing scans together in an immersive space" loading="lazy">
<img src="{img('Screenshot-2025-12-23-at-8.36.36-PM.png', 900)}" alt="Splats With Phones cohort session" loading="lazy">
</div>
<div class="prose" id="apply">
<h2>Apply for the next cohort</h2>
<form class="nice" action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Splats With Phones application, tanitxr.org">
<input type="hidden" name="_captcha" value="true">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" style="display:none">
<label class="req" for="sp-name">Full Name</label><input id="sp-name" type="text" name="name" required>
<label class="req" for="sp-email">Email</label><input id="sp-email" type="email" name="email" required>
<label class="req" for="sp-tz">Time Zone</label><input id="sp-tz" type="text" name="time_zone" placeholder="Example: EST, GMT+1, Tunisia time" required>
<label class="req" for="sp-why">Why do you want to join?</label>
<textarea id="sp-why" name="why" rows="4" placeholder="Tell us what draws you to this cohort and what you hope to gain from it. We are interested in your motivation and curiosity, not perfection." required></textarea>
<label class="req" for="sp-bio">Short Bio</label>
<textarea id="sp-bio" name="bio" rows="4" placeholder="What you do, what you are studying, or any communities or projects you are involved in." required></textarea>
<label class="req" for="sp-exp">Experience Level</label>
<select id="sp-exp" name="experience" required><option value="">Any level is welcome, pick one</option>
<option>None yet</option><option>Beginner</option><option>Some experience</option><option>Advanced</option></select>
<label class="req" for="sp-att">Attendance Commitment</label>
<select id="sp-att" name="attendance" required><option value="">This course is live and interactive, pick one</option>
<option>Yes, I can attend at least 5 of 6 sessions</option><option>Not sure yet</option></select>
<label for="sp-more">Anything else you want us to know?</label>
<textarea id="sp-more" name="more" rows="3" placeholder="Anything that might help us better understand you or your availability."></textarea>
<button class="btn btn-gold" type="submit">Apply</button>
</form>
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
was founded in 2025 by <a href="team/ines-said.html">Ines Said</a>, a Tunisian XR developer, to preserve
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
<p>As part of the event, <a href="team/dr-caroline-nickerson.html">Caroline Nickerson, PhD</a>, led a
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
<div class="stats icons" style="margin-top:14px">
<div><img src="{img('artifacts.png', 200, as_jpeg=False)}" alt=""><b style="color:var(--gold-dark)">{stat('artifacts')}</b><span style="color:var(--gray)">Artifacts Scanned</span></div>
<div><img src="{img('sites.png', 200, as_jpeg=False)}" alt=""><b style="color:var(--gold-dark)">{stat('sites')}</b><span style="color:var(--gray)">Sites Documented</span></div>
<div><img src="{img('volunteer-1.png', 200, as_jpeg=False)}" alt=""><b style="color:var(--gold-dark)">{stat('volunteers')}</b><span style="color:var(--gray)">Volunteers</span></div>
<div><img src="{img('global.png', 200, as_jpeg=False)}" alt=""><b style="color:var(--gold-dark)">{stat('reach')}</b><span style="color:var(--gray)">Global Reach</span></div>
</div>
</div></section>
<section class="pad" style="background:var(--cloud)"><div class="wrap"><div class="prose">
<h2 style="margin-top:0">We Are A Non-Profit Organization</h2>
<p>Tanit XR operates under fiscal sponsorship with Florida Community Innovation (FCI), a U.S. 501(c)(3)
nonprofit. This partnership allows us to accept tax-deductible donations while we grow toward becoming a
fully independent nonprofit organization.</p>
<p>Our mission is to preserve Tunisia’s endangered heritage through digital scans, immersive technology, and
education. With every artifact we scan and every volunteer we train, we are proving that heritage can be
safeguarded for future generations, no matter the threats of climate change and neglect.</p>
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
{page_hero("Contact", "Contact", bg="sv-IMG_7959.jpg", pos="center 35%")}
<section class="pad"><div class="wrap">
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:56px">
<div>
<h2 class="sec-title">Send us your Questions/Feedback</h2>
<p style="color:var(--gray)">We’ll get back to you as soon as we can.</p>
<form class="nice" action="{FORM_ENDPOINT}" method="POST">
<input type="hidden" name="_subject" value="Contact form, tanitxr.org">
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
        ("$50", "Cover a month of hosting and software for the open archive and the volunteers who optimize "
                "and publish models."),
        ("$250", "Run a free workshop or course session for the community, Splats With Phones, history lessons, "
                 "mentoring and interview prep for students."),
        ("$500", "Sponsor a community scanning and site clean-up day with local volunteers, covering travel, meals "
                 "and shared equipment, and start compensating local contributors for their time."),
        ("$1,000", "Build out the virtual museum and save toward professional scanning gear such as the XGRIDS "
                   "PortalCam, so the community can capture more than a phone allows."),
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
{page_hero("Coming Soon", "Coming Soon", bg="img_4606-copy.jpg", pos="center 40%")}
<section class="pad"><div class="wrap center" style="max-width:640px">
<h2 class="sec-title">👀 Something exciting is on the way.</h2>
<p class="sec-sub">This page will be live soon! In the meantime, explore our archive of 3D scans or join the
volunteer network helping to preserve Tunisia’s heritage.</p>
<a class="btn btn-gold" href="archive.html">Explore the Archive</a> &nbsp;
<a class="btn btn-line" href="index.html">Back Home</a>
</div></section>"""
    page("coming-soon.html", "Coming Soon", body, trending=False)

    # privacy (the old site's page was placeholder text, this is a real minimal policy)
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
        "about": "about.html", "news": "news.html", "our-people": "team.html",
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
        "opportunity": "opportunities.html", "person": "team.html",
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
        href = f"team/{slugify(htmod.unescape(p['title']['rendered']))}.html"
        targets[path_of(p["link"])] = href if href in people_files else "team.html"

    for o in load("opportunity.json"):
        targets[path_of(o["link"])] = f"opportunities.html#opp-{o['slug']}"

    for c in load("categories.json"):
        if "link" in c:
            targets[path_of(c["link"])] = "news.html" if c["name"] == "News" else "archive.html"

    # interim flat names used briefly during the rebuild, keep any shared links alive
    targets["people"] = "team.html"
    for m in MODELS:
        targets[f"model-{m['clean_slug']}"] = m["href"]
    for n in NEWS:
        targets[f"post-{n['clean_slug']}"] = n["href"]
    for p in TEAM + COMMUNITY:
        targets[f"person-{p['slug']}"] = p["href"]

    def pv(t):
        f, _, anchor = t.partition("#")
        stem = f[:-5]
        return ("" if stem == "index" else stem + "/") + (("#" + anchor) if anchor else "")

    built_pages = set(SITEMAP)  # real pages own their paths, never overwrite with a stub
    n = 0
    for path, target in targets.items():
        if not path or f"{path}/" in built_pages:
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
    # clear artifacts of the retired flat naming so stale full pages can't linger
    import glob as _glob
    for pat in ("model-*.html", "person-*.html", "post-*.html", "people.html"):
        for d in ("", "fr/", "ar/"):
            for f in _glob.glob(os.path.join(DOCS, d, pat)):
                os.remove(f)
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
        build_community()
        build_press()
        build_museum()
        build_services()
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
    # newsletter ⇄ board consistency (Ines: "everything needs to be reflected on the website")
    r = subprocess.run(["python3", os.path.join(HERE, "sync_check.py"), "--quiet"], capture_output=True, text=True)
    if r.returncode != 0:
        print("\n⚠ newsletter/website out of sync:\n" + r.stdout.strip())


if __name__ == "__main__":
    main()
