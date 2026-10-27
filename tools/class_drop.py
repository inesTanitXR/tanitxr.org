#!/usr/bin/env python3
"""Class scans onto Explore, minutes after a student exports them from Scaniverse.

  python3 tools/class_drop.py watch              # during class: watch the drop folders, publish each new .glb
  python3 tools/class_drop.py add FILE.glb [--by Maya] [--title "Coffee mug"]   # one file by hand
  python3 tools/class_drop.py list               # what is on the site from the class
  python3 tools/class_drop.py remove-all         # after the day: take every class scan down
  python3 tools/class_drop.py remove SLUG        # one scan

Settings live in ref/class-drop.json: the upload link, the room's name on Explore, and which
folders on this laptop to watch (the Drive folder if Drive for desktop syncs it, ~/Downloads for
AirDrop and email attachments, ~/ClassDrop for anything dragged in by hand).

What happens to each file: a copy is shrunk with gltf-transform (textures to 2048 px, meshopt),
the copy goes to media/models/class-<name>.glb, the scan is added to ref/class-models.json, the
Explore pages are rebuilt alone (python3 build.py --only walk, seconds), and the result is
committed and pushed. GitHub Pages then shows it on tanitxr.org/explore within a minute or two.
The original file is never touched. A file that fails is logged and skipped, the next one still
goes through. With --no-push nothing leaves the laptop, which is right for the local preview.

The file name carries the credit: Maya_CoffeeMug.glb becomes "Coffee Mug", scanned by Maya.
"""
import argparse, datetime as dt, json, os, re, shutil, socket, subprocess, sys, time

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG_PATH = os.path.join(HERE, "ref", "class-drop.json")
MODELS_PATH = os.path.join(HERE, "ref", "class-models.json")
STATE_PATH = os.path.join(HERE, "ref", "class-drop-state.json")   # which files were seen; gitignored
MODELS_DIR = os.path.join(HERE, "media", "models")
PREFIX = "class-"


def log(msg):
    print(f"[{dt.datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def load(path, default):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def save(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


CFG = load(CFG_PATH, {})


def models():
    m = load(MODELS_PATH, {})
    m.setdefault("label", CFG.get("label", "Class scans"))
    m.setdefault("sub", CFG.get("sub", "Scanned by students"))
    m.setdefault("where", CFG.get("where", ""))
    m.setdefault("place", CFG.get("place", "Scanned in class"))
    m.setdefault("items", [])
    return m


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "scan"


def pretty(s):
    """CoffeeMug, coffee_mug, coffee-mug -> Coffee Mug."""
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s)
    s = re.sub(r"[_\-\.]+", " ", s).strip()
    return " ".join(w[:1].upper() + w[1:] for w in s.split())


def parse_name(path):
    """Maya_CoffeeMug.glb -> ("Maya", "Coffee Mug"). No underscore: no name, the whole thing is the title."""
    base = os.path.splitext(os.path.basename(path))[0]
    base = re.sub(r"(\.glb)+$", "", base, flags=re.I)  # Maya_Mug.glb.glb, when the phone adds its own extension
    base = re.sub(r"\s*\(\d+\)$", "", base)          # "Maya_Mug (2).glb" from a second download
    if "_" in base:
        by, title = base.split("_", 1)
        return pretty(by).split(" ")[0] if by.strip() else "", pretty(title)
    m = re.match(r"Scaniverse \d{4}-\d\d-\d\d (\d\d)(\d\d)\d\d$", base)   # an export nobody renamed
    if m:
        return "", f"Class scan, {int(m.group(1))}:{m.group(2)}"
    return "", pretty(base)


def drive_folder_id():
    m = re.search(r"/folders/([A-Za-z0-9_-]+)", CFG.get("link", ""))
    return m.group(1) if m else None


def drive_list(fid):
    """The upload folder is shared by link, so its public listing needs no sign-in."""
    import html, urllib.request
    url = f"https://drive.google.com/embeddedfolderview?id={fid}"
    page = urllib.request.urlopen(url, timeout=30).read().decode("utf-8", "replace")
    return [(m.group(1), html.unescape(m.group(2)).strip()) for m in
            re.finditer(r'id="entry-([A-Za-z0-9_-]+)".*?flip-entry-title">([^<]*)<', page, re.S)]


