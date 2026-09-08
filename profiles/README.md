# Volunteer profile submissions

Each `.json` file here becomes a Community Contributor card on Our People
(plus a `person-<slug>.html` page) at the next `python3 build.py`.

Example — save as `firstname-lastname.json`:

```json
{
  "name": "Jane Doe",
  "role": "3D Generalist",
  "bio": "Jane helps clean up photogrammetry scans for Tanit XR. She studies digital arts in Tunis.",
  "photo": "https://example.com/jane.jpg",
  "linkedin": "https://www.linkedin.com/in/janedoe/",
  "instagram": "",
  "website": "",
  "approved": true
}
```

- `photo` can be any image URL (it is downloaded, resized, and self-hosted at build time),
  or a filename that exists in `media/`.
- Set `"approved": false` to keep a submission out of the site without deleting it.
