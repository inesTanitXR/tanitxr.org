#!/usr/bin/env python3
"""The numbers behind tanitxr.org, from GoatCounter, as a detailed Markdown report.

Usage:
  python3 tools/analytics_report.py                 # last 7 days against the 7 before, to stdout
  python3 tools/analytics_report.py --days 30       # any window
  python3 tools/analytics_report.py --months 12     # month by month, for a grant application
  python3 tools/analytics_report.py --grant         # lifetime totals since launch, plus Sketchfab views
  python3 tools/analytics_report.py --out ~/Documents/TanitXR-reports/   # also write a dated .md file

What is measured and why each number matters: ref/metrics-for-grants.md

The API token comes from the GOATCOUNTER_TOKEN environment variable, or from the file
~/.config/tanitxr/goatcounter.token (outside the repository on purpose). Create one at
https://tanitxr.goatcounter.com/user/api with "Read statistics" ticked. Nothing here writes to
GoatCounter or anywhere else except the optional report file. --grant also reads public model
statistics from the Sketchfab API (no token needed).
"""
import argparse, datetime as dt, json, os, re, sys, urllib.parse, urllib.request
from collections import Counter, defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("--code", default="tanitxr")
ap.add_argument("--days", type=int, default=7)
ap.add_argument("--months", type=int, default=0, help="month-by-month table instead of a daily window")
ap.add_argument("--grant", action="store_true", help="lifetime totals since launch plus Sketchfab views")
ap.add_argument("--since", default="2026-09-01", help="launch date for --grant")
ap.add_argument("--out", default="", help="folder to write the dated Markdown file into")
ap.add_argument("--json", action="store_true")
a = ap.parse_args()

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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


TRUNCATED = [False]


def hits(start, end):
    """GoatCounter caps this endpoint at 100 rows and has no pagination for it, so this is the
    100 busiest paths and events in the window. Totals come from stats/total, which is exact."""
    page = get("stats/hits", start=start.isoformat(), end=end.isoformat(), limit=100, daily="true")
    if page.get("more"):
        TRUNCATED[0] = True
    return page.get("hits", [])


def side(kind, start, end, limit=15):
    try:
        d = get(f"stats/{kind}", start=start.isoformat(), end=end.isoformat(), limit=limit)
        return [(s.get("name") or s.get("id") or "", s.get("count", 0)) for s in d.get("stats", [])]
    except Exception:
        return []


today = dt.date.today()
LABEL = {"collection_view": "Objects looked at", "collection_rotate": "Objects turned by hand",
         "collection_save": "Objects saved", "collection_share": "Shares", "collection_poster": "Share posters made",
         "share_sheet_opened": "Share sheet opened", "share_landing": "Arrived through a shared link",
         "badge_earned": "Badges earned", "nura_more": "Asked Nura for more", "nura_ask": "Nura's asks shown",
         "nura_ask_yes": "Nura's asks accepted", "volunteer_cameo": "Volunteer cameos seen",
         "xr_entered": "VR sessions", "ar_entered": "Passthrough or phone AR sessions", "ar_quicklook": "iPhone Quick Look",
         "xr_pick": "Pieces picked in VR", "xr_step": "Steps in VR",
         "room_opened": "Galleries opened", "room_pick": "Pieces picked in a gallery", "room_complete": "Rooms completed",
         "scan_demo_opened": "Scan demos watched", "map_opened": "Map opened", "map_jump": "Jumps from the map",
         "sound_toggle": "Sound toggled", "track_made": "Switched to volunteer-made", "track_scans": "Switched to scans",
         "tour_start": "Guided visits started", "tour_step": "Guided visit steps", "tour_done": "Guided visits finished",
         "explore_open": "Explore in 3D opened", "visit": "Visits counted (first or returning)",
         "dwell": "Time milestones reached", "depth": "Depth milestones reached",
         "donate_click": "Donate clicks", "newsletter_signup": "Newsletter sign-ups (form sent)",
         "form_submit": "Forms sent", "form-sent": "Forms delivered (thank-you page)"}
