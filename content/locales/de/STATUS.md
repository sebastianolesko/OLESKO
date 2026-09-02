# OLESKO German locale — draft status (unpublished)

Sebastian: **nothing is live.** This pack is the DE draft. Do not publish. Do not request Google indexing.

Site: `https://oleskostudio.com`  
Site ID: `6a7b43a328ec101a40bb1d20`  
Primary locale: English (`en`, id `6a876663b22843d8b60c22b0`, cmsLocaleId `6a876663b22843d8b60c2297`)  
Secondary locales at last MCP check: **none**

## Blocker: MCP cannot create locale `de`

Webflow Localization is initialized (primary English exists) but the secondary list is empty. Official Data API and the Webflow MCP **cannot add a locale**. That is Designer → Localize → Add locale, or Project Settings → Localization.

Designer MCP is **not connected** on this machine. To let an agent apply this pack after you add the locale, open Designer with the MCP app:

https://olesko-website----development.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99

### What to add (you, once)

1. Locale tag: `de`
2. Display name: German / Deutsch
3. Subdirectory: `de` (not a folder of duplicate static pages)
4. **Publishing: leave disabled.** Draft only.
5. Do not enable locale publishing. Do not publish the site.

After `de` exists, MCP can write secondary-locale page copy, page SEO, and schema. Primary English stays read-only via the localization tool.

## What this repo contains

| File | Purpose |
|---|---|
| `/llms.txt` | Full EN + DE studio rules. EN Collection now lists all **10** films (Look of Love + Let It Rain added). DE Collection rows use `/de/...` URLs and are labeled draft/unpublished. |
| `content/locales/de/apply.json` | Node-level DE copy for Home, Collection, Commission, About, 10 film pages, header, footer, commission CTA, film disclaimer. Ready for `update_static_content` / `update_component_content` once `localeId` exists. |
| `content/locales/de/seo-schema.json` | DE titles, meta, OG, and JSON-LD (Organization, WebSite, CollectionPage, WebPage, VideoObject). Mux `contentUrl` / `embedUrl` copied from live EN. Canonical = locale URL. |
| `content/locales/de/APPLY.md` | Apply order after you add locale `de`. |
| `content/locales/de/build_pack.py` | Regenerates the two JSON files. |
| This file | What MCP could not do. What still needs your publish yes. |

## CMS leftovers still on the site (blocks Localization Basic)

Re-checked via MCP on 2 Sep 2026. Still exactly two collections, both **zero items**. Not deleted.

| Collection | id | slug | items |
|---|---|---|---|
| Films-cms | `6a876663b22843d8b60c22c8` | `films-cms` | 0 |
| Posts | `6a87666d57cf52c62b38e6cf` | `posts` | 0 |

`data_cms_tool` has no delete-collection action (confirmed: `delete_collection` is rejected). Designer MCP is not connected. This environment has no Webflow Data API token, so `DELETE https://api.webflow.com/v2/collections/{id}` could not be sent.

Live films stay static `/films/...` pages. Do **not** create replacement collections. Do **not** publish. Do **not** enable locale publishing. Do **not** paste llms.txt.

### How to delete (you, then retry Localization Basic)

Designer: CMS → collection gear → Delete collection. Do that for **Films-cms** and **Posts**. Do not publish after.

Or put a site token with `cms:write` in the agent environment as `WEBFLOW_SITE_API_TOKEN` and say retry. Official call:

```
DELETE https://api.webflow.com/v2/collections/6a876663b22843d8b60c22c8
DELETE https://api.webflow.com/v2/collections/6a87666d57cf52c62b38e6cf
```

After both are gone, `get_collection_list` must return **zero** collections. Then retry Localization Basic checkout. Locale `de` stays unpublished.

## CMS films: there are no CMS film items to clone

Live films are **static pages** under `/films/...` (10 pages, including Look of Love and Let It Rain). Do **not** create Films-cms items. That would invent a second set of film URLs.

The Collection page still has an empty CMS list (“No items found”) plus the static cards. Left as-is. Not a DE task.

## llms.txt: MCP cannot write Site Settings

No MCP action writes the site-level llms.txt field. Live Site Settings still has the older 8-film English file.

