#!/usr/bin/env python3
"""Swap a newsletter's organiser links for counted tanitxr.org/go/ links.

  python3 tools/go_links.py ref/newsletter-edition-21.md --edition 21          # show what would change
  python3 tools/go_links.py ref/newsletter-edition-21.md --edition 21 --write  # rewrite the file

Each link that matches a call on the board becomes https://tanitxr.org/go/<call>/?ref=nl21. A reader
who clicks it lands on the organiser's page as before, and the click is counted per edition and per
item (tools/analytics_report.py, "Newsletter items clicked"). Links that match nothing are listed:
add those calls to the board (ref/opportunity_updates.json), rebuild, then run this again.
Short lines that end with a bare address (call.emare.eu) get a counted link too, matched to the board
call on that site whose name fits the line best. Run it after the build, because it reads the
forwarding pages in docs/go/."""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument("file"); ap.add_argument("--edition", required=True); ap.add_argument("--write", action="store_true")
a = ap.parse_args()


def norm(u):
    u = re.sub(r"^https?://(www\.)?", "", u.strip().lower())
    return u.split("#")[0].rstrip("/")


go = {}
gdir = os.path.join(HERE, "docs", "go")
for slug in sorted(os.listdir(gdir)):
    f = os.path.join(gdir, slug, "index.html")
    if os.path.exists(f):
        m = re.search(r'var U="([^"]+)"', open(f, encoding="utf-8").read())
        if m and slug != "opportunities":
            go.setdefault(norm(m.group(1)), slug)

text = open(a.file, encoding="utf-8").read()
tag = "nl" + re.sub(r"\D", "", a.edition)
done, missing = [], []


def swap(m):
    url = m.group(0)
    if "tanitxr.org" in url:
        return url
    slug = go.get(norm(url))
    if not slug:
        missing.append(url); return url
    new = f"https://tanitxr.org/go/{slug}/?ref={tag}"
    done.append((url, new)); return new


out = re.sub(r"https?://[^\s)>\]\"']+", swap, text)

# Short lines (Tunisia section, Still open) end with a bare address like "call.emare.eu" instead of a
# full link. Count those too: pick the board call on that site whose slug shares the most words with
# the line, and put its counted link in place of the bare address.
bydom = {}
for u, slug in go.items():
    bydom.setdefault(u.split("/")[0], []).append((u, slug))


def words(t):
    return set(re.findall(r"[a-z0-9]{3,}", t.lower()))


def swap_bare(m):
    line, bare = m.group(1), m.group(2)
    dom = norm(bare).split("/")[0]
    near = [c for d, cs in bydom.items() if d == dom or d.endswith("." + dom) or dom.endswith("." + d) for c in cs]
    cands = ("/" in bare and [c for c in near if c[0].startswith(norm(bare))]) or near
    if not cands:
        missing.append(bare); return m.group(0)
    lw = words(line)
    slug = max(cands, key=lambda c: len(lw & set(c[1].split("-"))))[1]
    new = f"https://tanitxr.org/go/{slug}/?ref={tag}"
    done.append((bare, new)); return line + new


out = re.sub(r"(?m)^(- .*?[ .,:;(]\s?)((?!tanitxr\.org)[a-z0-9-]+(?:\.[a-z0-9-]+)*\.[a-z]{2,}(?:/[^\s]*)?)\s*$", swap_bare, out)
for old, new in done:
    print(f"  {new}\n      was {old}")
print(f"\n{len(done)} links counted, {len(missing)} not on the board:")
for u in missing:
    print(f"  {u}")
if a.write and done:
    open(a.file, "w", encoding="utf-8").write(out)
    print(f"\nwritten to {a.file}")
