#!/usr/bin/env python3
"""Merge translated string batches into translations.py.

The batches are JSON files of the shape {"fr": {english: french}, "ar": {english: arabic}}.
Entries are appended to the FR and AR tables under a dated heading. Existing keys win, so
running this twice is harmless and hand edits are never overwritten.

  python3 tools/merge_translations.py out1.json out2.json ...
  python3 tools/merge_translations.py --check out1.json     # report only
"""
import argparse, datetime, html, glob, json, os, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("files", nargs="+")
ap.add_argument("--check", action="store_true")
a = ap.parse_args()

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(HERE, "translations.py")

sys.path.insert(0, HERE)
import translations as T

# the official names of outside opportunities stay in their own language: translating
# "AWE 2026 Startup Pitch Competition" would send someone looking for a call that does not exist
keep_english = set()
for f in ("ref/opportunity_updates.json", "wp-data/opportunity.json"):
    p = os.path.join(HERE, f)
    if os.path.exists(p):
        for m in re.findall(r'"title"\s*:\s*"((?:[^"\\]|\\.)*)"', open(p, encoding="utf-8").read()):
            keep_english.add(html.unescape(m.replace('\\"', '"')).strip())

# the table is applied to raw HTML, so a key has to look the way it looks in the file:
# entities for & and the apostrophe, &nbsp; for a non-breaking space
BLOB = "".join(open(f, encoding="utf-8").read()
               for f in glob.glob(os.path.join(HERE, "docs", "fr", "**", "index.html"), recursive=True))


def as_in_html(k):
    for cand in (k,
                 k.replace("&", "&amp;").replace("'", "&#x27;"),
                 k.replace("\xa0", "&nbsp;"),
                 k.replace("&", "&amp;").replace("'", "&#x27;").replace("\xa0", "&nbsp;")):
        if cand in BLOB:
            return cand
    return None


fr, ar, skipped, dupes, unmatched = {}, {}, 0, 0, 0
for pat in a.files:
    for path in sorted(glob.glob(pat)):
        d = json.load(open(path, encoding="utf-8"))
        for lang, table, existing in (("fr", fr, T.FR), ("ar", ar, T.AR)):
            for k, v in d.get(lang, {}).items():
                if k in keep_english or k.strip() == v.strip():
                    if lang == "fr":
                        skipped += 1
                    continue
                real = as_in_html(k)
                if real is None:
                    if lang == "fr":
                        unmatched += 1
                    continue
                if real in existing or real in table:
                    if lang == "fr":
                        dupes += 1
                    continue
                table[real] = v

print(f"{len(fr)} new French, {len(ar)} new Arabic. Skipped {skipped} (proper names or unchanged), "
      f"{dupes} already present, {unmatched} no longer appear on the pages.")
if a.check:
    sys.exit(0)


def block(pairs):
    out = []
    for k in sorted(pairs, key=lambda x: (-len(x), x)):
        out.append("    %r:\n        %r," % (k, pairs[k]) if len(k) + len(pairs[k]) > 90
                   else "    %r: %r," % (k, pairs[k]))
    return "\n".join(out)


stamp = datetime.date.today().isoformat()
src = open(TR, encoding="utf-8").read()
for table, pairs in (("FR", fr), ("AR", ar)):
    if not pairs:
        continue
    m = re.search(rf"^{table} = {{", src, re.M)
    if not m:
        sys.exit(f"could not find the {table} table")
    # find the closing brace of this table at column 0
    end = src.index("\n}", m.start())
    src = src[:end] + f"\n\n    # ---- added {stamp}: pages that were still English ----\n" + block(pairs) + src[end:]
open(TR, "w", encoding="utf-8").write(src)
print(f"translations.py updated. Rebuild with: python3 build.py")
