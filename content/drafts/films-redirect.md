# Draft: /films to /collection

Do not publish. Do not touch `googleTagIds`. Do not add `G-30WQTE8M3F`.

Live check on 2 October 2026, last published Thu Oct 01 2026 13:12:43 GMT:

- `GET /films` is 404 (site 404 page `6a7b43a528ec101a40bb1dae`)
- `GET /films/` is already a 301 to `/films`
- `GET /de-at/films` is the same 404
- `GET /watch` is the same 404. Leave `/watch` unpublished. Do not create it.
- `GET /contact` is the same 404. There is no redirect to `/commission`. Leave `/contact` alone.

Add exact 301 redirects in Webflow (Site settings, Publishing, 301 redirects). Exact paths only. A wildcard on `/films` would send the twenty film pages away.

| From | To | Status |
| --- | --- | --- |
| `/films` | `/collection` | 301 |
| `/de-at/films` | `/de-at/collection` | 301 |

`/films/` can stay as the existing slash redirect. It will land on `/films`, then on `/collection`.

These rules take effect on the next publish. Do not publish in this pass.
