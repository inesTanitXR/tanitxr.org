#!/usr/bin/env python3
"""Compile the website archive dataset from the Sketchfab ORG inventory.

Pairs each artifact's raw photogrammetry scan (preservation record) with its
optimized VR/game-ready twin, pulls descriptions + thumbnails for public models
from the public Sketchfab API, and merges the old WordPress titles/descriptions
where they match. Output: ref/archive-data.json
"""
import json
import re
import subprocess
import time
import os

HERE = os.path.dirname(os.path.abspath(__file__))
models = json.load(open(f"{HERE}/ref/sketchfab-org.json"))
wp = json.load(open(f"{HERE}/ref/models.json"))


def norm(name):
    n = name.lower()
    n = re.sub(r"\s*[–—-]\s*(copy|opt|otp)\s*$", "", n)
    n = re.sub(r"\s*[–—-]\s*$", "", n)
    n = re.sub(r"[–—-]", " ", n)
    n = re.sub(r"[^a-z0-9]", "", n)  # squash everything
    return n


def clean_title(name):
    t = re.sub(r"\s*[–—-]\s*(copy|opt|otp)\s*$", "", name, flags=re.I)
    t = re.sub(r"\s*[–—-]\s*$", "", t).strip()
    return t


def site_of(path):
    parts = [p.strip() for p in path.split(">")]
    site = parts[1] if len(parts) > 1 else ""
    place = parts[2] if len(parts) > 2 else site
    place = re.sub(r"\s*-\s*(Carthage|Kairouan)$", "", place)
    return site, place


groups = {}
decor = []
for m in models:
    top = m["path"].split(">")[0].strip()
    if "bad upload" in m["name"].lower():
        continue
    if top.startswith("Decorative"):
        if m["visibility"] == "public":
            decor.append(m)
        continue
    kind = "raw" if top.startswith("Photogrammetry") else "opt"
    site, place = site_of(m["path"])
    key = (site, norm(m["name"])[:34])
    g = groups.setdefault(key, {"raw": [], "opt": [], "site": site, "place": place, "names": []})
    g[kind].append(m)
    g["names"].append(m["name"])

# prefix-merge: an opt-only group whose key is a prefix of (or prefixed by) a raw group in the same site
merged = True
while merged:
    merged = False
    keys = list(groups.keys())
    for k in keys:
        if k not in groups:
            continue
        g = groups[k]
        if g["raw"] and g["opt"]:
            continue
        for k2 in keys:
            if k2 == k or k2 not in groups:
                continue
            g2 = groups[k2]
            if k[0] != k2[0]:
                continue
            a, b = k[1], k2[1]
            if not (a.startswith(b[:20]) or b.startswith(a[:20])):
                continue
            if (g["opt"] and not g["raw"] and g2["raw"]) or (g["raw"] and not g["opt"] and g2["opt"]):
                g2["raw"] += g["raw"]; g2["opt"] += g["opt"]; g2["names"] += g["names"]
                del groups[k]; merged = True
                break

wp_by_norm = {norm(w["title"]): w for w in wp}


def newest_public(lst):
    pub = [m for m in lst if m["visibility"] == "public"]
    return sorted(pub, key=lambda m: m["created"], reverse=True)[0] if pub else None


def api(uid):
    for _ in range(2):
        r = subprocess.run(["curl", "-s", "-m", "25",
                            f"https://api.sketchfab.com/v3/models/{uid}"],
                           capture_output=True, text=True)
        try:
            return json.loads(r.stdout)
        except json.JSONDecodeError:
            time.sleep(2)
    return {}


artifacts = []
locked = []
for (site, _), g in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[1]["place"])):
    raw = newest_public(g["raw"])
    opt = newest_public(g["opt"])
    org_opt = next((m for m in sorted(g["opt"], key=lambda x: x["created"], reverse=True)
                    if m["visibility"] == "org"), None)
    if not raw and not opt:
        locked.append({"names": sorted(set(g["names"])), "site": site, "why": "no public version"})
        continue
    primary = raw or opt
    title = clean_title(max(g["names"], key=len))
    wpm = wp_by_norm.get(norm(title)) or wp_by_norm.get(norm(primary["name"]))
    if wpm:
        title = wpm["title"]
    desc = (wpm or {}).get("text", "")
    meta = api(primary["uid"])
    if not desc:
        desc = (meta.get("description") or "").strip()
    thumbs = (meta.get("thumbnails") or {}).get("images", [])
    thumb = ""
    for t in sorted(thumbs, key=lambda x: x.get("width", 0), reverse=True):
        if t.get("width", 0) <= 1100:
            thumb = t.get("url", ""); break
    if not thumb and thumbs:
        thumb = thumbs[-1].get("url", "")
    artifacts.append({
        "title": title,
        "site": site, "place": g["place"],
        "preservation": raw and raw["uid"],
        "gameready": opt and opt["uid"],
        "gameready_locked": (org_opt["name"] if (org_opt and not opt) else None),
        "scanned_by": (raw or {}).get("creator") or "",
        "optimized_by": (opt or {}).get("creator") or "",
        "desc": desc[:2400],
        "thumb": thumb,
        "date": primary["created"],
        "wp_slug": (wpm or {}).get("slug"),
    })
    if org_opt and not opt:
        locked.append({"names": [org_opt["name"]], "site": site, "why": "optimized version is org-only"})
    time.sleep(0.15)

# "Made by our volunteers" — decorative/museum props modeled by the community
volunteer_made = []
seen_decor = set()
for m in sorted(decor, key=lambda x: x["created"], reverse=True):
    key = re.sub(r"\s*[–—-]\s*(copy|opt|otp)\s*$", "", m["name"], flags=re.I).strip().lower()
    if key in seen_decor:
        continue
    seen_decor.add(key)
    meta = api(m["uid"])
    thumbs = (meta.get("thumbnails") or {}).get("images", [])
    thumb = ""
    for t in sorted(thumbs, key=lambda x: x.get("width", 0), reverse=True):
        if t.get("width", 0) <= 1100:
            thumb = t.get("url", ""); break
    if not thumb and thumbs:
        thumb = thumbs[-1].get("url", "")
    volunteer_made.append({
        "title": clean_title(m["name"]),
        "uid": m["uid"],
        "by": m.get("creator") or "",
        "desc": (meta.get("description") or "").strip()[:600],
        "thumb": thumb,
        "date": m["created"],
    })
    time.sleep(0.15)

json.dump({"artifacts": artifacts, "locked": locked, "volunteer_made": volunteer_made},
          open(f"{HERE}/ref/archive-data.json", "w"), indent=1, ensure_ascii=False)
print(f"{len(volunteer_made)} volunteer-made decorative models")
paired = sum(1 for a in artifacts if a["preservation"] and a["gameready"])
print(f"{len(artifacts)} artifacts ({paired} with public game-ready twin), {len(locked)} locked/org-only notes")
for a in artifacts:
    print(f"  [{a['site'][:12]:<12}] {'RAW' if a['preservation'] else '   '} {'OPT' if a['gameready'] else ('LCK' if a['gameready_locked'] else '   ')} {a['title'][:58]}")
