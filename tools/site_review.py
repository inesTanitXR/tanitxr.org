#!/usr/bin/env python3
"""Weekly "would this embarrass us" sweep of tanitxr.org, as a Markdown checklist for Ines to review by hand.

  python3 tools/site_review.py              # what changed in the last 7 days, plus a full scan of the live pages
  python3 tools/site_review.py --days 14

It never edits anything. It lists candidates; a human decides. The first and most important check is a person's private
life landing in public by accident (health, family, money, legal trouble, visa status, conflicts, "don't tell anyone"),
on the site or in the public repository. Then:
  1. What changed: pages and repository files committed in the window (the repo is public, so ref/ and wp-data/ count too).
  2. Possibly confidential: emails other than the official one, phone numbers other than the official one, anything that
     looks like a key or token, words like confidential, internal, draft, password, salary, and dollar amounts on the
     partners and support pages (Ines: no amounts on the site until the team agrees).
  3. Possibly embarrassing wording: em dashes (banned in our copy), machine-sounding phrases, placeholders such as
     TODO, [CHECK], lorem, TBD, "coming soon", double words, unfinished brackets.
  4. People: pending usernames shown instead of names, and mentions of the scanning guide still being updated.
  5. Orphan pages: live pages nothing links to (old pages that should perhaps be removed).
  6. Broken pieces: images referenced but missing.
"""
import argparse, datetime as dt, html, os, re, subprocess, sys
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("--days", type=int, default=7)
a = ap.parse_args()
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(HERE, "docs")
os.chdir(HERE)

OFFICIAL_EMAILS = {"info@tanitxr.org"}
OFFICIAL_PHONES = {"14075627793"}
AI_PHRASES = ["delve", "tapestry", "testament to", "in today's", "unlock", "elevate", "seamless", "cutting-edge",
              "game-changer", "leverage", "it's important to note", "in conclusion", "furthermore", "moreover",
              "holistic", "synergy", "revolutioniz", "embark on", "realm", "pivotal", "underscore", "meticulous", "nestled"]
PLACEHOLDERS = [r"\[CHECK\]", r"\bTODO\b", r"\bTBD\b", r"\bFIXME\b", r"lorem ipsum", r"\bXXX\b", r"\[insert", r"\[name\]",
                r"\bplaceholder\b", r"coming soon", r"under construction", r"sample text", r"\[\w+ here\]"]
CONFIDENTIAL = [r"\bconfidential\b", r"\binternal (?:only|use)\b", r"\bdo not (?:share|publish|distribute)\b", r"\bdraft\b",
                r"\bpassword\b", r"\bpasscode\b", r"\bsalary\b", r"\bnot for publication\b",
                r"\bnda\b", r"\boff the record\b", r"\bunpublished\b"]
PENDING_HANDLES = ["danielgo257", "georgealyssa85"]
# a person's private life, the thing that must never land on the site by accident (health, family, money, legal, status)
PRIVATE_LIFE = [r"\b(?:sick|ill(?:ness)?|hospital(?:ized)?|surgery|diagnos\w*|cancer|therapy|depress\w*|anxiety|burn(?:ed)? ?out|mental health|disab\w*|medication|pregnan\w*|miscarriage)\b",
                r"\b(?:passed away|funeral|died|death in the family|grie\w+|mourning|condolences)\b",
                r"\b(?:divorce|break ?up|boyfriend|girlfriend|husband|wife|partner's|my kids|my children|custody|wedding)\b",
                r"\b(?:fired|laid off|lost (?:my|her|his|their) job|unemployed|quit(?:ting)? (?:my|her|his) job|resign\w*|salary|paycheck|broke|debt|can't afford|evict\w*|rent is)\b",
                r"\b(?:visa|immigration|green card|asylum|deport\w*|undocumented|residency permit)\b",
                r"\b(?:arrest\w*|lawsuit|sued|police|court date|harass\w*|assault\w*|abuse\w*)\b",
                r"\b(?:accident|crash|injur\w*|emergency room|ER visit)\b",
                r"\b(?:home address|lives at|apartment \d|date of birth|born on|social security|passport number)\b",
                r"\b(?:drunk|hangover|hooked up|rehab|addict\w*)\b",
                r"\b(?:argued|fight with|drama|conflict with|complained about|behind (?:his|her|their) back|toxic|fed up with|annoyed with)\b",
                r"\b(?:don't tell|between us|keep this private|please keep|off the record|not public yet|secret)\b"]
