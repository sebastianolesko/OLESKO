# Desktop soft join + opaque section 2 + readable laurels

Locked desktop stack. Phone CSS is not touched.

The 5.5rem opaque fill sat on top of `.home_service_transition` and removed the visible join. The fade is section-local again: absolute on `#service`, `68svh`, `translate: 0 calc(-100% + 2px)`, so it paints over the hero video at the join. `#service` is opaque `#0b0b0c` from the section box down. Service `z-index` is `auto` so the fade at `15` sits above the video (`0`) and under the laurels (`25`).

## Live publish

- `lastPublished`: pending one publish after a hard-refresh desktop proof
- `googleTagIds`: `[]`
