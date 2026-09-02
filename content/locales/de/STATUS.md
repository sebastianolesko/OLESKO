# OLESKO German (Austria) locale — applied, unpublished

Sebastian: **nothing is live.** Pack is applied to the existing draft locale. Do not publish. Do not request Google indexing.

Site: `https://oleskostudio.com`  
Site ID: `6a7b43a328ec101a40bb1d20`  
Primary locale: English (`en`, id `6a876663b22843d8b60c22b0`, cmsLocaleId `6a876663b22843d8b60c2297`)  
Secondary: **German (Austria)** (`de-AT`, id `6a983fb4dfdbdb9a5e8b882c`, cmsLocaleId `6a983fb4dfdbdb9a5e8b8831`, subdirectory `de-at`, **enabled: false**)

Last live publish (unchanged): **`2026-09-02T09:23:02.801Z`**. `googleTagIds` empty. `publish_site` was not called.

## Applied (this turn)

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

## FAQ questions (applied on de-AT)

Accordion questions were span + String nodes. Localization MCP strips `<span>`, so those strings could not be written. Each original span still wraps the toggle. Inside it, a localizable `h5.accordion_toggle_text.u-text-style-h5` holds the question. English heading copy is unchanged. de-AT headings are German. Same 13 items. No new FAQ rows.

| EN (primary heading) | DE written on de-AT | heading node |
|---|---|---|
| CAN I MAKE THIS MYSELF WITH AI SOFTWARE? | KANN ICH DAS SELBST MIT KI-SOFTWARE MACHEN? | `4d895fa8-66cd-3e23-13a7-ebb539f59f9c` |
| CAN I USE THIS IF THE MANUFACTURER ONLY ALLOWS OFFICIAL BRAND MATERIAL? | GEHT DAS, WENN DER HERSTELLER NUR OFFIZIELLES MARKENMATERIAL ERLAUBT? | `83039e7b-b200-fdda-9d2f-174f71eefc59` |
| WHAT IS A COMMISSIONED AUTOMOBILE FILM? | WAS IST EIN AUTOMOBILFILM AUF AUFTRAG? | `368b27dc-78b0-b61f-da33-f1098d00a301` |
| WHAT DO I NEED TO PROVIDE? | WAS MUSS ICH LIEFERN? | `ca15bc04-49e0-b415-2d24-3b032601e370` |
| DOES MY AUTOMOBILE NEED TO BE TRANSPORTED? | MUSS MEIN AUTOMOBIL TRANSPORTIERT WERDEN? | `58b2ed8d-04a8-b4d5-59f2-8886ef72f2df` |
| DOES MY FILM NEED A COMMERCIAL OBJECTIVE? | BRAUCHT MEIN FILM EIN KOMMERZIELLES ZIEL? | `6360e305-4063-d52e-5d3b-2048c210fb7f` |
| HOW LONG WILL MY FILM TAKE? | WIE LANGE DAUERT MEIN FILM? | `e810c2a3-a2cb-f0db-09b3-c782c48e17d7` |
| WILL MY BRAND GUIDELINES BE FOLLOWED? | WERDEN MEINE MARKENRICHTLINIEN BEACHTET? | `178ab66d-46b6-4aba-6050-5673e6e15c31` |
| IS THE IMAGERY REAL OR GENERATED? | SIND DIE BILDER ECHT ODER ERZEUGT? | `147a4df7-4071-122e-b0c3-0e6b5c1e4450` |
| CAN MY FILM INCLUDE A REAL SHOWROOM, VILLA OR IDENTIFIABLE PERSON? | KANN MEIN FILM EINEN ECHTEN SHOWROOM, EINE VILLA ODER EINE ERKENNBARE PERSON ZEIGEN? | `a8e96439-c1a2-85db-c4a0-f9802ecafb51` |
| CAN I SPECIFY THE NUMBER PLATE, BRANDING AND DELIVERY FORMAT? | KANN ICH KENNZEICHEN, BRANDING UND AUSLIEFERUNGSFORMAT VORGEBEN? | `efa85462-f607-f9cc-2caf-30e070d1790b` |
| WHAT USAGE RIGHTS ARE INCLUDED? | WELCHE NUTZUNGSRECHTE SIND ENTHALTEN? | `51038112-42e7-f285-de32-e1d2e757a556` |
| WILL MY COMMISSIONED FILM BE PUBLISHED? | WIRD MEIN AUFTRAGSFILM VERÖFFENTLICHT? | `9607c924-6490-3458-87d1-c0d71fb15b3d` |

## Leftovers (Designer on de-AT only)

- Primary header DE is still a **disabled span**, not a locale link. Do not type a fake `/de` or `/de-at` path on live EN until you publish.
- On the DE header, DE is current; EN → `/`. Bottom row still shows both as current until Designer fixes the switcher.
- Commission submit values still SEND ENQUIRY / SEND BRIEF (verified 2026-09-02). Official Pages Update Content wants `value` + `waitingText` on those submit nodes. MCP `update_static_content` only accepts `text` / `propertyOverrides`, so the write is rejected. `set_settings` on `buttonText` has no localeId and would overwrite live English. Designer is disconnected (login required). On de-AT set `ANFRAGE SENDEN` / `BRIEFING SENDEN` and `Bitte warten...` on:
  - Enquiry `0fc9e301-f2d1-cff1-0e91-2fc4442cdb1c` (`#commission-enquiry-submit`, `type=submit`)
  - Brief `a39ce365-82b8-2a52-a5ae-d47a9ab4712a` (`#commission-brief-submit`, `type=submit`)
  Keep method post, field names, no Lumos overlay, no `commissionformsubmit`.
- Live `hreflang` / sitemap `/de-at/` rows appear after you publish the locale. Do not paste `llms.txt` until then.

## What was not done (on purpose)

- No site publish, no CMS publish
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

| Page | id | EN path | DE path (unpublished) |
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
