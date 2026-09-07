# Desktop hero laurels + soft fade

Added 2026-09-07. Desktop scope.

## Cause

The readable-laurels split kept `.home_service_transition` as `position: absolute` on `#service` with `translate` up. Copy stayed above the shade, but the join read as a hard cut instead of the locked 68svh soft fade.

## Desktop fix (`min-width: 768px`, Home head CSS)

Keep the split stack. Pin the locked fade to the viewport between media and copy.

```css
.olesko_hero_media { position: fixed; z-index: 0; }
.olesko_hero_overlay { position: fixed; z-index: 2; }
.home_service_transition {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 15;
  height: 68svh;
  translate: none;
  background-image: linear-gradient(180deg, rgba(11, 11, 12, 0), rgba(11, 11, 12, 0.45) 72%, #0b0b0c);
}
.olesko_hero_inner { position: fixed; z-index: 25; }
.home_service_section > .section_contain { z-index: 30; }
```

No box, fill, or background on the laurels.

## Phone

Unchanged: transition `70svh` and the existing phone stack.

## Live publish

- `lastPublished`: `2026-09-07T13:27:46.806Z`
- `googleTagIds`: `[]`

## Desktop QA at 1440x900

Computed: `.home_service_transition` is `position: fixed`, `z-index: 15`, `68svh` (`288` to `900`), 3-stop `#0b0b0c` gradient. Inner / laurels `z-index: 25`.

Bright pixels (`L >= 180`): header `200` · H1 `218.1` · laurels `220.0`. No box or fill on the laurels.
