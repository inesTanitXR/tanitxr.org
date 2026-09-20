#!/usr/bin/env python3
"""Retire pages left behind by earlier builds.

Slugs changed over time, so docs/ still holds full pages at addresses the build no longer
produces: duplicates of live pages, missing from the sitemap, carrying no preview tags.
Deleting them would break any link someone shared. So each one becomes a small redirect to
its current address instead, carrying that page's title, description and preview image.

  python3 tools/retire_stale_pages.py            # dry run, prints what it would do
  python3 tools/retire_stale_pages.py --apply

Run it straight after `python3 build.py`: "stale" means "older than the newest build output".
"""
import argparse, difflib, html, os, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
a = ap.parse_args()

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(HERE, "docs")
SITE = "https://tanitxr.org/"
SKIP_TOP = {"assets", "media", "pdf"}

fresh = os.path.getmtime(os.path.join(DOCS, "index.html")) - 10
live_all = set(re.findall(r"<loc>https://tanitxr\.org/(.*?)</loc>", open(os.path.join(DOCS, "sitemap.xml"), encoding="utf-8").read()))
live_en = {u for u in live_all if not u.startswith(("fr/", "ar/"))}
live = live_all


def meta_of(path):
    h = open(path, encoding="utf-8").read()
    def one(pat, d=""):
        m = re.search(pat, h, re.S)
        return html.unescape(m.group(1)) if m else d
    return (one(r'<meta property="og:title" content="(.*?)"') or one(r"<title>(.*?)</title>"),
            one(r'<meta name="description" content="(.*?)"'),
            one(r'<meta property="og:image" content="(.*?)"'))


SECTION_OF = {"model": "archive", "person": "team", "post": "news"}


def target_for(rel):
    """The current address this stale page should point at: same section, closest slug."""
    own = rel[:-len("index.html")].rstrip("/") + "/"     # this page's own address
    stem = rel[:-len("index.html")].rstrip("/")
    lang = ""
    for pre in ("fr/", "ar/"):
        if stem.startswith(pre):
            lang, stem = pre, stem[len(pre):]
    # the interim flat naming used briefly during the rebuild: model-x, person-x, post-x
    head = stem.split("-")[0]
    if "/" not in stem and head in SECTION_OF:
        stem = SECTION_OF[head] + "/" + stem[len(head) + 1:]
    section = stem.split("/")[0] + "/" if "/" in stem else ""
    # match against the English addresses, which is what the sitemap lists, then put the
    # language back on and only keep it if that translated page really exists on disk
    candidates = [u for u in live_en if u.startswith(section) and (lang + u) != own]
    hit = ""
    if candidates:
        pref = [c for c in candidates if c.rstrip("/").startswith(stem) or stem.startswith(c.rstrip("/"))]
        pool = pref or candidates
        best = difflib.get_close_matches(stem + "/", pool, n=1, cutoff=0.55)
        hit = best[0] if best else ""
    if not hit:
        hit = section
    if lang and os.path.exists(os.path.join(DOCS, lang + hit, "index.html")):
        return lang + hit
    return hit


stale = []
for root, dirs, files in os.walk(DOCS):
    rel_root = os.path.relpath(root, DOCS)
    if rel_root.split(os.sep)[0] in SKIP_TOP:
        continue
    for fn in files:
        if not fn.endswith(".html"):
            continue
        fp = os.path.join(root, fn)
        if os.path.getmtime(fp) >= fresh:
            continue
        rel = os.path.relpath(fp, DOCS).replace(os.sep, "/")
        body = open(fp, encoding="utf-8").read()
        is_stub = 'http-equiv="refresh"' in body
        stale.append((rel, is_stub, len(body)))

full = [s for s in stale if not s[1]]
# redirects written before preview tags existed: keep the destination, add the tags
stubs = [s for s in stale if s[1] and "og:image" not in open(os.path.join(DOCS, s[0]), encoding="utf-8").read()]
print(f"{len(stale)} file(s) older than the last build: {len(full)} full page(s), "
      f"{len(stubs)} old redirect(s) with no preview tags.\n")

plan = []
for rel, is_stub, size in sorted(full):
    tgt = target_for(rel)
    plan.append((rel, tgt))
    print(f"  {rel}\n      -> /{tgt}" + ("" if tgt else "   (no match, will point at the home page)"))

for rel, is_stub, size in sorted(stubs):
    body = open(os.path.join(DOCS, rel), encoding="utf-8").read()
    m = re.search(r'url=([^"\']+)', body) or re.search(r'href="([^"]+)"', body)
    dest = (m.group(1) if m else "").strip()
    if dest.startswith("http"):
        tgt = dest[len(SITE):] if dest.startswith(SITE) else ""
    else:
        tgt = os.path.normpath(os.path.join(os.path.dirname(rel), dest)).replace(os.sep, "/").lstrip("./")
        tgt = tgt.rstrip("/") + "/" if tgt else ""
    plan.append((rel, tgt))
    print(f"  {rel} (redirect, adding tags)\n      -> /{tgt}")

if not a.apply:
    print(f"\nDry run. {len(plan)} file(s) would be rewritten. Re-run with --apply.")
    sys.exit(0)

for rel, tgt in plan:
    dest = SITE + tgt
    src = os.path.join(DOCS, tgt, "index.html") if tgt else os.path.join(DOCS, "index.html")
    title, desc, card = meta_of(src) if os.path.exists(src) else ("Tanit XR", "", "")
    out = os.path.join(DOCS, rel)
    with open(out, "w", encoding="utf-8") as f:
        f.write(
            '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
            f'<title>{html.escape(title)}</title>'
            f'<meta name="description" content="{html.escape(desc)}">'
            f'<link rel="canonical" href="{dest}">'
            '<meta property="og:type" content="website">'
            '<meta property="og:site_name" content="Tanit XR">'
            f'<meta property="og:title" content="{html.escape(title)}">'
            f'<meta property="og:description" content="{html.escape(desc)}">'
            f'<meta property="og:url" content="{dest}">'
            f'<meta property="og:image" content="{html.escape(card)}">'
            '<meta property="og:image:width" content="1200">'
            '<meta property="og:image:height" content="630">'
            '<meta name="twitter:card" content="summary_large_image">'
            f'<meta http-equiv="refresh" content="0;url={dest}">'
            f'<script>location.replace("{dest}"+location.hash)</script>'
            f'</head><body><p>This page moved. <a href="{dest}">Continue to {html.escape(title)}</a></p></body></html>')
print(f"\n{len(plan)} page(s) turned into redirects. Nothing was deleted, every old link still works.")