**Do not paste the bilingual `/llms.txt` into live Site Settings until you publish DE.** The DE rows use `/de/...` URLs. Those 404 until the locale is published.

When you say publish:

1. Publish DE (and only then)
2. Paste `/llms.txt` from this repo into Site Settings → llms.txt
3. Publish again so crawlers see the new file

Until then, the repo file is the source of truth.

## Header switcher

Live header DE is a **disabled span**, not a locale link. Wiring it to `/de` on the primary locale before the locale exists would 404 if anyone published by accident.

After you add `de`:

- Primary header: EN current, DE → locale `de` (Webflow locale link, not a fake `/de` path you typed)
- DE header: DE current, EN → `/`
- Menu + bar + bottom language row all three

Do not treat IMPRINT / PRIVACY as German legal. Labels stay English so nobody thinks a DE legal page exists.

## FAQ questions

`get_page_content` returns FAQ **answers** (localizable). FAQ **questions** live in `accordion_toggle_text` spans and did not come back in that payload. `set_text` has no `localeId` and would overwrite English.

After `de` exists, set these on the **DE locale only** (Designer or a locale-aware write):

| EN | DE | node (toggle text) |
|---|---|---|
| CAN I MAKE THIS MYSELF WITH AI SOFTWARE? | KANN ICH DAS SELBST MIT KI-SOFTWARE MACHEN? | `bc61f72d-608a-d5ee-1f27-d36e12220cf6` |
| CAN I USE THIS IF THE MANUFACTURER ONLY ALLOWS OFFICIAL BRAND MATERIAL? | GEHT DAS, WENN DER HERSTELLER NUR OFFIZIELLES MARKENMATERIAL ERLAUBT? | `c2e1f317-16f6-7d17-7546-ddd849486b74` |
| WHAT IS A COMMISSIONED AUTOMOBILE FILM? | WAS IST EIN AUTOMOBILFILM AUF AUFTRAG? | `ee7a7955-3390-8fe0-0996-4c4b89761154` |
| WHAT DO I NEED TO PROVIDE? | WAS MUSS ICH LIEFERN? | `ee7a7955-3390-8fe0-0996-4c4b8976115d` |
| DOES MY AUTOMOBILE NEED TO BE TRANSPORTED? | MUSS MEIN AUTOMOBIL TRANSPORTIERT WERDEN? | `ee7a7955-3390-8fe0-0996-4c4b89761166` |
| DOES MY FILM NEED A COMMERCIAL OBJECTIVE? | BRAUCHT MEIN FILM EIN KOMMERZIELLES ZIEL? | `ee7a7955-3390-8fe0-0996-4c4b8976116f` |
| HOW LONG WILL MY FILM TAKE? | WIE LANGE DAUERT MEIN FILM? | `ee7a7955-3390-8fe0-0996-4c4b89761178` |
| WILL MY BRAND GUIDELINES BE FOLLOWED? | WERDEN MEINE MARKENRICHTLINIEN BEACHTET? | `ee7a7955-3390-8fe0-0996-4c4b89761181` |
| IS THE IMAGERY REAL OR GENERATED? | SIND DIE BILDER ECHT ODER ERZEUGT? | `ee7a7955-3390-8fe0-0996-4c4b8976118a` |
| CAN MY FILM INCLUDE A REAL SHOWROOM, VILLA OR IDENTIFIABLE PERSON? | KANN MEIN FILM EINEN ECHTEN SHOWROOM, EINE VILLA ODER EINE ERKENNBARE PERSON ZEIGEN? | `ee7a7955-3390-8fe0-0996-4c4b89761193` |
| CAN I SPECIFY THE NUMBER PLATE, BRANDING AND DELIVERY FORMAT? | KANN ICH KENNZEICHEN, BRANDING UND AUSLIEFERUNGSFORMAT VORGEBEN? | `ee7a7955-3390-8fe0-0996-4c4b8976119c` |
| WHAT USAGE RIGHTS ARE INCLUDED? | WELCHE NUTZUNGSRECHTE SIND ENTHALTEN? | `ee7a7955-3390-8fe0-0996-4c4b897611a5` |
| WILL MY COMMISSIONED FILM BE PUBLISHED? | WIRD MEIN AUFTRAGSFILM VERÖFFENTLICHT? | sibling of summary `ee7a7955-3390-8fe0-0996-4c4b897611b1` |

