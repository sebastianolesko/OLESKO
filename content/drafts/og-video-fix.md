# Draft: og:video on six film pages

Do not publish. Do not touch `googleTagIds`. Do not add `G-30WQTE8M3F`. Do not apply this in Designer in this pass.

Live check on 6 October 2026. Last published still Thu Oct 01 2026 13:12:43 GMT. All 40 Collection film URLs in the sitemap (20 English, 20 de-AT) were fetched. EN and de-AT agree on every slug.

## Verification

`twitter:player` is not the working pattern. Louvre has `og:video` and no `twitter:player`. The same is true of 9 other films. Only Miami Night, Winter Roadster, Amalfi Noon, and Cap Ferrat also have `twitter:player`, `twitter:player:width` `1920`, and `twitter:player:height` `1080`. No page has `twitter:player:stream` or `og:video:url`.

| Film | EN URL | de-AT URL | og:video |
| --- | --- | --- | --- |
| Horsepower | https://oleskostudio.com/films/horsepower-rolls-royce-phantom | https://oleskostudio.com/de-at/films/horsepower-rolls-royce-phantom | no |
| On the Rocks | https://oleskostudio.com/films/on-the-rocks-ferrari-296-gtb | https://oleskostudio.com/de-at/films/on-the-rocks-ferrari-296-gtb | no |
| Closed Roads Racing | https://oleskostudio.com/films/closed-roads-racing-isle-of-man | https://oleskostudio.com/de-at/films/closed-roads-racing-isle-of-man | no |
| Through the Pines | https://oleskostudio.com/films/through-the-pines-lamborghini-revuelto | https://oleskostudio.com/de-at/films/through-the-pines-lamborghini-revuelto | no |
| Desert Storm | https://oleskostudio.com/films/desert-storm-land-rover-defender-110-v8 | https://oleskostudio.com/de-at/films/desert-storm-land-rover-defender-110-v8 | no |
| Arctic Sailing with Orcas | https://oleskostudio.com/films/arctic-sailing-with-orcas-wallywind-110 | https://oleskostudio.com/de-at/films/arctic-sailing-with-orcas-wallywind-110 | no |
| Miami Night | https://oleskostudio.com/films/miami-night-ferrari-daytona-cabriolet | https://oleskostudio.com/de-at/films/miami-night-ferrari-daytona-cabriolet | yes |
| Winter Roadster | https://oleskostudio.com/films/winter-roadster-mercedes-benz-300-sl | https://oleskostudio.com/de-at/films/winter-roadster-mercedes-benz-300-sl | yes |
| Amalfi Noon | https://oleskostudio.com/films/amalfi-noon-bentley-continental-gt-azure | https://oleskostudio.com/de-at/films/amalfi-noon-bentley-continental-gt-azure | yes |
| Cap Ferrat | https://oleskostudio.com/films/cap-ferrat-riva-rivale | https://oleskostudio.com/de-at/films/cap-ferrat-riva-rivale | yes |
| Mountain Sanctuary | https://oleskostudio.com/films/mountain-sanctuary-mercedes-amg-g-63 | https://oleskostudio.com/de-at/films/mountain-sanctuary-mercedes-amg-g-63 | yes |
| Let It Rain | https://oleskostudio.com/films/let-it-rain-nurburgring-nordschleife | https://oleskostudio.com/de-at/films/let-it-rain-nurburgring-nordschleife | yes |
| The Look of Love | https://oleskostudio.com/films/the-look-of-love-ferrari-250-gt-california-spyder | https://oleskostudio.com/de-at/films/the-look-of-love-ferrari-250-gt-california-spyder | yes |
| Riviera Summer Cruise | https://oleskostudio.com/films/riviera-summer-cruise-aston-martin-db12-volante | https://oleskostudio.com/de-at/films/riviera-summer-cruise-aston-martin-db12-volante | yes |
| Alpine Autumn High Pass | https://oleskostudio.com/films/alpine-autumn-high-pass-porsche-992-gt3-touring | https://oleskostudio.com/de-at/films/alpine-autumn-high-pass-porsche-992-gt3-touring | yes |
| Along the Sea Wall | https://oleskostudio.com/films/along-the-sea-wall-bentley-continental-gtc | https://oleskostudio.com/de-at/films/along-the-sea-wall-bentley-continental-gtc | yes |
| On the Flooded Salt | https://oleskostudio.com/films/on-the-flooded-salt-lamborghini-revuelto | https://oleskostudio.com/de-at/films/on-the-flooded-salt-lamborghini-revuelto | yes |
| At the Louvre | https://oleskostudio.com/films/at-the-louvre-ferrari-250-gto | https://oleskostudio.com/de-at/films/at-the-louvre-ferrari-250-gto | yes |
| Into the Highland Fog | https://oleskostudio.com/films/into-the-highland-fog-mercedes-amg-gt | https://oleskostudio.com/de-at/films/into-the-highland-fog-mercedes-amg-gt | yes |
| Down the Avenue | https://oleskostudio.com/films/down-the-avenue-mercedes-benz-190-sl | https://oleskostudio.com/de-at/films/down-the-avenue-mercedes-benz-190-sl | yes |

