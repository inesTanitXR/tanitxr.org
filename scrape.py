#!/usr/bin/env python3
"""Scrape tanitxr.org WordPress content via wp-json + rendered HTML.

Outputs:
  wp-data/<type>.json   - full JSON dumps of every content type
  html/<slug>.html      - rendered HTML of every page (design reference)
"""
import json
import os
import time
import urllib.request
import urllib.parse

BASE = "https://tanitxr.org/wp-json/wp/v2"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wp-data")
HTML_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")
os.makedirs(OUT, exist_ok=True)
os.makedirs(HTML_OUT, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) tanitxr-rebuild-scraper"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def fetch_all(rest_base, extra=""):
    """Paginate through a wp/v2 collection."""
    items = []
    page = 1
    while True:
        url = f"{BASE}/{rest_base}?per_page=100&page={page}&_embed=1{extra}"
        try:
            data = json.loads(fetch(url))
        except urllib.error.HTTPError as e:
            if e.code == 400 and page > 1:  # past last page
                break
            print(f"  !! {rest_base} page {page}: HTTP {e.code}")
            break
        if not isinstance(data, list) or not data:
            break
        items.extend(data)
        if len(data) < 100:
            break
        page += 1
        time.sleep(0.3)
    return items


TYPES = [
    "pages", "posts", "media",
    "opportunity", "person", "artifact", "heritage_site", "region",
    "categories", "tags", "users",
    "modula-gallery",
]

for t in TYPES:
    print(f"Fetching {t} ...")
    items = fetch_all(t)
    path = os.path.join(OUT, f"{t.replace('/', '_')}.json")
    with open(path, "w") as f:
        json.dump(items, f, indent=1)
    print(f"  {len(items)} items -> {path}")

# Rendered HTML of every page (for design + Elementor content)
pages = json.load(open(os.path.join(OUT, "pages.json")))
posts = json.load(open(os.path.join(OUT, "posts.json")))
targets = [(p["slug"], p["link"]) for p in pages]
# a few post permalinks too, to capture the single-post template
for p in posts[:3]:
    targets.append(("post-" + p["slug"], p["link"]))

for slug, link in targets:
    out = os.path.join(HTML_OUT, f"{slug}.html")
    if os.path.exists(out):
        continue
    print(f"HTML {link}")
    try:
        html = fetch(link)
        with open(out, "wb") as f:
            f.write(html)
    except Exception as e:
        print(f"  !! {link}: {e}")
    time.sleep(0.3)

print("Done.")
