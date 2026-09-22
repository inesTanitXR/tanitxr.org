#!/usr/bin/env python3
"""Everything Nura can say, and where each button goes.

  python3 tools/nura_lines.py            # English
  python3 tools/nura_lines.py --lang fr  # French, or ar
  python3 tools/nura_lines.py --all      # all three

Which page shows which set is decided by nura_kind() in build.py. "{next}" is filled in by
the page itself: the article after this article, another object from the same dig, or the
models a volunteer scanned. A line that needs one is left out on a page that has none.
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
os.environ.setdefault("TANITXR_IMPORT_ONLY", "1")

src = open(os.path.join(HERE, "build.py"), encoding="utf-8").read()
start = src.index("NURA_LINES = {")
end = src.index("\ndef nura_kind(")
ns = {}
exec(src[start:end], ns)
LINES = ns["NURA_LINES"]

WHERE = {
    "home": "the home page",
    "archive": "the archive list and the galleries",
    "object": "one object's page",
    "news": "the news and stories page",
    "article": "a story",
    "people": "Our People",
    "person": "one volunteer's profile",
    "museum": "the virtual museum",
    "opportunities": "the opportunities board (most people arrive here from LinkedIn)",
    "join": "volunteer, create a profile, the scanning guide",
    "support": "the donate page",
    "other": "any other page",
    "praise": "anywhere, on the third page of a visit",
    "ask": "anywhere except the donate page and the forms, on the fifth page, once a month",
}

ap = argparse.ArgumentParser()
ap.add_argument("--lang", default="en")
ap.add_argument("--all", action="store_true")
a = ap.parse_args()

for lang in (["en", "fr", "ar"] if a.all else [a.lang]):
    L = LINES[lang]
    print(f"\n{'=' * 72}\n{lang.upper()}\n{'=' * 72}")
    for kind, where in WHERE.items():
        rows = L.get(kind)
        if not rows:
            continue
        print(f"\n{kind.upper()}  ({where})")
        for t, label, href in rows:
            print(f"  • {t}")
            if label:
                print(f"      [{label}] → {href}")
            elif href == "{next}":
                print(f"      [the page's own button] → {href}")
    print(f"\n  close button: {L['hush']}\n  her label: {L['tab']}")