## Root cause

These are 20 static pages, one Webflow page per film, localized to de-AT. There is no CMS item id on the published HTML, and each film has its own `data-wf-page`. The Mux player and the VideoObject JSON-LD are already filled on the six pages. The playback id is not empty.

Pages that have `og:video` carry this extra block in the page head custom code, after the Mux player script and before the Google Site Tools script:

```html
<meta property="og:video" content="https://player.mux.com/PLAYBACK_ID">
<meta property="og:video:secure_url" content="https://player.mux.com/PLAYBACK_ID">
<meta property="og:video:type" content="text/html">
<meta property="og:video:width" content="1920">
<meta property="og:video:height" content="1080">
<meta property="og:url" content="https://oleskostudio.com/films/SLUG">
```

Louvre uses that block with playback id `Ew5FZhdef02EiwtkpJ768ZJL1N6FKOpfKuyRp1KjpFJI`. The URL is the Mux player page, `text/html`, not `https://stream.mux.com/<id>.m3u8`. Width and height are `1920` and `1080` on every working page except Mountain Sanctuary, which is `2560` and `1440`. `og:video` and `og:video:secure_url` are the same URL. The head block is not localized: a de-AT page repeats the English `og:url` even though its canonical link is the `/de-at/films/` URL.

The six pages have the Mux script and the player, and they do not have this block. `og:url` is missing with `og:video`. That is the same snippet, not a second bug.

## Apply

On each page below, Page settings, Custom code, inside the head tag. Paste the block after the existing Mux player script. Leave the Google Site Tools script alone. One paste on the English page covers de-AT, because that is how Louvre already behaves. Do not add `twitter:player`. Do not publish.

### Horsepower

Page `6abe53a949d68feb10fb388d`. Playback id `s4HulY6x5CJh7SlQpG46fC2S5nXvltXMvkTu5xvtPP4`.

```html
<meta property="og:video" content="https://player.mux.com/s4HulY6x5CJh7SlQpG46fC2S5nXvltXMvkTu5xvtPP4">
<meta property="og:video:secure_url" content="https://player.mux.com/s4HulY6x5CJh7SlQpG46fC2S5nXvltXMvkTu5xvtPP4">
<meta property="og:video:type" content="text/html">
<meta property="og:video:width" content="1920">
<meta property="og:video:height" content="1080">
<meta property="og:url" content="https://oleskostudio.com/films/horsepower-rolls-royce-phantom">
```

### On the Rocks

Page `6abe53aaee0ad8c71b93d254`. Playback id `2nbkAxpkuj3pKT9IuKQPHHSYiDI02R8adVF014l1m01w4c`.

