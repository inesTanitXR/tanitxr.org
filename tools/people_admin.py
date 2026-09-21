#!/usr/bin/env python3
"""Everyone on Our People, in one list, with an approval step.

ref/people.json is the single source for the team and the community contributors. A volunteer
profile submitted through the site arrives as one file in profiles/ (see profiles/README.md);
this moves it into the list once a human approves it. Nothing appears on the site until then.

  python3 tools/people_admin.py                       # who is published, who is waiting
  python3 tools/people_admin.py show rachel-west      # one person's record in full
  python3 tools/people_admin.py approve jane-doe      # publish (from profiles/ or the list)
  python3 tools/people_admin.py hold jane-doe         # take back off the site, keep the record
  python3 tools/people_admin.py edit jane-doe role "3D Generalist"
  python3 tools/people_admin.py group jane-doe core   # core team, or community

After approving, run `python3 build.py` and push. Nothing here touches the live site by itself.
"""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PEOPLE = os.path.join(HERE, "ref", "people.json")
PROFILES = os.path.join(HERE, "profiles")
LINK_KEYS = ("linkedin", "instagram", "website", "github", "sketchfab", "other_link")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def load():
    return json.load(open(PEOPLE, encoding="utf-8"))


def save(doc):
    json.dump(doc, open(PEOPLE, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def pending():
    """Submissions sitting in profiles/ that are not in the list yet."""
    doc = load()
    known = {p["slug"] for p in doc["people"]}
    out = []
    for f in sorted(glob.glob(os.path.join(PROFILES, "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        if not d.get("name"):
            continue
        s = d.get("slug") or slugify(d["name"])
        if s not in known:
            out.append((f, s, d))
    return out


def as_record(d, slug):
    return {
        "name": d["name"].strip(),
        "role": (d.get("role") or "Volunteer").strip(),
        "slug": slug,
        "group": d.get("group") or "community",
        "bio": re.sub(r"\s+", " ", (d.get("bio") or "")).strip(),
        "photo": d.get("photo") or d.get("photo_url") or None,
        "links": [d[k].strip() for k in LINK_KEYS if d.get(k)]
                 + ([f"mailto:{d['public_email'].strip()}"] if d.get("public_email") else []),
        "approved": False,
        "submitted": d.get("submitted") or d.get("date") or "",
    }


args = sys.argv[1:]
cmd = args[0] if args else "list"

if cmd == "list":
    doc = load()
    live = [p for p in doc["people"] if p.get("approved")]
    held = [p for p in doc["people"] if not p.get("approved")]
    core = [p for p in live if p.get("group") == "core"]
    comm = [p for p in live if p.get("group") != "core"]
    print(f"On the site: {len(live)} people ({len(core)} core team, {len(comm)} community)\n")
    for p in core:
        print(f"  core       {p['slug']:<28} {p['role']}")
    for p in comm:
        print(f"  community  {p['slug']:<28} {p['role']}")
    if held:
        print(f"\nIn the list but held back ({len(held)}):")
        for p in held:
            print(f"  held       {p['slug']:<28} {p['role']}")
    pend = pending()
    if pend:
        print(f"\nWaiting for you ({len(pend)} new submission{'s' if len(pend) > 1 else ''}):")
        for f, s, d in pend:
            bio = re.sub(r"\s+", " ", d.get("bio", ""))[:90]
            print(f"\n  {d['name']}  ({s})")
            print(f"    role : {d.get('role') or '(none given)'}")
            print(f"    bio  : {bio}{'…' if len(d.get('bio', '')) > 90 else ''}")
            links = [d[k] for k in LINK_KEYS if d.get(k)]
            print(f"    links: {', '.join(links) if links else '(none)'}")
            print(f"    photo: {d.get('photo') or d.get('photo_url') or '(none)'}")
            print(f"    file : {os.path.relpath(f, HERE)}")
        print("\n  Publish one with: python3 tools/people_admin.py approve <slug>")
    else:
        print("\nNothing waiting.")
    sys.exit(0)

if len(args) < 2:
    sys.exit(__doc__)
target = args[1]
doc = load()
by_slug = {p["slug"]: p for p in doc["people"]}

if cmd == "show":
    p = by_slug.get(target)
    if not p:
        for f, s, d in pending():
            if s == target:
                print(json.dumps(d, indent=1, ensure_ascii=False))
                sys.exit(0)
        sys.exit(f"no one with the slug {target}")
    print(json.dumps(p, indent=1, ensure_ascii=False))

elif cmd == "approve":
    if target in by_slug:
        by_slug[target]["approved"] = True
        save(doc)
        print(f"{by_slug[target]['name']} is approved. Run python3 build.py, then push.")
    else:
        for f, s, d in pending():
            if s == target:
                rec = as_record(d, s)
                rec["approved"] = True
                doc["people"].append(rec)
                save(doc)
                os.makedirs(os.path.join(PROFILES, "done"), exist_ok=True)
                os.rename(f, os.path.join(PROFILES, "done", os.path.basename(f)))
                print(f"{rec['name']} added to ref/people.json and approved.")
                print("Check the record with: python3 tools/people_admin.py show " + s)
                print("Then run python3 build.py and push.")
                break
        else:
            sys.exit(f"no submission or record with the slug {target}")

elif cmd == "hold":
    if target not in by_slug:
        sys.exit(f"no one with the slug {target}")
    by_slug[target]["approved"] = False
    save(doc)
    print(f"{by_slug[target]['name']} is held back. Rebuild to take the page down.")

elif cmd == "group":
    if target not in by_slug or len(args) < 3 or args[2] not in ("core", "community"):
        sys.exit("usage: group <slug> core|community")
    by_slug[target]["group"] = args[2]
    save(doc)
    print(f"{by_slug[target]['name']} is now in {args[2]}.")

elif cmd == "edit":
    if target not in by_slug or len(args) < 4:
        sys.exit("usage: edit <slug> <field> <value>")
    field, value = args[2], args[3]
    if field not in ("name", "role", "bio", "photo"):
        sys.exit("field must be one of: name, role, bio, photo")
    by_slug[target][field] = value
    save(doc)
    print(f"{by_slug[target]['name']}: {field} updated.")

else:
    sys.exit(__doc__)
