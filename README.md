# tanitxr.org — static rebuild

Static replacement for the old WordPress/Elementor/JetEngine site (rebuilt 2026-09-08).
GitHub Pages serves `main:/docs`.

## Updating the site

1. Edit content in `build.py` (page copy lives in the `build_*` functions; models, news,
   people, and opportunities come from `wp-data/` + `ref/` JSON).
2. Rebuild:

   ```bash
   python3 build.py
   ```

3. Commit and push — the site updates in about a minute.

## Layout

| Path | What it is |
|---|---|
| `build.py` | The whole site generator — edit this |
| `docs/` | Generated site (deployed) — never edit by hand |
| `wp-data/` | JSON scraped from the old WordPress REST API |
| `ref/` | Cleaned text/data extracted from the old rendered pages |
| `media/` | Downloaded media library (not committed — 1.5 GB, lives only on the Mac) |
| `profiles/` | Volunteer profile submissions (JSON) — merged into Our People at build |
| `worker/` | Optional Cloudflare Worker for instant profile publishing |
| `html/` | Raw HTML snapshots of the old site (reference, not committed) |

## Volunteer profiles

Submissions from `/create-profile.html` arrive by email (FormSubmit → info@tanitxr.org).
To publish one: add a JSON file to `profiles/` (see `profiles/README.md`), run
`python3 build.py`, commit, push. The profile appears on Our People with its own page.

## New scans / news posts

Add entries to `ref/models.json` or `ref/news.json` (same shape as the existing entries:
title, date, sketchfab embed URL, text, image), rebuild, push.
