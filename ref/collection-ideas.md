# The Collection: ideas, and what state each one is in

Everything Ines raised while we built tanitxr.org/walk, so nothing gets lost.
Last updated 2026-09-18, overnight.

## Built and live

| Idea | Where it ended up |
|---|---|
| A 3D page like the UNESCO museum | `/walk/`. One artifact at a time, scroll to move, drag to turn |
| Not a museum simulation | Dropped the rooms and corridors. The real walkable museum stays in Unity with Patrick's team |
| Use the real scans | 53 game-ready models pulled from Sketchfab, compressed about 90 percent (meshopt + webp) |
| Consider real size | Exact measured size on every label, taken from the model files |
| Better titles | Site names stripped out of titles; the place is its own field |
| Volunteer credits | Scanned by / optimized by / modelled by on all 53 |
| Nura as a companion | Floats, faces you, follows your cursor, trails sparkles, waves when clicked |
| Nura not as a ruler | She is a guide, not a scale reference. Objects are one comfortable size |
| Less text in her bubble | One short line, about a dozen words. The long text is behind "Tell me more" |
| Nura speaks | A speaker button reads her line aloud with the browser's own voice |
| Nura moves with the object | She swings around it as you turn it |
| Something happens when you click her | She waves, her sparkles flare, and her bubble opens |
| Signal that it rotates | A ring with two arrows around the object, not a small text hint |
| Gamify it | Six badges: First Turn, Curator, Good Listener, Site Surveyor, Guardian, Whole Collection |
| Intro hints at the game | The opening card says: tap Nura, save things, find the badges |
| Saving leads somewhere | A tray of what you saved, jump back to any of it, or share the whole set as one link |
| Donate | A gold Donate button on every object |
| Post image, not a link | A camera button renders the object at 1200x1200 with title, size, credit and the Tanit XR mark |
| Nura teaches scanning | Three dashed circles around a real object, a phone travelling them, Nura flying the same path |
| When to show the tutorial | Not a surprise. A "How to scan" button that is always there, plus one offer after three turns |
| Put it on the website | In the Archive menu, the footer, and a band on the home page |
| A share sheet with the platforms | One sheet for everything: shows the generated image, the caption, and LinkedIn, Facebook, X, WhatsApp, copy, save. On a phone the device sheet is offered, which is the only route that reaches Instagram |
| A room for each artist | The hand-modelled work is now one room per maker, and the cameo has a 'See Rachel's room' button that jumps straight there |
| A cinematic entrance | The first artifact turns in the dark under one shaft of light, dust drifting, lines arriving one at a time. All controls stay hidden until you enter |
| Showcase volunteer-made work | Two doors at the entrance: 42 scanned in Tunisia, or 11 modelled by hand. Volunteer work is a choice, not a footnote at the end |
| A volunteer says "I made this" | The first time you reach an object someone worked on, their photo appears with a line and a link to their profile. Once per volunteer |
| Nura rotates with the object | She swings around it as you turn it, and flies the circle herself during the scan demo |
| Does it work in a VR headset | Yes. In a Quest browser there is now an Enter VR button, and the object stands at the size it really is. This is where the measurements pay off |

## Not done yet, and what each needs

| Idea | What it needs |
|---|---|
| **Splats: "see it in its real environment"** | Scaniverse can export a splat as `.ply`. Spark (World Labs) renders splats inside three.js, so a splat could fade in around an object. Blocked only on getting files out of the app: open a scan in Scaniverse, Share or Export, choose the splat/PLY option, drop it in Drive |
| **Nura's real voice** | Three recorded lines already exist in Drive from MIT Reality Hack (`Object_1/2/3.mp3`). They are not matched to objects yet. Today she uses the browser's robot voice |
| **Patrick's museum pieces** | Ines wants his fragments and room pieces shown too. Nothing of his is in the Sketchfab archive data, so we need the files or their Sketchfab ids before they can appear |
| **Tunisian background music** | Not started. Needs properly licensed audio, and should be off by default with a toggle. See the open question below |
| **Hackathon track and the October 22 event** | Ines asked for these to be mentioned on the site. Not added yet |
| **Analytics** | `ref/analytics.json` is wired but switched off. Cloudflare Web Analytics is free and needs no cookie banner. Once a token is in there, views, rotations, saves and shares start recording, which is what grant applications ask for |
| **The cactus model** | 47 MB and will not compress. Left out of the 3D page, still in the archive viewer |
| **Two volunteers show as usernames** | `danielgo257` and `georgealyssa85` need their real names in `ref/creators-map.json` |

## Found by auditing, worth knowing

- **The links on the walk page were all broken.** Its data sits in a JSON blob, which the
  build's URL rewriting cannot see into, so every "Full record" and profile link resolved to
  `/walk/archive/...` instead of `/archive/...`. Fixed by resolving them off the site root.
- **The rest of the site is clean**: 30,299 internal links across 857 pages, none broken.
- **`optimized_by` is only the Sketchfab account that uploaded the game-ready file**, not
  necessarily who did the work, and `model_overrides` in `ref/creators-map.json` is still
  empty. Two accounts, `danielgo257` and `georgealyssa85`, have no real name, so we were
  printing usernames as credits. Those now read "optimized by a Tanit XR volunteer" until
  Ines fills in the names or the overrides.
- **`scanned_by` is never a person** in this data, only blank or the org account. So scans
  are credited to the community, which is the honest maximum.

## Open questions for Ines

- **Music**: what mood, and is there anything the community recorded that we are free to use? Anything copyrighted is out.
- **The scanning guide** Rachel and Bety are updating: not published, and not described on the site, at Ines's request. Say when it is ready.
