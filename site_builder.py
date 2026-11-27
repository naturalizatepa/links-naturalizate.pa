"""Genera el sitio estático de Alfonso Villarreal con la arquitectura de Naturalízate.pa.

Uso:
    python3 -B site_builder.py

Escribe en esta carpeta las páginas de `pages_content.PAGES` y el índice de
búsqueda `catalog-index.js`. No requiere dependencias externas.
"""

import json
from html import escape
from pathlib import Path

from pages_content import EMAIL, FAQ, PAGES, WHATSAPP
from services_data import ALL_SERVICES, CATEGORIES, CATEGORY_BY_SLUG, LEGAL_GROUPS

ROOT = Path(__file__).resolve().parent

# Dominio público del sitio. Déjelo vacío mientras no exista un despliegue:
# canonical, og:url y og:image solo se emiten cuando este valor no está vacío.
SITE = ""

MAP = "https://www.google.com/maps/search/?api=1&amp;query=Ciudad+de+Panama"
GUIDE = "https://naturalizatepa.github.io/naturalizate-pa/guia.html"


def nav_link(href, label, active, key):
    current = ' aria-current="page"' if active == key else ""
    return f'<a class="nav-link" href="{href}"{current}>{label}</a>'


# Chevron único reutilizado por todos los niveles del menú (gira por CSS).
CARET = '<svg viewBox="0 0 12 12" width="11" height="11" aria-hidden="true"><path d="m2 4.5 4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /></svg>'


def menu_list(nodes, level):
    """Lista de submenú recursiva, como el MegaNavbar de la referencia.

    Los nodos con `children` despliegan un panel lateral (flyout) en escritorio
    y un acordeón anidado en móvil. Cada nivel usa el mismo marcado, de modo que
    el efecto al desplegar es idéntico en todos los niveles.
    """
    items = []
    for node in nodes:
        href, label = node["href"], escape(node["label"])
        children = node.get("children")
        if children:
            identifier = node["id"]
            items.append(
                f'<li class="nav-subitem has-submenu" data-subdropdown>'
                f'<div class="nav-subrow"><a class="nav-sublink" href="{href}">{label}</a>'
                f'<button class="nav-subcaret" type="button" aria-label="Abrir submenú de {label}" aria-expanded="false" aria-controls="{identifier}">{CARET}</button></div>'
                f'<div class="nav-subpanel" id="{identifier}">{menu_list(children, level + 1)}</div>'
                f'</li>'
            )
        else:
            items.append(f'<li class="nav-subitem"><a class="nav-sublink" href="{href}">{label}</a></li>')
    return f'<ul class="nav-menu nav-menu-l{level}">' + "".join(items) + "</ul>"


def dropdown(href, label, key, active, nodes, identifier, align_right=False):
    current = ' aria-current="page"' if active == key else ""
    panel_class = "nav-panel nav-panel-right" if align_right else "nav-panel"
    return f'''<div class="nav-item has-dropdown" data-dropdown>
      <a class="nav-link" href="{href}"{current}>{label}</a>
      <button class="nav-caret" type="button" aria-label="Abrir submenú de {label}" aria-expanded="false" aria-controls="{identifier}">{CARET}</button>
      <div class="{panel_class}" id="{identifier}">{menu_list(nodes, 2)}</div>
    </div>'''


def navigation(active):
    # Menú de tres niveles: Áreas de práctica → categoría → servicios, igual que
    # la navegación pública de la referencia, pero con el catálogo del despacho.
    areas = [
        {
            "href": f"{category['slug']}.html",
            "label": category["title"],
            "id": f"submenu-{category['slug']}",
            "children": [
                {"href": f"{category['slug']}.html#{service['slug']}", "label": service["title"]}
                for service in category["services"]
            ],
        }
        for category in CATEGORIES
    ]
    areas.append({"href": "areas-de-practica.html", "label": "Ver el catálogo completo →"})
    information = [
        {"href": "informacion-legal.html#articulos", "label": "Notas de práctica"},
        {"href": "informacion-legal.html#proceso", "label": "Etapas del trabajo"},
        {"href": "informacion-legal.html#enlaces-oficiales", "label": "Enlaces del Gobierno"},
        {"href": GUIDE, "label": "Guía de Naturalízate.pa ↗"},
    ]
    items = [
        nav_link("index.html", "Inicio", active, "inicio"),
        dropdown("areas-de-practica.html", "Áreas de práctica", "areas", active, areas, "submenu-areas"),
        nav_link("propiedad-horizontal.html", "Propiedad horizontal", active, "ph"),
        nav_link("propiedades.html", "Propiedades", active, "propiedades"),
        nav_link("honorarios.html", "Honorarios", active, "honorarios"),
        nav_link("descargo.html", "Descargo", active, "descargo"),
        dropdown("informacion-legal.html", "Información legal", "informacion", active, information, "submenu-informacion", align_right=True),
        nav_link("herramientas.html", "Herramientas", active, "herramientas"),
        nav_link("contacto.html", "Contáctenos", active, "contacto"),
    ]
    return "\n".join(items)


