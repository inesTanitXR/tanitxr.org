# The Collection: every idea, and where it stands

Everything Ines raised while we built tanitxr.org/walk, so nothing gets lost.
Last updated 2026-09-18, afternoon. Earlier versions of this file described an entrance
gate and two doors; both were removed at Ines's request, and this reflects what is live.

## Built and live

| Idea | Where it ended up |
|---|---|
| A 3D page like the UNESCO museum, the simple one | `/walk/`. One artifact at a time, scroll to move, drag to turn. No rooms or corridors; the real walkable museum is Patrick's Unity build |
| Starts in 3D, no landing page | The first artifact is lit, turning and draggable from the first frame. The light eases up over the first second |
| A better opening object | The Tanit Stela, with its symbol, leads the collection |
| Use the real scans | 53 game-ready models pulled from Sketchfab with Ines's token, compressed about 90 percent (meshopt + webp), 35 MB in all |
| Consider real size | The exact measured size on every label, taken from the model files. In VR the objects stand at that size |
| Better titles and text | Site names out of titles, "Test Scan" prefixes gone, no em dashes anywhere in the copy |
| Volunteer credits | Scanned by / optimized by / modelled by on all 53. Where an account has no real name the username shows, as Ines prefers |
| Nura as a companion | Floats, faces you, follows your cursor, swings around an object as you turn it, trails sparkles, waves when clicked |
| Nura is quiet until asked | A gold pulse says she has something. Tap her for one short line; the long text is behind "Tell me more" |
| Nura speaks in her own voice | The three lines recorded at MIT Reality Hack play for the Tanit Stela, the Draped Statue and the Roman Column. Everything else uses the browser's voice |
| Nura welcomes you back | On a return visit with progress she says how many you have seen and how many are left |
| Signal that it rotates | A ring with two arrows around the object until you have turned one |
| Gamify it | Six badges. Finishing a room earns a moment from Nura and a chime |
| Saving leads somewhere | A tray of what you saved, jump back, clear, or share the set as one link |
| Share sheet with the platforms | Shows the generated image and caption, then LinkedIn, Facebook, X, WhatsApp, copy, save. The device sheet on phones reaches Instagram |
| Post image, not a link | The camera button renders a 1200x1200 image with title, size, credit and the mark |
| Showcase volunteer-made work | A persistent switch at the top: Scanned in Tunisia, or Made by volunteers |
| A room for each artist | One room per maker, and "See all of Rachel's work together" puts every piece in one scene on plinths; click one to bring it forward |
| A volunteer says "I made this" | Their photo, line and profile link, once per volunteer, with a button into their room |
| Nura teaches scanning | Three dashed circles around the object you are on, a phone travelling them, Nura flying the same path. A "How to scan" button that is always there, plus one offer after three turns |
| VR in a Quest browser | Enter VR lays seven pieces on an arc at real size, labels floating above each, controller rays, hold the trigger to turn one, trigger on empty space for the next set, Nura's line on a panel and read aloud |
| See the VR layout without a headset | `?xrpreview=1` builds the same arc and puts the camera at standing eye height |
| A map of the whole collection | A "Map" button opens a strip of every object along the bottom, grouped by room, seen ones marked, click to jump |
| Events on the site | Home page and Community page list what is coming: CityCamp Gainesville on September 20 with two Tanit XR tracks, and the DC evening with TAYP on October 22. Past events drop off at build time |
| Link previews site-wide | Every page carries Open Graph and Twitter tags. Before this, every link ever posted showed as a bare URL |
| Small pleasures | A soft synthesized chime on save and badge, scroll that settles each object in the centre, a breathing glow until the first model arrives |

## Not done, and what each needs

| Idea | What it needs |
|---|---|
| **Splats: "see it in its real environment"** | Scaniverse exports `.ply`; Spark (World Labs) renders splats in three.js. The community already publishes splats to arrival.space in Mark Jeffcock's course. Needs the files in Drive |
| **Patrick's museum pieces** | Nothing of his is in the Sketchfab archive data. Needs files or Sketchfab ids |
| **Tunisian background music** | Needs properly licensed audio. Anything copyrighted is out |
| **The DC event venue** | Listed as "to be announced" until Ines confirms it |
| **Analytics** | `ref/analytics.json` is wired but off. Cloudflare Web Analytics is free; a token switches it on |
| **The cactus model** | 47 MB, will not compress; stays in the archive viewer only |
| **Real names for two accounts** | `danielgo257` and `georgealyssa85` in `ref/creators-map.json`, and `model_overrides` for any credit the uploader field gets wrong |

## Found by auditing

- Site-wide: 30,299 internal links across 857 pages, none broken. Home, archive, galleries,
  opportunities, community and team load with no failed requests.
- The board's featured photo was resolving inside JSON to `/opportunities/assets/...`, the same
  trap the walk page had. Fixed by resolving off the stylesheet, which the build has already
  rewritten to the right depth.
- `optimized_by` records the Sketchfab account that uploaded the game-ready file, and for all
  28 it matches the org dump. `scanned_by` is never a person, only the org account.

## Open questions for Ines

- **Music**: mood, and anything the community recorded that we may use.
- **The scanning guide** Rachel and Bety are updating: not described on the site until they say so.
