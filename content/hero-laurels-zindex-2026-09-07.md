# Desktop hero laurels + soft join + opaque section 2

Live QA: the soft `.home_service_transition` gradient is visible and stays. Section 2 was see-through because `#service` was `background-color: transparent` and the solid fill started at `68svh`, so service copy sat in the fade over the hero video.

## Paint path

Desktop `min-width: 768px` only. Phone `70svh` rules stay locked.

1. Hero split unchanged: media `fixed` `z-index: 0`, inner `fixed` `z-index: 25`. Laurels stay readable at rest.
2. `#service` stays `z-index: 30` so the join fade paints over the video.
3. Soft shade stays on `.home_service_transition`: `position: absolute`, no `translate -100%`, height `68svh`.
4. Opaque `#0b0b0c` starts `16svh` into the section: section `background-image` fill plus `::before` behind content. The first `16svh` stays a see-through join. Service copy sits on solid black.

## Live publish

- `lastPublished`: pending this pass
- `googleTagIds`: `[]`
