# How tanitxr.org runs itself — the operating manual

*(written 2026-09-11; ask Claude to update this file when the system changes)*

## The machine, at a glance

| When | What | Who does it |
|---|---|---|
| Any time, from your phone | Drop opportunity names/links in the **📥 Opportunity Inbox** Apple Note, screenshots in **iCloud Drive → Opportunities Inbox**, site photos/videos in **iCloud Drive → Website Media**, or files in the shared **Google Drive** | **You** (10 seconds each) |
| Every day, 10am | **Inbox sweep**: researches your dropped items, verifies deadlines at the source, publishes open ones to the website board, writes them into the next newsletter draft (your exact format + LinkedIn tag table), tidies the Apple Note, reminds you of shortlist deadlines ≤10 days | Automatic |
| Every Monday, 9am | **Board check**: re-verifies every open opportunity (closed/extended?), curates the ⭐ featured spot (with the org's own banner), curates **your personal apply-shortlist**, refreshes the impact stats, harvests any new newsletter edition from LinkedIn | Automatic |
| When you say **"update the site media"** | Places new Website-Media photos/videos across the site, replaces weaker images, shows before/after | Claude, on request |
| When you say **"refresh the archive"** | Re-harvests the Sketchfab org, re-pairs preservation + game-ready versions, rebuilds | Claude, on request |
| When an edition is ready | You paste `ref/next-edition-draft.md` into LinkedIn, tag the pages listed in its table, hit publish | **You** (5 minutes) |

Tasks run while the Claude app is open on this Mac; if it was closed, they catch up at next launch. Manage them in the **Scheduled** sidebar (each has "Run now" — do that once per task to pre-approve its tools).

## Your personal application shortlist

`ref/ines-shortlist.json` — opportunities Claude thinks YOU should apply to, each with a reason.
The Monday check adds new fits; the daily sweep pings you when a deadline is ≤10 days away.
Tell Claude "mark X applied" or "skip X" and it stops reminding you.

## The data files that drive everything

| File | Drives |
|---|---|
| `ref/opportunity_updates.json` | The opportunities board (new items, deadline patches, featured spot) |
| `ref/ines-shortlist.json` | Your personal apply-list + reminders |
| `ref/stats.json` | The animated impact numbers (home + About) |
| `ref/archive-data.json` (via `compile_archive.py`) | The 3D archive, from the Sketchfab org |
| `ref/next-edition-draft.md` | The always-ready next newsletter |
| `profiles/*.json` | Volunteer profiles on /team/ |
| `translations.py` | French + Arabic for everything |

Everything is plain files in the GitHub repo — any web developer could take over tomorrow.

## One-time setups still waiting on you

1. **Cloudflare account (~15 min)** — unlocks three things at once: instant volunteer-profile publishing, the 👍/✅ reaction buttons, and per-opportunity view/click/apply analytics (your future evidence for selling featured listings). Guide: `worker/README.md`.
2. **Newsletter email service** — recommended Kit (free ≤10k subscribers) or MailerLite; then Claude wires the signup form and can automate a biweekly email digest. Signups currently arrive by email as a stopgap.
3. **FormSubmit activation** — the first submission on each form emails info@tanitxr.org an activation link; click it once.
4. **Flip ~13 optimized Sketchfab models to Public** (they're org-only) so their pages gain the 🎮 game-ready section — then say "refresh the archive".
5. **DNS cutover** when you're happy: point tanitxr.org at GitHub Pages, cancel WordPress. Every old link already redirects.

## Money funnel (when you're ready)
Featured listings on the board are built and auto-curated; when a sponsor pays, their listing takes the gold spot with their image, and the reaction/analytics numbers are your rate card. Invoicing runs through your fiscal sponsor.