PRIVATE_LIFE_RE = re.compile("|".join(PRIVATE_LIFE), re.I)
# text files in the public repository that carry people's words (Slack, Drive, applications, event plans)
REPO_TEXT_DIRS = ("ref", "wp-data")
KEY_LIKE = re.compile(r"(?<![a-zA-Z0-9/])(?:[a-f0-9]{40,}|sk-[A-Za-z0-9]{16,}|xox[abp]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{30,}|ghp_[A-Za-z0-9]{30,}|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,})")
SKETCHFAB_UID = re.compile(r"sketchfab\.com/(?:models|3d-models)/[^\"' ]*([a-f0-9]{32})")

out = []
def P(s=""): out.append(s)

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

def text_of(path):
    h = open(path, encoding="utf-8", errors="ignore").read()
    h = re.sub(r"<script.*?</script>|<style.*?</style>|<header.*?</header>|<nav.*?</nav>|<footer.*?</footer>|<title.*?</title>", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    return html.unescape(re.sub(r"\s+", " ", h))

def en_pages():
    for root, _, files in os.walk(DOCS):
        rel = os.path.relpath(root, DOCS)
        if rel.split(os.sep)[0] in ("fr", "ar", "assets", "models", "media"):
            continue
        for fn in files:
            if fn.endswith(".html"):
                yield os.path.join(root, fn)

def url_of(path):
    rel = os.path.relpath(path, DOCS).replace(os.sep, "/")
    rel = re.sub(r"index\.html$", "", rel)
    return "/" + rel

def snippet(txt, m, width=70):
    s = max(0, m.start() - width); e = min(len(txt), m.end() + width)
    return ("…" if s else "") + txt[s:e].strip() + ("…" if e < len(txt) else "")

since = (dt.date.today() - dt.timedelta(days=a.days)).isoformat()
P(f"# tanitxr.org review, {dt.date.today().strftime('%d %B %Y')}\n")
P(f"Candidates only. Nothing here was changed; every line needs a human look. Window: since {since}.\n")

# 1. what changed -------------------------------------------------------------------------------
P("## 1. New or changed since last week\n")
commits = sh(f'git log --since="{since}" --pretty=format:"%h %ad %s" --date=short').strip()
P("Commits:" if commits else "No commits in the window.")
for c in commits.splitlines():
    P(f"- {c}")
changed = sh(f'git log --since="{since}" --name-only --pretty=format: | sort -u').split()
pages = sorted({url_of(os.path.join(HERE, f)) for f in changed if f.startswith("docs/") and f.endswith(".html")
                and not f.startswith(("docs/fr/", "docs/ar/"))})
others = sorted(f for f in changed if not f.startswith("docs/") and os.path.exists(f))
if pages:
    P("\nPages changed (English):")
    for u in pages[:80]: P(f"- https://tanitxr.org{u}")
    if len(pages) > 80: P(f"- and {len(pages) - 80} more")
if others:
    P("\nFiles outside the site that changed (the repository is public, so anyone can read these):")
    for f in others[:60]: P(f"- {f}")
P("")

# 2 to 6: scan every English page ---------------------------------------------------------------
found = defaultdict(list)   # section -> lines
all_text = {}
for path in sorted(en_pages()):
    txt = text_of(path); all_text[path] = txt
    u = url_of(path)
    for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.-]+", txt):
        if m.group(0).lower() not in OFFICIAL_EMAILS and not m.group(0).endswith(("example.com", ".png", ".jpg")):
            found["Emails other than info@"].append(f"- {u}: `{m.group(0)}`")
    for m in re.finditer(r"\+?\d[\d\s().-]{8,}\d", txt):
        digits = re.sub(r"\D", "", m.group(0))
        if 10 <= len(digits) <= 13 and digits.lstrip("0") not in OFFICIAL_PHONES and not re.fullmatch(r"20\d{6,}", digits):
            found["Phone numbers other than the official one"].append(f"- {u}: `{m.group(0).strip()}` {snippet(txt, m, 40)}")
    raw = open(path, encoding="utf-8", errors="ignore").read()
    for m in KEY_LIKE.finditer(raw):
        if SKETCHFAB_UID.search(raw[max(0, m.start() - 60):m.end()]) or "assets/img/" in raw[max(0, m.start() - 40):m.start()]:
            continue
        found["Looks like a key or token"].append(f"- {u}: `{m.group(0)[:12]}…`")
    for pat in CONFIDENTIAL:
        for m in re.finditer(pat, txt, re.I):
            found["Words that hint at something not meant to be public"].append(f"- {u}: {snippet(txt, m)}")
    if "/partners/" in u:
        for m in re.finditer(r"\$\s?\d[\d,]*|\d[\d,]*\s?(?:USD|dollars)", txt):
            found["Dollar amounts on the partners page"].append(f"- {u}: {snippet(txt, m, 50)}")
    for m in re.finditer(r"—", txt):
        found["Em dashes (banned in our copy)"].append(f"- {u}: {snippet(txt, m, 45)}")
    low = txt.lower()
    for ph in AI_PHRASES:
        for m in re.finditer(re.escape(ph), low):
            found["Machine-sounding phrases"].append(f"- {u}: {snippet(txt, m, 50)}")
    for pat in PLACEHOLDERS:
        m = re.search(pat, txt, re.I)
        if m: found["Placeholders and unfinished bits"].append(f"- {u}: {snippet(txt, m, 45)}")
    for m in re.finditer(r"\b(\w{3,})\s+\1\b", txt, re.I):
        if m.start() < 250 or m.group(1)[0].isupper(): continue      # breadcrumb and hero repeat the title and place
        found["Doubled words"].append(f"- {u}: {snippet(txt, m, 35)}")
    for m in PRIVATE_LIFE_RE.finditer(txt):
        if "/archive/" in u or "/news/" in u:   # history texts talk about death and war; people pages and community pages are the risk
            if not re.search(r"\b(?:volunteer|team|slack|she|he|they) ", txt[max(0, m.start()-120):m.start()], re.I): continue
        found["Private matters of a person, on the site"].append(f"- {u}: {snippet(txt, m, 60)}")
    for h in PENDING_HANDLES:
        if h in txt:
            found["Usernames shown where a real name is still missing"].append(f"- {u}: {h}")
    for m in re.finditer(r'<img[^>]+src="([^"]+)"[^>]*>', raw):
        src = m.group(1)
        if src.startswith(("http", "data:")) or any(c in src for c in "'+{"): continue
        target = os.path.normpath(os.path.join(os.path.dirname(path), src.split("?")[0])) if not src.startswith("/") else os.path.join(DOCS, src.lstrip("/"))
        if not os.path.exists(target):
            found["Images referenced but missing"].append(f"- {u}: {src}")

