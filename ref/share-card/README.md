# The picture a link preview shows

When someone pastes tanitxr.org into iMessage, WhatsApp, LinkedIn or Slack, the app fetches
`og:image` and `og:title` from the page and draws a card. Before November 2026 the home page
handed it a bare photo of ruins and the word "Home", which told a stranger nothing.

These are the three designs we drew instead. `a.html` is the one live on the home page; the
others are kept so swapping is a one-line change rather than a redesign.

- `a.html` cream panel with the logo and the headline, Ines at Byrsa beside it
- `b.html` the same photo full width, logo and headline over it
- `c.html` "Hi, I'm Ines", first person, for a card only she sends

To render one, with Chrome:

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
      --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
      --window-size=1200,630 --virtual-time-budget=6000 \
      --screenshot=card.png "file://$PWD/ref/share-card/a.html"
    sips -s format jpeg -s formatOptions 88 card.png --out media/share-card-2026-11.jpg

1200 by 630 is what every scraper wants; a portrait image gets shrunk to a thumbnail or dropped.

Two things to know when changing it:

- The filename carries a date on purpose. Facebook, LinkedIn and iMessage cache a preview by
  its URL, sometimes for weeks. Overwriting `share-card-2026-11.jpg` would leave the old picture
  showing; a new name is what makes them fetch again.
- `build.py` crops cards into `docs/assets/img/<name>-card.jpg` and skips the work when that
  file already exists. Delete it before rebuilding, or the old crop stays.

The headline itself lives in `build.py`, as `share_title` on the home page, and is translated
in `translations.py` like any other sentence.
