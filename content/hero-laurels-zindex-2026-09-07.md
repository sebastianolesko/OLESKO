# Desktop soft join + opaque section 2 + readable laurels

Locked desktop stack. Phone CSS was not touched.

`.home_service_transition` is section-local: `position: absolute` on `#service`, `68svh`, `translate: 0 calc(-100% + 2px)`, gradient `transparent → 0.45 at 72% → #0b0b0c`. `#service` is opaque `#0b0b0c`. Service `z-index` is `auto` so the fade at `15` sits above the video (`0`) and under the laurels (`25`). No fixed bottom overlay.

## Live publish

- `lastPublished`: `2026-09-07T14:34:03.374Z`
- `googleTagIds`: `[]`

Hard-refresh desktop 1440, no injected CSS: fade is `absolute`, `translate: 0 calc(-100% + 2px)`, `612px`, `z-index: 15`. Service bg `rgb(11, 11, 12)`. Rest laurel glyphs mean L `219`. Rest gutter darkens from ~89 to ~15 over the lower hero. Join at scroll 280 ramps into flat L `11.1` at the section box. Deep section 2 stays L `11.1`.
