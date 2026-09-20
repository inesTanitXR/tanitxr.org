#!/usr/bin/env python3
"""What is still English on the French and Arabic pages.

New copy is written in English, so every time a page changes the other two languages fall
behind. This finds the gap by comparing the built pages: any visible text that is identical
on the English page and its French twin has never been translated.

  python3 tools/translation_status.py                 # a short report per page
  python3 tools/translation_status.py --list          # every untranslated string
  python3 tools/translation_status.py --out new.json  # write them ready for translating

Run it after `python3 build.py`. To close the gap, translate the strings in the JSON file
and merge them with tools/merge_translations.py.

Opportunity titles and descriptions, object descriptions and article bodies are treated as
content, not interface copy, and are left out: they come from outside sources and stay in
their original language on purpose.
"""
import argparse, collections, html, json, os, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("--list", action="store_true")
ap.add_argument("--out", default="")
ap.add_argument("--quiet", action="store_true", help="one line, for other scripts")
a = ap.parse_args()

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(HERE, "docs")

PAGES = ["", "opportunities/", "explore/", "partners/", "volunteer/", "community/", "support/",
         "contact/", "archive/", "news/", "team/", "museum/", "galleries/", "create-profile/",
         "scanning-guide/", "splats-with-phones/", "press/", "unique-mappers/",
         "el-jem-conference/", "immersegt-2026/", "privacy/", "thank-you/", "about/"]


def visible(path):
    h = open(path, encoding="utf-8").read()
    h = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", h, flags=re.S)
    out = set()
    for t in re.findall(r">([^<>]+)<", h):
        s = html.unescape(t).strip()
        if s and re.search(r"[A-Za-z]{3}", s):
            out.add(s)
    for v in re.findall(r'(?:alt|title|placeholder|aria-label)="([^"]{4,})"', h):
        s = html.unescape(v).strip()
        if s and re.search(r"[A-Za-z]{3}", s):
            out.add(s)
    return out


content = set()
for f in ("ref/opportunity_updates.json", "wp-data/opportunity.json", "wp-data/posts.json", "ref/models.json"):
    p = os.path.join(HERE, f)
    if os.path.exists(p):
        for m in re.findall(r'"(?:desc|description|text|content|excerpt|title)"\s*:\s*"((?:[^"\\]|\\.){15,})"',
                            open(p, encoding="utf-8").read()):
            content.add(html.unescape(m.replace('\\"', '"')).strip()[:50])

missing, per_page = collections.Counter(), collections.Counter()
for u in PAGES:
    en = os.path.join(DOCS, u, "index.html")
    fr = os.path.join(DOCS, "fr", u, "index.html")
    if not (os.path.exists(en) and os.path.exists(fr)):
        continue
    for s in visible(en) & visible(fr):
        if s[:50] in content:
            continue
        missing[s] += 1
        per_page[u or "home"] += 1

if a.quiet:
    print(f"{len(missing)} untranslated string(s) across {len(per_page)} page(s)")
    sys.exit(1 if missing else 0)

print(f"{len(missing)} string(s) still English on the French and Arabic pages, "
      f"{sum(len(s) for s in missing)} characters.\n")
if per_page:
    for u, c in per_page.most_common():
        print(f"  {c:>4}  /{u if u != 'home' else ''}")
if a.list:
    print()
    for s in sorted(missing, key=lambda x: (-len(x), x)):
        print("  -", s.replace("\n", " ")[:160])
if a.out:
    json.dump(sorted(missing), open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nwritten to {a.out}. Translate it, then: python3 tools/merge_translations.py {a.out}")
sys.exit(0)