def header(active):
    return f'''<a class="skip-link" href="#contenido">Saltar al contenido</a>
    <header class="site-masthead">
      <div class="shell masthead-inner">
        <div class="utility-row"><span class="utility-locale"><span class="locale-mark" aria-hidden="true">PA</span> Panamá · Español</span><a href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">WhatsApp +507 6255-7583 <span aria-hidden="true">↗</span></a></div>
        <div class="brand-block"><a class="brand-link" href="index.html" aria-label="Alfonso Villarreal, página de inicio"><img src="assets/logo_horizontal_1600.png" alt="Alfonso Villarreal · Abogado" width="1600" height="400" /></a><p>Abogado · Idoneidad No. 25795 · Panamá</p></div>
      </div>
    </header>
    <nav class="site-nav" aria-label="Navegación principal">
      <div class="shell nav-inner">
        <a class="nav-mobile-brand" href="index.html" aria-label="Alfonso Villarreal, inicio"><img src="assets/icono_v_balanza.svg" alt="" width="1000" height="1000" /></a>
        <button class="menu-toggle" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
        <div class="nav-links" id="nav-links">{navigation(active)}</div>
      </div>
    </nav>'''


ORIENTATION_BAR = '''<div class="orientation-bar"><div class="shell orientation-bar-inner"><span class="ob-mark" aria-hidden="true">§</span><p><strong>El primer contacto y la orientación inicial son gratuitos.</strong> La auditoría de cada caso tiene costo y se cotiza antes de iniciar.</p><a href="honorarios.html#retainer-ph">Cómo funciona <span aria-hidden="true">→</span></a></div></div>'''


SEARCH = '''<div class="search-region">
      <form class="site-search" role="search" id="site-search" autocomplete="off">
        <label for="search-input">Buscar</label>
        <div class="search-field"><input id="search-input" type="search" placeholder="Buscar un servicio, un trámite o un área" aria-controls="search-results" /><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="10.8" cy="10.8" r="6.8" /><path d="m16 16 5.1 5.1" stroke-linecap="round" /></svg></div>
      </form>
      <div class="search-results" id="search-results" aria-live="polite" hidden></div>
    </div>'''


HERO = '''<figure class="hero-banner">
      <img src="assets/img/oficina-panama.jpg" alt="Imagen ilustrativa de una oficina jurídica con vista a la Ciudad de Panamá" width="1728" height="576" fetchpriority="high" />
      <figcaption>Imagen ilustrativa</figcaption>
    </figure>'''


