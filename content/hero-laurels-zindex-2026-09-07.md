# Desktop hero laurels paint order

Added 2026-09-07. Reopened: the tint is on desktop, not phone.

## Cause

`.olesko_hero` is `position: fixed`. That creates a root stacking context, so raising `.olesko_hero_inner` to `z-index: 25` cannot lift copy above `.home_service_transition` (`68svh`, paints over the hero). Class z-index inside the hero is not enough.

## Desktop fix (`min-width: 768px`, Home head CSS)

Break the hero into independent viewport layers. Phone rules stay locked.

```css
@media screen and (min-width: 768px) {
  .olesko_hero {
    position: relative !important;
    inset: auto !important;
    height: 0 !important;
    min-height: 0 !important;
    overflow: visible !important;
    z-index: auto !important;
    isolation: auto !important;
    transform: none !important;
    filter: none !important;
  }
  .olesko_hero_media {
    position: fixed !important;
    inset: 0 !important;
    z-index: 0 !important;
  }
  .olesko_hero_overlay {
    position: fixed !important;
    inset: 0 !important;
    z-index: 2 !important;
  }
  .olesko_hero_inner {
    position: fixed !important;
    inset: 0 !important;
    z-index: 25 !important;
    isolation: isolate;
    pointer-events: none;
  }
  .olesko_hero_inner a,
  .olesko_hero_inner button {
    pointer-events: auto;
  }
  .page_main > section.home_service_section:not(.olesko_hero) {
    z-index: auto;
  }
  .home_service_transition,
  .home_service_transition:lang(de-at) {
    z-index: 15 !important;
    height: 68svh !important;
    background-image: linear-gradient(180deg, rgba(11, 11, 12, 0), #0b0b0c) !important;
  }
  .home_service_section::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 30;
    background-color: inherit;
    pointer-events: none;
  }
  .home_service_section > .section_contain {
    position: relative;
    z-index: 30;
  }
}
```

Required desktop stack, live at 1440x900:

1. video / media `position: fixed; z-index: 0`
2. `.home_service_transition` `68svh` (`612px`, `z-index: 15`, top 290 to 902) under the laurels
3. `.olesko_hero_inner` `position: fixed; z-index: 25` (copy + laurels, no box or fill)
4. `.section_contain` `z-index: 30` covers laurels at the join

## Live publish

- `lastPublished`: `2026-09-07T12:49:48.818Z`
- `googleTagIds`: `[]`
- Phone `70svh` fade unchanged

## Desktop pixel QA (1440x900)

Rest, bright pixels only (`L >= 180`):

- header mean L `200.0` RGB `(200, 200, 199)`
- H1 mean L `218.6` RGB `(220, 219, 214)`
- laurels mean L `220.1` RGB `(224, 220, 212)`
- video bottom edge mean L `13.2` (shade still tints the media)

Before this split, laurel luma sat around `13` to `15`.

At the join (`#service` contain top `706` to `780`), the laurel band has no remaining bright pixels. The next section covers them.
