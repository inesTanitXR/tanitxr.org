# The Collection: ideas, and what state each one is in

Everything Ines raised while we built tanitxr.org/walk, so nothing gets lost.
Last updated 2026-09-18.

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

## Not done yet, and what each needs

| Idea | What it needs |
|---|---|
| **Splats: "see it in its real environment"** | Scaniverse can export a splat as `.ply`. Spark (World Labs) renders splats inside three.js, so a splat could fade in around an object. Blocked only on getting files out of the app: open a scan in Scaniverse, Share or Export, choose the splat/PLY option, drop it in Drive |
| **Nura's real voice** | Three recorded lines already exist in Drive from MIT Reality Hack (`Object_1/2/3.mp3`). They are not matched to objects yet. Today she uses the browser's robot voice |
| **Tunisian background music** | Not started. Needs properly licensed audio, and should be off by default with a toggle. See the open question below |
| **Hackathon track and the October 22 event** | Ines asked for these to be mentioned on the site. Not added yet |
| **Analytics** | `ref/analytics.json` is wired but switched off. Cloudflare Web Analytics is free and needs no cookie banner. Once a token is in there, views, rotations, saves and shares start recording, which is what grant applications ask for |
| **The cactus model** | 47 MB and will not compress. Left out of the 3D page, still in the archive viewer |
| **Two volunteers show as usernames** | `danielgo257` and `georgealyssa85` need their real names in `ref/creators-map.json` |

## Open questions for Ines

- **Music**: what mood, and is there anything the community recorded that we are free to use? Anything copyrighted is out.
- **The scanning guide** Rachel and Bety are updating: not published, and not described on the site, at Ines's request. Say when it is ready.