# events whose second path segment is worth a table of its own
DIM = {"collection_view": "Object", "collection_save": "Object", "collection_share": "Network", "collection_poster": "Object",
       "share_landing": "Object", "nura_more": "Object", "room_pick": "Object", "xr_pick": "Object", "map_jump": "Object",
       "badge_earned": "Badge", "nura_ask": "Ask", "nura_ask_yes": "Ask", "room_opened": "Maker", "room_complete": "Room",
       "tour_step": "Step", "explore_open": "Device", "visit": "Kind", "dwell": "Stayed at least", "depth": "Looked at",
       "donate_click": "From page", "newsletter_signup": "From page", "form_submit": "From page", "form-sent": "Form",
       "volunteer_cameo": "Volunteer", "xr_entered": "Object", "ar_entered": "Object"}
NAME, UIDS = {}, {}
try:
    html = open(os.path.join(HERE, "docs", "explore", "index.html"), encoding="utf-8").read()
    cfg = json.loads(re.search(r"WALK_CFG=(\{.*?\})</script>", html, re.S).group(1))
    NAME = {i["slug"]: i["title"] for i in cfg["items"]}
except Exception:
    pass


def pretty(kind, key):
    if DIM.get(kind) == "Object":
        return NAME.get(key, key.replace("-", " "))
    return key.replace("-", " ")


def look(pg, path):
    """GoatCounter stores /opportunities, the site links /opportunities/. Accept either."""
    return pg.get(path, pg.get(path.rstrip("/"), pg.get(path.rstrip("/") + "/", 0))) or 0


def summarise(start, end):
    total = get("stats/total", start=start.isoformat(), end=end.isoformat())
    hs = hits(start, end)
    pages = [h for h in hs if not h.get("event")]
    events = [h for h in hs if h.get("event")]
    fam, per = Counter(), defaultdict(Counter)
    for h in events:
        name, _, rest = h["path"].partition("/")
        fam[name] += h.get("count", 0)
        if rest and name in DIM:
            per[name][rest] += h.get("count", 0)
    daily = Counter()
    for p in pages:
        for d in p.get("stats", []):
            daily[d["day"]] += d.get("daily", 0)
    ev = total.get("total_events", 0)
    return {"visits": total.get("total", 0) - ev, "events_total": ev, "unique": total.get("total", 0),
            "pages": sorted(((p["path"], p.get("count", 0)) for p in pages), key=lambda x: -x[1]),
            "events": fam, "per": per, "daily": dict(sorted(daily.items()))}


def sketchfab_totals():
    """Lifetime views, likes and downloads of every model the site embeds, from Sketchfab's public API."""
    uids = set()
    for root, _, files in os.walk(os.path.join(HERE, "docs")):
        for fn in files:
            if fn.endswith(".html"):
                try:
                    uids |= set(re.findall(r"sketchfab\.com/models/([a-f0-9]{32})", open(os.path.join(root, fn), encoding="utf-8").read()))
                except Exception:
                    pass
    rows, tot = [], Counter()
    for u in sorted(uids):
        try:
            with urllib.request.urlopen(f"https://api.sketchfab.com/v3/models/{u}", timeout=30) as r:
                d = json.load(r)
        except Exception:
            continue
        v, l, dl = d.get("viewCount", 0), d.get("likeCount", 0), d.get("downloadCount", 0)
        rows.append((d.get("name", u), v, l, dl))
        tot["views"] += v; tot["likes"] += l; tot["downloads"] += dl; tot["models"] += 1
    rows.sort(key=lambda r: -r[1])
    return tot, rows


lines = []
def P(s=""): lines.append(s)


