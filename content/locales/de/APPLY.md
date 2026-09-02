# How to apply the DE pack (after locale `de` exists)

Do not publish. Do not enable locale publishing.

1. Designer → Localize → Add locale: tag `de`, subdirectory `de`, publishing **off**.
2. `get_site` on `6a7b43a328ec101a40bb1d20`. Copy the secondary locale `id` into `localeId` in `apply.json` and `seo-schema.json`.
3. `update_component_content` for each entry in `apply.json` → `components`.
4. `update_static_content` for each entry in `apply.json` → `pages`.
5. `bulk_update_pages` / `bulk_update_pages_schema_markup` from `seo-schema.json` with that `localeId`.
6. Designer: convert the **primary** header DE span into a real locale link (MCP cannot edit primary via the localization tool). On DE, EN stays `/`.
7. Designer on the DE locale: set FAQ question spans listed in `STATUS.md`. Set Commission button values `ANFRAGE SENDEN` / `BRIEFING SENDEN` and waiting text `Bitte warten...`.
8. Save. Webflow should emit `hreflang` en ↔ de. Canonical stays the locale URL.
9. Stop. Wait for Sebastian’s publish yes.

Do not paste `/llms.txt` into Site Settings until DE is published. Those `/de/...` rows 404 until then.
