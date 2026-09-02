# OLESKO German (Austria) locale

## Breadcrumbs (2026-09-02)

**lastPublished: `2026-09-02T20:13:32.677Z`** on apex + www. `publishScope: site`. `googleTagIds: []`. Header, menu, and breadcrumb slashes share one rule: inherit size/weight from the labels, even `0.75em` padding, `vertical-align: middle`. Language items hug the slash (`first-child` flex-end, `last-child` flex-start). No hard-set `.75rem` on the slash.

Inner pages only. Not Home. Quiet type: `olesko_eyebrow` + `u-text-style-small` + `u-text-transform-uppercase` + `u-color-faded`. Links use `olesko_breadcrumb_link`. Separator is a dedicated `olesko_breadcrumb_separator` (inherits trail type; `padding-left/right: 0.75em`). Do not reuse `olesko_header_language_separator` on crumbs. Last crumb is a self page-link with `aria-current="page"`.

EN visible: HOME / COLLECTION, HOME / COMMISSION, HOME / ABOUT, HOME / COLLECTION / [film title], HOME / IMPRINT, HOME / PRIVACY.

DE visible (menu words): START / KOLLEKTION, START / AUFTRAG, START / ÜBER, START / KOLLEKTION / [English film title]. Imprint/Privacy stay English pages.

JSON-LD keeps the existing page object and adds a BreadcrumbList sibling in `@graph`. Legal pages that had null schema now have BreadcrumbList only. item URLs are absolute `https://oleskostudio.com/…`. No crumbs on Home. Reality stays hidden. Commission buttons stay SEND ENQUIRY / SEND BRIEF. No `googleTagIds`. `llms.txt` untouched.

Live `/collection`:

```html
<nav aria-label="Breadcrumb" class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded u-column-start-1 u-column-span-8"><a href="/" class="olesko_breadcrumb_link">HOME</a><span aria-hidden="true" class="olesko_breadcrumb_separator">/</span><a aria-current="page" href="/collection" class="olesko_breadcrumb_link w--current">COLLECTION</a></nav>
```

```json
{"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "HOME", "item": "https://oleskostudio.com/"}, {"@type": "ListItem", "position": 2, "name": "COLLECTION", "item": "https://oleskostudio.com/collection"}]}
```

Live `/de-at/collection`:

```html
<nav aria-label="Breadcrumb" class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded u-column-start-1 u-column-span-8"><a href="/de-at" class="olesko_breadcrumb_link">START</a><span aria-hidden="true" class="olesko_breadcrumb_separator">/</span><a aria-current="page" href="/de-at/collection" class="olesko_breadcrumb_link w--current">KOLLEKTION</a></nav>
```

```json
{"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "START", "item": "https://oleskostudio.com/de-at"}, {"@type": "ListItem", "position": 2, "name": "KOLLEKTION", "item": "https://oleskostudio.com/de-at/collection"}]}
```

---

## Live verify (2026-09-02)

**lastPublished: `2026-09-02T16:51:45.136Z`** on apex + www. `publishScope: site`. `googleTagIds: []`. de-AT `enabled: true`.

Live HTML on `https://oleskostudio.com/` and `https://oleskostudio.com/de-at` has real `<a href>` for EN and DE in header and menu. No `German version in preparation`.

English home header:

```html
<div aria-label="Language" class="olesko_header_language"><a href="/" aria-current="page" hreflang="en" lang="en" class="olesko_header_language_item">EN</a><span aria-hidden="true" class="olesko_header_language_separator">/</span><a lang="de" hreflang="de" href="/de-at" class="olesko_header_language_item">DE</a></div>
```

English home menu:

```html
<div aria-label="Language" class="olesko_menu_language"><a href="/" aria-current="page" hreflang="en" lang="en" class="olesko_header_language_item">EN</a><span aria-hidden="true" class="olesko_header_language_separator">/</span><a lang="de" hreflang="de" href="/de-at" class="olesko_header_language_item">DE</a></div>
```

English home menu bottom:

```html
<div aria-label="Language" class="olesko_menu_bottom_languages"><a href="/" aria-current="page" hreflang="en" lang="en" class="olesko_menu_bottom_item olesko_menu_bottom_item_current">ENGLISH</a><a lang="de" hreflang="de" href="/de-at" class="olesko_menu_bottom_item">DEUTSCH</a></div>
```

de-AT home header:

