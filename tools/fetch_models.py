#!/usr/bin/env python3
"""Refresh the 3D models used by walk.html.

Pulls each .glb listed in ref/museum-3d.json from the team's Drive folder, compresses it
for the web (meshopt geometry + webp textures, roughly a 90% size cut), and writes the
result into media/models/ where build.py picks it up.

    python3 tools/fetch_models.py           # all stations
    python3 tools/fetch_models.py tanit-stela

Needs node (for npx @gltf-transform/cli) and the Drive files to stay 'anyone with the link'.
"""
import json, os, subprocess, sys, tempfile, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(HERE, "ref", "museum-3d.json")))
OUT = os.path.join(HERE, "media", "models")
DRIVE = "https://drive.usercontent.google.com/download?id={}&export=download&confirm=t"


def fetch(drive_id, dest):
    req = urllib.request.Request(DRIVE.format(drive_id), headers={"User-Agent": "tanitxr-fetch"})
    with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
        f.write(r.read())
    if open(dest, "rb").read(4) != b"glTF":
        raise SystemExit(f"  ✗ {drive_id} did not return a .glb (check that sharing is still "
                         f"'Anyone with the link, Viewer')")


def optimize(src, dest):
    subprocess.run(["npx", "--yes", "@gltf-transform/cli@4", "optimize", src, dest,
                    "--compress", "meshopt", "--texture-compress", "webp",
                    "--texture-size", "2048", "--simplify", "false"],
                   check=True, capture_output=True)


def main():
    only = set(sys.argv[1:])
    os.makedirs(OUT, exist_ok=True)
    for st in CFG["stations"]:
        if only and st["slug"] not in only:
            continue
        print(f"→ {st['slug']}")
        with tempfile.TemporaryDirectory() as td:
            raw = os.path.join(td, "raw.glb")
            fetch(st["drive_id"], raw)
            dest = os.path.join(OUT, st["slug"] + ".glb")
            optimize(raw, dest)
            print(f"  ✓ {os.path.getsize(raw)/1e6:.2f} MB → {os.path.getsize(dest)/1e6:.2f} MB")
    print("\nNow run: python3 build.py")


if __name__ == "__main__":
    main()