def footer():
    return f'''<footer class="site-footer shell" id="contacto-pie">
      <div class="footer-columns">
        <section class="footer-form-col" aria-labelledby="footer-form-title">
          <h2 id="footer-form-title">Escríbanos</h2>
          <form class="contact-form footer-form" data-wa-form>
            <label class="visually-hidden" for="footer-name">Nombre</label><input id="footer-name" name="nombre" type="text" placeholder="Nombre" autocomplete="name" required />
            <label class="visually-hidden" for="footer-email">Correo electrónico</label><input id="footer-email" name="correo" type="email" placeholder="Correo electrónico" autocomplete="email" required />
            <label class="visually-hidden" for="footer-message">Mensaje</label><textarea id="footer-message" name="mensaje" placeholder="Mensaje" rows="4" required></textarea>
            <label class="check-line"><input type="checkbox" name="novedades" value="Sí" /> Me interesa recibir notas legales</label>
            <button class="form-submit" type="submit">Enviar <span aria-hidden="true">→</span></button>
            <p class="form-note" data-form-status role="status">Al enviar, se abrirá WhatsApp con sus datos para que revise y confirme el mensaje. No guardamos datos en esta página.</p>
          </form>
        </section>
        <section class="footer-contact-col" aria-labelledby="footer-contact-title">
          <h2 id="footer-contact-title">Contáctenos</h2>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">⌖</span><div><strong>Atención</strong><address>Ciudad de Panamá<br />Asuntos en toda la República</address></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">◔</span><div><strong>WhatsApp</strong><a href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">+507 6255-7583</a></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">✉</span><div><strong>Correo electrónico</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">§</span><div><strong>Idoneidad</strong><address>No. 25795<br />Corte Suprema de Justicia de Panamá</address></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">↗</span><div><strong>Más información</strong><a href="areas-de-practica.html">Áreas de práctica</a><a href="honorarios.html">Criterios de honorarios</a><a href="{GUIDE}" target="_blank" rel="noopener noreferrer">Guía de naturalización</a></div></div>
        </section>
        <section class="footer-map-col" aria-labelledby="footer-map-title">
          <h2 id="footer-map-title">Ubicación</h2>
          <div class="map-preview"><span class="map-schematic-label">Esquema ilustrativo</span><div class="map-streets" aria-hidden="true"><span class="map-road map-road-one"></span><span class="map-road map-road-two"></span><span class="map-road map-road-three"></span><span class="map-road map-road-four"></span><span class="map-marker"></span></div><div class="map-preview-caption"><strong>Ciudad de Panamá</strong><span>Atención en toda la República</span></div></div>
          <a class="map-open" href="{MAP}" target="_blank" rel="noopener noreferrer">Ver ubicación en Google Maps <span aria-hidden="true">↗</span></a>
        </section>
      </div>
      <div class="footer-bottom"><img src="assets/logo_horizontal_1600.png" alt="Alfonso Villarreal" width="1600" height="400" loading="lazy" /><div><p>© <span id="year">2026</span> Alfonso Villarreal · Abogado</p><small>Despacho privado. La información es general y no garantiza un resultado. Cada encargo se delimita por escrito.</small></div></div>
      <a class="floating-contact" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer" aria-label="Escribir por WhatsApp al despacho Alfonso Villarreal"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.4 11.7a8.3 8.3 0 0 1-12.1 7.4l-4.8 1.1 1.2-4.6A8.3 8.3 0 1 1 20.4 11.7Z"/><path d="M8.5 8.3c.4-.3.8-.2 1 .3l.8 1.8c.1.3.1.5-.1.8l-.6.8c.8 1.4 1.9 2.4 3.3 3.1l.7-.7c.3-.2.5-.3.8-.2l1.8.7c.5.2.6.6.3 1-.5.8-1.2 1.2-2.1 1.2-3.3-.1-7-3.5-7.1-6.9 0-.8.4-1.5 1.2-1.9Z"/></svg></a>
    </footer>'''


def structured_data():
    attorney = {
        "@type": "Attorney",
        "@id": (SITE + "#despacho") if SITE else "#despacho",
        "name": "Alfonso Villarreal",
        "description": "Despacho de abogados en Ciudad de Panamá: estrategia legal, negociación, representación y prevención en asuntos civiles, corporativos, patrimoniales, inmobiliarios, familiares, migratorios y laborales.",
        "telephone": "+507 6255-7583",
        "email": EMAIL,
        "areaServed": "PA",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Ciudad de Panamá",
            "addressCountry": "PA",
        },
        "founder": {"@type": "Person", "name": "Alfonso Villarreal", "jobTitle": "Abogado"},
        "knowsAbout": [group["title"] for group in LEGAL_GROUPS],
    }
    if SITE:
        attorney["url"] = SITE
    faq = {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}}
            for question, answer in FAQ
        ],
    }
    graph = {"@context": "https://schema.org", "@graph": [attorney, faq]}
    return (
        '<script type="application/ld+json">'
        + json.dumps(graph, ensure_ascii=False, separators=(",", ":"))
        + "</script>"
    )