```html
<div aria-label="Language" class="olesko_header_language"><a href="/" lang="en" aria-current="page" hreflang="en" class="olesko_header_language_item">EN</a><span aria-hidden="true" class="olesko_header_language_separator">/</span><a href="/de-at" lang="de" hreflang="de" aria-current="page" class="olesko_header_language_item">DE</a></div>
```

de-AT home menu:

```html
<div aria-label="Language" class="olesko_menu_language"><a href="/" lang="en" aria-current="page" hreflang="en" class="olesko_header_language_item">EN</a><span aria-hidden="true" class="olesko_header_language_separator">/</span><a href="/de-at" lang="de" hreflang="de" aria-current="page" class="olesko_header_language_item">DE</a></div>
```

Collection, commission, about, and film pages also have those three `<a href>` switchers. `oleskolangpair` 1.0.0 is in the footer and pairs matching paths after load. Imprint/Privacy stay English (`Imprint. OLESKO` / `Privacy. OLESKO`). Reality stays `.home_reality_section.u-section.u-theme-light { display: none; }`. Commission submits stay `SEND ENQUIRY` / `SEND BRIEF`.

---

## Language switcher (2026-09-02)

Disabled DE spans are gone in OLESKO Global Header (`881a26d8-3f1e-e90c-0186-847d7679f286`). EN and DE are real `<a href>` in the header, menu, and menu-bottom row on English primary and de-AT.

| Spot | EN | DE |
|---|---|---|
| Header `olesko_header_language` | `881a26d8-3f1e-e90c-0186-847d7679f28a` → `/` | `dd7ac7c5-345c-2049-115e-57514581294c` → `/de-at` |
| Menu `olesko_menu_language` | `881a26d8-3f1e-e90c-0186-847d7679f29a` → `/` | `fc070936-6271-7b7e-8dac-fe8de3dcd478` → `/de-at` |
| Menu bottom | `0d488183-5fa9-8d2b-d025-f0bcb735f0c0` ENGLISH → `/` | `7410d705-9d60-5936-d7be-706b6a6efd79` DEUTSCH → `/de-at` |

Old disabled spans (`…f28c`, `…f29c`, `…f0c2`) deleted. Title `German version in preparation` is gone. Site footer script `oleskolangpair` 1.0.0 rewrites those hrefs to the matching path (`/collection` ↔ `/de-at/collection`, films too). Imprint/Privacy stay English URLs; DE from those pages goes to `/de-at`. `oleskowatchvideo` 1.0.0 still applied. No new rem. No `olesko_header_language_item_current` class (it does not exist).

---

Sebastian said **PUBLISH**. Full-site `publish_site` ran earlier. `/de-at` is public (`enabled: true`). Do not open Designer for commission buttons.

Site: `https://oleskostudio.com`  
Site ID: `6a7b43a328ec101a40bb1d20`  
Primary locale: English (`en`, id `6a876663b22843d8b60c22b0`, cmsLocaleId `6a876663b22843d8b60c2297`)  
Secondary: **German (Austria)** (`de-AT`, id `6a983fb4dfdbdb9a5e8b882c`, cmsLocaleId `6a983fb4dfdbdb9a5e8b8831`, subdirectory `de-at`, **enabled: false**)

Last live publish: **`2026-09-02T16:34:37.873Z`** (also on `oleskostudio.com` and `www.oleskostudio.com`). `googleTagIds` still empty. `publishScope: site`. Webflow subdomain included.

## Copy lock (unpublished de-AT, 2026-09-02)

MCP wrote **only** localeId `6a983fb4dfdbdb9a5e8b882c`. English primary not edited. `publish_site` not called. lastPublished still `2026-09-02T09:23:02.801Z`.

1. **kluge Technik replacements: 1.** Live + pack body `28ea34b7-fdff-c129-ec54-21a8f43bf721` was `mit kluger Technik` → `mit intelligenter Technologie`. No other `kluge`/`kluger Technik` on de-AT, SEO, OG, nav, footer, or CTA. About “Technik” / “moderne Technik” / FAQ “Bildtechnik” left alone.
2. **Delivery line is exactly `in einer Woche geliefert`.** Other week/turnaround phrasing killed (`IN EINER WOCHE`, `EINE WOCHE` / `ÜBLICHE` / `LIEFERZEIT`, `in einer Woche bei Ihnen`, `in der Regel innerhalb einer Woche…`, `etwa eine Woche`). Empty laurel lines inherit English `STANDARD`/`TURNAROUND`, so those two subdued spans are `·` (not a delivery claim).

