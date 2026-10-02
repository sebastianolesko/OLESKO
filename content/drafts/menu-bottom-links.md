# Draft: global menu bottom links

Do not publish. Do not touch `googleTagIds`. Do not add `G-30WQTE8M3F`.

Replace the three `aria-disabled` spans at the bottom of the global menu with real links. Keep the labels CONTACT, IMPRINT, and PRIVACY. Keep the existing classes so the row stays at 64% opacity, uppercase, with no underline. Global `a` already sets `color: inherit` and `text-decoration: none`. `.olesko_menu_bottom_item:hover` raises opacity to 1.

CONTACT goes to the commission page, the same destination as the commission CTA. The footer Connect item stays `mailto:sebastian@oleskostudio.com`. IMPRINT and PRIVACY match the footer legal links.

The header is shared chrome. Primary locale uses root paths. de-AT uses the locale prefix, the same way the footer already does.

## English

Replace:

```html
<span aria-disabled="true" title="Contact page in preparation" class="olesko_menu_bottom_contact">CONTACT</span>
```

with:

```html
<a href="/commission" class="olesko_menu_bottom_contact olesko_menu_bottom_item">CONTACT</a>
```

Replace:

```html
<span aria-disabled="true" title="Imprint page in preparation" class="olesko_menu_bottom_item">IMPRINT</span> <span aria-disabled="true" title="Privacy page in preparation" class="olesko_menu_bottom_item">PRIVACY</span>
```

with:

```html
<a href="/imprint" class="olesko_menu_bottom_item">IMPRINT</a> <a href="/privacy" class="olesko_menu_bottom_item">PRIVACY</a>
```

## de-AT

Same labels. Locale paths:

```html
<a href="/de-at/commission" class="olesko_menu_bottom_contact olesko_menu_bottom_item">CONTACT</a>
```

```html
<a href="/de-at/imprint" class="olesko_menu_bottom_item">IMPRINT</a> <a href="/de-at/privacy" class="olesko_menu_bottom_item">PRIVACY</a>
```

If one component holds both locales, set the primary links to `/commission`, `/imprint`, and `/privacy`, then set the de-AT link overrides to `/de-at/commission`, `/de-at/imprint`, and `/de-at/privacy`.

Leave the language switcher, the main nav, and the footer as they are.
