# Phone hero laurels z-index

Added 2026-09-07. Stack only. Laurel look unchanged (no box, no fill, no background).

## Problem

The mobile soft fade on `.olesko_hero_media::after` (transparent to `#0B0B0C`) painted over the phone laurels.

## Stack

Unchanged:

- `.olesko_hero_media` `z-index: 0`
- `.olesko_hero_media::after` (small) `z-index: 2`
- `.olesko_hero_overlay` `z-index: 2`
- `.olesko_hero_inner` `z-index: 3` desktop / `4` small
- `.home_service_transition` `z-index: 3`

Changed:

- `.olesko_hero_laurels` `z-index: 3` on small and tiny (already `position: relative`)

Laurels sit above the new hero shade (`::after` at 2) and stay below the transition shade (3), because `.olesko_hero` uses `isolation: isolate` so in-hero layers cannot rise above the next-section transition.

Desktop transition fade is untouched. `googleTagIds` left empty.
