#!/usr/bin/env python3
"""Newsletter ⇄ website consistency check.

Every opportunity linked from a newsletter edition must exist on the board
(ref/opportunity_updates.json or wp-data/opportunity.json), and every open
board item published since the last edition must appear in some edition or in
the next-edition draft. Exit code 1 when something is out of sync, so build.py
and the scheduled tasks surface it.

    python3 sync_check.py            # report
    python3 sync_check.py --quiet    # only print problems
"""
import glob
import json
import os
import re
import sys
from datetime import date
from urllib.parse import urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))
QUIET = "--quiet" in sys.argv


def norm(url):
    """Compare by host + path only (ignores utm params, trailing slash, www, http/https)."""
    if not url:
        return ""
    url = url.strip().rstrip("/")
    if not re.match(r"https?://", url):
        url = "https://" + url
    p = urlsplit(url)
    host = p.netloc.lower().removeprefix("www.")
    return host + p.path.rstrip("/").lower()


def host(url):
    return norm(url).split("/")[0]


# ---- website side --------------------------------------------------------
board = {}  # norm(url) -> (title, published, deadline)
upd = json.load(open(os.path.join(HERE, "ref", "opportunity_updates.json")))
for e in upd.get("new", []):
    board[norm(e["url"])] = (e["title"], e.get("published", ""), e.get("deadline_date") or e.get("deadline_type") or "")
for m in upd.get("matches", {}).values() if isinstance(upd.get("matches"), dict) else []:
    if isinstance(m, dict) and m.get("url"):
        board.setdefault(norm(m["url"]), (m.get("title", "?"), "", m.get("deadline_date", "")))
for o in json.load(open(os.path.join(HERE, "wp-data", "opportunity.json"))):
    meta = o.get("meta") if isinstance(o.get("meta"), dict) else {}
    url = meta.get("url") or meta.get("link") or ""
    t = o.get("title", {})
    t = t.get("rendered", t) if isinstance(t, dict) else str(t)
    if url:
        board.setdefault(norm(url), (t, o.get("date", "")[:10], meta.get("deadline", "")))
board_hosts = {host(u) for u in board}

# ---- newsletter side -----------------------------------------------------
editions = sorted(glob.glob(os.path.join(HERE, "ref", "newsletter-edition-*.md"))) + \
    [os.path.join(HERE, "ref", "next-edition-draft.md")]
in_newsletter = {}  # norm(url) -> edition file
link_re = re.compile(r"👉[^\n]*?(https?://[^\s)\]]+)")
for f in editions:
    if not os.path.exists(f):
        continue
    for m in link_re.finditer(open(f, encoding="utf-8").read()):
        in_newsletter.setdefault(norm(m.group(1)), os.path.basename(f))

problems = []

# 1. newsletter → website
for u, f in in_newsletter.items():
    if u in board:
        continue
    if host(u) in board_hosts:  # same organisation, different deep link — treat as present
        continue
    problems.append(f"NOT ON WEBSITE  {u}   (linked in {f})")

# 2. website → newsletter (only items published in the last 45 days and still open)
today = date.today()
for u, (title, published, deadline) in board.items():
    if not published:
        continue
    try:
        age = (today - date.fromisoformat(published[:10])).days
    except ValueError:
        continue
    if age > 45:
        continue
    if deadline and re.match(r"\d{4}-\d{2}-\d{2}", str(deadline)) and date.fromisoformat(deadline) < today:
        continue
    if u in in_newsletter or host(u) in {host(x) for x in in_newsletter}:
        continue
    problems.append(f"NOT IN NEWSLETTER  {title}  ({u}, published {published[:10]}) — add to ref/next-edition-draft.md")

if not QUIET:
    print(f"board items: {len(board)} · newsletter links: {len(in_newsletter)} · editions scanned: "
          f"{sum(1 for f in editions if os.path.exists(f))}")
for p in problems:
    print("  !!", p)
if not problems and not QUIET:
    print("  ✓ newsletter and website are in sync")
sys.exit(1 if problems else 0)
