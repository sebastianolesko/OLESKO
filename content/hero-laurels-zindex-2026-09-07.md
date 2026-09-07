# Desktop join matches mobile softness

Desktop `.home_service_transition` now uses the same soft stops as mobile. The 80%/92% hard ramp is gone.

## Desktop CSS (`min-width: 768px` only)

```css
.home_service_transition,
.home_service_transition:lang(de-at) {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  z-index: 3;
  height: 70svh;
  translate: 0 calc(-100% + 2px);
  pointer-events: none;
  background-image: linear-gradient(180deg, rgba(11, 11, 12, 0), rgba(11, 11, 12, 0.45) 72%, #0b0b0c);
}
```

Kept: hero shell `fixed` / `z-index: 0`, page sections `z-index: 30` (content scrolls over the hero), `#service` opaque `#0B0B0C`. Phone `max-width: 767` / `479` rules were not edited.

## Inject proof (1440, before publish)

Transition computed: height `630px` (`70svh`), `linear-gradient(rgba(11, 11, 12, 0), rgba(11, 11, 12, 0.45) 72%, rgb(11, 11, 12))`. No 80%/92%. Hero `fixed` / `0`. Inner `relative`. Service `relative` / `30`, bg `rgb(11, 11, 12)`. At scroll 900, `elementFromPoint` hits `#service` title / film grid.
