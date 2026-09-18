#!/usr/bin/env python3
"""The numbers behind tanitxr.org, from GoatCounter, as a detailed Markdown report.

Usage:
  python3 tools/analytics_report.py                 # last 7 days against the 7 before, to stdout
  python3 tools/analytics_report.py --days 30       # any window
  python3 tools/analytics_report.py --months 12     # month by month, for a grant application
  python3 tools/analytics_report.py --out ~/Documents/TanitXR-reports/   # also write a dated .md file

The API token comes from the GOATCOUNTER_TOKEN environment variable, or from the file
~/.config/tanitxr/goatcounter.token (outside the repository on purpose). Create one at
https://tanitxr.goatcounter.com/user/api with "Read statistics" ticked. Nothing here writes to
GoatCounter or anywhere else except the optional report file.
"""
import argparse, datetime as dt, json, os, sys, urllib.parse, urllib.request
from collections import Counter, defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("--code", default="tanitxr")
ap.add_argument("--days", type=int, default=7)
ap.add_argument("--months", type=int, default=0, help="month-by-month table instead of a daily window")
ap.add_argument("--out", default="", help="folder to write the dated Markdown file into")
ap.add_argument("--json", action="store_true")
a = ap.parse_args()

tok = os.environ.get("GOATCOUNTER_TOKEN", "").strip()
if not tok:
    p = os.path.expanduser("~/.config/tanitxr/goatcounter.token")
    if os.path.exists(p):
        tok = open(p).read().strip()
if not tok:
    sys.exit("No API token. Set GOATCOUNTER_TOKEN or put the token in ~/.config/tanitxr/goatcounter.token")
base = f"https://{a.code}.goatcounter.com/api/v0/"

def get(path, **q):
    url = base + path + ("?" + urllib.parse.urlencode(q, doseq=True) if q else "")
    req = urllib.request.Request(url, headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def hits(start, end):
    out, after = [], None
    while True:
        page = get("stats/hits", start=start.isoformat(), end=end.isoformat(), limit=100, daily="true",
                   **({"after": after} if after else {}))
        out += page.get("hits", [])
        if not page.get("more") or not out:
            break
        after = out[-1]["path_id"]
    return out

def side(kind, start, end, limit=15):
    try:
        d = get(f"stats/{kind}", start=start.isoformat(), end=end.isoformat(), limit=limit)
        return [(s.get("name") or s.get("id") or "?", s.get("count", 0)) for s in d.get("stats", [])]
    except Exception:
        return []

today = dt.date.today()
LABEL = {"collection_view": "Objects looked at", "collection_rotate": "Objects turned by hand",
         "collection_save": "Objects saved", "collection_share": "Shares", "badge": "Badges earned",
         "xr_entered": "VR sessions", "ar_entered": "Passthrough or phone AR sessions", "ar_quicklook": "iPhone Quick Look",
         "donate_click": "Donate clicks", "scan_demo": "Scan demos watched", "nura_more": "Asked Nura for more",
         "room_opened": "Galleries opened", "room_pick": "Pieces picked in a gallery", "share_sheet_opened": "Share sheet opened",
         "map_jump": "Jumps from the map", "sound_toggle": "Sound toggled", "xr_pick": "Pieces picked in VR"}
NAME = {}
try:
    import re
    html = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "explore", "index.html"), encoding="utf-8").read()
    cfg = json.loads(re.search(r"WALK_CFG=(\{.*?\})</script>", html, re.S).group(1))
    NAME = {i["slug"]: i["title"] for i in cfg["items"]}
except Exception:
    pass

def summarise(start, end):
    total = get("stats/total", start=start.isoformat(), end=end.isoformat())
    hs = hits(start, end)
    pages = [h for h in hs if not h.get("event")]
    events = [h for h in hs if h.get("event")]
    fam, per_obj = Counter(), defaultdict(Counter)
    for h in events:
        name, _, rest = h["path"].partition("/")
        fam[name] += h.get("count", 0)
        if rest and name in ("collection_view", "collection_save", "collection_share", "room_pick", "xr_pick"):
            per_obj[name][rest] += h.get("count", 0)
    daily = Counter()
    for p in pages:
        for d in p.get("stats", []):
            daily[d["day"]] += d.get("daily", 0)
    return {"visits": total.get("total", 0), "unique": total.get("total_unique", total.get("total_utc", 0)),
            "pages": sorted(((p["path"], p.get("count", 0)) for p in pages), key=lambda x: -x[1]),
            "events": fam, "per_obj": per_obj, "daily": dict(sorted(daily.items()))}