def event_tables(cur, prev=None, top=10):
    P("\n## What people did in the Collection\n")
    if prev is not None:
        P("| | This period | Before |"); P("|---|---|---|")
        for k in sorted(set(cur["events"]) | set(prev["events"]), key=lambda k: -cur["events"].get(k, 0)):
            P(f"| {LABEL.get(k, k)} | {cur['events'].get(k, 0):,} | {prev['events'].get(k, 0):,} |")
    else:
        P("| | Times |"); P("|---|---|")
        for k, n in cur["events"].most_common():
            P(f"| {LABEL.get(k, k)} | {n:,} |")
    # funnels worth reading as one line
    ev = cur["events"]
    fun = []
    if ev.get("nura_ask"): fun.append(f"Nura's asks: {ev['nura_ask']:,} shown, {ev.get('nura_ask_yes', 0):,} accepted ({ev.get('nura_ask_yes', 0) / ev['nura_ask'] * 100:.0f}%).")
    if ev.get("tour_start"): fun.append(f"Guided visits: {ev['tour_start']:,} started, {ev.get('tour_done', 0):,} finished ({ev.get('tour_done', 0) / ev['tour_start'] * 100:.0f}%).")
    if ev.get("share_sheet_opened"): fun.append(f"Sharing: {ev['share_sheet_opened']:,} opened the share sheet, {ev.get('collection_share', 0):,} shared.")
    if ev.get("explore_open"):
        d = cur["per"].get("dwell", Counter()); dp = cur["per"].get("depth", Counter())
        fun.append(f"Of {ev['explore_open']:,} Explore sessions, {d.get('3-min', 0):,} stayed 3 minutes or more and {dp.get('10-objects', 0):,} looked at 10 objects or more.")
    if fun:
        P(""); [P(f"- {f}") for f in fun]
    for k in ("collection_view", "collection_save", "collection_share", "share_landing", "nura_more", "nura_ask", "nura_ask_yes",
              "badge_earned", "room_opened", "tour_step", "explore_open", "visit", "dwell", "depth",
              "donate_click", "newsletter_signup", "form_submit", "form-sent", "volunteer_cameo"):
        rows = cur["per"].get(k, Counter()).most_common(top if DIM.get(k) == "Object" else 30)
        if rows:
            P(f"\n### {LABEL.get(k, k)}, by {DIM[k].lower()}\n"); P(f"| {DIM[k]} | Times |"); P("|---|---|")
            for key, n in rows: P(f"| {pretty(k, key)} | {n:,} |")


if a.grant:
    start = dt.date.fromisoformat(a.since); end = today
    cur = summarise(start, end)
    P(f"# Tanit XR online, {start.strftime('%d %B %Y')} to {end.strftime('%d %B %Y')}\n")
    P("Website numbers from GoatCounter (no cookies, no personal data). Sketchfab numbers are lifetime, from its public API.\n")
    P("| | Total |"); P("|---|---|")
    P(f"| Page views | {cur['visits']:,} |"); P(f"| Actions recorded | {cur['events_total']:,} |")
    pg = dict(cur["pages"])
    P(f"| Explore in 3D sessions | {cur['events'].get('explore_open', look(pg, '/explore/')):,} |")
    P(f"| Objects looked at | {cur['events'].get('collection_view', 0):,} |")
    P(f"| Objects saved | {cur['events'].get('collection_save', 0):,} |"); P(f"| Shares | {cur['events'].get('collection_share', 0):,} |")
    P(f"| VR, AR and Quick Look sessions | {cur['events'].get('xr_entered', 0) + cur['events'].get('ar_entered', 0) + cur['events'].get('ar_quicklook', 0):,} |")
    P(f"| Newsletter sign-ups from the site | {cur['events'].get('newsletter_signup', 0):,} |"); P(f"| Donate clicks | {cur['events'].get('donate_click', 0):,} |")
    for kind, title in (("locations", "Countries"), ("toprefs", "Where visitors came from"), ("campaigns", "Campaigns (links with ?ref=)")):
        rows = side(kind, start, end, 25)
        if rows:
            P(f"\n## {title}\n"); P("| | Page views and actions |"); P("|---|---|")
            for n, c in rows: P(f"| {n or ('(direct)' if kind == 'toprefs' else '(unknown)')} | {c:,} |")
    event_tables(cur, top=15)
    tot, rows = sketchfab_totals()
    if tot:
        P("\n## Open 3D models on Sketchfab, lifetime\n")
        P("| | Total |"); P("|---|---|")
        P(f"| Models published | {tot['models']:,} |"); P(f"| Views | {tot['views']:,} |"); P(f"| Likes | {tot['likes']:,} |"); P(f"| Downloads | {tot['downloads']:,} |")
        P("\n### Most viewed models\n"); P("| Model | Views | Downloads |"); P("|---|---|---|")
        for n, v, l, dl in rows[:15]: P(f"| {n} | {v:,} | {dl:,} |")
    P("\nNumbers the site cannot count (volunteers, hours, scans, workshops) live in ref/metrics-for-grants.md, section 5.")