if any(f.startswith("docs/scanning-guide") for f in changed):
    found["Scanning guide page changed (Rachel and Bety's updated guide is not to be published yet)"].append("- https://tanitxr.org/scanning-guide/ changed in the window")

# 4b. the public repository: people's private matters in files anyone can read
def repo_text_files():
    for d in REPO_TEXT_DIRS:
        for root, _, files in os.walk(os.path.join(HERE, d)):
            if "node_modules" in root: continue
            for fn in files:
                if fn.endswith((".md", ".json", ".txt", ".csv")) and os.path.getsize(os.path.join(root, fn)) < 3_000_000:
                    yield os.path.join(root, fn)
for path in repo_text_files():
    rel = os.path.relpath(path, HERE)
    try: txt = open(path, encoding="utf-8", errors="ignore").read()
    except Exception: continue
    flat = re.sub(r"\s+", " ", txt)
    hits = list(PRIVATE_LIFE_RE.finditer(flat))
    new = rel in changed
    for m in hits[:6 if new else 3]:
        found["Private matters of a person, in the public repository" + (" (changed this week)" if new else "")].append(f"- {rel}: {snippet(flat, m, 60)}")
    for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.-]+", flat):
        e = m.group(0).lower()
        if e not in OFFICIAL_EMAILS and not e.endswith(("example.com", ".png", ".jpg", ".js", ".py")) and "@tanitxr.org" not in e and "noreply" not in e:
            found["Emails of people in the public repository"].append(f"- {rel}: `{m.group(0)}`")

