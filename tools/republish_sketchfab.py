#!/usr/bin/env python3
"""Replace the file behind each Sketchfab model, wait for processing, then publish it.

The first upload of the volunteer-made pieces used the same glb files the website uses.
Those are compressed with meshopt, quantized geometry and WebP textures, and Sketchfab's
converter rejects all three, so every model sat as an unprocessed draft that could not be
published. This uploads a plain glb in its place, keeping the same model id, so every link
already written into the site and into ref/made-pieces.json still works.

Build the plain files first:
  python3 tools/convert_unity_pieces.py ~/Documents/GitHub/VRApp --sketchfab /tmp/skfb

Then:
  SKETCHFAB_TOKEN=... python3 tools/republish_sketchfab.py /tmp/skfb            # dry run
  SKETCHFAB_TOKEN=... python3 tools/republish_sketchfab.py /tmp/skfb --apply
  SKETCHFAB_TOKEN=... python3 tools/republish_sketchfab.py /tmp/skfb --apply --only patrick-arch-1

The token is read from the environment on purpose; nothing secret lives in this repository.
"""
import argparse, json, mimetypes, os, sys, time, urllib.error, urllib.parse, urllib.request, uuid

ap = argparse.ArgumentParser()
ap.add_argument("folder", help="folder of plain .glb files named <slug>.glb")
ap.add_argument("--apply", action="store_true")
ap.add_argument("--only", default="", help="one slug, for a careful first run")
ap.add_argument("--wait", type=int, default=600, help="seconds to wait for processing")
a = ap.parse_args()

tok = os.environ.get("SKETCHFAB_TOKEN", "").strip()
if not tok:
    sys.exit("set SKETCHFAB_TOKEN in the environment first")
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, "ref", "made-pieces.json")
data = json.load(open(SRC))
AUTH = {"Authorization": "Token " + tok}


def api(path, data=None, method="GET", ctype=None):
    h = dict(AUTH)
    if ctype:
        h["Content-Type"] = ctype
    req = urllib.request.Request("https://api.sketchfab.com/v3" + path, data=data, method=method, headers=h)
    with urllib.request.urlopen(req, timeout=600) as r:
        body = r.read()
        return r.status, (json.loads(body) if body.strip() else {})


def multipart(fpath):
    b = uuid.uuid4().hex.encode()
    fn = os.path.basename(fpath)
    body = (b"--" + b + f'\r\nContent-Disposition: form-data; name="modelFile"; filename="{fn}"\r\n'
            f"Content-Type: {mimetypes.guess_type(fn)[0] or 'application/octet-stream'}\r\n\r\n".encode())
    body += open(fpath, "rb").read() + b"\r\n--" + b + b"--\r\n"
    return body, "multipart/form-data; boundary=" + b.decode()


todo = []
for p in data["pieces"]:
    if not p.get("sketchfab"):
        continue
    if a.only and p["slug"] != a.only:
        continue
    f = os.path.join(a.folder, p["slug"] + ".glb")
    if not os.path.exists(f):
        print(f"  no file for {p['slug']}, skipping")
        continue
    todo.append((p, p["sketchfab"].rstrip("/").split("/")[-1], f))

print(f"{len(todo)} model(s) to replace and publish, from {a.folder}")
for p, uid, f in todo:
    print(f"  {os.path.getsize(f)/1e6:6.1f} MB  {p['title'][:44]:<46} {uid}")
if not a.apply:
    print("\nDry run. Re-run with --apply.")
    sys.exit(0)

done = failed = 0
for p, uid, f in todo:
    title = p["title"][:40]
    try:
        body, ctype = multipart(f)
        api(f"/models/{uid}", data=body, method="PUT", ctype=ctype)
    except urllib.error.HTTPError as e:
        print(f"  upload failed  {title}: {e.code} {e.read()[:200]}")
        failed += 1
        continue
    # Wait for Sketchfab to process the new file before it will let us publish. For the first
    # minute the API still reports the OLD file's state, so a FAILED there means nothing.
    state, waited = "PENDING", 0
    while waited < a.wait:
        time.sleep(10)
        waited += 10
        try:
            _, m = api(f"/models/{uid}")
        except urllib.error.HTTPError:
            continue
        state = ((m.get("status") or {}).get("processing") or "PENDING").upper()
        if state == "SUCCEEDED":
            break
        if state == "FAILED" and waited >= 90:
            break
    if state != "SUCCEEDED":
        print(f"  not processed  {title}: {state} after {waited}s")
        failed += 1
        continue
    _, m = api(f"/models/{uid}")
    desc = (m.get("description") or "").replace("https://tanitxr.org/walk/", "https://tanitxr.org/explore/")
    # A JSON PATCH is accepted but refuses with "Cannot publish an unprocessed model";
    # the form encoding is the one that works.
    form = urllib.parse.urlencode({"isPublished": "true", "description": desc}).encode()
    try:
        api(f"/models/{uid}", data=form, method="PATCH", ctype="application/x-www-form-urlencoded")
    except urllib.error.HTTPError as e:
        print(f"  publish failed {title}: {e.code} {e.read()[:200]}")
        failed += 1
        continue
    _, m = api(f"/models/{uid}")
    if not m.get("publishedAt"):
        print(f"  no publish date {title}")
        failed += 1
        continue
    print(f"  published      {title:<42} {m.get('viewerUrl', '')}")
    done += 1

print(f"\n{done} published, {failed} failed.")