def drive_fetch(fid, name, into):
    """Download one file from the shared folder into a watched folder. It lands under a dot name
    first and is renamed when complete, so the watcher never picks up half a file."""
    import urllib.request
    base, ext = os.path.splitext(os.path.basename(name))
    dst = os.path.join(into, base + ext)
    if os.path.exists(dst):
        dst = os.path.join(into, f"{base}-{fid[:5]}{ext}")
    part = os.path.join(into, "." + os.path.basename(dst) + ".part")
    url = f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t"
    with urllib.request.urlopen(url, timeout=300) as r, open(part, "wb") as f:
        shutil.copyfileobj(r, f)
    with open(part, "rb") as f:
        if f.read(4) != b"glTF":
            os.remove(part)
            raise RuntimeError("Drive did not hand back a .glb (is the folder still shared by link?)")
    os.rename(part, dst)
    return dst


BLENDER = "/Applications/Blender.app/Contents/MacOS/Blender"


def gt(src, dst, size, err=0.0001, ratio=0):
    cmd = ["npx", "--yes", "@gltf-transform/cli@4", "optimize", src, dst,
           "--compress", "meshopt", "--texture-compress", "webp", "--texture-size", str(size),
           "--simplify-error", str(err), "--simplify-ratio", str(ratio)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    if r.returncode != 0 or not os.path.exists(dst):
        raise RuntimeError("gltf-transform failed: " + (r.stderr or r.stdout)[-400:])
    return os.path.getsize(dst)


def shrink(src, dst):
    """Textures first: gltf-transform optimize with webp at 2048 px, then 1024, then 512, which is
    what a Scaniverse export usually needs (its weight is an 8k jpg). If the file is still over
    the budget in ref/class-drop.json the mesh itself is the weight, so Blender decimates it
    (meshopt's simplifier stops at texture seams on scans; Decimate does not), then the texture
    pass runs again on the lighter mesh."""
    max_bytes = int(float(CFG.get("max_mb", 7.5)) * 1_000_000)
    n = 0
    for size in (2048, 1024, 512):
        n = gt(src, dst, size)
        log(f"    {n/1e6:.1f} MB with textures at {size} px")
        if n <= max_bytes:
            return n
    if os.path.exists(BLENDER):
        tmp, plain = dst + ".dec.glb", dst + ".plain.glb"
        # Blender cannot read a meshopt or Draco file (a re-shared one from Sketchfab), so hand it
        # a plain copy; a fresh Scaniverse export is already plain and passes through unchanged
        import glob
        nm = next((os.path.dirname(os.path.dirname(d)) for d in
                   glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/@gltf-transform/cli"))), None)
        if nm:
            subprocess.run(["node", os.path.join(HERE, "tools", "class_plain.cjs"), nm, src, plain],
                           capture_output=True, text=True, timeout=900)
        bsrc = plain if os.path.exists(plain) else src
        for ratio in (0.3, 0.1, 0.03):
            log(f"    decimating the mesh to {ratio:.0%} in Blender")
            r = subprocess.run([BLENDER, "-b", "--python", os.path.join(HERE, "tools", "class_decimate.py"), "--",
                                bsrc, tmp, str(ratio)], capture_output=True, text=True, timeout=1800)
            if r.returncode != 0 or not os.path.exists(tmp):
                log("    Blender failed: " + (r.stderr or r.stdout)[-300:].strip()); break
            for size in (2048, 1024):
                n = gt(tmp, dst, size)
                log(f"    {n/1e6:.1f} MB decimated, textures at {size} px")
                if n <= max_bytes:
                    for t in (tmp, plain):
                        if os.path.exists(t):
                            os.remove(t)
                    return n
        for t in (tmp, plain):
            if os.path.exists(t):
                os.remove(t)
    if os.path.exists(dst):
        os.remove(dst)
    raise RuntimeError(f"still {n/1e6:.1f} MB after shrinking, over the {max_bytes/1e6:.0f} MB page budget")


def publish(push=True, what="class scans"):
    r = subprocess.run([sys.executable, os.path.join(HERE, "build.py"), "--only", "walk"],
                       capture_output=True, text=True, cwd=HERE, timeout=900)
    if r.returncode != 0:
        raise RuntimeError("build failed: " + (r.stderr or r.stdout)[-600:])
    if not push:
        log("  built locally (no push)")
        return
    paths = ["docs/explore", "docs/fr/explore", "docs/ar/explore", "docs/explore.html", "docs/fr/explore.html", "docs/ar/explore.html", "docs/assets/models", "docs/assets/walk.js",
             "docs/assets/walk.fr.js", "docs/assets/walk.ar.js", "ref/class-models.json"]
    subprocess.run(["git", "add"] + paths, cwd=HERE, check=False, capture_output=True)
    c = subprocess.run(["git", "commit", "-q", "-m", what], cwd=HERE, capture_output=True, text=True)
    if c.returncode != 0 and "nothing to commit" in (c.stdout + c.stderr):
        log("  nothing new to publish"); return
    p = subprocess.run(["git", "push", "-q"], cwd=HERE, capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        raise RuntimeError("push failed: " + p.stderr[-300:])
    log("  pushed. On tanitxr.org/explore in a minute or two")


def add(path, by=None, title=None, push=True, publish_now=True):
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        raise RuntimeError("no such file: " + path)
    nb, nt = parse_name(path)
    by, title = (by or nb), (title or nt)
    slug = PREFIX + slugify((by + "-" if by else "") + title)
    m = models()
    n = 2
    base = slug
    while any(i["slug"] == slug for i in m["items"]):
        slug = f"{base}-{n}"; n += 1
    os.makedirs(MODELS_DIR, exist_ok=True)
    dst = os.path.join(MODELS_DIR, slug + ".glb")
    log(f"+ {os.path.basename(path)} -> {title}" + (f", scanned by {by}" if by else "") + f" ({os.path.getsize(path)/1e6:.1f} MB)")
    size = shrink(path, dst)
    m["items"].append({"slug": slug, "title": title, "by": by, "date": dt.datetime.now().isoformat(timespec="minutes"),
                       "source": os.path.basename(path), "bytes": size})
    save(MODELS_PATH, m)
    if publish_now:
        publish(push, f"class: add {title}")
    return slug


def remove(slugs, push=True):
    m = models()
    keep = [i for i in m["items"] if i["slug"] not in slugs]
    gone = [i for i in m["items"] if i["slug"] in slugs]
    if not gone:
        log("nothing to remove"); return
    m["items"] = keep
    save(MODELS_PATH, m)
    for i in gone:
        f = os.path.join(MODELS_DIR, i["slug"] + ".glb")
        if os.path.exists(f):
            os.remove(f)
        log(f"- {i['title']}" + (f" ({i['by']})" if i.get("by") else ""))
    if not keep and os.path.exists(MODELS_PATH):
        os.remove(MODELS_PATH)
    publish(push, "class: remove " + (", ".join(i["title"] for i in gone) if len(gone) < 4 else f"{len(gone)} scans"))


def wait_until_still(path, seconds=4):
    """A file still being copied in (Drive, AirDrop) grows; wait until it has stopped."""
    last = -1
    for _ in range(60):
        n = os.path.getsize(path)
        if n == last:
            return True
        last = n
        time.sleep(seconds)
    return False


def watch(push=True, every=20):
    folders = [os.path.expanduser(f) for f in CFG.get("folders", ["~/ClassDrop"])]
    for f in folders:
        os.makedirs(f, exist_ok=True)
    state = load(STATE_PATH, {"done": {}})
    ip = local_ip()
    log("watching " + ", ".join(folders))
    log(f"preview on this network: http://{ip}:8737/explore/   (python3 -m http.server 8737 --directory docs --bind 0.0.0.0)")
    log("Ctrl-C to stop. Files already here are left alone; only new ones go up.")
    # anything already in the folders at start is not from this class, except what arrived while a
    # previous run was stopped (a restart mid-class must not swallow a scan)
    since = state.get("last_loop", 0)
    for f in folders:
        for fn in os.listdir(f):
            p = os.path.join(f, fn)
            if fn.lower().endswith(".glb") and os.path.getmtime(p) < since - 60 or (fn.lower().endswith(".glb") and not since):
                state["done"].setdefault(p, "present at start")
    fid, drive_into = drive_folder_id(), folders[0]
    if fid and "drive" not in state:          # first run only; after that every unseen Drive file is new
        try:
            for i, n in drive_list(fid):        # already in the Drive folder: not from this class
                state.setdefault("drive", {}).setdefault(i, "present at start")
            log("also checking the Drive upload folder (" + str(len(state.get("drive", {}))) + " files already there, left alone)")
        except Exception as e:
            log(f"  !! could not read the Drive folder: {e}")
    save(STATE_PATH, state)
    while True:
        if fid:
            try:
                for i, n in drive_list(fid):
                    if i in state.setdefault("drive", {}) or not n.lower().endswith(".glb"):
                        continue
                    log(f"  new on Drive: {n}")
                    state["drive"][i] = drive_fetch(i, n, drive_into)
                    save(STATE_PATH, state)
            except Exception as e:
                log(f"  !! Drive check: {e}")
        for f in folders:
            try:
                names = sorted(os.listdir(f), key=lambda n: os.path.getmtime(os.path.join(f, n)))
            except OSError:
                continue
            for fn in names:
                p = os.path.join(f, fn)
                if not fn.lower().endswith(".glb") or fn.startswith(".") or p in state["done"]:
                    continue
                if not wait_until_still(p):
                    log(f"  {fn} keeps changing, will look again"); continue
                h = file_hash(p)      # the same scan via Drive and Downloads (or AirDrop) goes up once
                if h in state.setdefault("hashes", {}):
                    log(f"  {fn} is the same file as {state['hashes'][h]}, skipped")
                    state["done"][p] = "duplicate of " + state["hashes"][h]
                    save(STATE_PATH, state); continue
                try:
                    slug = add(p, push=push)
                    state["done"][p] = slug
                    state["hashes"][h] = slug
                except Exception as e:
                    log(f"  !! {fn}: {e}")
                    state["done"][p] = "failed: " + str(e)[:120]
                save(STATE_PATH, state)
        state["last_loop"] = time.time()
        save(STATE_PATH, state)
        time.sleep(every)


def file_hash(path):
    import hashlib
    d = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            d.update(chunk)
    return d.hexdigest()


def local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]; s.close()
        return ip
    except OSError:
        return "localhost"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("watch"); w.add_argument("--no-push", action="store_true"); w.add_argument("--every", type=int, default=20)
    a = sub.add_parser("add"); a.add_argument("file"); a.add_argument("--by"); a.add_argument("--title"); a.add_argument("--no-push", action="store_true")
    sub.add_parser("list")
    r = sub.add_parser("remove"); r.add_argument("slug"); r.add_argument("--no-push", action="store_true")
    ra = sub.add_parser("remove-all"); ra.add_argument("--no-push", action="store_true")
    x = ap.parse_args()
    if x.cmd == "watch":
        watch(push=not x.no_push, every=x.every)
    elif x.cmd == "add":
        add(x.file, x.by, x.title, push=not x.no_push)
    elif x.cmd == "list":
        m = models()
        if not m["items"]:
            print("no class scans on the site"); return
        for i in m["items"]:
            print(f"{i['date'][:16]}  {i['title']:<32} {i.get('by') or '':<12} {i['slug']}  ({i.get('bytes', 0)/1e6:.1f} MB)")
    elif x.cmd == "remove":
        remove([x.slug], push=not x.no_push)
    elif x.cmd == "remove-all":
        m = models()
        if not m["items"]:
            print("nothing to remove"); return
        print(f"This takes {len(m['items'])} class scan(s) off the site and pushes. Type yes to go on: ", end="", flush=True)
        if sys.stdin.readline().strip().lower() != "yes":
            print("left as they are"); return
        remove([i["slug"] for i in m["items"]], push=not x.no_push)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nstopped")
