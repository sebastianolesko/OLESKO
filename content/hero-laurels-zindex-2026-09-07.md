# Desktop hero laurels + section-local soft join

Independent live QA (hard-refresh desktop ~1440) showed the join was still a hard cut into black `#service`, while laurels stayed bright. Translating `.home_service_transition` up into the hero does not paint the join: with service `z-index: auto` the fade sits behind the fixed video, and `u-theme-dark` keeps the section box opaque `#0b0b0c`.

A fixed viewport overlay on the hero is the wrong model. Soft shade stays on `.home_service_transition` inside the second section.

## Paint path that makes the join visible

Desktop `min-width: 768px` only. Phone `70svh` rules stay locked.

1. Keep the hero layer split so laurels stay readable at rest: media `fixed` `z-index: 0`, inner `fixed` `z-index: 25`.
2. `#service` paints above the video: `z-index: 30`, `isolation: isolate`.
3. `#service` background is transparent, so video can show through the top of the section.
4. `.home_service_transition` is section-local: `position: absolute; top: -2px; translate: none; height: calc(68svh + 2px)`. No upward `-100%` translate. No `position: fixed`.
5. Gradient runs down from the section top: transparent → mid stops → `#0b0b0c` over `68svh`.
6. `#service::after` is a solid `#0b0b0c` fill from `68svh` to the section bottom, so the rest of the page is not see-through.
7. `.section_contain` stays above the fade (`z-index: 3`). Desktop `::before` stays off.

At rest the fade sits below the fold, so laurels stay bright. On scroll the section comes over the video and the first `68svh` is a see-through fade.

## Live publish

- `lastPublished`: pending this pass
- `googleTagIds`: `[]`