| Where | node | String |
|---|---|---|
| Home hero laurel | `5b3c7b25-e77b-cfe4-245d-1e1676ee0e27` (`…0e2c`) | `in einer Woche geliefert` |
| Home service H2 | `28ea34b7-fdff-c129-ec54-21a8f43bf71d` | `IHR AUTO. KEIN echter Dreh. KEIN RISIKO. in einer Woche geliefert.` |
| Home service body | `28ea34b7-fdff-c129-ec54-21a8f43bf721` | `… mit intelligenter Technologie. … in einer Woche geliefert.` |
| Home process | `8dda0860-6443-e88d-fe16-1e70ea760893` | `Ihr Film kommt gebrauchsfertig, in einer Woche geliefert, ohne reale Produktion.` |
| Home FAQ answer | `ee7a7955-3390-8fe0-0996-4c4b8976117d` | `Ein üblicher Auftrag wird in einer Woche geliefert.` |
| Home JSON-LD FAQ | WIE LANGE DAUERT MEIN FILM? | `Ein üblicher Auftrag wird in einer Woche geliefert.` |
| Commission intro | `35f671f4-2ad3-d413-7137-ff0ac44e687d` | `Übliche Arbeit wird persönlich gemacht, in einer Woche geliefert.` |

Kept (not turnaround): `WAS MUSS ICH LIEFERN?`, `gelieferten Fotografien/Bildern`, `IHRE GELIEFERTEN FOTOGRAFIEN`, `AUSLIEFERUNGSFORMAT`, `die Sie liefern`, FAQ “Lieferung, Nutzung”.

Commission submit values still English (`SEND ENQUIRY` / `SEND BRIEF`, waiting `Please wait...`). MCP cannot send `value`/`waitingText`. Designer disconnected. Do not use `set_settings` (no localeId; would overwrite live EN).

## Applied (earlier)

MCP wrote **only** localeId `6a983fb4dfdbdb9a5e8b882c`. English primary SEO and copy were not overwritten.

| Surface | Result |
|---|---|
| Header, footer, commission CTA, film disclaimer | German (components, earlier this run) |
| Home, Collection, Commission, About | German static copy |
| Home FAQ **questions** (13) | German on de-AT via new h5 nodes inside the original accordion spans. English headings unchanged. |
| 10 static film pages | German blurbs, disclosure, TEILEN, LINK KOPIEREN. Titles stay English. Mux embeds unchanged. |
| SEO titles, meta, OG | German on those 14 pages. `publishedPath` is `/de-at/...`. |
| JSON-LD | Organization / WebSite / WebPage / FAQPage / CollectionPage / AboutPage / VideoObject. `inLanguage` `de-AT`. URLs `/de-at/`. Live Mux `contentUrl` / `embedUrl`. |
| Imprint + Privacy | Still English. EN slugs `/imprint` `/privacy` unchanged. de-AT metadata still English. No DE legal copy written. |
| Reality / “BUT IS IT REAL?” | German copy on de-AT (`ABER IST ES ECHT?`). Display not changed. Section stays hidden. |
| CMS | `get_collection_list` → `collections: []`. Films-cms and Posts were not recreated. |
| Collection empty-state node `b92297f0-eaff-dfe5-9c28-de759a2d043f` | **Node not found** (CMS list gone). Other Collection strings wrote. |

## Fahrzeug lock (2026-09-02, de-AT only)

Sebastian lock: German `Automobil*` / `Automobile` / compounds replaced with `Fahrzeug` / `Fahrzeuge` / `Fahrzeugs` / `Fahrzeugen` as grammar requires. English primary untouched (`automobile` stays). English identifiers (`brief-automobile`, `data-name="Automobile"`, `Second automobile in one film`, `aria-label="Selected automobile films"`) untouched. Imprint/Privacy body stays English; de-AT footer chrome uses Fahrzeuge. `llms.txt` not changed (live file is English only). Reality stays hidden. Commission buttons stay SEND ENQUIRY / SEND BRIEF.

## FAQ questions (applied on de-AT)

Accordion questions were span + String nodes. Localization MCP strips `<span>`, so those strings could not be written. Each original span still wraps the toggle. Inside it, a localizable `h5.accordion_toggle_text.u-text-style-h5` holds the question. English heading copy is unchanged. de-AT headings are German. Same 13 items. No new FAQ rows.