elif a.months:
    P(f"# tanitxr.org, month by month\n")
    P("| Month | Page views | Actions | Opportunities page | Explore in 3D | Objects viewed | Saved | Shared | VR or AR | Sign-ups | Donate clicks |")
    P("|---|---|---|---|---|---|---|---|---|---|---|")
    m = (today.replace(day=1) - dt.timedelta(days=31 * (a.months - 1))).replace(day=1)
    while m <= today:
        nxt = (m.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
        end = min(nxt - dt.timedelta(days=1), today)
        s = summarise(m, end)
        pg, ev = dict(s["pages"]), s["events"]
        P(f"| {m.strftime('%B %Y')} | {s['visits']:,} | {s['events_total']:,} | {look(pg, '/opportunities/'):,} | {look(pg, '/explore/'):,} | "
          f"{ev.get('collection_view', 0):,} | {ev.get('collection_save', 0):,} | {ev.get('collection_share', 0):,} | "
          f"{ev.get('xr_entered', 0) + ev.get('ar_entered', 0) + ev.get('ar_quicklook', 0):,} | {ev.get('newsletter_signup', 0):,} | {ev.get('donate_click', 0):,} |")
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
    P(f"| Page views | {cur['visits']:,} | {prev['visits']:,} | {delta(cur['visits'], prev['visits'])} |")
    P(f"| Actions recorded | {cur['events_total']:,} | {prev['events_total']:,} | {delta(cur['events_total'], prev['events_total'])} |")
    pg, ppg = dict(cur["pages"]), dict(prev["pages"])
    for path, label in (("/opportunities/", "Opportunities page"), ("/explore/", "Explore in 3D"), ("/", "Home page"),
                        ("/community/", "Community"), ("/volunteer/", "Volunteer"), ("/support/", "Support"),
                        ("/partners/", "Partner with us"), ("/museum/", "Virtual Museum"), ("/thank-you/", "Thank-you page (forms completed)")):
        P(f"| {label} | {look(pg, path):,} | {look(ppg, path):,} | {delta(look(pg, path), look(ppg, path))} |")
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
            P(f"\n## {title}\n"); P("| | Page views and actions |"); P("|---|---|")
            for n, c in rows: P(f"| {n or ('(direct)' if kind == 'toprefs' else '(unknown)')} | {c:,} |")
    event_tables(cur, prev)
    if TRUNCATED[0]:
        P("\nThe page and event tables show the 100 busiest paths, which is all the API returns at once. "
          "Visits and unique visitors above are exact.")
    P("\nDashboard with everything, live: https://tanitxr.goatcounter.com")

report = "\n".join(lines)
if a.json:
    print(json.dumps({"report": report}))
else:
    print(report)
if a.out:
    os.makedirs(os.path.expanduser(a.out), exist_ok=True)
    tag = "-grant" if a.grant else ("-months" if a.months else "")
    fn = os.path.join(os.path.expanduser(a.out), f"tanitxr-{today.isoformat()}{tag}.md")
    open(fn, "w", encoding="utf-8").write(report + "\n")
    print(f"\nwritten to {fn}", file=sys.stderr)
