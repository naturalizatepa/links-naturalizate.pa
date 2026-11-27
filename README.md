# Alfonso Villarreal · Abogado — Sitio web

Sitio web estático del despacho **Alfonso Villarreal · Abogado** (Idoneidad No. 25795, Ciudad de Panamá), con la submarca **Naturalízate.pa** para naturalización panameña. Estrategia legal, negociación, representación y prevención en asuntos civiles, corporativos, patrimoniales, inmobiliarios, familiares, migratorios y laborales.

- **WhatsApp:** [+507 6255-7583](https://wa.me/50762557583)
- **Correo:** [Villarreallawyers@proton.me](mailto:Villarreallawyers@proton.me)
- **Guía de naturalización:** [naturalizatepa.github.io/naturalizate-pa/guia.html](https://naturalizatepa.github.io/naturalizate-pa/guia.html)

> El primer contacto y la orientación inicial son gratuitos. La auditoría de cada caso tiene costo y se cotiza antes de iniciar. Ningún servicio garantiza una decisión judicial o administrativa.

---

## Características principales

- **Menú multinivel** con efecto de despliegue (flyouts en escritorio, acordeón en móvil), clonado en estructura y comportamiento de la referencia kerycruz.com, pero con código original.
- **Menú principal optimizado de 6 opciones:** Inicio · Áreas de práctica · Propiedad horizontal · Honorarios · Recursos · Contáctenos (CTA dorado).
- **Áreas de práctica como acordeón de dos niveles:** cada área del derecho se despliega y, dentro, cada subsección muestra sus trámites.
- **Migas de pan** en todas las páginas internas, **menú fijo (sticky)** en escritorio y **botón «volver arriba»**.
- **Buscador** de servicios, trámites y áreas (índice en `catalog-index.js`, tecla `/` para enfocar).
- **Brand Book & Bible** completo en `brandbook.html` y **62 activos de marca** listos para usar.
- **Formularios que preparan un mensaje de WhatsApp** (no almacenan datos en la página).
- **Accesible:** HTML semántico, `aria-current`, `skip-link`, foco visible y soporte de `prefers-reduced-motion`.

---

## Estructura del sitio (20 páginas generadas)

| Página | Archivo | Contenido |
|---|---|---|
| Portada | `index.html` | Presentación, puertas persona/empresa, áreas, retainer PH, método, FAQ y preparación de consulta |
| Áreas de práctica | `areas-de-practica.html` | Catálogo completo en acordeón (10 áreas del derecho · 11 categorías · 110 servicios) |
| Propiedad horizontal | `propiedad-horizontal.html` | Retainer legal **Reina Legal**: 3 paquetes, auditoría y frentes de trabajo |
| Operaciones inmobiliarias | `propiedades.html` | Revisión jurídica de compraventas |
| Honorarios | `honorarios.html` | Criterios de propuesta y rangos del retainer PH |
| Información legal | `informacion-legal.html` | Notas de práctica, etapas del trabajo y enlaces del Gobierno |
| Preparar una consulta | `herramientas.html` | Herramienta para ordenar el primer mensaje |
| Contáctenos | `contacto.html` | Formulario, WhatsApp, correo y ubicación |
| Descargo | `descargo.html` | Aviso legal y alcance de la información |
| 404 | `404.html` | Página de error con enlaces útiles |
| 10 páginas de categoría | `sociedades.html`, `litigios.html`, `patrimonio.html`, `empresas.html`, `propiedad-intelectual.html`, `bienes-raices.html`, `familia.html`, `migracion.html`, `trabajo.html`, `servicios-estrategicos.html` | Ficha de cada categoría con sus servicios |

Además, `brandbook.html` es el manual de marca independiente y `links.html` conserva la antigua página de enlaces (link-hub) de Naturalízate.pa.

---

## Áreas de práctica

10 áreas del derecho que agrupan 11 categorías y **110 servicios**:

1. Derecho corporativo y comercial
2. Litigios y derecho procesal
3. Derecho patrimonial y sucesorio
4. Propiedad intelectual y regulación
5. Derecho inmobiliario
6. Derecho de familia
7. Derecho migratorio y nacionalidad
8. Derecho laboral y permisos de trabajo
9. Asesoría jurídica empresarial
10. Propiedad horizontal y comunidades

Cada servicio enlaza a su ficha y a un contacto prellenado por área y servicio.

---

## Marca

Manual completo en **[`brandbook.html`](brandbook.html)** (10 capítulos: esencia, logotipo, color, tipografía, voz, imagen, aplicaciones, marca de agua, activos y submarca).

### Paleta — regla 60·30·10

| % | Rol | Color | Variación |
|---|---|---|---|
| **60%** | Principal / dominante | Navy `#0D1B2A` | Navy medio `#1B3A57` |
| **30%** | Secundarios / textos y complementos | Marfil `#F5F1E8` + Pizarra `#5C6772` | Blanco `#FFFFFF` |
| **10%** | Acento / elementos clave | Dorado `#C5A572` | Dorado oscuro `#A5814D` |

### Tipografía

- **Playfair Display** (serif, normal + itálica) para títulos.
- **Inter** (sans) para texto y UI.
- Autoalojadas en `assets/fonts/` (woff2), sin depender de Google Fonts.

### Activos de marca (62 archivos en `assets/brand/`)

Generados con precisión desde los SVG reales del despacho:

- **Logotipos** (29): principal, horizontal, isotipo, blanco, dark, naturalízate y variantes en 1600/800/400 px.
- **Iconos / favicon** (8): 512, 192, 180, 64, 32, 16 + app icon.
- **Marcas de agua** (5): isotipo, logo, patrón diagonal, texto diagonal y versión blanca.
- **Redes / web** (8): OG 1200×630, Twitter 1500×500, Instagram post 1080² y story 1080×1920, LinkedIn 1584×396, Facebook 820×312, WhatsApp 500², YouTube 2560×1440.
- **Papelería** (4): tarjeta frente/reverso (90×50 mm), membrete A4 y firma de correo.
- **Brandbook** (7): barra 60·30·10 y muestras de color.

El índice de activos está en `assets/brand/manifest.json`.

---

## Arquitectura técnica

Sitio **estático sin dependencias de servidor**. Se genera con Python y se sirve como archivos planos.

- `site_builder.py` — generador: navegación, cabecera, pie, migas de pan, páginas, índice de búsqueda, `robots.txt` y `sitemap.xml`.
- `pages_content.py` — contenido y componentes de cada página.
- `services_data.py` — catálogo de categorías, servicios y áreas del derecho.
- `styles.css` — estilos (marca, menú multinivel, acordeón, navegación optimizada).
- `app.js` — menú, buscador, formularios de WhatsApp, mapa bajo demanda, volver arriba y apertura de anclas.
- `catalog-index.js` — índice de búsqueda (generado).
- `tools/build-brand-assets.mjs` — generador de activos de marca (usa `sharp`).

### Cómo generar el sitio

```bash
python3 -B site_builder.py
# o bien:
npm run build
```

Regenera las 20 páginas, `catalog-index.js` y `robots.txt`. El `sitemap.xml` solo se genera cuando se define el dominio público en la constante `SITE` de `site_builder.py`.

### Cómo regenerar los activos de marca

```bash
npm install        # instala sharp (una sola vez)
npm run brand      # = node tools/build-brand-assets.mjs
```

### Vista previa local

```bash
python3 -m http.server 8000 --bind 0.0.0.0
# abrir http://localhost:8000/
```

---

## Estructura de archivos

```
.
├── index.html … (20 páginas generadas)
├── brandbook.html          # Manual de marca independiente
├── links.html              # Link-hub heredado de Naturalízate.pa
├── site_builder.py         # Generador del sitio
├── pages_content.py        # Contenido de las páginas
├── services_data.py        # Catálogo de servicios
├── styles.css              # Estilos
├── app.js                  # Interacción
├── catalog-index.js        # Índice de búsqueda (generado)
├── robots.txt              # Generado
├── site.webmanifest        # PWA básica
├── assets/
│   ├── fonts/              # Playfair Display + Inter (woff2)
│   ├── img/                # Imágenes de contenido
│   ├── brand/              # 62 activos de marca + manifest.json
│   └── logo_*.svg / *.png  # Logotipos e iconos fuente
├── tools/
│   └── build-brand-assets.mjs
└── package.json            # scripts build / brand
```

---

## SEO y despliegue

- Meta `description`, Open Graph y Twitter Card en cada página.
- Datos estructurados `schema.org` (`Attorney` + `FAQPage` en portada; `Service` en propiedad horizontal).
- `robots.txt` permitido; las páginas conservan `noindex, follow` mientras no haya despliegue público.
- Para publicar: define `SITE` en `site_builder.py` (p. ej. `https://tu-dominio/`), regenera y ajusta el meta robots a `index, follow` si deseas indexación. Se emitirán `canonical`, `og:url`, `og:image` y `sitemap.xml`.

---

## Contacto y enlaces

- **WhatsApp:** [+507 6255-7583](https://wa.me/50762557583)
- **Correo:** [Villarreallawyers@proton.me](mailto:Villarreallawyers@proton.me)
- **Sitio / guía Naturalízate.pa:** [naturalizatepa.github.io/naturalizate-pa](https://naturalizatepa.github.io/naturalizate-pa/)
- **Instagram:** [@naturalizate.pa](https://www.instagram.com/naturalizate.pa/)
- **TikTok:** [@naturalizate.pa](https://www.tiktok.com/@naturalizate.pa)
- **LinkedIn:** [Alfonso Villarreal](https://www.linkedin.com/in/naturalizate-pa/)

---

## Aviso

Despacho privado. La información del sitio es general y no garantiza un resultado. Cada encargo se delimita por escrito. Consulta el [descargo](descargo.html) completo.

© 2026 Alfonso Villarreal · Abogado · Idoneidad No. 25795, Panamá.
