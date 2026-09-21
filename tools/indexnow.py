#!/usr/bin/env python3
"""Tell Bing which pages changed, instead of waiting to be crawled.

Bing's index is what several AI assistants search, so a page Bing has not seen is a page an
assistant cannot find. IndexNow is a plain notification: it accepts a list of URLs from anyone
who serves the matching key file at the site root, which build.py writes.

  python3 tools/indexnow.py                 # every page in the sitemap
  python3 tools/indexnow.py --since HEAD~1  # only what changed in the last commit
  python3 tools/indexnow.py --check         # print what would be sent

The key lives in ref/indexnow.json and is public by design. Yandex shares the same protocol,
so one call reaches both. Google does not take IndexNow: it finds changes through the sitemap
and Search Console.
"""
import argparse, json, os, re, subprocess, sys, urllib.error, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://tanitxr.org/"

ap = argparse.ArgumentParser()
ap.add_argument("--since", default="", help="a git ref: send only pages changed since it")
ap.add_argument("--check", action="store_true")
a = ap.parse_args()

cfg = os.path.join(HERE, "ref", "indexnow.json")
if not os.path.exists(cfg):
    sys.exit("ref/indexnow.json is missing, so there is no key to prove the site with")
key = json.load(open(cfg)).get("key", "").strip()
if not key:
    sys.exit("no key in ref/indexnow.json")

sitemap = open(os.path.join(HERE, "docs", "sitemap.xml"), encoding="utf-8").read()
urls = list(dict.fromkeys(re.findall(r"<loc>(https://tanitxr\.org/[^<]*)</loc>", sitemap)))

if a.since:
    changed = subprocess.run(["git", "diff", "--name-only", a.since, "--", "docs"],
                             cwd=HERE, capture_output=True, text=True).stdout.split()
    touched = set()
    for f in changed:
        if not f.endswith(".html"):
            continue
        rel = f[len("docs/"):]
        rel = re.sub(r"index\.html$", "", rel)
        touched.add(SITE + rel)
    urls = [u for u in urls if u in touched] or []
    if not urls:
        print("nothing in the sitemap changed since " + a.since)
        sys.exit(0)

print(f"{len(urls)} page(s) to submit, starting with {urls[0]}")
if a.check:
    sys.exit(0)

body = json.dumps({"host": "tanitxr.org", "key": key,
                   "keyLocation": f"{SITE}{key}.txt",
                   "urlList": urls[:10000]}).encode()
req = urllib.request.Request("https://api.indexnow.org/IndexNow", data=body, method="POST",
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        print(f"Bing accepted the list ({r.status}). It crawls them in its own time, usually days.")
except urllib.error.HTTPError as e:
    detail = e.read()[:300].decode("utf-8", "replace")
    if "SiteVerification" in detail:
        print("Bing has not fetched the key file yet. It is served at "
              f"{SITE}{key}.txt — wait a few minutes and run this again.")
    else:
        print(f"Bing refused the list ({e.code}): {detail}")
    sys.exit(1)