| EN (primary heading) | DE written on de-AT | heading node |
|---|---|---|
| CAN I MAKE THIS MYSELF WITH AI SOFTWARE? | KANN ICH DAS SELBST MIT KI-SOFTWARE MACHEN? | `4d895fa8-66cd-3e23-13a7-ebb539f59f9c` |
| CAN I USE THIS IF THE MANUFACTURER ONLY ALLOWS OFFICIAL BRAND MATERIAL? | GEHT DAS, WENN DER HERSTELLER NUR OFFIZIELLES MARKENMATERIAL ERLAUBT? | `83039e7b-b200-fdda-9d2f-174f71eefc59` |
| WHAT IS A COMMISSIONED AUTOMOBILE FILM? | WAS IST EIN FAHRZEUGFILM AUF AUFTRAG? | `368b27dc-78b0-b61f-da33-f1098d00a301` |
| WHAT DO I NEED TO PROVIDE? | WAS MUSS ICH LIEFERN? | `ca15bc04-49e0-b415-2d24-3b032601e370` |
| DOES MY AUTOMOBILE NEED TO BE TRANSPORTED? | MUSS MEIN FAHRZEUG TRANSPORTIERT WERDEN? | `58b2ed8d-04a8-b4d5-59f2-8886ef72f2df` |
| DOES MY FILM NEED A COMMERCIAL OBJECTIVE? | BRAUCHT MEIN FILM EIN KOMMERZIELLES ZIEL? | `6360e305-4063-d52e-5d3b-2048c210fb7f` |
| HOW LONG WILL MY FILM TAKE? | WIE LANGE DAUERT MEIN FILM? | `e810c2a3-a2cb-f0db-09b3-c782c48e17d7` |
| WILL MY BRAND GUIDELINES BE FOLLOWED? | WERDEN MEINE MARKENRICHTLINIEN BEACHTET? | `178ab66d-46b6-4aba-6050-5673e6e15c31` |
| IS THE IMAGERY REAL OR GENERATED? | SIND DIE BILDER ECHT ODER ERZEUGT? | `147a4df7-4071-122e-b0c3-0e6b5c1e4450` |
| CAN MY FILM INCLUDE A REAL SHOWROOM, VILLA OR IDENTIFIABLE PERSON? | KANN MEIN FILM EINEN ECHTEN SHOWROOM, EINE VILLA ODER EINE ERKENNBARE PERSON ZEIGEN? | `a8e96439-c1a2-85db-c4a0-f9802ecafb51` |
| CAN I SPECIFY THE NUMBER PLATE, BRANDING AND DELIVERY FORMAT? | KANN ICH KENNZEICHEN, BRANDING UND AUSLIEFERUNGSFORMAT VORGEBEN? | `efa85462-f607-f9cc-2caf-30e070d1790b` |
| WHAT USAGE RIGHTS ARE INCLUDED? | WELCHE NUTZUNGSRECHTE SIND ENTHALTEN? | `51038112-42e7-f285-de32-e1d2e757a556` |
| WILL MY COMMISSIONED FILM BE PUBLISHED? | WIRD MEIN AUFTRAGSFILM VERÖFFENTLICHT? | `9607c924-6490-3458-87d1-c0d71fb15b3d` |

## Publish verification (2026-09-02)

| Check | Result |
|---|---|
| `lastPublished` | `2026-09-02T16:34:37.873Z` (was `2026-09-02T09:23:02.801Z`) |
| de-AT `enabled` | **false** (unchanged). Primary EN also reports `enabled: false` (normal for primary). |
| `https://oleskostudio.com/de-at/` | 301 → `/de-at` → **404** Page not found. English 404 title. |
| `https://oleskostudio.com/` | **200**. Title `OLESKO. Commissioned Films for Exclusive Cars. Generated from Your Images`. `IMPOSSIBLE FILMS`, `smart technology`, `IN ONE WEEK`. No German Home SEO. |
| hreflang | **None** on live EN home. Canonical is `https://oleskostudio.com` only. |
| `sitemap.xml` | **200**, 16 EN locs. **No `/de-at/`**. No xhtml hreflang. |
| Reality | English `BUT IS IT REAL?` still in HTML. CSS `.home_reality_section.u-section.u-theme-light { display: none; }`. |
| Imprint / Privacy | Still English titles. |
| Commission buttons | Still `SEND ENQUIRY` / `SEND BRIEF` / `Please wait...`. |
| CMS | `collections: []`. Not recreated. |
| `llms.txt` | Not written. Site Settings / Designer only. |

