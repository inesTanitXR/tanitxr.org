# What Tanit XR measures, and why

The numbers a funder asks for, where each one comes from, and what it proves. Everything on the
website is counted by GoatCounter (no cookies, no personal data, visitors are never identified),
so the figures can be quoted in public. Nothing here tracks a person; it counts actions.

Weekly report: `python3 tools/analytics_report.py --days 7`. Month by month for an application:
`--months 12`. Lifetime totals since launch plus Sketchfab views: `--grant`. The Monday task
delivers the weekly one automatically once the API token is saved.

## 1. Reach: who finds us

| Number | Source | Proves |
|---|---|---|
| Visits and unique visitors, by week and by month | GoatCounter | Audience size and growth |
| Countries | GoatCounter locations | International reach; Tunisia vs diaspora vs new publics |
| Devices: desktop, phone, headset | `explore_open/<device>` | The experience works where people are, incl. VR headsets |
| First vs returning visitors | `visit/first`, `visit/returning` | People come back, a sign of value not curiosity |
| Where visitors came from (referrers), campaigns `?ref=` | GoatCounter | Which channels work (newsletter, Instagram, LinkedIn, partners) |
| Shared links that land on an object | `share_landing/<object>` | Word of mouth: shares that turned into visits |
| Sketchfab views, likes, downloads per model, lifetime | Sketchfab public API, in `--grant` | Open access is used; downloads mean reuse in education and research |

## 2. Engagement: what they do once inside

| Number | Source | Proves |
|---|---|---|
| Objects looked at, total and per object | `collection_view/<object>` | Which heritage draws attention; content decisions |
| Objects turned by hand | `collection_rotate` | Active looking, not scrolling past |
| Time spent: 1, 3, 10, 20 minute milestones | `dwell/<mark>` | Depth of attention (museum studies quote average dwell) |
| Objects seen per visit: 3, 10, 25, 50, everything | `depth/<mark>` | Breadth of exploration |
| Asked Nura for more | `nura_more/<object>` | Interpretation is wanted, not only visuals |
| Badges earned, by badge | `badge_earned/<badge>` | Learning loop completed (whole collection, all sites) |
| Galleries opened, by maker | `room_opened/<maker>` | Volunteer work is seen, not only the archive |
| Guided visit started and finished | `tour_start`, `tour_done`, `tour_step/<n>` | Donor tour completion rate |
| Scan demo watched | `scan_demo_opened` | Interest in the method, a pipeline for volunteers |
| VR sessions, passthrough or phone AR sessions, iPhone Quick Look | `xr_entered`, `ar_entered`, `ar_quicklook` | Immersive use, the XR in Tanit XR |
| Map opened and jumps from the map | `map_opened`, `map_jump/<object>` | Place matters to visitors; link to the physical sites |

## 3. Attachment: what they keep and pass on

| Number | Source | Proves |
|---|---|---|
| Objects saved, total and per object | `collection_save/<object>` | Personal attachment; the "collection" behaviour |
| Shares by network (WhatsApp, Instagram, X, Facebook, LinkedIn, device share, link copied) | `collection_share/<network>` | Organic distribution; which networks to invest in |
| Share posters made | `collection_poster/<object>` | Content created by visitors |
| Share sheet opened vs shares completed | `share_sheet_opened` vs `collection_share` | Friction in sharing |

## 4. Conversion: what it leads to

| Number | Source | Proves |
|---|---|---|
| Nura's asks shown vs accepted, by ask (share, donate, volunteer, newsletter, save, gallery, VR) | `nura_ask/<ask>` vs `nura_ask_yes/<ask>` | Which invitations work; a real conversion funnel |
| Donate clicks, by page | `donate_click/<page>` | Intent to give (Tuesday reports the actual gifts) |
| Newsletter sign-ups, by page | `newsletter_signup/<page>` (Kit holds the true subscriber count) | Audience we can reach again |
| Forms submitted and completed | `form_submit/<page>` then `form-sent/<form>` | Contact, opportunity tips, volunteer profiles |
| Volunteer page and Get Involved traffic | GoatCounter pages | Pipeline into the community |

## 5. Numbers the website cannot count (keep them by hand, quarterly)

- Volunteers active this quarter, countries they live in, hours contributed (Slack, Thursday call attendance).
- Objects scanned, optimized, modelled; sites documented; models published open (repo data and Sketchfab).
- Newsletter subscribers and open rate (Kit). LinkedIn newsletter subscribers and reach (LinkedIn analytics).
- Workshops, talks, school sessions and people reached in person.
- Press and mentions.
- Partnerships signed (INP, Agence du patrimoine, universities, Unique Mappers).

## Baselines and targets

Fill this in after the first full month of data, then update every quarter.

| Measure | Baseline (month) | Target in 12 months |
|---|---|---|
| Unique visitors per month | | |
| Countries per month | | |
| Objects looked at per visit (median depth) | | |
| Visitors staying 3 minutes or more | | |
| Saves per 100 visits | | |
| Shares per 100 visits | | |
| Newsletter sign-ups per month | | |
| VR or AR sessions per month | | |
| Tour completion rate | | |

## How to phrase it in an application

Lead with reach and depth together: "In [month], [N] people from [K] countries explored the
collection, looking at a median of [D] objects each; [P]% stayed more than three minutes, and
[S] saved or shared an object." Then the open-access line from Sketchfab: "[V] views and [X]
downloads of our open 3D models since [year]." Then the community line from section 5.

## Privacy line for applications and the website

"We count actions, not people. Our analytics (GoatCounter) set no cookies, store no IP addresses
and cannot identify a visitor. Every number we publish comes straight from that dashboard and
can be shown on request."