lines = []
def P(s=""): lines.append(s)

if a.months:
    P(f"# tanitxr.org, month by month\n")
    P("| Month | Visits | Unique visitors | Opportunities page | Explore in 3D | Objects viewed | Saved | Shared |")
    P("|---|---|---|---|---|---|---|---|")
    m = (today.replace(day=1) - dt.timedelta(days=31 * (a.months - 1))).replace(day=1)
    while m <= today:
        nxt = (m.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
        end = min(nxt - dt.timedelta(days=1), today)
        s = summarise(m, end)
        pg = dict(s["pages"])
        P(f"| {m.strftime('%B %Y')} | {s['visits']:,} | {s['unique']:,} | {pg.get('/opportunities/', 0):,} | {pg.get('/explore/', 0):,} | "
          f"{s['events'].get('collection_view', 0):,} | {s['events'].get('collection_save', 0):,} | {s['events'].get('collection_share', 0):,} |")
        m = nxt
else:
    end = today; start = today - dt.timedelta(days=a.days - 1)
    pstart = start - dt.timedelta(days=a.days); pend = start - dt.timedelta(days=1)
    cur, prev = summarise(start, end), summarise(pstart, pend)
    def delta(x, y):
        if not y: return "new" if x else ""
        ch = (x - y) / y * 100
        return f"{'+' if ch >= 0 else ''}{ch:.0f}%"
    P(f"# tanitxr.org, {start.strftime('%d %b')} to {end.strftime('%d %b %Y')}\n")
    P(f"Compared with the {a.days} days before.\n")
    P("| | This period | Before | Change |")
    P("|---|---|---|---|")
    P(f"| Visits | {cur['visits']:,} | {prev['visits']:,} | {delta(cur['visits'], prev['visits'])} |")
    P(f"| Unique visitors | {cur['unique']:,} | {prev['unique']:,} | {delta(cur['unique'], prev['unique'])} |")
    pg, ppg = dict(cur["pages"]), dict(prev["pages"])
    for path, label in (("/opportunities/", "Opportunities page"), ("/explore/", "Explore in 3D"), ("/", "Home page"),
                        ("/community/", "Community"), ("/volunteer/", "Volunteer"), ("/support/", "Support"), ("/museum/", "Virtual Museum")):
        P(f"| {label} | {pg.get(path, 0):,} | {ppg.get(path, 0):,} | {delta(pg.get(path, 0), ppg.get(path, 0))} |")
    P("\n## Day by day\n")
    P("| Day | Page views |"); P("|---|---|")
    for d, n in cur["daily"].items():
        P(f"| {d} | {n:,} |")
    P("\n## Most visited pages\n")
    P("| Page | Views |"); P("|---|---|")
    for path, n in cur["pages"][:20]:
        P(f"| {path} | {n:,} |")
    for kind, title in (("toprefs", "Where visitors came from"), ("locations", "Countries"), ("campaigns", "Campaigns (links with ?ref=)"),
                        ("browsers", "Browsers"), ("systems", "Devices and systems")):
        rows = side(kind, start, end)
        if rows:
            P(f"\n## {title}\n"); P("| | Visitors |"); P("|---|---|")
            for n, c in rows: P(f"| {n or '(direct)'} | {c:,} |")
    P("\n## What people did in the Collection\n")
    P("| | This period | Before |"); P("|---|---|---|")
    for k in sorted(set(cur["events"]) | set(prev["events"]), key=lambda k: -cur["events"].get(k, 0)):
        P(f"| {LABEL.get(k, k)} | {cur['events'].get(k, 0):,} | {prev['events'].get(k, 0):,} |")
    for k, title in (("collection_view", "Most looked at"), ("collection_save", "Most saved"), ("collection_share", "Most shared")):
        rows = cur["per_obj"].get(k, Counter()).most_common(10)
        if rows:
            P(f"\n### {title}\n"); P("| Object | Times |"); P("|---|---|")
            for slug, n in rows: P(f"| {NAME.get(slug, slug)} | {n:,} |")
    P("\nDashboard with everything, live: https://tanitxr.goatcounter.com")

report = "\n".join(lines)
if a.json:
    print(json.dumps({"report": report}))
else:
    print(report)
if a.out:
    os.makedirs(os.path.expanduser(a.out), exist_ok=True)
    fn = os.path.join(os.path.expanduser(a.out), f"tanitxr-{today.isoformat()}{'-months' if a.months else ''}.md")
    open(fn, "w", encoding="utf-8").write(report + "\n")
    print(f"\nwritten to {fn}", file=sys.stderr)