## Leftover that blocks `/de-at`

Webflow will not compile a secondary locale until Localize → **Enable publishing to the subdirectory** is on, then publish again. Data API / MCP cannot set `enabled: true`. Designer MCP is disconnected (login required). After that toggle, republish the full site (same domain IDs + subdomain). Then hreflang and sitemap `/de-at/` should appear.

## Leftovers (Designer on de-AT only)

- Language switcher links are in the component. Pairing script sets current + matching hrefs after load.
- Commission submit values still SEND ENQUIRY / SEND BRIEF (verified 2026-09-02). Official Pages Update Content wants `value` + `waitingText` on those submit nodes. MCP `update_static_content` only accepts `text` / `propertyOverrides`, so the write is rejected. `set_settings` on `buttonText` has no localeId and would overwrite live English. Designer is disconnected (login required). On de-AT set `ANFRAGE SENDEN` / `BRIEFING SENDEN` and `Bitte warten...` on:
  - Enquiry `0fc9e301-f2d1-cff1-0e91-2fc4442cdb1c` (`#commission-enquiry-submit`, `type=submit`)
  - Brief `a39ce365-82b8-2a52-a5ae-d47a9ab4712a` (`#commission-brief-submit`, `type=submit`)
  Keep method post, field names, no Lumos overlay, no `commissionformsubmit`.
- Live `hreflang` / sitemap `/de-at/` rows appear after you publish the locale. Do not paste `llms.txt` until then.

## What was not done (on purpose)

- Full site published 2026-09-02T16:34:37.873Z. No CMS publish. Locale publishing still off.
- No new locale created
- No custom-domain changes
- No Google indexing request
- No `/de` folder of duplicate static pages
- No Seedance / Higgsfield on the public site
- No new rem, no new Lumos tokens
- No Films-cms / Posts recreated
- Imprint / Privacy not translated
- Reality section not unhidden
- Live English pages not edited (hreflang is Webflow’s job after publish)

## Page IDs

| Page | id | EN path | DE path |
|---|---|---|---|
| Home | `6a83fdcf46ec1970b6eb307b` | `/` | `/de-at` |
| Collection | `6a8471318afbe9b46708f954` | `/collection` | `/de-at/collection` |
| Commission | `6a8471320e6ee1e88c0037c2` | `/commission` | `/de-at/commission` |
| About | `6a8471331d2d68eb848af612` | `/about` | `/de-at/about` |
| Imprint | `6a8b7dede6239a222989a4f9` | `/imprint` | leave EN |
| Privacy | `6a8b7ded6e9a5fb3c6f8fec9` | `/privacy` | leave EN |
| Let it rain | `6a94a5aa1d755181100606b7` | `/films/let-it-rain-nurburgring-nordschleife` | `/de-at/films/...` |
| The Look of Love | `6a94835baff009655de6bdca` | `/films/the-look-of-love-ferrari-250-gt-california-spyder` | same slug under `/de-at` |
| Riviera Summer Cruise | `6a8b402d69195cfc7d432a59` | `/films/riviera-summer-cruise-aston-martin-db12-volante` | same |
| Alpine Autumn High Pass | `6a8b402d3f30e7ce2c689cec` | `/films/alpine-autumn-high-pass-porsche-992-gt3-touring` | same |
| Along the Sea Wall | `6a8b075dacef99c64dc2ba1d` | `/films/along-the-sea-wall-bentley-continental-gtc` | same |
| On the Flooded Salt | `6a8b402e3f30e7ce2c689d4b` | `/films/on-the-flooded-salt-lamborghini-revuelto` | same |
| At the Louvre | `6a8b402efd4a464888ee176a` | `/films/at-the-louvre-ferrari-250-gto` | same |
| Into the Highland Fog | `6a8b402ffa314513088680ba` | `/films/into-the-highland-fog-mercedes-amg-gt` | same |
| Down the Avenue | `6a8b402fefdad2a541be5cf8` | `/films/down-the-avenue-mercedes-benz-190-sl` | same |
| Mountain Sanctuary | `6a8b4030d04c77b87628e041` | `/films/mountain-sanctuary-mercedes-amg-g-63` | same |

Register: Sie / Ihr Film. Never “ein OLESKO-Film.” Film titles stay English. Mux playback IDs stay. Colors and tokens unchanged.
