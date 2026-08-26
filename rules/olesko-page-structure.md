# OLESKO inner page structure (locked)

Read this before building or editing Collection, Commission, film pages, About, or any new inner page. Do not invent a parallel shell.

Collection breaks when the 12-column grid sits directly in the section. The side inset comes from `section_contain` + `u-container`.

## Inner page shell

```
page_wrap + u-theme-dark
  Global Styles
  Global Guides
  OLESKO Global Header
  page_main#main
    olesko_page_section + u-section + u-theme-dark  (#page)
      section_contain + u-container
        olesko_section_grid + u-grid-custom
          intro and/or content
  OLESKO Global Footer
```

`section_contain` + `u-container` is required. Never put `olesko_section_grid` as a direct child of the section.

## Intro band

Copy (eyebrow, H1, supporting text) sits in:

`olesko_section_intro` + `u-grid-subgrid` + `u-column-start-3` + `u-column-span-8`

Do not start inner-page copy at column 1. Do not span 12 columns for intro copy.

## Content placement

- Collection film cards: same as Home. Class `home_service_film_card` + `u-grid-stack` + `u-column-span-6`. Odd cards `u-column-start-1`, even cards `u-column-start-7`. Still sits in a Div `home_service_film_media` (play triangle is `::after` on that class), then `home_service_film_image`, then copy. Do not put the still as a direct child of the card. The whole card is a page link to `/films/{slug}`; do not nest another link inside it.
- Film pages: intro copy in the 8-column band. Mux player and share are siblings of the intro, still inside `section_contain` + `u-container`, full width of that container. Player class `olesko_film_embed`. Never reuse the Home lightbox class `olesko_film_video`.
- Commission: forms stay inside the same grid, in the 8-column band unless Sebastian asks otherwise.

## Do not

- Do not skip `section_contain` + `u-container`.
- Do not add page-top padding on `.olesko_page_section.u-section` globally.
- Do not use Films CMS for public Collection cards.
- Do not publish unless Sebastian asks.

This file is also stored as a Cursor always-on rule (`.cursor/rules/olesko-page-structure.mdc`) and as a Webflow Designer rule (`rules/olesko-page-structure.md`).