## Imprint and Privacy

Left in English. No invented legal German. Pending Dolores. Do not publish legal DE.

## Home “BUT IS IT REAL?”

DE copy is in `apply.json`. The section stays **hidden**. This job does not unhide it.

## What was not done (on purpose)

- No site publish
- No custom-domain changes
- No Google indexing request
- No `/de` folder of duplicate static pages
- No Seedance / Higgsfield on the public site
- No new GitHub repo, no new Cursor project
- No new rem, no new Lumos tokens
- No Films-cms items created
- Header DE switcher not pointed at `/de` on the live primary (locale missing)

## After you add locale `de` (agent or you)

1. `get_site` → read `localeId` and `cmsLocaleId` for `de`
2. Apply `apply.json` with that `localeId`
3. Apply `seo-schema.json` (`update_page_settings` + schema markup, `localeId`)
4. Wire header language links to the real locale
5. Set FAQ question spans on DE only
6. Save in Designer so Webflow can emit `hreflang` en ↔ de
7. **Stop. Wait for your publish yes.**

## Success checklist (draft)

- [ ] Locale `de` exists as subdirectory (you)
- [ ] DE copy, SEO, OG, schema on Home, Collection, Commission, About, 10 films (pack ready; apply blocked)
- [ ] hreflang in locale HTML (needs locale + Designer save)
- [ ] DE switcher points at DE locale (needs locale)
- [x] Report written
- [x] llms.txt in repo (Site Settings paste later, after publish)

## Page IDs (for apply)

| Page | id | EN path | DE path (after locale) |
|---|---|---|---|
| Home | `6a83fdcf46ec1970b6eb307b` | `/` | `/de` |
| Collection | `6a8471318afbe9b46708f954` | `/collection` | `/de/collection` |
| Commission | `6a8471320e6ee1e88c0037c2` | `/commission` | `/de/commission` |
| About | `6a8471331d2d68eb848af612` | `/about` | `/de/about` |
| Imprint | `6a8b7dede6239a222989a4f9` | `/imprint` | leave EN |
| Privacy | `6a8b7ded6e9a5fb3c6f8fec9` | `/privacy` | leave EN |
| Let it rain | `6a94a5aa1d755181100606b7` | `/films/let-it-rain-nurburgring-nordschleife` | `/de/films/let-it-rain-nurburgring-nordschleife` |
| The Look of Love | `6a94835baff009655de6bdca` | `/films/the-look-of-love-ferrari-250-gt-california-spyder` | `/de/films/the-look-of-love-ferrari-250-gt-california-spyder` |
| Riviera Summer Cruise | `6a8b402d69195cfc7d432a59` | `/films/riviera-summer-cruise-aston-martin-db12-volante` | same slug under `/de` |
| Alpine Autumn High Pass | `6a8b402d3f30e7ce2c689cec` | `/films/alpine-autumn-high-pass-porsche-992-gt3-touring` | same |
| Along the Sea Wall | `6a8b075dacef99c64dc2ba1d` | `/films/along-the-sea-wall-bentley-continental-gtc` | same |
| On the Flooded Salt | `6a8b402e3f30e7ce2c689d4b` | `/films/on-the-flooded-salt-lamborghini-revuelto` | same |
| At the Louvre | `6a8b402efd4a464888ee176a` | `/films/at-the-louvre-ferrari-250-gto` | same |
| Into the Highland Fog | `6a8b402ffa314513088680ba` | `/films/into-the-highland-fog-mercedes-amg-gt` | same |
| Down the Avenue | `6a8b402fefdad2a541be5cf8` | `/films/down-the-avenue-mercedes-benz-190-sl` | same |
| Mountain Sanctuary | `6a8b4030d04c77b87628e041` | `/films/mountain-sanctuary-mercedes-amg-g-63` | same |

Register: Sie / Ihr Film. Never “ein OLESKO-Film.” Film titles stay English. Mux playback IDs stay. Colors and tokens unchanged.
