#!/usr/bin/env python3
"""How much the Collection has actually been used, for the site to say out loud.

  python3 tools/collection_stats.py          # write ref/collection-stats.json
  python3 tools/collection_stats.py --print  # show the numbers, write nothing

GoatCounter's public counter endpoint gives the count for one path, with no token and no
limit on how many paths you ask about. The API's stats/hits would be one request instead of
a hundred and fifty, but it stops at 100 rows with no pagination, so the tail of the
collection would quietly go missing from a total. Slow and exact beats fast and short here.

The numbers are read from the built page, so run it after a build. It is cheap to run
weekly; nothing here needs a secret, so a scheduled run does not need the API token.
"""
import argparse, concurrent.futures as cf, datetime, json, os, re, sys, urllib.error, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument("--print", dest="show", action="store_true")
a = ap.parse_args()

cfg_file = os.path.join(HERE, "docs", "explore", "index.html")
if not os.path.exists(cfg_file):
    sys.exit("docs/explore/index.html is missing, so run build.py first")
html = open(cfg_file, encoding="utf-8").read()
cfg = json.loads(re.search(r"window\.WALK_CFG=(\{.*?\})\s*</script>", html, re.S).group(1))
code = cfg.get("gc")
if not code:
    sys.exit("no GoatCounter code in the page, so there is nothing to count")
slugs = [i["slug"] for i in cfg["items"]]


def count(path):
    """(unique visitors, total hits) for one counted path, or (0, 0)."""
    url = f"https://{code}.goatcounter.com/counter/{path}.json"
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            d = json.load(r)
    except (urllib.error.URLError, ValueError, TimeoutError):
        return 0, 0
    num = lambda v: int(re.sub(r"\D", "", str(v)) or 0)
    return num(d.get("count_unique")), num(d.get("count"))


paths = ([f"collection_view/{s}" for s in slugs]
         + [f"collection_save/{s}" for s in slugs]
         + ["/explore/", "TOTAL"])
with cf.ThreadPoolExecutor(max_workers=8) as pool:
    got = dict(zip(paths, pool.map(count, paths)))

views = {s: got[f"collection_view/{s}"] for s in slugs}
saves = {s: got[f"collection_save/{s}"] for s in slugs}
# Views are the number a funder asks about, so totals are what is recorded and shown.
# Unique visitors are kept alongside them because the two together say something neither
# says alone. Saves are counted but not displayed: a save lives in one browser's storage
# until that browser is cleared, so it measures nothing worth putting on a page.
stats = {
    "_what": "What the Collection has been used for, from the public GoatCounter counters. "
             "Regenerate with tools/collection_stats.py after a build.",
    "as_of": datetime.date.today().isoformat(),
    "objects": len(slugs),
    "object_views": sum(t for _, t in views.values()),       # total views of objects
    "objects_viewed": sum(1 for _, t in views.values() if t),
    "experience_views": got["/explore/"][1],                 # views of the Collection itself
    "people": got["/explore/"][0],                           # distinct visitors to it
    "saved": sum(t for _, t in saves.values()),
    "site_views": got["TOTAL"][1],
}
# the strongest honest figure here: how many objects somebody looks at once they are in.
# A total of 311 is a small number; eight objects per visit is not.
if stats["experience_views"]:
    stats["per_visit"] = round(stats["object_views"] / stats["experience_views"], 1)
order = sorted(views.items(), key=lambda kv: -kv[1][1])
stats["most_viewed"] = [{"slug": s, "views": t} for s, (_, t) in order[:5] if t]

if a.show:
    print(json.dumps(stats, indent=1))
else:
    out = os.path.join(HERE, "ref", "collection-stats.json")
    json.dump(stats, open(out, "w"), indent=1)
    print(f"{stats['objects']} objects · {stats['object_views']} views across "
          f"{stats['objects_viewed']} of them · {stats['experience_views']} views of the "
          f"Collection itself  -> ref/collection-stats.json")
