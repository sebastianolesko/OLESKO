# Desktop hero laurels paint order

Added 2026-09-07. Reopened: the tint is on desktop, not phone.

## Cause

`.olesko_hero` is `position: fixed` with `isolation: isolate` and `z-index: 0`. `#service` is `z-index: 30`. `.home_service_transition` is `68svh` and translates up over the hero, so it paints over the laurels at rest.

## Desktop fix (`min-width: 768px`, Home head CSS)

- `.olesko_hero` `z-index: auto` + `isolation: auto` so inner layers can compete
- media `0`, overlay `2`
- inner / copy / laurels `z-index: 25` (no box, no fill, no background)
- `#service` `z-index: auto`
- `.home_service_transition` stays `68svh` with the locked fade, `z-index: 15` (above media, below laurels)
- `.section_contain` `z-index: 30` so the join / next section still covers laurels on scroll

## Phone

Locked fade restored: transition `70svh` and the previous phone stack. Not the target of this fix.

`googleTagIds` left empty. Scripts untouched.
