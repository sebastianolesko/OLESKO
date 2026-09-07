# Desktop hero revert: content scrolls over the hero

Locked diagnosis (live CSS, lastPublished `2026-09-07T14:34:03.374Z`): desktop `@media (min-width: 768px)` had forced `.olesko_hero` `height: 0` and `.olesko_hero_media` / `_overlay` / `_inner` to `position: fixed` with inner `z-index: 25`. H1 and laurels stayed pinned while `#service` scrolled under them.

## One fix

Deleted that rewrite. Desktop is back to the pre-thrash model:

- Hero shell `position: fixed; inset: 0; z-index: 0` (full viewport). Not `height: 0`.
- Page sections `position: relative; z-index: 30` so content scrolls over the hero.
- `#service` opaque `#0B0B0C`.
- Soft join kept on `.home_service_transition` (absolute, `68svh`, `translate: 0 calc(-100% + 2px)`). The join ramp stays clear through the laurel band so the z-30 overlay does not wash the glyphs.
- Within the hero only: `.olesko_hero_inner` (`relative`, `z-index: 3`) sits above `.olesko_hero_media::after` (`z-index: 2`, `68svh` 3-stop fade). Media, overlay, and inner are not viewport-fixed.
- Phone `max-width: 767` / `479` rules were not edited.

## Inject proof (1440 x 900, before publish)

- Hero `position: fixed`, `z-index: 0`, height `900px`. Inner `relative` / `3`. Media `absolute` (not fixed).
- Transition `absolute`, `translate: 0 calc(-100% + 2px)`, height `612px`.
- Service `relative` / `30`, background `rgb(11, 11, 12)`.
- Rest laurel glyphs max L `232.5`, L>200 count `1222` (matches the prior readable live rest).
- Soft join: rest gutter darkens through the lower hero; at scroll 280 the lower viewport is flat L `11.1`.
- At scroll 900, `elementFromPoint` on the rest H1/laurel boxes hits `#service` title / film grid. Rest-position luma is L `11.1`. Copy does not stay pinned.

## Live publish

- `lastPublished`: `2026-09-07T14:56:45.558Z`
- `googleTagIds`: `[]`

Hard-refresh desktop 1440, no injected CSS: rewrite gone (`height: 0` / `z-index: 25` absent). Hero `fixed` / `0`, height `900px`. Inner `relative` / `3`. Media `absolute`. Service `relative` / `30`, bg `rgb(11, 11, 12)`. Transition `absolute`, `translate: 0 calc(-100% + 2px)`, `612px`. Rest laurel glyphs max L `232.5`, L>200 count `1215`. Gutter ramps `68 → 14` into the join. At scroll 280 the lower viewport is flat L `11.1`. At scroll 900, rest H1/laurel positions are L `11.1` and `elementFromPoint` hits `#service` title / film grid.