```html
<meta property="og:video" content="https://player.mux.com/2nbkAxpkuj3pKT9IuKQPHHSYiDI02R8adVF014l1m01w4c">
<meta property="og:video:secure_url" content="https://player.mux.com/2nbkAxpkuj3pKT9IuKQPHHSYiDI02R8adVF014l1m01w4c">
<meta property="og:video:type" content="text/html">
<meta property="og:video:width" content="1920">
<meta property="og:video:height" content="1080">
<meta property="og:url" content="https://oleskostudio.com/films/on-the-rocks-ferrari-296-gtb">
```

### Closed Roads Racing

Page `6abe53ab166a2e9d0d3aa8b5`. Playback id `PD02STxY8WJgUxiOqpUm2a28wA01kW0101QWethgc9PbVPg`.

```html
<meta property="og:video" content="https://player.mux.com/PD02STxY8WJgUxiOqpUm2a28wA01kW0101QWethgc9PbVPg">
<meta property="og:video:secure_url" content="https://player.mux.com/PD02STxY8WJgUxiOqpUm2a28wA01kW0101QWethgc9PbVPg">
<meta property="og:video:type" content="text/html">
<meta property="og:video:width" content="1920">
<meta property="og:video:height" content="1080">
<meta property="og:url" content="https://oleskostudio.com/films/closed-roads-racing-isle-of-man">
```

### Through the Pines

Page `6aa13278d6b477ed4a9b6411`. Playback id `eo01Ev202H017vIkaH00fWGDCTVlO1aLfXmnlsRKYrie7fo`.

```html
<meta property="og:video" content="https://player.mux.com/eo01Ev202H017vIkaH00fWGDCTVlO1aLfXmnlsRKYrie7fo">
<meta property="og:video:secure_url" content="https://player.mux.com/eo01Ev202H017vIkaH00fWGDCTVlO1aLfXmnlsRKYrie7fo">
<meta property="og:video:type" content="text/html">
<meta property="og:video:width" content="1920">
<meta property="og:video:height" content="1080">
<meta property="og:url" content="https://oleskostudio.com/films/through-the-pines-lamborghini-revuelto">
```

### Desert Storm

Page `6a9fbe20b53df77a75fa90e2`. Playback id `WFI8Zj2uK00ehpezSjnZHOdjIS1Evdgpg3pCdOIy00BpI`.

```html
<meta property="og:video" content="https://player.mux.com/WFI8Zj2uK00ehpezSjnZHOdjIS1Evdgpg3pCdOIy00BpI">
<meta property="og:video:secure_url" content="https://player.mux.com/WFI8Zj2uK00ehpezSjnZHOdjIS1Evdgpg3pCdOIy00BpI">
<meta property="og:video:type" content="text/html">
<meta property="og:video:width" content="1920">
<meta property="og:video:height" content="1080">
<meta property="og:url" content="https://oleskostudio.com/films/desert-storm-land-rover-defender-110-v8">
```

### Arctic Sailing with Orcas

Page `6a9ed742189f6c70a9f5fe57`. Playback id `ft2ArQE3EXJu3VllHG38bcE3BfELS7rLlieUJvndXM8`.

```html
<meta property="og:video" content="https://player.mux.com/ft2ArQE3EXJu3VllHG38bcE3BfELS7rLlieUJvndXM8">
<meta property="og:video:secure_url" content="https://player.mux.com/ft2ArQE3EXJu3VllHG38bcE3BfELS7rLlieUJvndXM8">
<meta property="og:video:type" content="text/html">
<meta property="og:video:width" content="1920">
<meta property="og:video:height" content="1080">
<meta property="og:url" content="https://oleskostudio.com/films/arctic-sailing-with-orcas-wallywind-110">
```

## Check later, still without treating staging as proof until publish

After the head code is saved, Designer preview on each of the six pages should show the five `og:video` tags plus `og:url`. Live `curl` stays without those tags until a later publish. de-AT should show the same English `og:url` as the English page.
