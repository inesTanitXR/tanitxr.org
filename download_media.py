#!/usr/bin/env python3
"""Download web-sized renditions of the tanitxr.org media library.

Images: prefer the 'large' (1024px) or '1536x1536' size; fall back to full.
PDFs/SVGs: full file. Skips videopress. Saves to media/<original filename>.
Writes media/index.json mapping attachment id -> local file + metadata.
"""
import json
import os
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(HERE, "media")
os.makedirs(MEDIA_DIR, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 tanitxr-rebuild"}

media = json.load(open(os.path.join(HERE, "wp-data", "media.json")))
index = {}
errors = []

def pick_url(m):
    mime = m["mime_type"]
    if mime.startswith("video"):
        return None
    details = m.get("media_details", {})
    sizes = details.get("sizes", {})
    if mime.startswith("image") and mime != "image/svg+xml":
        for key in ("1536x1536", "large", "2048x2048", "full"):
            if key in sizes:
                return sizes[key]["source_url"]
    return m.get("source_url")

for m in media:
    url = pick_url(m)
    if not url:
        continue
    fname = os.path.basename(url.split("?")[0])
    dest = os.path.join(MEDIA_DIR, fname)
    index[m["id"]] = {
        "file": fname,
        "source_url": m.get("source_url"),
        "picked_url": url,
        "mime": m["mime_type"],
        "alt": m.get("alt_text", ""),
        "title": m.get("title", {}).get("rendered", ""),
    }
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        continue
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
            f.write(r.read())
        print(f"ok  {fname}")
    except Exception as e:
        errors.append((url, str(e)))
        print(f"ERR {url}: {e}")
    time.sleep(0.15)

with open(os.path.join(MEDIA_DIR, "index.json"), "w") as f:
    json.dump(index, f, indent=1)

print(f"\n{len(index)} files indexed, {len(errors)} errors")
for u, e in errors:
    print(" ", u, e)
