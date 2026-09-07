# Recommended films trio on film pages

Added 2026-09-07. Live on every film page (EN + de-AT).

## Placement

After `#page` (player / disclaimer / share) and before `OLESKO Commission CTA`.

```
page_main#main
  #page  (olesko_page_section)
  OLESKO Recommended Films
  OLESKO Commission CTA
```

## Component

- Name: `OLESKO Recommended Films`
- ID: `2e30479a-3f5e-1f60-0b4c-44fce20f2be6`
- Section `id="recommended"`, aria-label `Recommended films`
- Shell: `olesko_page_section` + `u-section` + `u-theme-dark` → `section_contain` + `u-container` → `olesko_section_grid` + `u-grid-custom`
- Intro: `olesko_section_intro` + `u-grid-subgrid` + `u-column-start-3` + `u-column-span-8`

## Exact trio (always all three, this order)

1. Cap Ferrat — slug `cap-ferrat-riva-rivale` — page `6a9d7d4ff12ffea9f6d5cfcb`
2. The Look of Love — slug `the-look-of-love-ferrari-250-gt-california-spyder` — page `6a94835baff009655de6bdca`
3. Mountain Sanctuary — slug `mountain-sanctuary-mercedes-amg-g-63` — page `6a8b4030d04c77b87628e041`

If the current page is one of the three, still show all three. No fourth substitute.

Cards reuse Collection language: whole-card `Link.home_service_film_card` (no nested link). Still in `home_service_film_media` then `home_service_film_image`. Layout: card 1 start-1 span-6, card 2 start-7 span-6, card 3 start-1 span-6. Links are Webflow page links so they locale-pair (`/films/...` and `/de-at/films/...`).

## Copy

EN eyebrow: `RECOMMENDED`. CTA: `WATCH THE FILM`.

- Cap Ferrat: `RIVA RIVALE · CAP FERRAT` / `CAP FERRAT.`
- The Look of Love: `FERRARI 250 GT CALIFORNIA SPYDER · LAKE COMO` / `THE LOOK OF LOVE.`
- Mountain Sanctuary: `MERCEDES-AMG G 63 · MOUNTAINS` / `MOUNTAIN SANCTUARY.`

de-AT eyebrow: `EMPFOHLEN`. CTA: `FILM ANSEHEN`.

- Cap Ferrat eyebrow unchanged
- The Look of Love: `FERRARI 250 GT CALIFORNIA SPYDER · COMER SEE`
- Mountain Sanctuary: `MERCEDES-AMG G 63 · BERGE`

## Locks

No em/en dashes. Reality hidden. Commission buttons English. `googleTagIds` empty. H1/hero fades untouched. Breadcrumbs and language switcher unchanged.
