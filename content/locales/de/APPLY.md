# How to apply the DE pack (German Austria, unpublished)

Do not publish. Do not enable locale publishing. Do not create a locale.

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
5. Designer on **de-AT only** (do not overwrite EN): convert the primary header DE span into a real locale link. On DE, EN stays `/`. FAQ questions are already German on the h5 nodes in `STATUS.md`. Set Commission button values `ANFRAGE SENDEN` / `BRIEFING SENDEN` and waiting text `Bitte warten...` (`value` / `waitingText` on the native submit nodes).
6. Save. Webflow should emit `hreflang` en ↔ de-AT after a Designer save. Canonical stays the locale URL under `/de-at/`.
7. Stop. Wait for Sebastian’s publish yes. Do not call `publish_site`.

Do not paste `/llms.txt` into Site Settings until DE is published. Those `/de-at/...` rows 404 until then.
