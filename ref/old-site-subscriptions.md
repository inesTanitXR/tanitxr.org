# Subscriptions from the old WordPress site

Worked out on 2026-10-01 from the domain's live DNS records and from the Internet Archive's
copy of the old site (3 December 2025). This is evidence of what was **installed and still
pointed at**, not a billing statement. Only the receipts prove what is being charged.

## CONFIRMED on 2026-10-01, read from the WordPress.com account

Two live purchases, both auto-renewing, and **both owned by a WordPress.com account that is
not Ines's**. Her own account, `inessaid88`, has no active upgrades, no billing history and
no payment method on file. She has never been charged by WordPress.com.

| Purchase | Renews | Auto-renew | Price | Owner |
|---|---|---|---|---|
| **Domain `tanitxr.org`** (registered 15 Jul 2025) | 15 June 2028 | **on** | not shown to her | a different account |
| **Professional Email**, 3 mailboxes | 25 July 2027 | **on** | **$105/year** + tax | a different account |

The three mailboxes are `ines@`, `info@` **and `laura@tanitxr.org`**. They are a separate
purchase from the domain, so "keep the domain, cancel the rest" would take all three down,
Laura's included.

A third purchase, the **WordPress.com Business plan**, is active on the site and also sits in
Caroline's account. See the plugin section below.

**The real problem is not the money.** The domain and every staff mailbox sit in somebody
else's account. Ines cannot manage the billing, cannot change the card, and cannot stop a
lapse. If that account's card fails or its owner becomes unreachable, the domain and all
three mailboxes expire and the site and the email go with them. Finding out whose account it
is, and getting both purchases transferred, matters more than any cancellation below.

WHOIS privacy on the domain is **disabled**, so the registrant details are public.

## The plugins, read from the site's own plugin list on 2026-10-01

**The WordPress.com Business plan is active** on the TANIT XR site. An earlier note here said
no plan existed; that was wrong. Purchases owned by Caroline's account are invisible from
Ines's, the same way the domain and the mailboxes were. The plan's price and renewal date are
in Caroline's account, not readable from Ines's.

The site is marked **Unreachable**, so the plan is being paid for a site that no longer runs.

### Certainly paid, no free edition exists

| Plugin | Vendor | Notes |
|---|---|---|
| **Elementor Pro** | elementor.com | Listed by name as Pro, separate from the free Elementor also installed |
| **JetEngine** | crocoblock.com | Paid only. This is the one Ines was worried about, and it is there |
| **JetEngine, custom visibility conditions** | crocoblock.com | addon |
| **JetEngine, dynamic tables builder** | crocoblock.com | addon |
| **JetEngine post expiration period** | crocoblock.com | addon |
| **JetSmartFilters** | crocoblock.com | paid |
| **Filter Everything PRO** | filtereverything.pro | Listed by name as PRO |

Six Crocoblock products on one site points at the all-inclusive subscription rather than
single-plugin licences. JetFormBuilder is also installed; its core is free.

### Probably paid, worth checking the receipt

- **TranslatePress** — the free edition allows one extra language and the site ran French and Arabic
- **Blocksy Companion** — listed without "Pro", so possibly the free edition
- **Modula**, **Search & Filter**, **WP All Import**, **Bit Integrations**, **Stackable**, **Frontend Admin**, **Image Optimizer** — each is freemium; the list does not say which edition

### Free, ignore

Akismet, Classic Editor, Crowdsignal, Gutenberg, Gravatar Enhanced, Jetpack, Layout Grid,
Page Optimize, WPCode Lite, WPForms Lite, WPSyncSheets Lite, WP Import Export Lite,
WP Ultimate CSV Importer.

### Where these are billed

None of them appear in WordPress.com billing, so they were bought directly from the vendors:
elementor.com, crocoblock.com, filtereverything.pro, translatepress.com. Those receipts will
be in the Titan mailboxes, not in Gmail.

## Do not cancel these

| Thing | Evidence | Why it stays |
|---|---|---|
| **Titan email** | `MX mx1.titan.email`, `mx2.titan.email` | This is `ines@tanitxr.org`. Cancelling it takes your email address down, and with it every form, login and reply on the site. |
| **The domain registration** | `NS ns1/2/3.wordpress.com` | `tanitxr.org` is registered and its DNS is served at WordPress.com. Lose this and the whole site goes dark, including the GitHub Pages one. |

**Check before touching the WordPress.com plan:** Titan is often sold *through* WordPress.com
and bundled into the plan. If it is, cancelling or downgrading the plan can kill the email.
The Purchases page below lists them separately if they are billed separately.

## Likely paid, and safe to cancel

Nothing on the new site uses any of these. It is a static site built by `build.py`; there is
no WordPress, no theme, no plugin.

| Thing | Evidence from the archived page | Confidence it was paid |
|---|---|---|
| **TranslatePress** | `wp-content/plugins/translatepress-multilingual` | **High.** The free edition allows one extra language only. The old site ran English, French *and* Arabic, which needs a paid plan. |
| **Elementor** | `<meta name="generator" content="Elementor 3.33.2">` | Unknown. Pro is a yearly licence; the free edition also emits this tag. |
| **Blocksy** | theme `blocksy` + `blocksy-child`, `blocksy-companion` v2.1.18 / 2.1.22 | Unknown. A child theme suggests real customisation, which usually means Pro. |
| **Yoast SEO** | `yoast-schema-graph` in the markup | Unknown. Premium exists; free is very common. |
| **Jetpack** | `jetpack` plugin, `stats.wp.com`, `i0.wp.com` | Unknown. Has both a free tier and paid tiers. |
| **WordPress.com plan** | `_spf.wpcloud.com`, `/_static/??-` asset loader | **Certain there is an account.** The plan can likely drop to the cheapest tier that keeps the domain, the DNS and the email. |

A caveat on the "unknown" rows: WordPress.com serves plugin assets through a URL
concatenator, so individual plugin paths are hidden. The absence of a `-pro` marker is **not**
evidence that the free edition was used. Only the receipts settle these.

## Also seen

- **Tuesday** donations, campaign `73DO5` (`donors.tuesday.app/campaign/73DO5`). Check whether
  it carries a monthly fee or only a cut per donation, and whether that campaign is still the
  one the new site points at.

## Where to look, highest yield first

1. **wordpress.com/me/purchases** — every plan, domain and marketplace subscription bought
   through WordPress.com, each with its renewal date and an auto-renew switch. This one page
   probably answers most of the list above.
2. **The card or PayPal statement for the last 12 months.** This is the only complete record.
   Annual licences renew once a year, so a full twelve months is the minimum worth reading.
3. **Each vendor's own account page**, for anything bought directly rather than through
   WordPress.com: elementor.com, creativethemes.com (Blocksy), translatepress.com, yoast.com.

## Order of work

1. Read the Purchases page and write down what is there, before cancelling anything.
2. Confirm how Titan is billed.
3. Cancel the plugin and theme licences. The new site cannot use them.
4. Decide the WordPress.com plan last, once the email question is settled.

Never cancel something whose renewal you have not first seen on a statement. A subscription
you cannot find may simply be billed under a vendor name you do not recognise.
