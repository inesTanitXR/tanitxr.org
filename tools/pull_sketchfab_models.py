#!/usr/bin/env python3
"""Pull game-ready .glb files for the archive's artifacts from Sketchfab, then compress them
for the web (meshopt + webp, roughly a 90% size cut) into media/models/.

Needs a Sketchfab API token for the account that owns the models. Pass it in the
environment, never on disk and never in this repo:

    SKETCHFAB_TOKEN=... python3 tools/pull_sketchfab_models.py
    SKETCHFAB_TOKEN=... python3 tools/pull_sketchfab_models.py --limit 12

Prefers each artifact's game-ready (optimized) twin, because volunteers already decimated
those for real-time use. Falls back to the preservation scan only when there is no twin.
Writes media/models/manifest.json describing what landed.
"""
import argparse, json, os, re, subprocess, sys, tempfile, unicodedata, urllib.error, urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "media", "models")
API = "https://api.sketchfab.com/v3"
TOKEN = os.environ.get("SKETCHFAB_TOKEN", "").strip()


def slugify(s):                                   # must match build.py
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def fix_mojibake(s):
    for k, v in {"‚Äì": "-", "‚Äî": "-", "‚Ä¶": "...", "√¥": "o", "‚Ä¢": "-"}.items():
        s = s.replace(k, v)
    return s


def get(url):
    req = urllib.request.Request(url, headers={"Authorization": f"Token {TOKEN}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def download(url, dest):
    with urllib.request.urlopen(urllib.request.Request(url), timeout=600) as r, open(dest, "wb") as f:
        f.write(r.read())


def optimize(src, dest):
    subprocess.run(["npx", "--yes", "@gltf-transform/cli@4", "optimize", src, dest,
                    "--compress", "meshopt", "--texture-compress", "webp",
                    "--texture-size", "2048", "--simplify", "false"],
                   check=True, capture_output=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="stop after N artifacts")
    args = ap.parse_args()
    if not TOKEN:
        sys.exit("Set SKETCHFAB_TOKEN in the environment (get one at sketchfab.com/settings/password).")

    data = json.load(open(os.path.join(HERE, "ref", "archive-data.json")))
    arts = data["artifacts"]
    todo = []
    # models volunteers built by hand for the virtual museum (lamps, pottery, plants)
    for vm in data.get("volunteer_made", []):
        if vm.get("uid"):
            todo.append({"slug": slugify(fix_mojibake(vm["title"])), "title": vm["title"],
                         "uid": vm["uid"], "kind": "volunteer-made",
                         "site": "Made by volunteers", "place": "Made by volunteers"})
    for a in arts:
        uid = a.get("gameready") or a.get("preservation")
        if not uid:
            continue
        todo.append({"slug": slugify(fix_mojibake(a["title"]).strip().rstrip(".")),
                     "title": fix_mojibake(a["title"]).strip().rstrip("."),
                     "uid": uid, "kind": "game-ready" if a.get("gameready") else "preservation",
                     "site": a["site"], "place": fix_mojibake(a.get("place", ""))})
    if args.limit:
        todo = todo[:args.limit]

    os.makedirs(OUT, exist_ok=True)
    done, failed = [], []
    for i, m in enumerate(todo, 1):
        dest = os.path.join(OUT, m["slug"] + ".glb")
        if os.path.exists(dest):
            print(f"[{i}/{len(todo)}] {m['slug']}: already here, skipping")
            done.append({**m, "bytes": os.path.getsize(dest)})
            continue
        print(f"[{i}/{len(todo)}] {m['slug']} ({m['kind']})", flush=True)
        try:
            d = get(f"{API}/models/{m['uid']}/download")
            src = d.get("glb") or d.get("gltf")
            if not src or not src.get("url"):
                raise RuntimeError("no glb/gltf in download response")
            with tempfile.TemporaryDirectory() as td:
                raw = os.path.join(td, "raw.glb")
                download(src["url"], raw)
                if open(raw, "rb").read(4) != b"glTF":
                    raise RuntimeError("not a glb (probably a zipped gltf)")
                optimize(raw, dest)
                print(f"    {os.path.getsize(raw)/1e6:.2f} MB -> {os.path.getsize(dest)/1e6:.2f} MB",
                      flush=True)
            done.append({**m, "bytes": os.path.getsize(dest)})
        except Exception as e:
            print(f"    ! {type(e).__name__}: {e}", flush=True)
            failed.append({**m, "error": str(e)[:200]})

    json.dump({"models": done, "failed": failed}, open(os.path.join(OUT, "manifest.json"), "w"),
              indent=1, ensure_ascii=False)
    print(f"\n{len(done)} ready, {len(failed)} failed -> media/models/manifest.json")
    print(f"total {sum(m['bytes'] for m in done)/1e6:.1f} MB")


if __name__ == "__main__":
    main()
