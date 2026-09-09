# Profile worker — "form creates a page", without JetEngine

This optional Cloudflare Worker makes volunteer profile submissions appear on
**Our People** automatically (within ~1 minute), like the old JetEngine flow —
free on Cloudflare's free tier.

Until it's deployed, the create-profile form emails submissions to info@tanitxr.org
instead (FormSubmit), and profiles are published by adding a JSON file to `profiles/`
and rebuilding — nothing is broken without the worker, it's an upgrade.

## How it works

1. `create-profile.html` POSTs the form to the worker.
2. The worker commits `profiles/<name>.json` to this repo (the permanent record,
   baked in at the next `build.py` run), and
3. appends the profile to `docs/profiles-live.json` — `people.html` reads that file
   in the browser, so the new card shows up on the live site right away.
4. At your next local `python3 build.py`, the profile gets a real `person-*.html`
   page with a self-hosted photo, and the live queue is emptied.

## Setup (one time, ~10 minutes)

1. Create a free Cloudflare account (or log in) → Workers & Pages → Create Worker.
2. Paste `tanitxr-worker.js` as the worker code.
3. In GitHub (the inesTanitXR account): Settings → Developer settings →
   Fine-grained tokens → new token, repository access = `inesTanitXR/tanitxr.org` only,
   permission = **Contents: Read and write**. Copy it.
4. In the worker: Settings → Variables →
   - Secret `GITHUB_TOKEN` = the token
   - Variable `REPO` = `inesTanitXR/tanitxr.org`
   - Variable `AUTO_APPROVE` = `true` (publish instantly) or `false` (hold for review;
     you flip `"approved": true` in the JSON file to publish)
5. Deploy, copy the worker URL (e.g. `https://tanit-profiles.<you>.workers.dev`).
6. In `build.py`, set `PROFILE_ENDPOINT = "<worker URL>"` (the constant near the top,
   next to FORM_ENDPOINT), rebuild, push.

## Spam

The form has a honeypot field and the worker strips HTML from every field.
If spam ever gets through, set `AUTO_APPROVE` to `false` — submissions then wait
in `profiles/` until approved.

## Reactions & counters (same worker)

The worker also powers the board's 👍 Helpful / ✅ I applied buttons and counts
views and Apply-clicks per opportunity:

1. In the worker: Settings → Bindings → add a **KV namespace** binding named `STATS`
   (create a new namespace, e.g. `tanitxr-stats`).
2. In `build.py`, set `REACTIONS_ENDPOINT = "<worker URL>"`, rebuild, push.
3. Stats are public JSON at `<worker URL>/stats` — per opportunity: views, clicks,
   thumbs, applied. That's the evidence for selling featured listings later
   ("featured spots get N views and N applications").

No accounts, no cookies for visitors — one anonymous counter per action, with a
localStorage flag preventing double-votes per browser.
