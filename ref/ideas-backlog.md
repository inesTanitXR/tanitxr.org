# Ideas backlog: everything suggested for tanitxr.org, and where each one stands

Started 2026-09-25 from the full site review (report: https://claude.ai/artifact/8jRYGfD1jXvJ2vmYTBFFcC).
Ines: "keep track of all these suggestions so we never forget them". This file is the tracker.
Older Collection ideas live in `ref/collection-ideas.md`; nothing there is repeated here.

Status words: **live** (built and deployed), **built** (in the repo, not yet checked by Ines),
**next** (agreed, not started), **needs Ines** (a decision, a key or an account), **parked**.

## Explore (the Collection)

| Idea | Status | Notes |
|---|---|---|
| Every object has its own Nura opener, 69 distinct lines, en/fr/ar | live 2026-09-25 | `ref/nura-openers.json` |
| Ask Nura: a text box under her line, answering from the label by keyword | removed 2026-09-26 | Ines: it did not work well. It answered anything, confidently, whether or not it had matched. Nura herself kept |
| Nura reacts when you turn things (2nd, 6th and 14th object turned) | live 2026-09-25 | three lines, gone by themselves |
| Scaniverse import, including splats | dead 2026-09-26 | the phone broke and the scans were only on it, never backed up to iCloud. Nothing left to import. Only what reached Sketchfab survives |
| "Make a poster" button on the label | dropped 2026-09-25 | Ines: Share already makes the picture |
| Museum page links the hall preview (`/explore/?hall=1`, scans inside Patrick's hall) | built 2026-09-25 | |
| Classroom mode `/explore/?class=1`: no asks, no donate button, quiet Nura | built 2026-09-25 | for teachers; five-object route still to do |
| Object of the week on the home page, changes every ISO week | built 2026-09-25 | gives the newsletter and Instagram a fixed beat |
| Nura's "Tell me more" rewritten in her voice, 69 objects, en/fr/ar | built 2026-09-25 | `ref/nura-notes.json`; edit there, rebuild |
| Nura ends one line in three with a question | live 2026-09-25 | in the notes and the openers |
| Screen readers hear the object change and Nura's line (`aria-live`) | built 2026-09-25 | |
| Before-and-after slider: the phone photo next to the model | next | needs the source photos per object in Drive |
| "Then and now" on the map chip: street photo, distance, "go there" | next | 16 objects have GPS |
| Adopt an object: a named sponsor line on the label for a monthly gift | needs Ines | tiers and wording; never sells volunteer labour |
| Neapolis landing page: the storm, the press, the only 3D record | next | strongest single story on the site |
| Object comparisons: the four stelae side by side at real scale | next | gallery-room code does most of it |
| Splats, "see it in its environment" | dead 2026-09-26 | needed the raw Scaniverse captures, which are gone with the phone. Alive again only if someone rescans a site |
| Nura asks a question back ("which one should I show your friend?") | live 2026-09-25 | three thumbnails of objects you saw; the pick opens the share card |
| Nura's real voice on all 69 objects and the 69 long lines | needs Ines | ElevenLabs key; `tools/nura_script.py --record` |
| Wave and point animations for Nura | parked | only if the GLB has the clips |
| Phone track switch showing both pills | parked | the one-pill design was deliberate; revisit with a screenshot |
| Before-and-after of the Neapolis beach | next | part of the landing page |
| Keyboard rotation, focus trap in the share sheet, 44 px tap targets | next | accessibility list from the review |
| Hand-tracking menu on Quest, refused passthrough message | next | |
| Nura on WhatsApp ("send me a photo of an old thing") | parked | needs a number and a small service |
| Sound: a real recording of the medina or the Zitouna call, cleared and credited | needs Ines | replaces the generated maqam |

## Site-wide

| Idea | Status | Notes |
|---|---|---|
| "How to cite" block on every object page and in llms-full.txt | built 2026-09-25 | assistants quote what is easy to quote |
| `/impact/` page: the numbers, refreshed by the weekly task, one link for grant annexes | built 2026-09-25 | fill the baselines table on 1 October |
| Home and archive descriptions stop promising Dougga and El Jem | built 2026-09-25 | no objects from either exist |
| French and Arabic meta descriptions on the main pages | built 2026-09-25 | rows in translations.py |
| French gender and role fixes, "Fiche" for Record, generic "par" by-lines | built 2026-09-25 | |
| Arabic brand written one way ("Tanit XR") | built 2026-09-25, partly | "TanitXR" and "تانيت إكس آر" are gone; about 36 values still say "تانيت XR", Ines to choose |
| Images over 600 KB re-encoded (27 files, 22 MB) | live 2026-09-25 | every photo is WebP now; 50 MB of referenced images became 23 MB; the volunteer-page PNG hero (1.4 MB) is the one left |
| One number for "objects" across home, About, archive, galleries, Explore | built 2026-09-25 | home and About say "3D models published" (Sketchfab public count in ref/stats.json, refreshed weekly); the Collection band counts the Collection (69); archive and galleries count what they list |
| Object name drift (Sidi Sahib vs Sahbi, Zawiya vs Mausoleum, Neapolis title) | next | `ref/models.json` |
| Duplicate Explore CSS block in build.py | next | remove on a quiet day, check the home header after |
| Sitemap lastmod per page, localised titles for the 21 identical groups | parked | |
| Double-hop redirects /fr/walk.html | next | comes from tools/retire_stale_pages.py; point the .html stubs straight at /explore/ |
| "Wikipedia home" for every object: upload the 47 scans to Wikimedia Commons | needs Ines | account and licence choice; largest free audience there is |
| The Storm Harry protocol: a one-page emergency scanning protocol offered to the INP | next | write it; it is what makes Tanit XR the people they call |
| Printed 10 cm Tanit stela in every Carthage classroom, QR to Explore | needs Ines | a few dinars each |
| "Lost and found" for heritage: a report form with photo and pin | next | the map of reports is a document nobody else has |
| Yearly "State of Tunisian heritage in 3D" report | next | first edition from the January numbers |
| A scanning day as a wedding gift, delivered by paid staff | needs Ines | pricing; volunteers never |
| Weekly object post to LinkedIn, Instagram and Facebook | parked | see `linkedin-to-instagram-facebook` wish |

## Funding (see `ref/funding-next-steps.md` for today's actions)

| Idea | Status |
|---|---|
| Featured listings on the Opportunities board as earned income | needs Ines: a price |
| Adopt an object tiers on the Partners page | needs Ines: tiers |
| Institution licences for the VR museum once it ships | parked |
| Paid workshops for diaspora firms, delivered by hired staff | parked |
| The scanning guide and El Jem paper as a paid course for institutions | parked |
| Tour link (`/explore/?tour=1`) in every grant email | needs Ines |
| Grant baselines table filled on 1 October | next |