# 5. orphan pages
linked = set()
for path, _ in all_text.items():
    raw = open(path, encoding="utf-8", errors="ignore").read()
    for m in re.finditer(r'href="([^"#?]+)', raw):
        href = m.group(1)
        if href.startswith("http") and "tanitxr.org" not in href: continue
        href = re.sub(r"^https?://(?:www\.)?tanitxr\.org", "", href)
        if href.startswith("/"):
            linked.add(href if href.endswith("/") or "." in href.split("/")[-1] else href + "/")
        else:
            base = os.path.dirname(url_of(path))
            linked.add(os.path.normpath(os.path.join(base, href)).replace("\\", "/") + ("/" if not href.endswith(".html") and not href.endswith("/") else ""))
def norm(u): return re.sub(r"\.html$", "/", u)
linked_n = {norm(u) for u in linked} | {norm(u.replace("/index", "/")) for u in linked}
for path in all_text:
    u = url_of(path)
    if u in ("/", "/404.html", "/thank-you/", "/coming-soon/") or "/archive/" in u or "/team/" in u or "/news/" in u or "/opportunities/" in u: continue
    raw = open(path, encoding="utf-8", errors="ignore").read()
    if 'http-equiv="refresh"' in raw: continue
    if u not in linked_n and u.rstrip("/") + ".html" not in linked:
        found["Live pages nothing links to (remove, or link them on purpose)"].append(f"- https://tanitxr.org{u}")

order = ["Private matters of a person, on the site", "Private matters of a person, in the public repository (changed this week)",
         "Private matters of a person, in the public repository", "Emails of people in the public repository",
         "Emails other than info@", "Phone numbers other than the official one", "Looks like a key or token",
         "Words that hint at something not meant to be public", "Dollar amounts on partner or support pages",
         "Usernames shown where a real name is still missing", "Scanning guide page changed (Rachel and Bety's updated guide is not to be published yet)",
         "Em dashes (banned in our copy)", "Machine-sounding phrases", "Placeholders and unfinished bits", "Doubled words",
         "Live pages nothing links to (remove, or link them on purpose)", "Images referenced but missing"]
P("## 2. Private matters and confidential things\n")
for k in order[:9]:
    rows = sorted(set(found[k]))
    P(f"### {k} ({len(rows)})"); [P(r) for r in rows[:40]]
    if len(rows) > 40: P(f"- and {len(rows) - 40} more")
    P("")
P("## 3. People and pending items\n")
for k in order[9:11]:
    rows = sorted(set(found[k])); P(f"### {k} ({len(rows)})"); [P(r) for r in rows[:40]]; P("")
P("## 4. Wording that could embarrass us\n")
for k in order[11:15]:
    rows = sorted(set(found[k])); P(f"### {k} ({len(rows)})"); [P(r) for r in rows[:40]]
    if len(rows) > 40: P(f"- and {len(rows) - 40} more")
    P("")
P("## 5. Structure\n")
for k in order[15:]:
    rows = sorted(set(found[k])); P(f"### {k} ({len(rows)})"); [P(r) for r in rows[:40]]; P("")
P("Public repository (anything in it is readable by anyone): https://github.com/inesTanitXR/tanitxr.org")
print("\n".join(out))
