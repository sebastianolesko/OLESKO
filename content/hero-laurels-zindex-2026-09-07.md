# Desktop hero laurels + section-local soft join

The hard cut was not a missing 68svh layer. Desktop `.home_service_section::before` painted a solid `#0b0b0c` fill at `z-index: 30` over the service box, so the hero-to-section join was a knife edge. Pinning `.home_service_transition` to the viewport was the wrong model.

## Paint path that makes the join visible

1. Revert `.home_service_transition` to section-local: `position: absolute; top: 0; translate: 0 calc(-100% + 2px); height: 68svh`.
2. Remove the desktop `::before` solid fill (`content: none`).
3. Keep service `overflow: visible` and `z-index: auto` so the translated fade paints over the fixed video (`z-index: 0`) and under the copy (`z-index: 25`).
4. `.section_contain` stays `z-index: 30` so laurels pass under the section body at the join.

Phone `70svh` rules and phone `::before` stay locked.

## Live publish

- `lastPublished`: `2026-09-07T14:00:16.889Z`
- `googleTagIds`: `[]`

Hard-refresh at 1440x900: transition is `position: absolute` with `translate: 0 calc(-100% + 2px)`, `68svh`, not a fixed overlay. Desktop `::before` is `none`. Laurel glyphs at rest mean L `220`. Join luma ramps into `#0b0b0c` over the 68svh band.
