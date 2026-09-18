#!/usr/bin/env python3
"""Upload volunteer-made pieces to the Tanit XR Sketchfab account as private drafts.

Usage:
  SKETCHFAB_TOKEN=... python3 tools/upload_sketchfab.py ref/made-pieces.json [--publish]

Reads the same list the Collection uses, uploads each glb from media/models/ once (a
'sketchfab' field is written back so a second run skips it), and leaves every model as an
unpublished draft unless --publish is given, so the maker can look it over first. The token
is read from the environment on purpose; nothing secret lives in this repository.
"""
import json, mimetypes, os, sys, urllib.request, uuid

tok = os.environ.get("SKETCHFAB_TOKEN", "").strip()
if not tok:
    sys.exit("set SKETCHFAB_TOKEN in the environment first")
src = sys.argv[1] if len(sys.argv) > 1 else "ref/made-pieces.json"
publish = "--publish" in sys.argv
data = json.load(open(src))
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def multipart(fields, fpath):
    b = uuid.uuid4().hex.encode()
    body = b""
    for k, v in fields.items():
        body += b"--" + b + f'\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    fn = os.path.basename(fpath)
    body += (b"--" + b + f'\r\nContent-Disposition: form-data; name="modelFile"; filename="{fn}"\r\n'
             f"Content-Type: {mimetypes.guess_type(fn)[0] or 'application/octet-stream'}\r\n\r\n".encode())
    body += open(fpath, "rb").read() + b"\r\n--" + b + b"--\r\n"
    return body, b"multipart/form-data; boundary=" + b

changed = False
for p in data["pieces"]:
    if p.get("sketchfab"):
        print("already up:", p["slug"]); continue
    f = os.path.join(HERE, "media", "models", p["slug"] + ".glb")
    if not os.path.exists(f):
        print("missing file:", f); continue
    desc = (f'{p["title"]}, modelled by {p["by"]} for the Tanit XR virtual museum of Tunisian heritage. '
            f'{p.get("note", "")}\n\nPart of the volunteer-built collection at https://tanitxr.org/walk/')
    fields = {"name": f'{p["title"]} (Tanit XR museum)', "description": desc,
              "tags": "tanitxr tunisia museum vr architecture volunteer",
              "categories": "architecture", "license": "by-nc-sa",
              "isPublished": "true" if publish else "false", "isInspectable": "true"}
    body, ctype = multipart(fields, f)
    req = urllib.request.Request("https://api.sketchfab.com/v3/models", data=body, method="POST",
                                 headers={"Authorization": "Token " + tok, "Content-Type": ctype.decode()})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            uid = json.load(r)["uid"]
    except urllib.error.HTTPError as e:
        print("failed:", p["slug"], e.code, e.read()[:200]); continue
    p["sketchfab"] = f"https://sketchfab.com/3d-models/{uid}"
    changed = True
    print("uploaded:", p["slug"], "->", p["sketchfab"], "(draft)" if not publish else "")
if changed:
    json.dump(data, open(src, "w"), indent=1, ensure_ascii=False)
    print("wrote", src)