def build_page(filename, page):
    title = escape(page["title"], quote=True)
    description = escape(page["description"], quote=True)
    home = page.get("home", False)
    robots = page.get("robots", "noindex, follow")
    canonical = page.get("canonical")
    if canonical is None and SITE:
        canonical = SITE if home else SITE + filename
    canonical_tag = f'<link rel="canonical" href="{canonical}" />' if canonical else ""
    og_url = f'<meta property="og:url" content="{canonical}" />' if canonical else ""
    og_image = f'<meta property="og:image" content="{SITE}og-image.png" />' if SITE else ""
    main = f'''<main class="shell main-shell{' is-home' if home else ' is-inner'}" id="contenido">
    {HERO if home else ''}
    {SEARCH}
    {page['body']}
    </main>'''
    return f'''<!doctype html>
<html lang="es-PA">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#0D1B2A" />
    <meta name="robots" content="{robots}" />
    <meta name="description" content="{description}" />
    {canonical_tag}
    <meta property="og:type" content="website" />
    <meta property="og:locale" content="es_PA" />
    <meta property="og:site_name" content="Alfonso Villarreal · Abogado" />
    {og_url}
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    {og_image}
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{description}" />
    <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png" />
    <link rel="icon" type="image/svg+xml" href="assets/icono_v_balanza.svg" />
    <link rel="apple-touch-icon" href="assets/apple-touch-180.png" />
    <link rel="manifest" href="site.webmanifest" />
    <link rel="preload" href="assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="preload" href="assets/fonts/playfair-display-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="stylesheet" href="styles.css" />
    <script src="catalog-index.js" defer></script>
    <script src="app.js" defer></script>
    {structured_data() if home else page.get('jsonld', '')}
    <title>{title}</title>
  </head>
  <body data-page="{page['active']}">
    {header(page['active'])}
    {ORIENTATION_BAR}
    {main}
    {footer()}
    {page.get('scripts', '')}
  </body>
</html>
'''


def build_catalog_index():
    entries = [
        {
            "title": service["title"],
            "detail": category["title"],
            "href": f"{category['slug']}.html#{service['slug']}",
            "terms": f"{category['title']} {service['description']}",
        }
        for category, service in ALL_SERVICES
    ]
    entries.extend(
        {"title": category["title"], "detail": "Área de práctica", "href": f"{category['slug']}.html", "terms": category["intro"]}
        for category in CATEGORIES
    )
    entries.extend(
        {"title": group["title"], "detail": "Área del derecho", "href": f"areas-de-practica.html#{group['slug']}", "terms": group["intro"]}
        for group in LEGAL_GROUPS
    )
    entries.extend([
        {"title": "Retainer legal para propiedad horizontal", "detail": "Reina Legal · 3 paquetes", "href": "propiedad-horizontal.html", "terms": "propiedad horizontal retainer reina legal edificio condominio administrador junta directiva ley 284 asamblea acta reglamento morosidad"},
        {"title": "Reina Legal Esencial", "detail": "Retainer PH · hasta 40 unidades", "href": "propiedad-horizontal.html#esencial", "terms": "paquete retainer propiedad horizontal basico prevencion"},
        {"title": "Reina Legal Preventivo", "detail": "Retainer PH · 41 a 120 unidades", "href": "propiedad-horizontal.html#preventivo", "terms": "paquete retainer propiedad horizontal asambleas morosidad reglamento"},
        {"title": "Reina Legal Integral", "detail": "Retainer PH · más de 120 unidades", "href": "propiedad-horizontal.html#integral", "terms": "paquete retainer propiedad horizontal uso mixto torres gobernanza"},
        {"title": "Auditoría legal del PH", "detail": "Diagnóstico con costo", "href": "propiedad-horizontal.html#auditoria", "terms": "auditoria legal propiedad horizontal diagnostico documentos precio"},
        {"title": "Honorarios y propuestas", "detail": "Alcance por escrito", "href": "honorarios.html", "terms": "precio costo tarifa honorarios propuesta orientacion gratuita auditoria"},
        {"title": "Contáctenos", "detail": "WhatsApp, correo y ubicación", "href": "contacto.html", "terms": "contacto telefono email whatsapp direccion"},
        {"title": "Información legal", "detail": "Notas, etapas y fuentes", "href": "informacion-legal.html", "terms": "noticias gobierno enlaces etapas proceso"},
        {"title": "Preparar una consulta", "detail": "Herramienta", "href": "herramientas.html", "terms": "herramienta seleccionar area preparar consulta"},
        {"title": "Operaciones inmobiliarias", "detail": "Compraventas y títulos", "href": "propiedades.html", "terms": "propiedades inmuebles compraventa"},
        {"title": "Descargo y aviso legal", "detail": "Alcance de la información", "href": "descargo.html", "terms": "descargo aviso legal privacidad"},
        {"title": "Naturalízate.pa", "detail": "Submarca de naturalización", "href": GUIDE, "terms": "naturalizacion nacionalidad residencia"},
    ])
    (ROOT / "catalog-index.js").write_text(
        "window.AV_SERVICE_INDEX = " + json.dumps(entries, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    return len(entries)


def main():
    build_catalog_index()
    for filename, page in PAGES.items():
        target = ROOT / filename
        target.write_text(build_page(filename, page), encoding="utf-8")
        print(f"Generated {target.name}: {target.stat().st_size} bytes")


if __name__ == "__main__":
    main()
