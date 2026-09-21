#!/usr/bin/env python3
"""Move models from the Tanit XR user account into the Tanit XR organisation.

There is an undocumented but working endpoint for this: POST /v3/models/<uid>/transfer with
an org and a project. It keeps the model id, so every link and embed already published stays
valid, and the model keeps its licence, its downloads and its view count. No re-upload.

The call usually answers 504 because the gateway gives up before Sketchfab finishes, while
the transfer itself completes, so this checks the organisation's model list afterwards
instead of trusting the status code.

  SKETCHFAB_TOKEN=... python3 tools/transfer_sketchfab_to_org.py                # dry run
  SKETCHFAB_TOKEN=... python3 tools/transfer_sketchfab_to_org.py --apply
  SKETCHFAB_TOKEN=... python3 tools/transfer_sketchfab_to_org.py --apply --only patrick-arch-1

By default it works through the pieces in ref/made-pieces.json. The token is read from the
environment on purpose; nothing secret lives in this repository.
"""
import argparse, json, os, sys, urllib.error, urllib.parse, urllib.request

ORG = "bfe8b79ccf834cf5b6bc32245c271a66"      # the Tanit XR organisation, sketchfab.com/tanitXR
PROJECT = "e3189892b894413b9aafa16726828dcc"  # its only project, "Tanit XR"

ap = argparse.ArgumentParser()
ap.add_argument("--apply", action="store_true")
ap.add_argument("--only", default="")
ap.add_argument("--org", default=ORG)
ap.add_argument("--project", default=PROJECT)
a = ap.parse_args()

tok = os.environ.get("SKETCHFAB_TOKEN", "").strip()
if not tok:
    sys.exit("set SKETCHFAB_TOKEN in the environment first")
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pieces = json.load(open(os.path.join(HERE, "ref", "made-pieces.json")))["pieces"]


def api(path, data=None, method="GET", ctype=None, timeout=120):
    h = {"Authorization": "Token " + tok}
    if ctype:
        h["Content-Type"] = ctype
    req = urllib.request.Request("https://api.sketchfab.com/v3" + path, data=data, method=method, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read()
        return r.status, (json.loads(body) if body.strip() else {})


def org_models():
    """Every model id currently in the organisation, following the pages."""
    out, path = set(), f"/orgs/{a.org}/models"
    for _ in range(20):
        _, d = api(path)
        out |= {r["uid"] for r in d.get("results", [])}
        nxt = d.get("next")
        if not nxt:
            break
        path = nxt.split("/v3", 1)[1]
    return out


inside = org_models()
todo = []
for p in pieces:
    if not p.get("sketchfab") or (a.only and p["slug"] != a.only):
        continue
    uid = p["sketchfab"].rstrip("/").split("/")[-1]
    todo.append((p["title"], uid, uid in inside))

already = sum(1 for _, _, i in todo if i)
print(f"{len(todo)} piece(s); {already} already in the organisation, {len(todo) - already} to move.")
for t, uid, i in todo:
    print(f"  {'in org  ' if i else 'to move '} {t[:44]:<46} {uid}")
if not a.apply:
    print("\nDry run. Re-run with --apply.")
    sys.exit(0)

moved = failed = 0
for title, uid, i in todo:
    if i:
        continue
    body = urllib.parse.urlencode({"org": a.org, "project": a.project}).encode()
    try:
        api(f"/models/{uid}/transfer", data=body, method="POST",
            ctype="application/x-www-form-urlencoded")
    except urllib.error.HTTPError as e:
        if e.code not in (502, 503, 504):     # a gateway timeout usually still succeeded
            print(f"  failed  {title[:40]}: {e.code} {e.read()[:160]}")
            failed += 1
            continue
    except Exception as e:
        print(f"  failed  {title[:40]}: {e}")
        failed += 1
        continue
    if uid in org_models():
        print(f"  moved   {title[:40]}")
        moved += 1
    else:
        print(f"  unclear {title[:40]}: the call returned but it is not in the organisation yet")
        failed += 1

print(f"\n{moved} moved, {failed} not moved. Model ids are unchanged, so nothing on the site needs editing.")
