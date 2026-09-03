# How to apply the DE pack (German Austria, unpublished)

Full site was published 2026-09-02T16:34:37.873Z. de-AT is still `enabled: false`, so `/de-at` 404s. Enable publishing on that locale in Localize, then publish again. Do not create a locale.

Existing secondary locale (do not recreate):

- displayName: German (Austria)
- locale id: `6a983fb4dfdbdb9a5e8b882c`
- cmsLocaleId: `6a983fb4dfdbdb9a5e8b8831`
- tag: `de-AT` (not `de`)
- subdirectory: `de-at` (not `de`)
- enabled: false

1. `get_site` on `6a7b43a328ec101a40bb1d20`. Confirm the IDs above. Do not add a locale.
2. `update_component_content` for each entry in `apply.json` → `components` with that `localeId`.
3. `update_static_content` for each entry in `apply.json` → `pages` with that `localeId`. Skip Imprint and Privacy.
4. `bulk_update_pages` / `bulk_update_pages_schema_markup` from `seo-schema.json` with that `localeId`. All canonicals, og:url, JSON-LD `url`, and hreflang use `/de-at/` and `de-AT`.
5. Language switcher is already real links in the header component (EN `/`, DE `/de-at`) plus footer script `oleskolangpair`. Do not put DE back to a disabled span. Commission submit buttons stay SEND ENQUIRY / SEND BRIEF.
6. Canonical stays the locale URL under `/de-at/`.
7. Full-site publish uses domain IDs for apex + www, plus the Webflow subdomain.

Do not paste `/llms.txt` into Site Settings until DE is published. Those `/de-at/...` rows 404 until then.
