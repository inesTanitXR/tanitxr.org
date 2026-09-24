#!/usr/bin/env python3
"""Make the fortnightly Instagram carousel from the opportunity board.

  python3 tools/opportunity_cards.py              # the next 6 deadlines
  python3 tools/opportunity_cards.py --count 8
  python3 tools/opportunity_cards.py --days 60    # only deadlines inside 60 days

Writes numbered PNGs at 1080 x 1350 into social/<date>/ and prints a caption to paste.
Upload them in order: Instagram keeps the order of the files you pick.

The design follows the website, because the website is the brand: cream paper, ink text,
one gold rule, Yeseva One for the name of the thing and Roboto for the details. Left
aligned, wide margins, nothing centred, no gradients, no icons, no rounded boxes. A card
should look like a printed index card, not like a template.
"""
import argparse, datetime, html, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1080, 1350

ap = argparse.ArgumentParser()
ap.add_argument("--count", type=int, default=6, help="how many opportunities (default 6)")
ap.add_argument("--days", type=int, default=90, help="only deadlines within this many days")
ap.add_argument("--keep-html", action="store_true")
a = ap.parse_args()

board = os.path.join(HERE, "ref", "board.json")
if not os.path.exists(board):
    sys.exit("ref/board.json is missing. Run python3 build.py first.")
items = json.load(open(board, encoding="utf-8"))["items"]

today = datetime.date.today()
limit = today + datetime.timedelta(days=a.days)


def when(o):
    """The board writes deadlines the way a person does, "April 17, 2026", not as a date."""
    d = (o.get("deadline_date") or "").strip()
    for fmt in ("%Y-%m-%d", "%B %d, %Y", "%d %B %Y", "%B %Y"):
        try:
            return datetime.datetime.strptime(d, fmt).date()
        except ValueError:
            pass
    return None


# soonest first, still open, and far enough away that somebody can actually apply
soon = sorted((o for o in items
               if when(o) and today + datetime.timedelta(days=5) <= when(o) <= limit),
              key=when)[:a.count]
if not soon:
    sys.exit("nothing on the board has a deadline in that window")

MARK = os.path.join(HERE, "media", "cropped-TanitXR-Logo_red_vertical.png")
e = lambda s: html.escape(str(s or ""))


def nice(d):
    return f"{d.day} {d.strftime('%B')}"


def who(o):
    el = [x for x in (o.get("eligibility") or []) if x and x.lower() != "open to all"]
    return ", ".join(el[:3]) or "Open to all"


def where(o):
    bits = [b for b in (o.get("mode"), o.get("country") or o.get("region")) if b]
    return " · ".join(bits)


