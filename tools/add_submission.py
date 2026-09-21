#!/usr/bin/env python3
"""Turn one form submission into a pending record, whatever it arrived in.

A submission can reach us as a row in the submissions sheet, as the email FormSubmit sends, or
pasted by hand. This normalises any of those into the queue the site already understands, held
back until someone approves it with tools/people_admin.py.

  # a row or a JSON object, from a file or from a pipe
  python3 tools/add_submission.py row.json
  pbpaste | python3 tools/add_submission.py -

  # or the raw text of the FormSubmit email, which arrives as "Field: value" lines
  python3 tools/add_submission.py --email mail.txt

  --kind profile   which form it was; profile is the default and the only one that publishes
                   a page today. Anything else is filed under submissions/<kind>/ for review.

It never approves anything and never touches the live site.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES = os.path.join(HERE, "profiles")
OTHER = os.path.join(HERE, "submissions")

ap = argparse.ArgumentParser()
ap.add_argument("source", help="a .json file, or - for standard input")
ap.add_argument("--email", action="store_true", help="the source is the text of the notification email")
ap.add_argument("--kind", default="")
a = ap.parse_args()

raw = sys.stdin.read() if a.source == "-" else open(a.source, encoding="utf-8").read()

# FormSubmit's email is a list of "Field: value" lines, sometimes with the label capitalised
FIELD_NAMES = {"name": "name", "your name": "name", "role": "role", "what you do": "role",
               "bio": "bio", "about you": "bio", "short bio": "bio",
               "email": "email", "public email": "public_email", "photo": "photo_url",
               "photo url": "photo_url", "linkedin": "linkedin", "instagram": "instagram",
               "website": "website", "github": "github", "sketchfab": "sketchfab",
               "other link": "other_link", "form": "_form"}

if a.email:
    data = {}
    for line in raw.splitlines():
        m = re.match(r"\s*([A-Za-z][A-Za-z ._-]{1,30})\s*[:\t]\s*(.+?)\s*$", line)
        if not m:
            continue
        key = FIELD_NAMES.get(m.group(1).strip().lower().replace("_", " "))
        if key and not data.get(key):
            data[key] = m.group(2).strip()
else:
    data = json.loads(raw)
    # a sheet row may use the column titles, which are already our field names
    data = {FIELD_NAMES.get(str(k).strip().lower().replace("_", " "), str(k).strip()): v
            for k, v in data.items() if str(v).strip() != ""}

kind = (a.kind or data.get("_form") or "profile").strip().lower()
if not data.get("name"):
    sys.exit("no name found in that submission, so there is nothing to file. "
             "Check the input, or pass --email if it is the notification email.")

slug = re.sub(r"[^a-z0-9]+", "-", data["name"].lower()).strip("-")

if kind == "profile":
    os.makedirs(PROFILES, exist_ok=True)
    out = os.path.join(PROFILES, slug + ".json")
    if os.path.exists(out):
        sys.exit(f"{os.path.relpath(out, HERE)} already exists; look at it before overwriting.")
    rec = {k: data.get(k, "") for k in ("name", "role", "bio", "photo_url", "public_email",
                                        "linkedin", "instagram", "website", "github",
                                        "sketchfab", "other_link")}
    rec["approved"] = False
    json.dump(rec, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"filed {os.path.relpath(out, HERE)} as waiting.")
    print("Review it with: python3 tools/people_admin.py")
else:
    d = os.path.join(OTHER, kind)
    os.makedirs(d, exist_ok=True)
    out = os.path.join(d, slug + ".json")
    json.dump(data, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"filed {os.path.relpath(out, HERE)} for review ({kind} submissions have no page yet).")
