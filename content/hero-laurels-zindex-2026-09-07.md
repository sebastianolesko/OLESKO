# Phone hero laurels paint order

Added 2026-09-07. Reopened after z-index 3 failed visual QA.

## Cause

Class z-index on `.olesko_hero_laurels` was not the paint winner.

Home page head CSS pinned `.olesko_hero` and, on phone, set `isolation: auto` plus `.home_service_transition { height: 70svh !important }`. That transition is a later sibling with `z-index: 3` and `pointer-events: none`, so it veiled the laurels at rest. The media `::after` shade was already under `.olesko_hero_inner`.

## Fix (stack / structure only)

Home head CSS, `max-width: 767px` and `479px`:

- `.olesko_hero` `z-index: 0` + `isolation: isolate` so `::after` stays inside media
- `.olesko_hero_media` `0`
- `.olesko_hero_media::after` `2` (fade look unchanged)
- `.olesko_hero_overlay` `2`
- `.olesko_hero_inner`, `.olesko_hero_content`, `.olesko_hero_laurels` `4`
- `.home_service_transition` height `8svh !important` (join only). Same gradient recipe.
- Removed the phone `z-index: auto` / `isolation: auto` overrides so `#service` stays `z-index: 30` and covers laurels only at the join

Desktop `@media (min-width: 768px)` stays `68svh` with the locked soft fade.

Designer: `.home_service_transition` small height `8svh`. Laurels small/tiny `z-index: 4`. No box, no fill, no background on laurels.

`googleTagIds` left empty. Scripts untouched.
