# Desktop hero laurels + soft join + opaque section 2

The soft `.home_service_transition` gradient stays. Section 2 was see-through because `#service` was transparent and the solid fill started at `68svh`, so service copy sat over the hero video.

## Paint path

Desktop `min-width: 768px` only. Phone `70svh` rules stay locked.

1. Hero split unchanged: media `fixed` `z-index: 0`, inner `fixed` `z-index: 25`. Laurels stay readable at rest.
2. `#service` stays `z-index: 30` so the join fade paints over the video.
3. Soft shade stays on `.home_service_transition`: `position: absolute`, no `translate -100%`, height `68svh`.
4. Opaque `#0b0b0c` starts at `5.5rem` (the section_contain padding): section `background-image` fill plus `::before` behind content. The top of the section stays a see-through join. Service copy sits on solid black.

## Live publish

- `lastPublished`: `2026-09-07T14:22:16.789Z`
- `googleTagIds`: `[]`

Hard-refresh desktop 1440: fade is `position: absolute`, `translate: none`, `68svh`. `::before` is `#0b0b0c` from `5.5rem`. Rest laurel glyphs mean L `219`. Join gutter ramps then goes flat L `11.1`. Deep section 2 gutter is L `11.1` with no video showing through.
