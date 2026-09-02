#!/usr/bin/env python3
"""Build unpublished DE apply.json + seo-schema.json for OLESKO Localization."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
SITE = "6a7b43a328ec101a40bb1d20"
LOCALE_ID = "6a983fb4dfdbdb9a5e8b882c"
CMS_LOCALE_ID = "6a983fb4dfdbdb9a5e8b8831"
LOCALE_TAG = "de-AT"
LOCALE_SUBDIR = "de-at"
LOCALE_PLACEHOLDER = LOCALE_ID

DISCLOSURE = (
    "Dieser Film enthält künstlich erzeugte oder KI-bearbeitete Bilder, "
    "in einer persönlich verantworteten Produktion."
)


def n(node_id: str, text: str) -> dict:
    return {"nodeId": node_id, "text": text}


def ov(node_id: str, props: list[tuple[str, str]]) -> dict:
    return {
        "nodeId": node_id,
        "propertyOverrides": [{"propertyId": pid, "text": txt} for pid, txt in props],
    }


header_nodes = [
    n(
        "8483c993-5b9b-373b-10ca-350451e6a75e",
        '<a class="olesko_skip_link" href="#main">Zum Hauptinhalt springen</a>',
    ),
    n(
        "881a26d8-3f1e-e90c-0186-847d7679f289",
        '<div class="olesko_header_language">'
        '<a class="olesko_header_language_item" href="/" data-w-id="881a26d8-3f1e-e90c-0186-847d7679f28a">EN</a>'
        '<span class="olesko_header_language_separator" data-w-id="570e69bf-6693-b7f6-8c0f-d9153113faa8">/</span>'
        '<a class="olesko_header_language_item" href="/de-at" data-w-id="dd7ac7c5-345c-2049-115e-57514581294c">DE</a>'
        "</div>",
    ),
    n(
        "8845307e-ac3d-5d32-1e0b-83cc53b83a8d",
        '<p id="olesko-menu-title" class="nav_screen-reader-text">Seitennavigation</p>',
    ),
    n(
        "881a26d8-3f1e-e90c-0186-847d7679f299",
        '<div class="olesko_menu_language">'
        '<a class="olesko_header_language_item" href="/" data-w-id="881a26d8-3f1e-e90c-0186-847d7679f29a">EN</a>'
        '<span class="olesko_header_language_separator" data-w-id="8fecbd68-a299-72a9-b980-3ceb2beb530a">/</span>'
        '<a class="olesko_header_language_item" href="/de-at" data-w-id="fc070936-6271-7b7e-8dac-fe8de3dcd478">DE</a>'
        "</div>",
    ),
    n(
        "881a26d8-3f1e-e90c-0186-847d7679f2a3",
        '<a class="olesko_menu_link u-text-style-h2" data-wf-link-page-id="6a83fdcf46ec1970b6eb307b">START</a>',
    ),
    n(
        "881a26d8-3f1e-e90c-0186-847d7679f2a6",
        '<a class="olesko_menu_link u-text-style-h2" data-wf-link-page-id="6a8471318afbe9b46708f954">KOLLEKTION</a>',
    ),
    n(
        "881a26d8-3f1e-e90c-0186-847d7679f2a9",
        '<a class="olesko_menu_link u-text-style-h2" data-wf-link-page-id="6a8471320e6ee1e88c0037c2">AUFTRAG</a>',
    ),
    n(
        "881a26d8-3f1e-e90c-0186-847d7679f2ac",
        '<a class="olesko_menu_link u-text-style-h2" data-wf-link-page-id="6a8471331d2d68eb848af612">ÜBER</a>',
    ),
    n(
        "0d488183-5fa9-8d2b-d025-f0bcb735f0c3",
        '<div class="olesko_menu_bottom_languages">'
        '<a class="olesko_menu_bottom_item" href="/" data-w-id="0d488183-5fa9-8d2b-d025-f0bcb735f0c0">ENGLISH</a>'
        '<a class="olesko_menu_bottom_item olesko_menu_bottom_item_current" href="/de-at" data-w-id="7410d705-9d60-5936-d7be-706b6a6efd79">DEUTSCH</a>'
        "</div>",
    ),
    # IMPRINT / PRIVACY stay English on purpose.
]

footer_nodes = [
    n(
        "c71826be-a2bb-fee5-bd98-26dfc1070f9d",
        "<p>Beauftragte visuelle Arbeiten für außergewöhnliche Automobile.</p>",
    ),
    n(
        "c71826be-a2bb-fee5-bd98-26dfc1070f9f",
        "<p>Wien, Österreich · Internationale Aufträge.</p>",
    ),
    n(
        "c71826be-a2bb-fee5-bd98-26dfc1070fa2",
        '<h2 id="footer-explore-title" class="olesko_footer_heading">Entdecken</h2>',
    ),
    n(
        "c71826be-a2bb-fee5-bd98-26dfc1070fa6",
        '<a class="olesko_footer_link" data-wf-link-page-id="6a83fdcf46ec1970b6eb307b">Start</a>',
    ),
    n(
        "c71826be-a2bb-fee5-bd98-26dfc1070fa9",
        '<a class="olesko_footer_link" data-wf-link-page-id="6a8471318afbe9b46708f954">Kollektion</a>',
    ),
    n(
        "c71826be-a2bb-fee5-bd98-26dfc1070fac",
        '<a class="olesko_footer_link" data-wf-link-page-id="6a8471320e6ee1e88c0037c2">Auftrag</a>',
    ),
    n(
        "c71826be-a2bb-fee5-bd98-26dfc1070faf",
        '<a class="olesko_footer_link" data-wf-link-page-id="6a8471331d2d68eb848af612">Über</a>',
    ),
    n("c71826be-a2bb-fee5-bd98-26dfc1070fb2", '<h2 class="olesko_footer_heading">Verbinden</h2>'),
    n(
        "c71826be-a2bb-fee5-bd98-26dfc1070fbe",
        '<li><a class="olesko_footer_link" href="#" data-w-id="a5b27790-5197-0868-5864-52ae5554f41c">Kontakt</a></li>',
    ),
]

cta_nodes = [
    n(
        "f343f630-2311-818c-25f1-2120a8f0ef1f",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">IHR FILM BEGINNT HIER</p>',
    ),
    n(
        "f343f630-2311-818c-25f1-2120a8f0ef21",
        '<h2 id="commission-title" class="olesko_section_grid_item u-text-style-h2">IHR FILM.</h2>',
    ),
    n(
        "f343f630-2311-818c-25f1-2120a8f0ef23",
        '<p class="home_commission_copy u-text-style-main u-color-faded">'
        "Beginnen Sie mit einer kurzen persönlichen Anfrage, oder bereiten Sie ein genaues Briefing "
        "zu Automobil, Zweck und Anforderungen vor. Jede Anfrage wird persönlich in Wien gelesen."
        "</p>",
    ),
    n(
        "f343f630-2311-818c-25f1-2120a8f0ef25",
        '<a class="olesko_cta u-column-span-full" data-wf-link-page-id="6a8471320e6ee1e88c0037c2">'
        '<span data-w-id="f343f630-2311-818c-25f1-2120a8f0ef26">AUFTRAG ANSEHEN</span>'
        '<span data-w-id="f343f630-2311-818c-25f1-2120a8f0ef28">→</span></a>',
    ),
]

disclaimer_nodes = [
    n(
        "8b4e95eb-fc30-c6aa-df8c-80e377a2c390",
        '<p class="olesko_film_copy u-color-faded">'
        "OLESKO ist nicht gesponsert, verbunden, genehmigt, empfohlen oder affiliert mit einem "
        "hier genannten oder gezeigten Fahrzeughersteller. Namen, Zeichen und Modellangaben "
        "sind nur beschreibend, um die Automobile zu benennen, die die Konzeptarbeit angeregt haben."
        "</p>",
    ),
    n(
        "3901362d-b8ec-4041-8f38-b97d19342db1",
        '<p class="olesko_film_copy u-color-faded">'
        "Das ist originale Konzeptarbeit. Sie zeigt kein bestimmtes reales Fahrzeug, keinen "
        "Besitzer und kein Inserat. Ähnlichkeiten mit einem konkreten Auto, einer Person oder "
        "einem Ort sind zufällig."
        "</p>",
    ),
]

home_nodes = [
    n(
        "5b3c7b25-e77b-cfe4-245d-1e1676ee0df7",
        '<h1 class="olesko_hero_title u-text-style-h2">'
        '<p class="nav_screen-reader-text" data-w-id="e294f67f-35b1-d906-60d4-c569e84b2c65">OLESKO. </p>'
        "UNMÖGLICHE FILME FÜR AUSSERGEWÖHNLICHE AUTOMOBILE</h1>",
    ),
    n(
        "5b3c7b25-e77b-cfe4-245d-1e1676ee0df9",
        '<a class="olesko_cta u-pointer-on" data-wf-link-page-id="6a8471320e6ee1e88c0037c2">'
        '<span data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0dfa">FILM BEAUFTRAGEN</span>'
        '<span data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0dfc">→</span></a>',
    ),
    n(
        "5b3c7b25-e77b-cfe4-245d-1e1676ee0dff",
        '<li class="olesko_hero_laurel">'
        '<span class="olesko_hero_laurel_side" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e00">'
        '<img src="https://s3.amazonaws.com/webflow-prod-assets/6a7b43a328ec101a40bb1d20/6a7b646b03d3b1363eea29cc_olesko-laurel-left.svg" loading="lazy" width="auto" height="auto" alt="__wf_reserved_inherit" class="olesko_hero_laurel_branch" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e01">'
        "</span> "
        '<span class="olesko_hero_laurel_copy" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e03">'
        '<span class="olesko_hero_laurel_line" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e04">PERSÖNLICH</span>'
        '<span class="olesko_hero_laurel_line_subdued" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e06">GEMACHT FÜR JEDES</span>'
        '<span class="olesko_hero_laurel_line_subdued" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e08">AUTOMOBIL</span></span>'
        '<span class="olesko_hero_laurel_side" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e0a">'
        '<img src="https://s3.amazonaws.com/webflow-prod-assets/6a7b43a328ec101a40bb1d20/6a7b646b460c187d667116b7_olesko-laurel-right.svg" loading="lazy" width="auto" height="auto" alt="__wf_reserved_inherit" class="olesko_hero_laurel_branch" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e0b">'
        "</span></li>",
    ),
    n(
        "5b3c7b25-e77b-cfe4-245d-1e1676ee0e0c",
        '<li class="olesko_hero_laurel">'
        '<span class="olesko_hero_laurel_side" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e0d">'
        '<img src="https://s3.amazonaws.com/webflow-prod-assets/6a7b43a328ec101a40bb1d20/6a7b646b03d3b1363eea29cc_olesko-laurel-left.svg" loading="lazy" width="auto" height="auto" alt="__wf_reserved_inherit" class="olesko_hero_laurel_branch" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e0e">'
        "</span> "
        '<span class="olesko_hero_laurel_copy" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e10">'
        '<span class="olesko_hero_laurel_line" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e11">30+ JAHRE</span>'
        '<span class="olesko_hero_laurel_line_subdued" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e13">ÜBER MARKE UND</span>'
        '<span class="olesko_hero_laurel_line_subdued" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e16">VISUELLES DESIGN</span></span>'
        '<span class="olesko_hero_laurel_side" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e18">'
        '<img src="https://s3.amazonaws.com/webflow-prod-assets/6a7b43a328ec101a40bb1d20/6a7b646b460c187d667116b7_olesko-laurel-right.svg" loading="lazy" width="auto" height="auto" alt="__wf_reserved_inherit" class="olesko_hero_laurel_branch" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e19">'
        "</span></li>",
    ),
    n(
        "5b3c7b25-e77b-cfe4-245d-1e1676ee0e1a",
        '<li class="olesko_hero_laurel">'
        '<span class="olesko_hero_laurel_side" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e1b">'
        '<img src="https://s3.amazonaws.com/webflow-prod-assets/6a7b43a328ec101a40bb1d20/6a7b646b03d3b1363eea29cc_olesko-laurel-left.svg" loading="lazy" width="auto" height="auto" alt="__wf_reserved_inherit" class="olesko_hero_laurel_branch" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e1c">'
        "</span> "
        '<span class="olesko_hero_laurel_copy" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e1e">'
        '<span class="olesko_hero_laurel_line" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e1f">WIEN</span>'
        '<span class="olesko_hero_laurel_line_subdued" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e21">INTERNATIONALE</span>'
        '<span class="olesko_hero_laurel_line_subdued" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e23">AUFTRÄGE</span></span>'
        '<span class="olesko_hero_laurel_side" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e25">'
        '<img src="https://s3.amazonaws.com/webflow-prod-assets/6a7b43a328ec101a40bb1d20/6a7b646b460c187d667116b7_olesko-laurel-right.svg" loading="lazy" width="auto" height="auto" alt="__wf_reserved_inherit" class="olesko_hero_laurel_branch" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e26">'
        "</span></li>",
    ),
    n(
        "5b3c7b25-e77b-cfe4-245d-1e1676ee0e27",
        '<li class="olesko_hero_laurel">'
        '<span class="olesko_hero_laurel_side" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e28">'
        '<img src="https://s3.amazonaws.com/webflow-prod-assets/6a7b43a328ec101a40bb1d20/6a7b646b03d3b1363eea29cc_olesko-laurel-left.svg" loading="lazy" width="auto" height="auto" alt="__wf_reserved_inherit" class="olesko_hero_laurel_branch" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e29">'
        "</span> "
        '<span class="olesko_hero_laurel_copy" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e2b">'
        '<span class="olesko_hero_laurel_line" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e2c">in einer Woche geliefert</span>'
        '<span class="olesko_hero_laurel_line_subdued" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e2e">·</span>'
        '<span class="olesko_hero_laurel_line_subdued" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e30">·</span></span>'
        '<span class="olesko_hero_laurel_side" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e32">'
        '<img src="https://s3.amazonaws.com/webflow-prod-assets/6a7b43a328ec101a40bb1d20/6a7b646b460c187d667116b7_olesko-laurel-right.svg" loading="lazy" width="auto" height="auto" alt="__wf_reserved_inherit" class="olesko_hero_laurel_branch" data-w-id="5b3c7b25-e77b-cfe4-245d-1e1676ee0e33">'
        "</span></li>",
    ),
    n(
        "28ea34b7-fdff-c129-ec54-21a8f43bf71b",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">BEAUFTRAGTE AUTOMOBILFILME</p>',
    ),
    n(
        "28ea34b7-fdff-c129-ec54-21a8f43bf71d",
        '<h2 id="service-title" class="home_service_title u-text-style-h2">IHR AUTO. KEIN echter Dreh. KEIN RISIKO. in einer Woche geliefert.</h2>',
    ),
    n(
        "c18d7b03-b0f8-fb20-f8cb-5004a01c3a8b",
        '<h2 id="service-title" class="home_service_title u-text-style-h2">für einen Bruchteil der Kosten.</h2>',
    ),
    n(
        "28ea34b7-fdff-c129-ec54-21a8f43bf71f",
        '<p class="home_service_text u-text-style-main">'
        "Ihr Automobil wird nicht transportiert, nicht gefahren, keiner Straße, keiner Crew und "
        "keinem Wetter ausgesetzt. Es findet kein echter Dreh statt. Nichts ist in Gefahr. </p>",
    ),
    n(
        "28ea34b7-fdff-c129-ec54-21a8f43bf721",
        '<p class="home_service_text u-text-style-main">'
        "Der Film entsteht vollständig aus Fotografien, die Sie liefern, mit intelligenter Technologie. "
        "Ihr genaues Automobil, in einer Umgebung die Sie wählen, in einer Woche geliefert. </p>",
    ),
    n(
        "0bb8b077-d226-6bb5-ca3d-7e919ab2b7e3",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">HYPERCARS · NÜRBURGRING NORDSCHLEIFE</p>',
    ),
    n("23f50644-2757-de2d-8f42-0a20b4b83e12", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a94a5aa1d755181100606b7">FILM ANSEHEN</a>'),
    n(
        "7b647455-8e6c-47c6-c5b0-fd208dc715da",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">FERRARI 250 GT CALIFORNIA SPYDER · COMER SEE</p>',
    ),
    n("bc3c50b4-6200-a83d-1887-e343a1114cad", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a8b402d69195cfc7d432a59">FILM ANSEHEN</a>'),
    n("56d5520a-6208-e709-be82-9f6cb072ca06", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN →</p>'),
    n(
        "4aa75bf6-3c53-6913-187f-a4a3229befd3",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">PORSCHE 992 GT3 TOURING · ALPEN</p>',
    ),
    n("8a4963dd-1aea-397e-9df3-5488a7094850", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a8b402d3f30e7ce2c689cec">FILM ANSEHEN</a>'),
    n("e8e6007b-4ebb-9c0e-7da3-3a03d06a426c", '<div class="u-display-contents">FILM ANSEHEN</div>'),
    n(
        "28ea34b7-fdff-c129-ec54-21a8f43bf755",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">BENTLEY CONTINENTAL GTC · ITALIEN</p>',
    ),
    n("ff6ba05c-06e4-8321-9686-96d60e151e21", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a8b075dacef99c64dc2ba1d">FILM ANSEHEN</a>'),
    n("6032f51f-78bb-5a87-cbdf-c57307d11839", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a8b402e3f30e7ce2c689d4b">FILM ANSEHEN</a>'),
    n("58d38e3b-9f23-87d4-210c-d98bd60f5ae0", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a8b402efd4a464888ee176a">FILM ANSEHEN</a>'),
    n(
        "28ea34b7-fdff-c129-ec54-21a8f43bf72f",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">MERCEDES-AMG GT · HIGHLANDS</p>',
    ),
    n("1e336686-6770-425e-25d2-c6ef41d0c57c", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a8b402ffa314513088680ba">FILM ANSEHEN</a>'),
    n(
        "28ea34b7-fdff-c129-ec54-21a8f43bf78e",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">MERCEDES-BENZ 190 SL · ENGLAND</p>',
    ),
    n("7fd54b09-595c-6843-6606-60c87ebbc0da", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a8b402fefdad2a541be5cf8">FILM ANSEHEN</a>'),
    n(
        "28ea34b7-fdff-c129-ec54-21a8f43bf768",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">MERCEDES-AMG G 63 · BERGE</p>',
    ),
    n("0a8b82bb-60de-f569-2c03-d7acbd3605d0", '<a class="olesko_cta u-justify-self-start" data-wf-link-page-id="6a8b4030d04c77b87628e041">FILM ANSEHEN</a>'),
    n(
        "c28474f0-3742-9825-4efe-95e90d03bf85",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">WO IHR FILM WIRKEN KANN</p>',
    ),
    n(
        "c28474f0-3742-9825-4efe-95e90d03bf87",
        '<h2 id="uses-title" class="olesko_section_grid_item u-text-style-h2">IHR FILM. VIELE MÖGLICHKEITEN.</h2>',
    ),
    n(
        "c28474f0-3742-9825-4efe-95e90d03bf8a",
        '<p class="home_uses_intro_copy u-text-style-main u-color-faded u-column-start-4 u-column-span-5">'
        "Ihr Film kann dort wirken, wo Ihre Geschichte gesehen werden soll: auf Ihrer Website, "
        "in der Werbung, in einem Automobilinserat, auf einem Showroom-Schirm, in den sozialen "
        "Medien, auf einer Ausstellung oder in einer direkten Präsentation.</p>",
    ),
    n("c28474f0-3742-9825-4efe-95e90d03bf8d", '<li class="home_uses_application_item u-text-style-h6 u-text-transform-uppercase u-color-faded">WEBSITE</li>'),
    n("c28474f0-3742-9825-4efe-95e90d03bf8f", '<li class="home_uses_application_item u-text-style-h6 u-text-transform-uppercase u-color-faded">WERBUNG</li>'),
    n("c28474f0-3742-9825-4efe-95e90d03bf91", '<li class="home_uses_application_item u-text-style-h6 u-text-transform-uppercase u-color-faded">INSERATE</li>'),
    n("c28474f0-3742-9825-4efe-95e90d03bf93", '<li class="home_uses_application_item u-text-style-h6 u-text-transform-uppercase u-color-faded">SHOWROOMS</li>'),
    n("c28474f0-3742-9825-4efe-95e90d03bf95", '<li class="home_uses_application_item u-text-style-h6 u-text-transform-uppercase u-color-faded">SOCIAL MEDIA</li>'),
    n("c28474f0-3742-9825-4efe-95e90d03bf97", '<li class="home_uses_application_item u-text-style-h6 u-text-transform-uppercase u-color-faded">AUSSTELLUNGEN</li>'),
    n("c28474f0-3742-9825-4efe-95e90d03bf99", '<li class="home_uses_application_item u-text-style-h6 u-text-transform-uppercase u-color-faded">PRÄSENTATIONEN</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cacda", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">PREISE</p>'),
    n(
        "ef8748c2-b05a-7be2-294c-2426ec6cacdc",
        '<h2 id="pricing-title" class="olesko_section_grid_item u-text-style-h2">EIN KLARER AUSGANGSPUNKT.</h2>',
    ),
    n(
        "ef8748c2-b05a-7be2-294c-2426ec6cacdf",
        '<p class="home_pricing_intro_copy u-text-style-main u-color-faded u-column-start-4 u-column-span-5">'
        "Ihr Film beginnt mit einem Basispaket nach Länge. Optionale Anforderungen kommen nur dazu, wenn Sie sie wünschen.</p>",
    ),
    n(
        "f299aaef-a1ed-91cd-3508-dbcfdd1f57ba",
        '<p class="home_pricing_intro_copy u-text-style-main u-color-faded u-column-start-4 u-column-span-5">'
        "Fragen Sie nach Paketen oder Staffelpreisen, wenn Sie mehr als einen Film brauchen.</p>",
    ),
    n("ef8748c2-b05a-7be2-294c-2426ec6cace2", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">BASISPAKET</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cace4", '<h3 class="home_pricing_package u-text-style-h3">KURZFILM</h3>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cace7", '<p class="home_pricing_price u-text-style-h4">AB €1.200,-</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cace9", '<p class="home_pricing_note u-text-style-small u-color-faded">15 Sekunden</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6caced", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">BASISPAKET</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cacef", '<h3 class="home_pricing_package u-text-style-h3">FEATUREFILM</h3>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cacf2", '<p class="home_pricing_price u-text-style-h4">AB €2.100,-</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cacf4", '<p class="home_pricing_note u-text-style-small u-color-faded">30 Sekunden</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cacf8", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">BASISPAKET</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cacfa", '<h3 class="home_pricing_package u-text-style-h3">PORTRAITFILM</h3>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cacfd", '<p class="home_pricing_price u-text-style-h4">AB €3.600,-</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cacff", '<p class="home_pricing_note u-text-style-small u-color-faded">60 Sekunden</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad06", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">ENTHALTEN</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad08", '<li class="home_pricing_list_item">Ein Automobil wie auf den gelieferten Bildern</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad12", '<li class="home_pricing_list_item">Zustand (Licht, Griffe, ...) wie auf den Bildern</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad0a", '<li class="home_pricing_list_item">Eine stimmige Umgebung, wie gewählt</li>'),
    n("4126c6f0-7fc9-bb58-2f4d-ce7d28255fae", '<li class="home_pricing_list_item">Mehrere Perspektiven und Ansichten</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad0c", '<li class="home_pricing_list_item">Ein gewähltes Seitenverhältnis</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad0e", '<li class="home_pricing_list_item">1080p Videoauflösung</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad10", '<li class="home_pricing_list_item">Allgemeiner Fahrer, wo nötig</li>'),
    n("bb1758b0-0d9d-bc37-3a9c-bd928b0b289c", '<li class="home_pricing_list_item">Kennzeichen wie auf den Bildern</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad16", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">OPTIONAL</p>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad18", '<li class="home_pricing_list_item">Weitere allgemeine Umgebung</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad1a", '<li class="home_pricing_list_item">Eigene reale Kundenumgebung</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad1c", '<li class="home_pricing_list_item">Eigene erkennbare Person</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad1e", '<li class="home_pricing_list_item">Zweites Automobil in einem Film</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad20", '<li class="home_pricing_list_item">Änderung des Kennzeichens</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad22", '<li class="home_pricing_list_item">4K Videoauflösung</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad24", '<li class="home_pricing_list_item">Weiteres Seitenverhältnis</li>'),
    n("ef8748c2-b05a-7be2-294c-2426ec6cad26", '<li class="home_pricing_list_item">Text- oder Logo-Einblendungen</li>'),
    n("b01cf29d-1a18-9133-f8dc-b027825ceeb6", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">DIE KOLLEKTION</p>'),
    n(
        "8c994f55-65ad-0b7c-a851-1fb06d5285f9",
        '<h2 id="collection-title" class="olesko_section_grid_item u-text-style-h2">UNMÖGLICHE FILME, MIT EINEM ZWECK.</h2>',
    ),
    n(
        "778a07b8-16fe-7d70-79ec-3ff09c6eac6f",
        '<p class="home_collection_text u-text-style-main">'
        "Ihr Film soll mehr tun, als Aufmerksamkeit halten. Er soll etwas Wesentliches über Ihr "
        "Automobil zeigen und eine bewusste emotionale Antwort auslösen.</p>",
    ),
    n(
        "aab1c3f6-647b-c44f-4bfc-21392a2b7c70",
        '<p class="home_collection_text u-text-style-main">'
        "Für einen Händler, ein Auktionshaus oder eine Marke kann dieses Gefühl einem klaren "
        "Kommunikationsziel dienen. Für einen Sammler darf der Zweck ganz persönlich sein. "
        "Die Poesie macht die Arbeit spürbar; der Zweck gibt diesem Gefühl etwas, worauf es wirken kann.</p>",
    ),
    n("393691c1-2869-d71d-808a-a9cbfdb3f6fa", '<h3 class="olesko_label u-text-style-h6 u-text-transform-uppercase">KOMMERZIELL ODER INSTITUTIONELL</h3>'),
    n(
        "d4fa76d3-e878-d829-5a70-ca3944411827",
        '<p class="home_collection_text u-text-style-main u-color-faded">'
        "Ein Film mit klaren Zielen: kommunizieren, positionieren oder ein definiertes Ziel einer Organisation stützen.</p>",
    ),
    n("31112435-88b5-5af4-f5f4-f6e4bd6a80dd", '<h3 class="olesko_label u-text-style-h6 u-text-transform-uppercase">SAMMLER ODER PERSÖNLICH</h3>'),
    n(
        "bd5e6421-f297-6c5f-be66-92376e80ee94",
        '<p class="home_collection_text u-text-style-main u-color-faded">'
        "Ein Film für die Bedeutung, die Geschichte oder die Emotion, die mit einem Automobil oder einer Sammlung verbunden ist.</p>",
    ),
    n("69f445b9-0b60-e4a3-137e-df9721c4a873", '<h3 class="olesko_label u-text-style-h6 u-text-transform-uppercase">KUNDENRICHTLINIEN</h3>'),
    n(
        "a5e715dd-fac8-c40d-54f6-93fb93b08a8f",
        '<p class="home_collection_text u-text-style-main u-color-faded u-text-wrap-default">'
        "Liegen Markenrichtlinien vor, folgt Ihr Film der freigegebenen Sprache, Identität, Tonlage, "
        "den visuellen Codes, der Logo-Nutzung, den Botschaften und den Kommunikationsvorgaben.</p>",
    ),
    n("c589ac41-6dab-9585-7536-4326785b509a", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">IHR AUTOMOBIL</p>'),
    n(
        "c589ac41-6dab-9585-7536-4326785b509c",
        '<h2 id="reality-title" class="olesko_section_grid_item u-text-style-h2">IHR AUTOMOBIL DORT, WO ES NIE WAR.</h2>',
    ),
    n(
        "c589ac41-6dab-9585-7536-4326785b509f",
        '<p class="home_reality_text u-text-style-main u-color-faded u-column-start-4 u-column-span-5">'
        "Ihr Automobil kann in einer anderen Stadt, in einer anderen Landschaft oder in einem "
        "Moment erscheinen, der nie stattfand, ohne seinen Ort zu verlassen.</p>",
    ),
    n(
        "c589ac41-6dab-9585-7536-4326785b50a2",
        '<p class="home_reality_statement_primary u-text-style-display u-text-transform-uppercase u-column-span-full">NICHTS DAVON IST JE PASSIERT.</p>',
    ),
    n("c589ac41-6dab-9585-7536-4326785b50a5", '<h3 class="home_reality_question_text u-text-style-h2">ABER IST ES ECHT?</h3>'),
    n(
        "c589ac41-6dab-9585-7536-4326785b50a9",
        '<p class="home_reality_resolution_copy u-text-style-h4 u-color-faded">Wirklichkeit ist mehr als das, was geschah. Sie ist das, was in Ihnen geschieht.</p>',
    ),
    n("c589ac41-6dab-9585-7536-4326785b50ab", '<p class="home_reality_resolution_final u-text-style-h2">WENN ES SIE BEWEGT, IST ES ECHT.</p>'),
    n(
        "c589ac41-6dab-9585-7536-4326785b50ae",
        '<p class="home_reality_disclosure u-text-style-small u-text-transform-uppercase u-color-faded u-column-span-full">KOMPONIERTE BILDER. FAHRZEUG WIE ANGEGEBEN.</p>',
    ),
    n("85e0ce51-87d8-2799-6e39-8b1761b207c7", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">DER ABLAUF</p>'),
    n(
        "ad295c4c-37cc-fa47-9728-b97769ed8a33",
        '<h2 id="process-title" class="olesko_section_grid_item u-text-style-h2">VON IHREN FOTOGRAFIEN ZU IHREM FERTIGEN FILM.</h2>',
    ),
    n(
        "49347a28-7cb3-25e7-2333-4aa6b89d6929",
        '<p class="home_process_intro_copy u-text-style-main u-color-faded u-column-start-4 u-column-span-5">'
        "Sie liefern klare Fotografien Ihres Automobils aus brauchbaren Winkeln und beschreiben "
        "das Ergebnis, das Sie im Sinn haben. Konzept, Komposition und Herstellung übernimmt das Studio.</p>",
    ),
    n("49f8ab6a-2a21-4cf6-b985-9c795d439be9", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">DANACH</p>'),
    n("836da381-52d8-4c29-bc84-ca0877e2e0b5", '<p class="home_process_comparison_caption u-text-style-h4 u-text-transform-uppercase">IHR FERTIGER FILM</p>'),
    n("a30dc286-b2be-b29a-7bcf-864a6908c8d3", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">DAVOR</p>'),
    n("04d6d54f-0c03-e57f-048d-2c2e7efbd025", '<p class="home_process_comparison_caption u-text-style-h4 u-text-transform-uppercase">IHRE GELIEFERTEN FOTOGRAFIEN</p>'),
    n("a3973a29-2dfe-fdd6-2730-0d69076da238", '<h3 class="home_process_step_heading u-text-style-h4 u-text-transform-uppercase">TEILEN SIE IHR AUTOMOBIL</h3>'),
    n(
        "f6b21d55-1a75-0b9a-6cf0-de4bb29bafe8",
        '<p class="home_process_step_copy u-text-style-main u-color-faded">Fotografien, Beschreibung, wichtige Details und Vorgaben zum Erscheinungsbild.</p>',
    ),
    n("1830b957-6548-0250-0ac4-f5980631d692", '<h3 class="home_process_step_heading u-text-style-h4 u-text-transform-uppercase">BESTIMMEN SIE DIE SZENE</h3>'),
    n(
        "f591d27c-6077-5517-9ed7-558834f481d2",
        '<p class="home_process_step_copy u-text-style-main u-color-faded">'
        "Zweck, Publikum, Geschichte, Umgebung, Länge, Format und der gewünschte Schluss oder die gewünschte Handlung.</p>",
    ),
    n("7217052c-32e5-4447-f939-86619bcc3d92", '<h3 class="home_process_step_heading u-text-style-h4 u-text-transform-uppercase">ERHALTEN SIE DIE FERTIGE ARBEIT</h3>'),
    n(
        "8dda0860-6443-e88d-fe16-1e70ea760893",
        '<p class="home_process_step_copy u-text-style-main u-color-faded">'
        "Ihr Film kommt gebrauchsfertig, in einer Woche geliefert, ohne reale Produktion.</p>",
    ),
    n(
        "aaa2b792-6d47-3a67-2a56-26858ec42113",
        '<p class="home_process_instruction u-text-style-main u-color-faded u-column-start-1 u-column-span-8">'
        "Ziehen Sie den Teiler, um das Ausgangsautomobil mit dem komponierten Ergebnis zu vergleichen.</p>",
    ),
    n(
        "219aae07-e2f2-b158-1096-0e2ebdc1dae6",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">PERSÖNLICH GEMACHT IN WIEN</p>',
    ),
    n(
        "219aae07-e2f2-b158-1096-0e2ebdc1daea",
        '<p class="u-text-style-main u-color-faded">Jeden Auftrag entwickle und kuratiere ich persönlich.</p>',
    ),
    n(
        "219aae07-e2f2-b158-1096-0e2ebdc1daec",
        '<p class="u-text-style-main u-color-faded">'
        "Mehr als 30 Jahre über Marke, visuelles Design, Marketing, internationalen Vertrieb und "
        "Unternehmertum, einschließlich Führungsrollen und dem Aufbau von Geschäften von Grund auf.</p>",
    ),
    n(
        "219aae07-e2f2-b158-1096-0e2ebdc1daee",
        '<p class="u-text-style-main u-color-faded">Sie arbeiten direkt mit mir, vom ersten Gespräch bis zur Übergabe.</p>',
    ),
    n(
        "b8e3e558-e357-d266-8ca2-b93b5f2c90c7",
        '<a class="olesko_cta" data-wf-link-page-id="6a8471331d2d68eb848af612">'
        '<span data-w-id="b8e3e558-e357-d266-8ca2-b93b5f2c90c4">MEHR ÜBER SEBASTIAN</span>'
        '<span data-w-id="b8e3e558-e357-d266-8ca2-b93b5f2c90c6">→</span></a>',
    ),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b8976114f",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">HÄUFIGE FRAGEN</p>',
    ),
    n("ee7a7955-3390-8fe0-0996-4c4b89761151", '<h2 id="faq-title" class="olesko_section_grid_item u-text-style-h2">FRAGEN, BEANTWORTET.</h2>'),
    n(
        "bc61f72d-608a-d5ee-1f27-d36e12220cfb",
        '<p class="home_faq_answer_copy">'
        "Ja. Jeder kann das, wenn er das Können hat und die Werkzeuge beherrscht. Die Software ist "
        "nicht der Auftrag. Der Auftrag ist das Wissen, wie ein echtes Automobil in Bewegung aussieht, "
        "und die Arbeit, es dorthin zu bringen.</p>",
    ),
    n(
        "c2e1f317-16f6-7d17-7546-ddd849486b79",
        '<p class="home_faq_answer_copy">'
        "Das ist keine Herstellerwerbung. Es ist ein beauftragter Film eines bestimmten Automobils, "
        "aus Ihren Fotografien, ohne Anspruch auf Markengenehmigung. Verbietet ein Händlervertrag "
        "tatsächlich inoffizielle Filme auf neuem Bestand, ist das Ihre Grenze. Für Ihr eigenes Auto, "
        "Inserat oder Ihren Kunden gilt das nicht in derselben Weise.</p>",
    ),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b89761159",
        '<p class="home_faq_answer_copy">'
        "Ihr beauftragter Film ist eine kurze visuelle Arbeit aus gelieferten Fotografien. Er kann Ihr "
        "Automobil in eine komponierte Geschichte, einen Ort oder eine Atmosphäre setzen, ohne einen "
        "konventionellen Location-Dreh.</p>",
    ),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b89761162",
        '<p class="home_faq_answer_copy">'
        "Klare Fotografien aus brauchbaren Winkeln, wichtige Erscheinungsdetails und eine kurze "
        "Beschreibung des Ergebnisses, das Sie wollen.</p>",
    ),
    n("ee7a7955-3390-8fe0-0996-4c4b8976116b", '<p class="home_faq_answer_copy">Nein. Ihr Film entsteht aus gelieferten Fotografien.</p>'),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b89761174",
        '<p class="home_faq_answer_copy">Nein. Ihr Film kann ein kommerzielles Ziel stützen, oder für persönliche Bedeutung und Emotion entstehen.</p>',
    ),
    n("ee7a7955-3390-8fe0-0996-4c4b8976117d", '<p class="home_faq_answer_copy">Ein üblicher Auftrag wird in einer Woche geliefert.</p>'),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b89761186",
        '<p class="home_faq_answer_copy">Ja. Gelieferte Richtlinien und Kommunikationsvorgaben gehen in Ihr Briefing ein.</p>',
    ),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b8976118f",
        '<p class="home_faq_answer_copy">'
        "Ihr Film verwendet komponierte Bilder und moderne Bildtechnik, die generative KI einschließen "
        "kann, in einem persönlich verantworteten Herstellungsprozess. Die Art der Bilder wird klar benannt.</p>",
    ),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b89761198",
        '<p class="home_faq_answer_copy">'
        "Ja. Eigene reale Orte und erkennbare Personen können als zusätzliche Anforderungen beauftragt "
        "werden, wenn geeignetes Referenzmaterial vorliegt.</p>",
    ),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b897611a1",
        '<p class="home_faq_answer_copy">'
        "Ja. Kennzeichen, Abschlussbranding, Seitenverhältnis und Auflösung können Teil Ihres Auftrags "
        "sein; manche Wahl kann den Preis ändern.</p>",
    ),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b897611aa",
        '<p class="home_faq_answer_copy">'
        "Zulässige Nutzungen sind für jeden Auftrag klar bestimmt. Ihre Vereinbarung legt Lieferung, "
        "Nutzung und etwaige Grenzen fest, bevor die Herstellung beginnt.</p>",
    ),
    n(
        "ee7a7955-3390-8fe0-0996-4c4b897611b3",
        '<p class="home_faq_answer_copy">'
        "Nur mit Ihrer gesonderten Zustimmung. Veröffentlichung in der Kollektion, in den sozialen "
        "Medien, Tags und Inseratslinks brauchen jeweils eigene Einwilligung.</p>",
    ),
    n("d29c937d-2a56-f55f-0db1-61c48e078159", '<p id="olesko-film-lightbox-title">FILM</p>'),
    n("d29c937d-2a56-f55f-0db1-61c48e07815b", '<a class="olesko_film_close" href="#">SCHLIESSEN ×</a>'),
]

collection_nodes = [
    n("e5f14414-aad2-ddda-5300-c52a03172fde", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">DIE KOLLEKTION</p>'),
    n("8a7c22be-2029-ddc7-7e6f-8dee79dcbea2", '<h1 id="collection-title" class="olesko_section_grid_item u-text-style-h2">Kollektion</h1>'),
    n("b92297f0-eaff-dfe5-9c28-de759a2d043f", "<div>Keine Einträge.</div>"),
    n("31245485-5c08-a629-2d34-990b3f7b7bdf", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">HYPERCARS · NÜRBURGRING NORDSCHLEIFE</p>'),
    n("ec0dd733-63f3-d5e8-dd16-587243ebde76", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("774cfe16-4468-7864-3d6a-86184ce2b0d3", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">FERRARI 250 GT CALIFORNIA SPYDER · COMER SEE</p>'),
    n("95593e6d-ba46-d04f-600f-96b5d91a7644", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("97142d9b-8db8-5912-3067-147f2b180fba", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("c45bde2b-c88f-1e96-02b9-8243d1f58ef5", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">PORSCHE 992 GT3 TOURING · ALPEN</p>'),
    n("d1a7d208-18c6-e377-2e47-ed84609cba46", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("0ff7b6cc-d3a3-f33f-691d-7a0d603e0356", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">BENTLEY CONTINENTAL GTC · KÜSTE</p>'),
    n("377d5941-12dc-e950-5f96-a784fc7ab918", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("17e5a54c-3f6c-5e39-afc6-3918ca3b328c", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("56db6a0e-d334-efaf-dc00-80e605845763", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("38bb8e50-1705-a3f6-db08-42875191522e", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("c8f675f6-7d9e-c6c4-9cc5-d237df0d327d", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
    n("a5510d52-1f68-f3c2-3270-2bc5b864f887", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">MERCEDES-AMG G 63 · BERGE</p>'),
    n("6d1475b1-48fe-45db-c332-a1a3c959ecac", '<p class="olesko_cta u-justify-self-start">FILM ANSEHEN</p>'),
]

LABEL = "c3778b1c-e9f9-7ed9-b7c9-f987a278ddb0"
commission_nodes = [
    n("2a097400-64ed-1286-6504-d64f1f23e3b8", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">AUFTRAG</p>'),
    n("5ea31196-f387-49a9-2820-804f3b63289d", '<h1 id="commission-title" class="olesko_section_grid_item u-text-style-h2">IHR FILM</h1>'),
    n(
        "35f671f4-2ad3-d413-7137-ff0ac44e687d",
        '<p class="olesko_commission_copy">Sie beauftragen einen Film Ihres Automobils aus Fotografien, die Sie liefern. Übliche Arbeit wird persönlich gemacht, in einer Woche geliefert.</p>',
    ),
    n(
        "fd72e77f-f435-bebf-63fc-1a2294326f1a",
        '<p class="olesko_commission_copy">Zwei Wege: eine allgemeine Anfrage, oder ein Briefing. Er spricht es durch, dann kommt das Angebot.</p>',
    ),
    n("c3a8fe0e-ce53-5f0c-713d-ab2f24a5862a", '<a class="olesko_commission_copy" data-wf-link-page-id="6a83fdcf46ec1970b6eb307b">Vollständige Paketliste auf Start</a>'),
    n("ba6404b5-efb9-437d-eb5f-2c14fdf72b1e", '<h3 class="olesko_commission_path_title">ALLGEMEINE ANFRAGE</h3>'),
    n("5b478404-5c97-3837-7d1f-2ed94fd1b523", '<p class="olesko_commission_copy">Eine kurze allgemeine Anfrage, wenn Sie eine Einschätzung wollen.</p>'),
    n("a8b9f64f-7885-c60e-c39f-0533264d4e94", '<label for="" class="form_label_text">Name *</label>'),
    n("4f6d771c-dad6-5ace-618f-a025816cd61c", '<label for="" class="form_label_text">Firma (optional)</label>'),
    n("9e18cb06-dd97-b845-923a-43b237b775f4", '<label for="" class="form_label_text">E-Mail *</label>'),
    n("969cbd29-bd2a-2fb5-0a01-f233d672bd9a", '<label for="" class="form_label_text">Telefon</label>'),
    n("42b9a94f-2796-de44-b2de-294fe8f110de", '<label for="" class="form_label_text">Nachricht *</label>'),
    n("8cc27b64-2cdd-cb3c-2db4-acb40079dae3", '<h2 class="olesko_label u-text-style-h6 u-text-transform-uppercase">WIR HABEN ES</h2>'),
    n(
        "8e91f074-72a0-29d0-1bdf-1b5c2e9ed901",
        '<p class="olesko_commission_copy form_success_wrap">Sebastian meldet sich, um es durchzusprechen. Das Angebot folgt diesem Gespräch.</p>',
    ),
    n("e28cdf41-f968-db01-c55e-fa0249bc306a", '<div class="form_error_text">Beim Senden ist etwas schiefgegangen.</div>'),
    n("4bc005e6-1891-4eb0-ee99-19a29892faef", '<h3 class="olesko_commission_path_title">BRIEFING SENDEN</h3>'),
    n(
        "3e3d42ec-6679-51a7-8432-52aae8a4ac75",
        '<p class="olesko_commission_copy">Sie wissen schon, was Sie wollen. Optionen, dann eine Anfrage. Kein Preis.</p>',
    ),
    n("7b0b15aa-716c-f74a-1d3c-3486865c3cab", '<label for="" class="form_label_text">Name *</label>'),
    n("19080533-51ef-e3e4-32de-890f944320b5", '<label for="" class="form_label_text">Firma (optional)</label>'),
    n("df88cc19-c72d-12c6-1549-11a6a522459c", '<label for="" class="form_label_text">E-Mail *</label>'),
    n("7d08f292-48e2-d1f4-8f6e-9672c1739705", '<label for="" class="form_label_text">Telefon</label>'),
    n("d8df9aea-0dda-0028-5e9b-7055be5cb4b0", '<label for="" class="form_label_text">Automobil *</label>'),
    ov("480571dd-2466-2c0a-271c-c17c9591daef", [("b4da0210-a11e-8169-6bd3-3724db9bdc28", "Länge")]),
    ov("81fa6aa4-7379-a531-24b2-14e9b5af28d9", [(LABEL, "15 Sekunden")]),
    ov("bae2bf93-ccc3-1aa8-74a8-e09b44cfdcb0", [(LABEL, "30 Sekunden")]),
    ov("9a8113c3-f70e-f68d-84a5-16628a909676", [(LABEL, "60 Sekunden")]),
    ov("52442bed-9ae2-ce37-1008-84c25f97bf94", [("b4da0210-a11e-8169-6bd3-3724db9bdc28", "Zweck")]),
    ov("e241ee45-643b-2385-c5c9-c21e6399cb23", [(LABEL, "Kommerziell / Werbung")]),
    ov("d190983d-ec5d-3b73-ebf2-c12116c0af22", [(LABEL, "Sammler / privat")]),
    n("259d1213-fe74-eb64-1b58-f42df341b408", '<label for="" class="form_label_text">Umgebung</label>'),
    ov("7c1c5ad8-6af8-f339-0953-5ed8e8d0176b", [("b4da0210-a11e-8169-6bd3-3724db9bdc28", "Format")]),
    ov("41a1ec2d-eb87-191c-038a-219794a091ed", [(LABEL, "Zu besprechen")]),
    ov("8529da91-2cb4-667c-3cb3-a3f6276d71b9", [("b4da0210-a11e-8169-6bd3-3724db9bdc28", "Extras")]),
    ov("ee1ec920-e72b-5491-e984-d399cc3b4686", [(LABEL, "Weitere allgemeine Umgebung")]),
    ov("d8cb75f1-3555-74df-8b9f-48e02fab67ac", [(LABEL, "Eigene reale Kundenumgebung")]),
    ov("2c43d4f9-706f-bfdc-f82f-bdd35a1c989b", [(LABEL, "Eigene erkennbare Person")]),
    ov("6184219f-7830-f7ae-5052-215f6e701dd3", [(LABEL, "Zweites Automobil in einem Film")]),
    ov("8bc9bc77-ec9e-2f0a-f4c7-7e56f6c973af", [(LABEL, "Änderung des Kennzeichens")]),
    ov("9f263d54-acc7-6e31-30da-c1f87b39532a", [(LABEL, "4K Videoauflösung")]),
    ov("0b28e19b-552c-2452-43c5-1c18e377c247", [(LABEL, "Weiteres Seitenverhältnis")]),
    ov("195acf75-a10b-ccae-dcb4-a3b8a77ccb04", [(LABEL, "Text- oder Logo-Einblendungen")]),
    n("aa4702fa-621c-9cef-7a28-d801e4afdb27", '<label for="" class="form_label_text">Nachricht</label>'),
    n("0e571bb7-24a4-a62d-945f-dca150bd62eb", '<h2 class="olesko_label u-text-style-h6 u-text-transform-uppercase">WIR HABEN ES</h2>'),
    n(
        "10fc7615-fedb-b2b6-8826-e3e4ce1bb472",
        '<p class="olesko_commission_copy form_success_wrap">Sebastian meldet sich, um es durchzusprechen. Das Angebot folgt diesem Gespräch.</p>',
    ),
    n("be9354bd-5374-d37b-9d80-91670ff115ec", '<div class="form_error_text">Beim Senden ist etwas schiefgegangen.</div>'),
]

about_nodes = [
    n(
        "a8851332-85d3-eb33-1e41-86e4ae13b0c0",
        '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">KREATIV AUSGEBILDET. KOMMERZIELL ERFAHREN.</p>',
    ),
    n(
        "b8bec284-07d7-67b2-f9d5-6eebc22e8c08",
        '<p class="home_collection_text u-text-style-main u-color-faded">Ich bin Designer, Verkäufer und Unternehmer in Wien.</p>',
    ),
    n(
        "59f455af-db1c-a337-9b0a-e83fc3e94c74",
        '<p class="home_collection_text u-text-style-main u-color-faded">'
        "Seit mehr als 30 Jahren arbeite ich dort, wo Design, Technik, Marketing und Vertrieb "
        "zusammenkommen. OLESKO bringt diese Erfahrung in einem persönlich geführten Studio zusammen.</p>",
    ),
    n("c91c1bb6-b883-4d6e-a851-faa58572d321", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">JAHRE BERUFLICHER ERFAHRUNG</p>'),
    n("e63f5945-092c-eb16-b335-6c16eabfa9f6", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">JAHRE SEIT MEINER ERSTEN WEBSITE</p>'),
    n("7898b1bf-0b4e-9342-8a6b-8b05e4b0312c", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">GEGRÜNDETE ODER MITGEGRÜNDETE UNTERNEHMEN</p>'),
    n("41e3f05b-9395-3d50-20d4-4b3556373705", '<h3 class="home_pricing_package u-text-style-h2">WIEN</h3>'),
    n("8efa2f41-30f0-7565-a411-5e911611542a", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">SITZ · INTERNATIONALE ERFAHRUNG</p>'),
    n("72dc6152-044d-db3d-602c-5b994fb8ec99", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">WOHER ICH KOMME</p>'),
    n("61b77b71-d3fb-e6fd-1e59-07ae97a0cf0e", '<h2 id="practice-title" class="olesko_section_grid_item u-text-style-h2">GEBAUT, DAMIT ES FUNKTIONIERT.</h2>'),
    n(
        "ee026905-196c-7301-76b2-33e6555546e6",
        '<p class="home_collection_text u-text-style-main">'
        "Ich bin als Tischler und Innenarchitekt ausgebildet. Das hat mich früh gelehrt: eine gute "
        "Idee muss nicht nur richtig aussehen, sie muss praktisch, tragfähig und präzise ausgeführt "
        "sein. Sie muss funktionieren.</p>",
    ),
    n(
        "1226c060-e4aa-c1a3-d9ed-373155da307b",
        '<p class="home_collection_text u-text-style-main">Ich war immer neugierig auf moderne Technik und habe vor etwa 35 Jahren meine erste Website programmiert.</p>',
    ),
    n(
        "5d48b132-63a3-addb-83c6-4f636d7d7238",
        '<p class="home_collection_text u-text-style-main">'
        "Seitdem habe ich in Design, Produktentwicklung, Marke, Marketing, internationalem Vertrieb "
        "und Management gearbeitet, unter anderem für Bene, IKEA und hali. Später habe ich the office "
        "republic, PRTTY, 1st Beauty Lab und OLESKO gegründet oder mitgegründet.</p>",
    ),
    n("b28a060e-02d2-52e6-cedb-78b38c631cc2", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">WIE ICH ARBEITE</p>'),
    n("30e57360-b7a9-8081-98f0-d58524655996", '<h2 id="work-title" class="olesko_section_grid_item u-text-style-h2">DER MODERNE VERKÄUFER.</h2>'),
    n("087c1daf-f0c6-a6c0-5273-a1c7c343db73", '<p class="home_collection_text u-text-style-main">So beschreibe ich mich noch immer.</p>'),
    n(
        "7682ea4c-2780-1e0f-e72b-fb8d2bcd10d7",
        '<p class="home_collection_text u-text-style-main">'
        "Design hat mich sehen gelehrt. Tischlerei hat mich bauen gelehrt. Technik hat mich neugierig "
        "gehalten. Vertrieb hat mich zuhören gelehrt. Unternehmen aufzubauen hat mich Verantwortung gelehrt.</p>",
    ),
    n(
        "5e120a29-da27-b4cc-ebf2-97b03d60b809",
        '<p class="home_collection_text u-text-style-main">'
        "Jeden OLESKO-Auftrag entwickle und kuratiere ich persönlich. Sie arbeiten direkt mit mir. "
        "Vom ersten Gespräch bis zum fertigen Film.</p>",
    ),
    n("8d352917-ea50-6e91-db48-445685c8406e", '<p class="olesko_eyebrow u-text-style-small u-text-transform-uppercase u-color-faded">PERSÖNLICHE VERANTWORTUNG</p>'),
    n("ab44808c-b830-0b2d-2c72-2c84e8122d36", '<h2 id="enquire-title" class="olesko_section_grid_item u-text-style-h2">IHR&nbsp;FILM.</h2>'),
    n(
        "3c9f8e75-5d30-5b25-8114-d2576c19ebae",
        '<p class="home_commission_copy u-text-style-main u-color-faded">'
        "Erzählen Sie mir von Ihrem Automobil und was Sie im Sinn haben. Ich sehe Ihr Material "
        "persönlich an und sage Ihnen, was möglich ist.</p>",
    ),
    n("fb4fe7b2-9a4c-4804-d185-9aa2994eca39", "<div>EIN GESPRÄCH BEGINNEN</div>"),
]


def film_share() -> list[dict]:
    return [
        n("4f06d78c-6a4b-e448-20d3-9816f40f6e9b", '<a class="olesko_cta olesko_film_share_button" href="#">TEILEN</a>'),
        n("900ff579-67eb-99b0-73a2-fbe268e3c3bb", '<a class="olesko_cta olesko_film_share_button" href="#">LINK KOPIEREN</a>'),
    ]


def film_blurb(html: str) -> dict:
    return n("f3c6087f-0d69-dadd-c0dc-9ef39cbe89c6", f'<p class="olesko_film_copy">{html}</p>')


def film_disclosure(node_id: str) -> dict:
    return n(node_id, f'<p class="olesko_film_copy u-color-faded">{DISCLOSURE}</p>')


films = {
    "6a94a5aa1d755181100606b7": {
        "slug": "let-it-rain-nurburgring-nordschleife",
        "title": "LET IT RAIN.",
        "nodes": [
            film_blurb(
                "Die Grüne Hölle ist nass. Gischt hinter einem Chiron, einer Valkyrie, einem Jesko Attack und einem Huayra. Vier Hypercars auf der Nordschleife, als wäre der Regen dafür aufgehoben worden."
            ),
            film_disclosure("d85092e4-ecf0-3c89-8aee-06384083eb41"),
            *film_share(),
        ],
    },
    "6a94835baff009655de6bdca": {
        "slug": "the-look-of-love-ferrari-250-gt-california-spyder",
        "title": "THE LOOK OF LOVE.",
        "nodes": [
            film_blurb(
                "Das Dach ist offen. Burgunderroter Aufbau auf der Como-Straße, Oleander in der Sonne. Ein 250 GT California Spyder, ohne Eile, als wäre der Nachmittag dafür aufgehoben worden."
            ),
            film_disclosure("d85092e4-ecf0-3c89-8aee-06384083eb41"),
            *film_share(),
        ],
    },
    "6a8b402d69195cfc7d432a59": {
        "slug": "riviera-summer-cruise-aston-martin-db12-volante",
        "title": "RIVIERA SUMMER CRUISE.",
        "nodes": [
            film_blurb(
                "Das Dach ist offen. Mittelmeerlicht auf dem Aufbau, die Corniche rollt sich auf, als wäre sie dafür aufgehoben worden. Ein DB12 Volante, ohne Eile, nah genug, um das Salz zu schmecken."
            ),
            film_disclosure("60239087-0df7-279e-27c6-2a99a6ab59f6"),
            *film_share(),
        ],
    },
    "6a8b402d3f30e7ce2c689cec": {
        "slug": "alpine-autumn-high-pass-porsche-992-gt3-touring",
        "title": "ALPINE AUTUMN HIGH PASS.",
        "nodes": [
            film_blurb(
                "Hohe Luft, dünnes Licht, der Pass öffnet sich durch Lärche und Stein. Ein 992 GT3 Touring an den Berg gehalten, ohne Eile, als hätte die Straße gewartet."
            ),
            film_disclosure("d149f4c6-f637-cfe0-6fc1-91eded3279cb"),
            *film_share(),
        ],
    },
    "6a8b075dacef99c64dc2ba1d": {
        "slug": "along-the-sea-wall-bentley-continental-gtc",
        "title": "ALONG THE SEA WALL.",
        "nodes": [
            film_blurb(
                "Das Dach ist offen. Silberner Aufbau gegen die Seemauer, Sonne auf dem Wasser, die Küste öffnet sich, als wäre sie dafür aufgehoben worden. Ein Continental GTC, ohne Eile, nah genug, um das Salz zu schmecken."
            ),
            film_disclosure("c56dc512-e92f-0774-ba0b-793f0624c8b2"),
            *film_share(),
        ],
    },
    "6a8b402e3f30e7ce2c689d4b": {
        "slug": "on-the-flooded-salt-lamborghini-revuelto",
        "title": "ON THE FLOODED SALT.",
        "nodes": [
            film_blurb(
                "Himmel und Salz als eine Fläche. Ein Revuelto auf dem überfluteten Salar, ohne Eile, der Horizont so still, er könnte Glas sein."
            ),
            film_disclosure("231256d3-5d94-853c-076a-7d2626d77186"),
            *film_share(),
        ],
    },
    "6a8b402efd4a464888ee176a": {
        "slug": "at-the-louvre-ferrari-250-gto",
        "title": "AT THE LOUVRE.",
        "nodes": [
            film_blurb(
                "Nacht auf dem Stein, roter Aufbau unter den Lampen. Ein 250 GTO in Paris, ohne Eile, als wäre die Straße dafür aufgehoben worden."
            ),
            film_disclosure("d85092e4-ecf0-3c89-8aee-06384083eb41"),
            *film_share(),
        ],
    },
    "6a8b402ffa314513088680ba": {
        "slug": "into-the-highland-fog-mercedes-amg-gt",
        "title": "INTO THE HIGHLAND FOG.",
        "nodes": [
            film_blurb(
                "Die Straße dünnt sich in den Nebel. Ein AMG GT in den Highlands, ohne Eile, Silber gegen das Nasse, nah genug, um den Regen zu schmecken."
            ),
            film_disclosure("7b4a83f3-56d6-8a0b-0aac-cfe840c2d0f6"),
            *film_share(),
        ],
    },
    "6a8b402fefdad2a541be5cf8": {
        "slug": "down-the-avenue-mercedes-benz-190-sl",
        "title": "DOWN THE AVENUE.",
        "nodes": [
            film_blurb(
                "Bäume in einer Reihe, heller Aufbau im Schatten. Ein 190 SL auf einer englischen Allee, ohne Eile, als wäre der Nachmittag dafür aufgehoben worden."
            ),
            film_disclosure("160ff042-61f7-467f-3f3d-895662ea4cbc"),
            *film_share(),
        ],
    },
    "6a8b4030d04c77b87628e041": {
        "slug": "mountain-sanctuary-mercedes-amg-g-63",
        "title": "MOUNTAIN SANCTUARY.",
        "nodes": [
            film_blurb(
                "Schnee, Stille, schwarzer Aufbau gegen den Gipfel. Ein G 63 in der hohen Luft, ohne Eile, als hätte der Berg gewartet."
            ),
            film_disclosure("20a012e1-f76d-7c79-1842-8da6e0d4bec6"),
            *film_share(),
        ],
    },
}

apply = {
    "do_not_publish": True,
    "site_id": SITE,
    "localeId": LOCALE_PLACEHOLDER,
    "notes": [
        "MCP cannot create locale de. Designer Localize first. Leave publishing disabled.",
        "Films are static pages. Films-cms has 0 items. Do not create CMS film items.",
        "Do not write Imprint or Privacy DE.",
        "Primary header DE switcher still needs Designer locale-link after de exists.",
        "FAQ questions are not in get_page_content. See STATUS.md.",
        "Commission submit-button values (SEND ENQUIRY / SEND BRIEF) need Designer on DE.",
        "Reality section is translated and stays hidden.",
    ],
    "components": [
        {
            "name": "OLESKO Global Header",
            "component_id": "881a26d8-3f1e-e90c-0186-847d7679f286",
            "nodes": header_nodes,
        },
        {
            "name": "OLESKO Global Footer",
            "component_id": "c71826be-a2bb-fee5-bd98-26dfc1070f99",
            "nodes": footer_nodes,
        },
        {
            "name": "OLESKO Commission CTA",
            "component_id": "f343f630-2311-818c-25f1-2120a8f0ef1a",
            "nodes": cta_nodes,
        },
        {
            "name": "OLESKO Film Disclaimer",
            "component_id": "8b4e95eb-fc30-c6aa-df8c-80e377a2c38e",
            "nodes": disclaimer_nodes,
        },
    ],
    "pages": [
        {"name": "Home", "page_id": "6a83fdcf46ec1970b6eb307b", "path": "/", "nodes": home_nodes},
        {"name": "Collection", "page_id": "6a8471318afbe9b46708f954", "path": "/collection", "nodes": collection_nodes},
        {"name": "Commission", "page_id": "6a8471320e6ee1e88c0037c2", "path": "/commission", "nodes": commission_nodes},
        {"name": "About", "page_id": "6a8471331d2d68eb848af612", "path": "/about", "nodes": about_nodes},
    ],
}

for page_id, meta in films.items():
    apply["pages"].append(
        {
            "name": meta["title"].rstrip("."),
            "page_id": page_id,
            "path": f"/films/{meta['slug']}",
            "nodes": meta["nodes"],
        }
    )

ORG = {
    "@id": "https://oleskostudio.com/#organization",
    "@type": "Organization",
    "address": {"@type": "PostalAddress", "addressCountry": "AT", "addressLocality": "Vienna"},
    "alternateName": ["OLESKO Studio", "oleskostudio.com"],
    "contactPoint": {
        "@type": "ContactPoint",
        "availableLanguage": ["English", "German"],
        "contactType": "sales",
        "email": "sebastian@oleskostudio.com",
        "url": "https://oleskostudio.com/de-at/commission",
    },
    "description": "Beauftragte Filme für exklusive Automobile, erzeugt aus Ihren Bildern.",
    "email": "sebastian@oleskostudio.com",
    "legalName": "OLESKO",
    "logo": {
        "@type": "ImageObject",
        "url": "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a830b20a53e873314bb9a04_olesko-webclip-1024.png",
    },
    "name": "OLESKO",
    "sameAs": [
        "https://www.instagram.com/olesko.studio/",
        "https://www.facebook.com/sebastianolesko/",
        "https://www.linkedin.com/in/sebastianolesko/",
    ],
    "url": "https://oleskostudio.com",
}

HOME_DESC = (
    "OLESKO ist das Wiener Studio von Sebastian Olesko. Beauftragte Filme für "
    "exklusive Automobile, erzeugt aus Ihren Bildern, ohne Transport, "
    "Straßensperrungen oder einen konventionellen Location-Dreh."
)
HOME_TITLE = "OLESKO. Beauftragte Filme für exklusive Automobile. Erzeugt aus Ihren Bildern"

film_schema = [
    (
        "6a94a5aa1d755181100606b7",
        "let-it-rain-nurburgring-nordschleife",
        "LET IT RAIN.",
        "Let it rain. Vier Hypercars auf der Nürburgring Nordschleife.",
        "OlX8CPetuXoNzDIwejgd7NOU1intYKyZ8h3toHIdrNg",
        "6a957cf4677cc64555e104fb",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a957cf4677cc64555e104fb_olesko-demo-hypercars-nurburgring-nordschleife-v3.jpg",
        "2026-08-31T00:00:00+02:00",
        "LET IT RAIN. Nürburgring Nordschleife. OLESKO",
    ),
    (
        "6a94835baff009655de6bdca",
        "the-look-of-love-ferrari-250-gt-california-spyder",
        "THE LOOK OF LOVE.",
        "The Look of Love. Ein Ferrari 250 GT California Spyder am Comer See.",
        "rs01FzIgY7VytHaQpcSz02eznRjuYts8zz2I9MIQ36dHo",
        "6a97e86a5886662d0a4028fb",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a97e86a5886662d0a4028fb_olesko-demo-ferrari-california-spyder-como-v3.jpg",
        "2026-08-30T00:00:00+02:00",
        "THE LOOK OF LOVE. Ferrari 250 GT California Spyder. OLESKO",
    ),
    (
        "6a8b402d69195cfc7d432a59",
        "riviera-summer-cruise-aston-martin-db12-volante",
        "RIVIERA SUMMER CRUISE.",
        "Riviera Summer Cruise. Ein Aston Martin DB12 Volante an der Côte d'Azur.",
        "02qnn02P7l2wIRJfRyjBTyhGoTTOoKjDelHwSxFe1OdKY",
        "6a89dd32b52c25150dc49fbc",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a89dd32b52c25150dc49fbc_olesko-demo-db12-volante-riviera.jpg",
        "2026-08-23T00:00:00+02:00",
        "RIVIERA SUMMER CRUISE. Aston Martin DB12 Volante. OLESKO",
    ),
    (
        "6a8b402d3f30e7ce2c689cec",
        "alpine-autumn-high-pass-porsche-992-gt3-touring",
        "ALPINE AUTUMN HIGH PASS.",
        "Alpine Autumn High Pass. Ein Porsche 992 GT3 Touring in den Alpen.",
        "JpRyvr01QDyNp5v1O5ODoWzzbiWll1HrNGlFGfwa6DQs",
        "6a899d738775ce81a7b4a072",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a899d738775ce81a7b4a072_olesko-demo-porsche-gt3-alpine.jpg",
        "2026-08-23T00:00:00+02:00",
        "ALPINE AUTUMN HIGH PASS. Porsche 992 GT3 Touring. OLESKO",
    ),
    (
        "6a8b075dacef99c64dc2ba1d",
        "along-the-sea-wall-bentley-continental-gtc",
        "ALONG THE SEA WALL.",
        "Along the Sea Wall. Ein Bentley Continental GTC an der italienischen Küste.",
        "HK7phtLFrY6EoR7Zb4J700hPvNkLRosTbDQZtirhxqqk",
        "6a88c73984092424b60c3dac",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a88c73984092424b60c3dac_olesko-demo-bentley-coast-v2.jpg",
        "2026-08-23T00:00:00+02:00",
        "ALONG THE SEA WALL. Bentley Continental GTC. OLESKO",
    ),
    (
        "6a8b402e3f30e7ce2c689d4b",
        "on-the-flooded-salt-lamborghini-revuelto",
        "ON THE FLOODED SALT.",
        "On the Flooded Salt. Ein Lamborghini Revuelto auf dem Salar de Uyuni.",
        "7vMDXoYF3ELCWh1Ht01rSTv856q9yP600Ns02PIzzhiztw",
        "6a87131f791cd9404feea96c",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a87131f791cd9404feea96c_olesko-demo-revuelto-uyuni-16x9.jpg",
        "2026-08-23T00:00:00+02:00",
        "ON THE FLOODED SALT. Lamborghini Revuelto. OLESKO",
    ),
    (
        "6a8b402efd4a464888ee176a",
        "at-the-louvre-ferrari-250-gto",
        "AT THE LOUVRE.",
        "At the Louvre. Ein Ferrari 250 GTO in Paris.",
        "Ew5FZhdef02EiwtkpJ768ZJL1N6FKOpfKuyRp1KjpFJI",
        "6a882be0ecb8ec0b729f1b8f",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a882be0ecb8ec0b729f1b8f_olesko-demo-ferrari-gto-paris-hires.jpg",
        "2026-08-23T00:00:00+02:00",
        "AT THE LOUVRE. Ferrari 250 GTO. OLESKO",
    ),
    (
        "6a8b402ffa314513088680ba",
        "into-the-highland-fog-mercedes-amg-gt",
        "INTO THE HIGHLAND FOG.",
        "Into the Highland Fog. Ein Mercedes-AMG GT in Schottland.",
        "Xcs02prXENY100cDYVvGjToQyZ21PJkaFpY006icNuVvgg",
        "6a88c8294e03304523ebb96d",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a88c8294e03304523ebb96d_olesko-demo-amg-fog-v2.jpg",
        "2026-08-23T00:00:00+02:00",
        "INTO THE HIGHLAND FOG. Mercedes-AMG GT. OLESKO",
    ),
    (
        "6a8b402fefdad2a541be5cf8",
        "down-the-avenue-mercedes-benz-190-sl",
        "DOWN THE AVENUE.",
        "Down the Avenue. Ein Mercedes-Benz 190 SL in England.",
        "7vlFqf2fLr3h5kneTRKmO6XCjMbU7Fu3zxgdPUelkTA",
        "6a881a76264cbbc0966e2d2e",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a881a76264cbbc0966e2d2e_olesko-demo-190sl-avenue-hires.jpg",
        "2026-08-23T00:00:00+02:00",
        "DOWN THE AVENUE. Mercedes-Benz 190 SL. OLESKO",
    ),
    (
        "6a8b4030d04c77b87628e041",
        "mountain-sanctuary-mercedes-amg-g-63",
        "MOUNTAIN SANCTUARY.",
        "Mountain Sanctuary. Ein Mercedes-AMG G 63 in den Bergen.",
        "svnxW67n6IeVArX329IXJiALGVi02TCWhNV3FXSthKjk",
        "6a968b386f1d9c22617c6d53",
        "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a968b386f1d9c22617c6d53_olesko-demo-g63-mountain-sanctuary-v3.jpg",
        "2026-08-23T00:00:00+02:00",
        "MOUNTAIN SANCTUARY. Mercedes-AMG G 63. OLESKO",
    ),
]

faq = [
    (
        "KANN ICH DAS SELBST MIT KI-SOFTWARE MACHEN?",
        "Ja. Jeder kann das, wenn er das Können hat und die Werkzeuge beherrscht. Die Software ist nicht der Auftrag. Der Auftrag ist das Wissen, wie ein echtes Automobil in Bewegung aussieht, und die Arbeit, es dorthin zu bringen.",
    ),
    (
        "GEHT DAS, WENN DER HERSTELLER NUR OFFIZIELLES MARKENMATERIAL ERLAUBT?",
        "Das ist keine Herstellerwerbung. Es ist ein beauftragter Film eines bestimmten Automobils, aus Ihren Fotografien, ohne Anspruch auf Markengenehmigung. Verbietet ein Händlervertrag tatsächlich inoffizielle Filme auf neuem Bestand, ist das Ihre Grenze. Für Ihr eigenes Auto, Inserat oder Ihren Kunden gilt das nicht in derselben Weise.",
    ),
    (
        "WAS IST EIN AUTOMOBILFILM AUF AUFTRAG?",
        "Ihr beauftragter Film ist eine kurze visuelle Arbeit aus gelieferten Fotografien. Er kann Ihr Automobil in eine komponierte Geschichte, einen Ort oder eine Atmosphäre setzen, ohne einen konventionellen Location-Dreh.",
    ),
    (
        "WAS MUSS ICH LIEFERN?",
        "Klare Fotografien aus brauchbaren Winkeln, wichtige Erscheinungsdetails und eine kurze Beschreibung des Ergebnisses, das Sie wollen.",
    ),
    ("MUSS MEIN AUTOMOBIL TRANSPORTIERT WERDEN?", "Nein. Ihr Film entsteht aus gelieferten Fotografien."),
    (
        "BRAUCHT MEIN FILM EIN KOMMERZIELLES ZIEL?",
        "Nein. Ihr Film kann ein kommerzielles Ziel stützen, oder für persönliche Bedeutung und Emotion entstehen.",
    ),
    ("WIE LANGE DAUERT MEIN FILM?", "Ein üblicher Auftrag wird in einer Woche geliefert."),
    ("WERDEN MEINE MARKENRICHTLINIEN BEACHTET?", "Ja. Gelieferte Richtlinien und Kommunikationsvorgaben gehen in Ihr Briefing ein."),
    (
        "SIND DIE BILDER ECHT ODER ERZEUGT?",
        "Ihr Film verwendet komponierte Bilder und moderne Bildtechnik, die generative KI einschließen kann, in einem persönlich verantworteten Herstellungsprozess. Die Art der Bilder wird klar benannt.",
    ),
    (
        "KANN MEIN FILM EINEN ECHTEN SHOWROOM, EINE VILLA ODER EINE ERKENNBARE PERSON ZEIGEN?",
        "Ja. Eigene reale Orte und erkennbare Personen können als zusätzliche Anforderungen beauftragt werden, wenn geeignetes Referenzmaterial vorliegt.",
    ),
    (
        "KANN ICH KENNZEICHEN, BRANDING UND AUSLIEFERUNGSFORMAT VORGEBEN?",
        "Ja. Kennzeichen, Abschlussbranding, Seitenverhältnis und Auflösung können Teil Ihres Auftrags sein; manche Wahl kann den Preis ändern.",
    ),
    (
        "WELCHE NUTZUNGSRECHTE SIND ENTHALTEN?",
        "Zulässige Nutzungen sind für jeden Auftrag klar bestimmt. Ihre Vereinbarung legt Lieferung, Nutzung und etwaige Grenzen fest, bevor die Herstellung beginnt.",
    ),
    (
        "WIRD MEIN AUFTRAGSFILM VERÖFFENTLICHT?",
        "Nur mit Ihrer gesonderten Zustimmung. Veröffentlichung in der Kollektion, in den sozialen Medien, Tags und Inseratslinks brauchen jeweils eigene Einwilligung.",
    ),
]

seo_pages = [
    {
        "id": "6a83fdcf46ec1970b6eb307b",
        "path": "/",
        "canonical": "https://oleskostudio.com/de-at",
        "title": "Home",
        "seo": {"title": HOME_TITLE, "description": HOME_DESC},
        "openGraph": {
            "title": HOME_TITLE,
            "titleCopied": True,
            "description": HOME_DESC,
            "descriptionCopied": True,
            "imageAssetId": "6a899d738775ce81a7b4a072",
        },
        "jsonLdSchema": {
            "@context": "https://schema.org",
            "@graph": [
                ORG,
                {
                    "@id": "https://oleskostudio.com/#website",
                    "@type": "WebSite",
                    "name": "OLESKO",
                    "publisher": {"@id": "https://oleskostudio.com/#organization"},
                    "url": "https://oleskostudio.com",
                    "inLanguage": ["en", "de-AT"],
                },
                {
                    "@id": "https://oleskostudio.com/de-at#webpage",
                    "@type": "WebPage",
                    "description": HOME_DESC,
                    "inLanguage": "de-AT",
                    "isPartOf": {"@id": "https://oleskostudio.com/#website"},
                    "name": HOME_TITLE,
                    "url": "https://oleskostudio.com/de-at",
                },
                {
                    "@id": "https://oleskostudio.com/de-at#faq",
                    "@type": "FAQPage",
                    "inLanguage": "de-AT",
                    "mainEntity": [
                        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                        for q, a in faq
                    ],
                },
            ],
        },
    },
    {
        "id": "6a8471318afbe9b46708f954",
        "path": "/collection",
        "canonical": "https://oleskostudio.com/de-at/collection",
        "title": "Collection",
        "seo": {
            "title": "Die Kollektion. OLESKO",
            "description": "Ausgewählte beauftragte Filme für exklusive Automobile.",
        },
        "openGraph": {
            "titleCopied": True,
            "descriptionCopied": True,
            "imageAssetId": "6a899d738775ce81a7b4a072",
        },
        "jsonLdSchema": {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "inLanguage": "de-AT",
            "description": "Ausgewählte beauftragte Filme für exklusive Automobile.",
            "mainEntity": {
                "@type": "ItemList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "name": name,
                        "position": i,
                        "url": f"https://oleskostudio.com/de-at/films/{slug}",
                    }
                    for i, (_pid, slug, name, *_rest) in enumerate(film_schema, start=1)
                ],
            },
            "name": "Die Kollektion. OLESKO",
            "publisher": {
                "@id": "https://oleskostudio.com/#organization",
                "@type": "Organization",
                "address": ORG["address"],
                "contactPoint": ORG["contactPoint"],
                "email": ORG["email"],
                "name": "OLESKO",
                "sameAs": ORG["sameAs"],
                "url": "https://oleskostudio.com",
            },
            "url": "https://oleskostudio.com/de-at/collection",
        },
    },
    {
        "id": "6a8471320e6ee1e88c0037c2",
        "path": "/commission",
        "canonical": "https://oleskostudio.com/de-at/commission",
        "title": "Commission",
        "seo": {
            "title": "Einen Film beauftragen. OLESKO",
            "description": "Beauftragen Sie einen Film für Ihr exklusives Automobil, erzeugt aus Ihren Bildern.",
        },
        "openGraph": {
            "titleCopied": True,
            "descriptionCopied": True,
            "imageAssetId": "6a89dd32b52c25150dc49fbc",
        },
        "jsonLdSchema": {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "inLanguage": "de-AT",
            "description": "Beauftragen Sie einen Film für Ihr exklusives Automobil, erzeugt aus Ihren Bildern.",
            "name": "Einen Film beauftragen. OLESKO",
            "publisher": {"@type": "Organization", "name": "OLESKO", "url": "https://oleskostudio.com"},
            "url": "https://oleskostudio.com/de-at/commission",
        },
    },
    {
        "id": "6a8471331d2d68eb848af612",
        "path": "/about",
        "canonical": "https://oleskostudio.com/de-at/about",
        "title": "About",
        "seo": {
            "title": "Über. OLESKO",
            "description": "Über OLESKO. Beauftragte Filme für exklusive Automobile.",
        },
        "openGraph": {
            "titleCopied": True,
            "descriptionCopied": True,
            "imageAssetId": "6a899d738775ce81a7b4a072",
        },
        "jsonLdSchema": {
            "@context": "https://schema.org",
            "@type": "AboutPage",
            "inLanguage": "de-AT",
            "description": "Über OLESKO. Beauftragte Filme für exklusive Automobile.",
            "mainEntity": {
                "@type": "Person",
                "image": "https://cdn.prod.website-files.com/6a7b43a328ec101a40bb1d20/6a81f40a7a61e6094a0ba10b_sebastian-olesko-portrait-native.jpg",
                "jobTitle": "Gründer",
                "name": "Sebastian Olesko",
                "sameAs": [
                    "https://www.linkedin.com/in/sebastianolesko/",
                    "https://www.facebook.com/sebastianolesko/",
                ],
                "url": "https://oleskostudio.com/de-at/about",
                "worksFor": {
                    "@id": "https://oleskostudio.com/#organization",
                    "@type": "Organization",
                    "address": ORG["address"],
                    "contactPoint": ORG["contactPoint"],
                    "email": ORG["email"],
                    "name": "OLESKO",
                    "sameAs": ORG["sameAs"],
                    "url": "https://oleskostudio.com",
                },
            },
            "name": "Über. OLESKO",
            "url": "https://oleskostudio.com/de-at/about",
        },
    },
]

for pid, slug, name, desc, mux, asset, thumb, upload, seo_title in film_schema:
    url = f"https://oleskostudio.com/de-at/films/{slug}"
    seo_pages.append(
        {
            "id": pid,
            "path": f"/films/{slug}",
            "canonical": url,
            "title": name.rstrip("."),
            "seo": {"title": seo_title, "description": desc},
            "openGraph": {
                "titleCopied": True,
                "descriptionCopied": True,
                "imageAssetId": asset,
            },
            "jsonLdSchema": {
                "@context": "https://schema.org",
                "@type": "VideoObject",
                "name": name,
                "description": desc,
                "duration": "PT30S",
                "contentUrl": f"https://stream.mux.com/{mux}.m3u8",
                "embedUrl": f"https://player.mux.com/{mux}",
                "encodingFormat": "application/x-mpegURL",
                "inLanguage": "de-AT",
                "thumbnailUrl": thumb,
                "uploadDate": upload,
                "url": url,
                "publisher": {"@type": "Organization", "name": "OLESKO", "url": "https://oleskostudio.com"},
            },
        }
    )

apply["cmsLocaleId"] = CMS_LOCALE_ID
apply["localeTag"] = LOCALE_TAG
apply["subdirectory"] = LOCALE_SUBDIR
apply["notes"] = [
    "Applied to existing unpublished locale German (Austria).",
    f"localeId {LOCALE_ID} cmsLocaleId {CMS_LOCALE_ID} tag {LOCALE_TAG} subdirectory {LOCALE_SUBDIR} enabled false.",
    "Films are static pages. Do not recreate Films-cms or Posts.",
    "Do not write Imprint or Privacy DE.",
    "FAQ questions and commission submit buttons may need Designer on de-AT.",
    "Reality section is translated and stays hidden.",
    "Do not publish.",
]

seo = {
    "do_not_publish": True,
    "site_id": SITE,
    "localeId": LOCALE_ID,
    "cmsLocaleId": CMS_LOCALE_ID,
    "localeTag": LOCALE_TAG,
    "subdirectory": LOCALE_SUBDIR,
    "hreflang": {
        "note": "Webflow Localization writes en <-> de-AT hreflang after the locale exists and a page is saved. Canonical is the locale URL under /de-at/.",
        "expected": [
            {"rel": "alternate", "hreflang": "en", "href": "https://oleskostudio.com{path}"},
            {"rel": "alternate", "hreflang": "de-AT", "href": "https://oleskostudio.com/de-at{path}"},
            {"rel": "alternate", "hreflang": "x-default", "href": "https://oleskostudio.com{path}"},
        ],
    },
    "pages": seo_pages,
}

(OUT / "apply.json").write_text(json.dumps(apply, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(OUT / "seo-schema.json").write_text(json.dumps(seo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote apply.json pages={len(apply['pages'])} components={len(apply['components'])}")
print(f"wrote seo-schema.json pages={len(seo['pages'])}")
