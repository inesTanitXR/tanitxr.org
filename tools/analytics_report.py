#!/usr/bin/env python3
"""Pull the numbers a grant report asks for from GoatCounter.

Usage:
  GOATCOUNTER_TOKEN=... python3 tools/analytics_report.py --code tanitxr --months 12

The token comes from goatcounter.com > Settings > API, with the "read statistics" and
"export" permissions. It is read from the environment on purpose: nothing secret lives in
this repository. Prints a monthly table (visits, unique visitors) and the Collection's own
events (objects viewed, saved, shared, turned; badges; VR sessions; donate clicks), plus the
objects people save most. Nothing is written anywhere.
"""
import argparse, datetime as dt, json, os, sys, urllib.parse, urllib.request
from collections import Counter

ap = argparse.ArgumentParser()
ap.add_argument("--code", required=True, help="the GoatCounter site code, e.g. tanitxr")
ap.add_argument("--months", type=int, default=12)
ap.add_argument("--json", action="store_true", help="print machine-readable JSON instead")
a = ap.parse_args()
tok = os.environ.get("GOATCOUNTER_TOKEN", "").strip()
if not tok:
    sys.exit("set GOATCOUNTER_TOKEN in the environment first")
base = f"https://{a.code}.goatcounter.com/api/v0/"

def get(path, **q):
    url = base + path + ("?" + urllib.parse.urlencode(q, doseq=True) if q else "")
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + tok,
                                               "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

today = dt.date.today()
start = (today.replace(day=1) - dt.timedelta(days=31 * (a.months - 1))).replace(day=1)
out = {"site": a.code, "from": start.isoformat(), "to": today.isoformat(), "months": [], "events": {}, "top_saved": []}

# 1. month by month: visits and unique visitors for the whole site
m = start
while m <= today:
    nxt = (m.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
    end = min(nxt - dt.timedelta(days=1), today)
    t = get("stats/total", start=m.isoformat(), end=end.isoformat())
    out["months"].append({"month": m.strftime("%Y-%m"), "visits": t.get("total", 0),
                          "unique_visitors": t.get("total_unique", t.get("total_utc", 0))})
    m = nxt

# 2. every path and event over the period, paged
hits, after = [], None
while True:
    page = get("stats/hits", start=start.isoformat(), end=today.isoformat(), limit=100,
               **({"after": after} if after else {}))
    hits += page.get("hits", [])
    if not page.get("more"):
        break
    after = hits[-1]["path_id"] if hits else None
    if after is None:
        break
events = [h for h in hits if h.get("event")]
pages = [h for h in hits if not h.get("event")]
fam = Counter()
saved = Counter()
for h in events:
    name = h["path"].split("/")[0]
    fam[name] += h.get("count", 0)
    if name == "collection_save" and "/" in h["path"]:
        saved[h["path"].split("/", 1)[1]] += h.get("count", 0)
out["events"] = dict(fam)
out["top_saved"] = saved.most_common(15)
walk = [p for p in pages if p["path"].startswith("/walk")]
out["collection_page_visits"] = sum(p.get("count", 0) for p in walk)

if a.json:
    print(json.dumps(out, indent=1)); sys.exit()
print(f"tanitxr.org, {out['from']} to {out['to']}\n")
print(f"{'month':8} {'visits':>8} {'unique':>8}")
for r in out["months"]:
    print(f"{r['month']:8} {r['visits']:>8,} {r['unique_visitors']:>8,}")
print(f"\nThe Collection page: {out['collection_page_visits']:,} visits")
labels = {"collection_view": "objects looked at", "collection_rotate": "objects turned by hand",
          "collection_save": "objects saved", "collection_share": "shares", "badge": "badges earned",
          "xr_entered": "VR sessions", "donate_click": "donate clicks", "scan_demo": "scan demos watched",
          "nura_more": "asked Nura for more", "room_open": "artist rooms opened"}
for k, n in sorted(fam.items(), key=lambda kv: -kv[1]):
    print(f"  {labels.get(k, k):28} {n:>8,}")
if saved:
    print("\nMost saved objects")
    for slug, n in out["top_saved"]:
        print(f"  {n:>5,}  {slug}")