def trim(s, n):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + "…"


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Yeseva+One&family=Roboto:wght@400;500;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{background:#555}
.card{width:1080px;height:1350px;background:#fdf9f2;color:#111518;position:relative;
  font-family:'Roboto',system-ui,sans-serif;padding:96px 92px;display:flex;flex-direction:column}
.kicker{font-size:26px;letter-spacing:.22em;text-transform:uppercase;color:#8a6200;font-weight:700}
.rule{height:3px;background:#ffcd05;width:132px;margin:34px 0 0}
.name{font-family:'Yeseva One',Georgia,serif;font-weight:400;font-size:82px;line-height:1.08;
  margin-top:40px;letter-spacing:-.005em}
.name.small{font-size:64px}
.name.tiny{font-size:54px}
.blurb{font-size:31px;line-height:1.5;color:#4a4540;margin-top:34px}
.spacer{flex:1}
.facts{border-top:1px solid rgba(17,21,24,.14);padding-top:30px;margin-top:52px;
  display:flex;flex-direction:column;gap:16px}
.fact{display:flex;gap:18px;font-size:29px;line-height:1.3}
.fact b{font-weight:700;min-width:190px;color:#111518}
.fact span{color:#4a4540}
.foot{display:flex;align-items:center;gap:20px;margin-top:40px}
.foot img{width:54px;height:54px;object-fit:contain}
.foot div{font-size:25px;color:#6b635a;line-height:1.3}
.n{position:absolute;top:96px;right:92px;font-size:26px;color:#a49a8e;letter-spacing:.06em}
/* cover */
.cover .big{font-family:'Yeseva One',Georgia,serif;font-size:132px;line-height:1.02;margin-top:44px}
.cover .sub{font-size:34px;line-height:1.45;color:#4a4540;margin-top:36px;max-width:19ch}
.list{margin-top:54px;display:flex;flex-direction:column;gap:22px}
.list div{font-size:30px;color:#111518;display:flex;gap:20px;align-items:baseline}
.list i{font-style:normal;color:#8a6200;font-weight:700;font-size:25px;min-width:104px}
/* end */
.end .big{font-family:'Yeseva One',Georgia,serif;font-size:96px;line-height:1.08;margin-top:44px}
.end .sub{font-size:33px;line-height:1.5;color:#4a4540;margin-top:34px}
.url{font-size:38px;font-weight:700;color:#111518;margin-top:auto;padding-top:34px;
  border-top:1px solid rgba(17,21,24,.14)}
"""


def card_open(extra=""):
    return f'<section class="card {extra}">'


cards = []

# ---- cover
rows = "".join(
    f'<div><i>{e(nice(when(o)))}</i>{e(trim(o["title"], 42))}</div>' for o in soon[:5])
cards.append(f"""{card_open('cover')}
<div class="kicker">Open calls</div>
<div class="rule"></div>
<div class="big">Deadlines<br>coming up</div>
<div class="sub">{len(soon)} opportunities for artists, XR creators and researchers, from the free board we keep at Tanit XR.</div>
<div class="list">{rows}</div>
<div class="spacer"></div>
<div class="foot"><img src="file://{MARK}"><div>tanitxr.org/opportunities<br>Updated every week</div></div>
</section>""")

# ---- one per opportunity
for i, o in enumerate(soon, start=1):
    title = trim(o["title"], 78)
    cls = "" if len(title) <= 34 else ("small" if len(title) <= 54 else "tiny")
    cards.append(f"""{card_open()}
<div class="n">{i} of {len(soon)}</div>
<div class="kicker">{e(o.get('type') or 'Open call')}</div>
<div class="rule"></div>
<div class="name {cls}">{e(title)}</div>
<div class="blurb">{e(trim(o.get('desc'), 190))}</div>
<div class="facts">
<div class="fact"><b>Deadline</b><span>{e(nice(when(o)))} {when(o).year}</span></div>
<div class="fact"><b>Who for</b><span>{e(trim(who(o), 54))}</span></div>
{f'<div class="fact"><b>Where</b><span>{e(where(o))}</span></div>' if where(o) else ''}
</div>
<div class="spacer"></div>
<div class="foot"><img src="file://{MARK}"><div>Full details on the board<br>tanitxr.org/opportunities</div></div>
</section>""")

# ---- closing
cards.append(f"""{card_open('end')}
<div class="kicker">The board</div>
<div class="rule"></div>
<div class="big">Free, and<br>always will be</div>
<div class="sub">We are a nonprofit. We keep this board because the people who scan
heritage with us need to find work and funding, and nobody should pay to see a list of
open calls.<br><br>Know one we are missing? Send it to us.</div>
<div class="spacer"></div>
<div class="url">tanitxr.org/opportunities</div>
<div class="foot"><img src="file://{MARK}"><div>Tanit XR<br>Preserving Tunisian heritage in 3D</div></div>
</section>""")

out = os.path.join(HERE, "social", today.isoformat())
os.makedirs(out, exist_ok=True)
page = os.path.join(out, "_cards.html")
with open(page, "w", encoding="utf-8") as f:
    f.write(f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>" + "".join(cards))

if not os.path.exists(CHROME):
    sys.exit(f"Chrome is not where I expected it ({CHROME}), so the images cannot be rendered. "
             f"The page is at {page} if you want to screenshot it yourself.")

for i in range(len(cards)):
    shot = os.path.join(out, f"{i + 1:02d}.png")
    one = os.path.join(out, f"_slide{i}.html")
    with open(one, "w", encoding="utf-8") as f:
        f.write(f"<!doctype html><meta charset='utf-8'><style>{CSS}body{{background:#fdf9f2}}</style>"
                + cards[i])
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--window-size={W},{H}",
                    "--virtual-time-budget=6000", f"--screenshot={shot}", "file://" + one],
                   capture_output=True)
    if not a.keep_html:
        os.remove(one)
if not a.keep_html:
    os.remove(page)

made = sorted(f for f in os.listdir(out) if f.endswith(".png"))
print(f"{len(made)} slides in social/{today.isoformat()}/")
for f in made:
    print("   ", f)

first = soon[0]
print("\n--- caption to paste ---\n")
print("Open calls with deadlines coming up, from the free board we keep at Tanit XR.\n")
for o in soon:
    print(f"{nice(when(o))} · {trim(o['title'], 60)}")
print("\nFull details and the rest of the board: tanitxr.org/opportunities")
print("\nWe are a nonprofit documenting Tunisian heritage in 3D. The board is free and "
      "always will be. Know one we are missing? Send it to us.")
