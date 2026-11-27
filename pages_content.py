"""Contenido del sitio Alfonso Villarreal en los componentes de Naturalízate.pa.

La estructura y las formas (masthead, bandas de portada, rejilla 75/25,
tarjetas de puerta, vías, banda oscura, perfil, FAQ, formulario y pie de
tres columnas) provienen de naturalizate-pa-main-v5. El texto, el catálogo y
la marca son del despacho Alfonso Villarreal.
"""

import json
from html import escape
from urllib.parse import quote

from services_data import CATEGORIES, CATEGORY_BY_SLUG, GROUP_BY_CATEGORY, LEGAL_GROUPS

WHATSAPP = "https://wa.me/50762557583?text=Hola%2C%20quisiera%20conversar%20sobre%20un%20asunto%20legal%20con%20el%20despacho%20Alfonso%20Villarreal."
EMAIL = "Villarreallawyers@proton.me"
NATURALIZATE = "https://naturalizatepa.github.io/naturalizate-pa/"
GUIDE = NATURALIZATE + "guia.html"

# Regla comercial única del sitio: la orientación inicial no se cobra; la
# auditoría del caso sí, porque supone revisar documentos y emitir criterio.
ORIENTATION_NOTE = "<strong>El primer contacto y la orientación inicial son gratuitos.</strong> La auditoría de cada caso tiene costo: revisar documentos, reglamento o expediente y emitir un criterio por escrito es trabajo profesional y se cotiza antes de comenzar."


def orientation_note(extra=""):
    return f'''<div class="orientation-note"><span class="on-label">Condiciones de atención</span><p>{ORIENTATION_NOTE}{extra}</p></div>'''


def sidebar(title="Áreas de práctica", exclude=None):
    links = "\n".join(
        f'<li><a href="areas-de-practica.html#{group["slug"]}">{escape(group["title"])}</a></li>'
        for group in LEGAL_GROUPS
        if exclude not in group["categories"]
    )
    return f'''<aside class="related-sidebar" aria-label="{escape(title)}">
        <h2>{escape(title)}</h2>
        <ul>{links}</ul>
        <div class="legal-precision"><p>Antes de avanzar, revise su situación con el despacho.</p><a class="text-action" href="contacto.html">Solicitar una conversación →</a></div>
      </aside>'''


def category_options():
    return "\n".join(
        f'<option value="{escape(cat["slug"])}">{escape(cat["title"])}</option>' for cat in CATEGORIES
    )


FAQ = [
    (
        "¿Cómo empieza un encargo?",
        "Con una orientación inicial gratuita: se escucha el problema y se indica si hace falta una revisión formal. Después de esa conversación, la auditoría del caso tiene costo y se cotiza según los documentos y el alcance. Con esa revisión el despacho presenta por escrito la propuesta antes de que usted decida contratar.",
    ),
    (
        "¿La orientación inicial es gratuita?",
        "Sí. El primer contacto y la orientación general no tienen costo. No incluyen revisión de documentos ni un dictamen: eso es precisamente la auditoría del caso, que sí se cobra porque exige leer el expediente, contrastarlo con la norma y entregar un criterio por escrito.",
    ),
    (
        "¿Qué es el retainer legal Reina Legal para propiedad horizontal?",
        "Es un acompañamiento mensual para administradores y juntas directivas de edificios y condominios. Incluye revisión de convocatorias, actas, contratos y estrategia de cobro según el nivel contratado. Antes de iniciar se realiza una auditoría legal del PH, que se cotiza aparte, y luego se propone por escrito el paquete y sus límites.",
    ),
    (
        "¿Cuánto cuestan los servicios?",
        "No hay una tarifa única: dos asuntos de la misma categoría pueden requerir trabajo distinto. La orientación inicial es gratuita y la auditoría del caso se cotiza. Como excepción, el retainer de propiedad horizontal publica rangos referenciales «desde» para sus tres paquetes; el monto final se confirma después de la auditoría y por escrito.",
    ),
    (
        "¿Se garantizan resultados o plazos?",
        "No. Las decisiones dependen de autoridades, contrapartes y terceros. El despacho explica riesgos y etapas, pero no promete aprobaciones, montos de recuperación ni fechas que no controla.",
    ),
    (
        "¿Atienden asuntos fuera de la ciudad?",
        "Sí. El despacho atiende asuntos en toda la República de Panamá y puede coordinar la comunicación por canales remotos cuando el caso lo permite.",
    ),
    (
        "¿Qué información envío en el primer mensaje?",
        "Describa el problema y su objetivo sin adjuntar pasaportes, datos bancarios ni documentos completos. Primero se acuerda el canal y el alcance; después se solicita la documentación necesaria.",
    ),
    (
        "¿La naturalización panameña forma parte del despacho?",
        "Sí. La práctica migratoria incluye la naturalización y se atiende también bajo la submarca Naturalízate.pa, con una guía pública de requisitos y una ruta de evaluación propia.",
    ),
]


def home():
    groups = "\n".join(
        f'''<article class="via-card">
          <span class="via-num">{group['number']} · Área del derecho</span>
          <h3><a href="areas-de-practica.html#{group['slug']}">{escape(group['title'])}</a></h3>
          <p>{escape(group['intro'])}</p>
          <a class="via-link" href="areas-de-practica.html#{group['slug']}">Ver trámites →</a>
        </article>'''
        for group in LEGAL_GROUPS
    )
    faqs = "\n".join(
        f'''<div class="faq-item">
          <h3><button class="faq-q" type="button" aria-expanded="false" aria-controls="faq-{index}"><span class="faq-num">{index:02d}</span>{escape(question)}<span class="faq-mark" aria-hidden="true">+</span></button></h3>
          <div class="faq-a" id="faq-{index}" hidden><p>{escape(answer)}</p></div>
        </div>'''
        for index, (question, answer) in enumerate(FAQ, 1)
    )
    return f'''<div class="content-columns home-columns">
      <article class="article-main">
        <h1>Estrategia legal antes de la demanda.</h1>
        <div class="article-text home-article">
          <figure class="portrait"><img src="assets/foto_alfonso.jpg" alt="Retrato del Lic. Alfonso Villarreal" width="480" height="720" /><figcaption>Lic. Alfonso Villarreal</figcaption></figure>
          <p>Recuperar, negociar, proteger y prevenir. El despacho explica qué opciones existen, qué riesgo tiene cada una y cuál es el siguiente paso antes de comprometer recursos en un proceso.</p>
          <p>Alfonso Villarreal es abogado en la República de Panamá, con idoneidad No. 25795. El trabajo empieza por comprender el problema, revisar los documentos y definir una ruta de negociación, prevención o representación. Si demandar no conviene, el despacho lo dice.</p>
          <p>La práctica integra asuntos <strong>civiles, corporativos, patrimoniales, inmobiliarios, familiares, migratorios y laborales</strong>. También ofrece recuperación de activos, asesoría jurídica externa, capacitaciones para equipos y el <strong>retainer legal Reina Legal para propiedad horizontal</strong>.</p>
          <p>Cada servicio se delimita después de una revisión individual: no se presumen tarifas, resultados ni plazos por el nombre de una categoría. El alcance se presenta por escrito antes de contratar.</p>
          <p>La naturalización panameña se atiende además bajo la submarca <a href="migracion.html#naturalizacion-panama">Naturalízate.pa</a>, con una guía pública de requisitos y una ruta de evaluación propia.</p>
          <p class="signature"><strong>Lic. Alfonso Villarreal</strong><br />Abogado · Idoneidad No. 25795</p>
        </div>
      </article>
      {sidebar("En esta página")}
    </div>
    <section class="home-band alt" id="puertas">
      <div class="band-head"><span class="eyebrow">Dos puertas de entrada claras</span><h2>Elija por dónde empieza: <em>persona</em> o <em>empresa</em></h2><p>El mismo estándar de revisión, con un alcance distinto según quien consulta. En ambos casos la propuesta se entrega por escrito.</p></div>
      <div class="doors-grid">
        <article class="door-card">
          <span class="door-badge">Puerta A · Personas y familias</span>
          <h3>Patrimonio, familia e inmigración</h3>
          <p class="door-price">A su medida <small>Alcance definido después de revisar el caso</small></p>
          <p><strong>Para quién:</strong> personas que necesitan ordenar un patrimonio, resolver un asunto familiar, comprar o vender un inmueble o gestionar una ruta migratoria.</p>
          <p class="door-subhead">Se revisa</p>
          <ul class="check-list"><li>Titularidad de bienes y sucesiones.</li><li>Patria potestad y asuntos de familia.</li><li>Compraventas y documentación registral.</li><li>Visas, residencias y naturalización.</li><li>Riesgo antes de firmar o demandar.</li></ul>
          <p class="door-subhead">No incluye</p>
          <ul class="check-list muted"><li>Dictamen sin revisar documentos.</li><li>Garantía de resultados o plazos.</li><li>Asesoría fiscal o contable.</li><li>Derecho extranjero.</li></ul>
          <a class="button-primary door-cta" href="contacto.html?perfil=persona">Consultar como persona <span aria-hidden="true">→</span></a>
        </article>
        <article class="door-card featured">
          <span class="door-badge">Puerta B · Empresas y administraciones</span>
          <h3>Sociedades, contratos y cumplimiento</h3>
          <p class="door-price">Por proyecto <small>Propuesta con tareas incluidas y excluidas</small></p>
          <p>Estructuración societaria, revisión contractual, propiedad intelectual, permisos y acompañamiento recurrente para equipos que toman decisiones.</p>
          <p class="door-subhead">Se revisa</p>
          <ul class="check-list"><li>Constitución, cambios y cierre de entidades.</li><li>Contratos comerciales y auditoría contractual.</li><li>Marcas y registros sanitarios.</li><li>Permisos de trabajo y cumplimiento laboral.</li><li>Departamento jurídico externo.</li><li>Retainer legal Reina Legal para propiedad horizontal.</li></ul>
          <p class="door-subhead">No incluye</p>
          <ul class="check-list muted"><li>Representación sin mandato escrito.</li><li>Resultados ante autoridades.</li><li>Auditoría contable o financiera.</li><li>Decisiones de negocio del cliente.</li></ul>
          <a class="button-primary door-cta" href="contacto.html?perfil=empresa">Consultar como empresa <span aria-hidden="true">→</span></a>
        </article>
      </div>
    </section>
    <section class="home-band" id="areas">
      <div class="band-head"><span class="eyebrow">La práctica · I–X</span><h2>Diez áreas del derecho, un mismo estándar.</h2><p>Seleccione el ámbito jurídico y después el trámite específico. El catálogo reúne asuntos de empresas, personas y comunidades.</p></div>
      <div class="vias-grid">{groups}</div>
      <p class="legal-precision">Los nombres de las áreas describen ámbitos de atención. No equivalen a una oferta de resultado: cada encargo requiere comprobar hechos, documentación y alcance antes de aceptarse.</p>
      <div class="inline-actions" style="margin-top:18px"><a class="button-primary" href="areas-de-practica.html">Ver el catálogo completo <span aria-hidden="true">→</span></a><a class="text-action" href="honorarios.html">Cómo se cotiza</a></div>
    </section>
    <section class="home-band alt" id="retainer-ph">
      <div class="band-head"><span class="eyebrow">Nuevo · Retainer legal Reina Legal</span><h2>El edificio no necesita más abogados. <em>Necesita prevención.</em></h2><p>Un acompañamiento mensual para administradores y juntas directivas de propiedad horizontal: reglamento, asambleas, actas, contratos y cobro revisados antes de que se conviertan en conflicto.</p></div>
      <div class="retainer-mini-grid">
        <article class="retainer-mini"><span class="package-tag">Nivel 1</span><h3>Reina Legal Esencial</h3><p>Hasta 40 unidades. Ordena convocatorias, actas y contratos básicos con respaldo documental.</p><p class="retainer-from">Desde B/. 350/mes</p></article>
        <article class="retainer-mini featured"><span class="package-tag">Nivel 2</span><h3>Reina Legal Preventivo</h3><p>41–120 unidades. Suma asambleas, morosidad, reglamento y un informe trimestral para la junta.</p><p class="retainer-from">Desde B/. 750/mes</p></article>
        <article class="retainer-mini"><span class="package-tag">Nivel 3</span><h3>Reina Legal Integral</h3><p>Más de 120 unidades o uso mixto. Gobierno, contratos, cobro prejudicial y acompañamiento permanente.</p><p class="retainer-from">Desde B/. 1,450/mes</p></article>
      </div>
      <div class="orientation-inline"><span aria-hidden="true">§</span><p>{ORIENTATION_NOTE}</p></div>
      <div class="inline-actions"><a class="button-primary" href="propiedad-horizontal.html">Ver el retainer y los tres paquetes <span aria-hidden="true">→</span></a><a class="text-action" href="propiedad-horizontal.html#auditoria">Qué incluye la auditoría</a></div>
    </section>
    <section class="home-band audit-band" id="metodo">
      <div class="band-head"><span class="eyebrow on-dark">Cómo trabajamos</span><h2>Estrategia. Negociación. Ejecución.</h2><p>Un proceso claro antes de comprometernos con una ruta jurídica.</p></div>
      <div class="audit-grid">
        <div>
          <h3>Tres decisiones antes de actuar</h3>
          <ul class="check-list"><li><strong>Entender.</strong> Escuchamos el objetivo y revisamos contratos, antecedentes y documentos relevantes.</li><li><strong>Definir.</strong> Explicamos opciones, riesgos, plazos que dependen de terceros y alcance de la propuesta.</li><li><strong>Actuar.</strong> Negociamos o gestionamos el asunto dentro del mandato acordado, con comunicación directa.</li><li><strong>Comunicar.</strong> Cada etapa tiene un responsable y un canal definido.</li><li><strong>Cerrar.</strong> Entregamos el resultado documental y las recomendaciones de prevención.</li></ul>
          <blockquote class="audit-quote">«No solo le explico el problema. Le digo qué hacer.»</blockquote>
        </div>
        <div class="audit-price-card">
          <span class="ap-label">Propuesta del despacho</span>
          <p class="ap-price ap-price-text">Orientación gratuita</p>
          <p class="ap-mode"><strong>El primer contacto no tiene costo.</strong> La auditoría del caso sí: revisar documentos, reglamento o expediente exige trabajo profesional y se cotiza antes de iniciar. El alcance y los honorarios se confirman por escrito.</p>
          <a class="button-primary ap-button" href="honorarios.html">Ver criterios de honorarios <span aria-hidden="true">→</span></a>
          <p class="ap-alt">¿Prefiere conversar primero? <a href="contacto.html">Escríbanos →</a></p>
        </div>
      </div>
      <p class="audit-disclaimer">Ningún servicio contratado garantiza una decisión judicial o administrativa. Los tiempos dependen de autoridades y contrapartes.</p>
    </section>
    <section class="home-band" id="perfil">
      <div class="profile-grid">
        <figure class="profile-photo"><img src="assets/foto_alfonso.jpg" alt="Lic. Alfonso Villarreal, abogado en Panamá" width="480" height="720" loading="lazy" /><figcaption>Lic. Alfonso Villarreal · Idoneidad No. 25795</figcaption></figure>
        <div>
          <span class="eyebrow">El despacho</span>
          <h2>Una firma que dice la verdad y luego ejecuta.</h2>
          <p>Alfonso Villarreal ejerce en la República de Panamá. La práctica combina prevención y representación: revisar antes de firmar, negociar antes de litigar y litigar cuando la vía extrajudicial no resuelve.</p>
          <p>El despacho atiende asuntos en toda la República y trabaja con documentos, no con promesas. Cuando un caso requiere asesoría contable, fiscal o de derecho extranjero, lo indica y coordina con la persona profesional correspondiente.</p>
          <div class="pillars">
            <div><h3>Prevención</h3><p>Contratos, auditorías y estructuración para reducir contingencias.</p></div>
            <div><h3>Negociación</h3><p>Rutas proporcionales antes de asumir el costo de un proceso.</p></div>
            <div><h3>Representación</h3><p>Gestión y seguimiento dentro de un mandato escrito.</p></div>
          </div>
          <p class="profile-addr">Ciudad de Panamá · Asuntos en toda la República</p>
          <div class="inline-actions"><a class="button-primary" href="areas-de-practica.html">Conocer las áreas <span aria-hidden="true">→</span></a><a class="text-action" href="contacto.html">Hablar con el despacho</a></div>
        </div>
      </div>
    </section>
    <section class="home-band alt" id="preguntas">
      <div class="band-head"><span class="eyebrow">Preguntas frecuentes</span><h2>Lo que conviene saber antes de escribir.</h2><p>Respuestas generales sobre alcance, honorarios y forma de trabajo.</p></div>
      <div class="faq-list">{faqs}</div>
    </section>
    <section class="home-band" id="calificacion">
      <div class="band-head"><span class="eyebrow">Prepare su consulta</span><h2>Cinco datos para ordenar el primer mensaje.</h2><p>Esta herramienta no emite un dictamen, no calcula impuestos y no guarda datos: prepara un mensaje de WhatsApp para que usted lo revise y decida si lo envía.</p></div>
      <form class="qual-form" data-qual-form>
        <div class="qual-progress"><span id="qual-count">0 de 5 respondidas</span><div class="progress-track" role="progressbar" aria-valuemin="0" aria-valuemax="5" aria-valuenow="0"><span id="qual-progress"></span></div></div>
        <div class="qual-grid">
          <p class="qual-field"><label for="q-area">Área de práctica <span>*</span></label><select id="q-area" name="Área" data-qual-field required><option value="">Seleccione un área</option>{category_options()}</select></p>
          <p class="qual-field"><label for="q-perfil">Quién consulta <span>*</span></label><select id="q-perfil" name="Perfil" data-qual-field required><option value="">Seleccione</option><option>Persona natural</option><option>Empresa o sociedad</option><option>Fundación o administración</option><option>Otro</option></select></p>
          <p class="qual-field"><label for="q-estado">Estado del asunto</label><select id="q-estado" name="Estado" data-qual-field><option value="">Seleccione</option><option>Solo estoy evaluando</option><option>Hay un plazo próximo</option><option>Ya existe un proceso</option><option>Necesito revisar un documento</option></select></p>
          <p class="qual-field"><label for="q-docs">Documentos disponibles</label><select id="q-docs" name="Documentos" data-qual-field><option value="">Seleccione</option><option>Contratos o acuerdos</option><option>Documentos de propiedad</option><option>Resoluciones o notificaciones</option><option>Ninguno por ahora</option></select></p>
          <p class="qual-field"><label for="q-objetivo">Objetivo principal</label><select id="q-objetivo" name="Objetivo" data-qual-field><option value="">Seleccione</option><option>Prevenir un conflicto</option><option>Negociar un acuerdo</option><option>Recuperar un activo</option><option>Iniciar o defender un proceso</option><option>Ordenar un trámite</option></select></p>
        </div>
        <div class="qual-actions"><button class="button-primary" type="submit">Preparar mensaje <span aria-hidden="true">→</span></button><a class="text-action" href="contacto.html">Prefiero el formulario de correo</a></div>
        <p class="form-note" data-qual-status role="status">Se abrirá WhatsApp con sus respuestas para que las revise. No incluya datos sensibles en este primer contacto.</p>
      </form>
    </section>
    <section class="home-band closing-band" id="contacto">
      <div><span class="eyebrow">Su siguiente paso</span><h2>Problemas legales. Soluciones claras.</h2><p>Describa el asunto. Le indicaremos cómo iniciar una evaluación y qué documentos conviene tener a mano.</p></div>
      <div class="inline-actions"><a class="button-primary light" href="contacto.html">Solicitar orientación <span aria-hidden="true">→</span></a><a class="button-primary outline-light" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">WhatsApp ↗</a></div>
    </section>'''


CHEVRON = '<svg class="pa-chev" viewBox="0 0 12 12" width="14" height="14" aria-hidden="true"><path d="m2 4.5 4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" /></svg>'


def practice_index():
    sections = []
    for gi, group in enumerate(LEGAL_GROUPS):
        cats = [CATEGORY_BY_SLUG[slug] for slug in group["categories"]]
        total = sum(len(c["services"]) for c in cats)
        audience = " ".join(c["audience"] for c in cats)
        subs = []
        for cat in cats:
            services = "".join(
                f'<li><a href="{cat["slug"]}.html#{svc["slug"]}"><span class="pa-svc-title">{escape(svc["title"])}</span><small>{escape(svc["description"])}</small></a></li>'
                for svc in cat["services"]
            )
            subs.append(f'''<details class="pa-details pa-level2">
            <summary class="pa-summary pa-sub-summary"><span class="pa-title">{escape(cat['title'])}</span><span class="pa-count">{len(cat['services'])} servicios</span>{CHEVRON}</summary>
            <div class="pa-body">
              <p class="pa-intro">{escape(cat['intro'])}</p>
              <ul class="pa-services">{services}</ul>
              <a class="pa-more" href="{cat['slug']}.html">Ver el área completa <span aria-hidden="true">→</span></a>
            </div>
          </details>''')
        opened = " open" if gi == 0 else ""
        sections.append(f'''<section class="content-section pa-group" id="{group['slug']}">
        <details class="pa-details pa-level1"{opened}>
          <summary class="pa-summary"><span class="pa-head"><span class="section-index">{group['number']} · Área del derecho</span><span class="pa-title">{escape(group['title'])}</span></span><span class="pa-count">{len(cats)} áreas · {total} servicios</span>{CHEVRON}</summary>
          <div class="pa-body">
            <p>{escape(group['intro'])}</p>
            <p class="audience-line"><strong>A quién ayudamos:</strong> {escape(audience)}</p>
            <div class="pa-subsections">{''.join(subs)}</div>
          </div>
        </details>
      </section>''')
    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <span class="eyebrow">Áreas de práctica</span>
      <h1>Áreas del derecho. Trámites específicos.</h1>
      <p>Despliegue cada área del derecho y, dentro de ella, cada subsección para ver sus trámites. Cada ficha indica a quién ayuda; alcance, documentos y honorarios se acuerdan tras revisar el asunto.</p>
      <span class="count-chip">{sum(len(cat['services']) for cat in CATEGORIES)} servicios en {len(LEGAL_GROUPS)} áreas del derecho</span>
    </div>
        {orientation_note()}
        {''.join(sections)}
        <div class="route-next"><h2>¿No ve exactamente su caso?</h2><p>Descríbalo y le indicaremos si el despacho puede asumirlo y en qué condiciones.</p><a class="button-primary" href="contacto.html">Consultar mi asunto <span aria-hidden="true">→</span></a></div>
      </article>
      {sidebar("Otras secciones")}
    </div>'''


def category_page(category):
    group = GROUP_BY_CATEGORY[category["slug"]]
    services = "\n".join(
        f'''<a href="contacto.html?servicio={quote(item['title'])}&amp;area={quote(category['title'])}" id="{item['slug']}"><span>{category['number']} {index:02d}</span><strong>{escape(item['title'])}</strong><small>{escape(item['description'])}</small><small class="persona-line"><strong>Para quién:</strong> {escape(item['persona'])}</small></a>'''
        for index, item in enumerate(category["services"], 1)
    )
    signals = "".join(f"<li>{escape(signal)}</li>" for signal in category.get("signals", []))
    special = ""
    if category["slug"] == "migracion":
        special = f'''<div class="service-subbrand"><img src="assets/logo_naturalizate_1600.png" alt="Naturalízate.pa" width="1600" height="610" loading="lazy" /><div><p>La naturalización se atiende también bajo Naturalízate.pa, submarca del despacho Alfonso Villarreal, con guía pública de requisitos.</p><a href="{GUIDE}" target="_blank" rel="noopener noreferrer">Leer la guía de Naturalízate.pa ↗</a></div></div>'''
    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <a class="breadcrumb" href="areas-de-practica.html#{group['slug']}">← {escape(group['title'])}</a>
      <span class="eyebrow">{category['number']} · Área de práctica</span>
      <h1>{escape(category['title'])}</h1>
      <p>{escape(category['intro'])}</p>
      <span class="count-chip">{len(category['services'])} servicios para evaluar</span>
        </div>
        <section class="audience-panel">
          <span class="eyebrow">A quién ayudamos</span>
          <h2>El servicio se explica desde su situación, no desde el trámite.</h2>
          <p>{escape(category['audience'])}</p>
          <p class="audience-label">Señales de que conviene revisar el caso</p>
          <ul class="signal-list">{signals}</ul>
        </section>
        <div class="article-list">{services}</div>
        {special}
        {orientation_note()}
        <div class="route-next"><h2>La ruta comienza por los hechos.</h2><p>La primera conversación no tiene costo y sirve para saber si hace falta una revisión formal. La auditoría del caso se cotiza antes de iniciar.</p><a class="button-primary" href="contacto.html?area={quote(category['title'])}">Hablar con el despacho <span aria-hidden="true">→</span></a></div>
      </article>
      {sidebar("Otras áreas", category['slug'])}
    </div>'''


def properties():
    category = CATEGORY_BY_SLUG["bienes-raices"]
    rows = "\n".join(
        f'''<a href="bienes-raices.html#{item['slug']}"><span>{category['number']} {index:02d}</span><strong>{escape(item['title'])}</strong><small>{escape(item['description'])}</small></a>'''
        for index, item in enumerate(category["services"], 1)
    )
    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <span class="eyebrow">Operaciones inmobiliarias</span>
      <h1>Documentos claros antes de firmar.</h1>
      <p>Esta sección reúne servicios jurídicos de compraventa; no es un portal de inmuebles ni publica propiedades de terceros.</p>
        </div>
        <div class="content-section"><h2>Compraventas, personas y sociedades.</h2><p>Un contrato inmobiliario exige revisar la titularidad, las facultades de quien firma y las obligaciones que asumirá cada parte. El análisis se adapta a la operación concreta.</p></div>
        <div class="article-list">{rows}</div>
        <div class="route-next"><h2>Antes de la firma.</h2><p>Reunimos título, paz y salvo, identificación de las partes y el borrador del contrato para señalar riesgos y pasos pendientes.</p><a class="button-primary" href="contacto.html?area=Bienes%20ra%C3%ADces">Solicitar revisión de operación <span aria-hidden="true">→</span></a></div>
      </article>
      {sidebar("Áreas relacionadas", "bienes-raices")}
    </div>'''


def fees():
    rows = "\n".join(
        f'''<tr><th scope="row"><a href="{cat['slug']}.html">{escape(cat['title'])}</a></th><td>{len(cat['services'])} servicios · alcance según el caso.</td><td>Propuesta por escrito</td></tr>'''
        for cat in CATEGORIES
    )
    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <span class="eyebrow">Honorarios</span>
      <h1>Primero, entender el asunto. Después, cotizar.</h1>
      <p>No todos los expedientes requieren el mismo trabajo. El despacho comunica alcance, honorarios, gastos externos y condiciones por escrito antes de contratar. La única excepción son los rangos referenciales del retainer de propiedad horizontal, que se publican como orientación y se confirman después de la auditoría.</p>
        </div>
        {orientation_note()}
        <section class="content-section" id="retainer-ph">
          <span class="eyebrow">Retainer legal · Propiedad horizontal</span>
          <h2>Tres niveles Reina Legal, un mismo criterio preventivo.</h2>
          <p>El retainer es mensual y se contrata después de una auditoría legal del edificio, que se cotiza aparte. Los montos indicados son un punto de partida referencial: el paquete definitivo depende de unidades, torres, uso mixto y estado documental.</p>
          <div class="table-scroll" tabindex="0" role="region" aria-label="Paquetes del retainer de propiedad horizontal">
            <table class="fees-table"><caption>Paquetes del retainer Reina Legal</caption>
              <thead><tr><th scope="col">Paquete</th><th scope="col">Para quién</th><th scope="col">Desde</th></tr></thead>
              <tbody>
                <tr><th scope="row"><a href="propiedad-horizontal.html#esencial">Reina Legal Esencial</a></th><td>Hasta 40 unidades, administración interna o con poco respaldo jurídico.</td><td>B/. 350/mes</td></tr>
                <tr><th scope="row"><a href="propiedad-horizontal.html#preventivo">Reina Legal Preventivo</a></th><td>41–120 unidades con administradora externa y junta directiva activa.</td><td>B/. 750/mes</td></tr>
                <tr><th scope="row"><a href="propiedad-horizontal.html#integral">Reina Legal Integral</a></th><td>Más de 120 unidades, uso mixto, varias torres o conflicto recurrente.</td><td>B/. 1,450/mes</td></tr>
              </tbody>
            </table>
          </div>
          <div class="inline-actions"><a class="button-primary" href="propiedad-horizontal.html">Ver qué incluye cada paquete <span aria-hidden="true">→</span></a><a class="text-action" href="propiedad-horizontal.html#auditoria">Costo y alcance de la auditoría</a></div>
          <p class="legal-small">Montos en balboas (B/.), a la par del dólar estadounidense. No incluyen litigios, cobro judicial, gastos registrales ni erogaciones de terceros; esos conceptos se cotizan por separado.</p>
        </section>
        <div class="table-scroll" tabindex="0" role="region" aria-label="Tabla de áreas y propuestas; desplace horizontalmente si es necesario">
          <table class="fees-table"><caption>Áreas del despacho y criterio de propuesta</caption>
            <thead><tr><th scope="col">Área</th><th scope="col">Qué se define</th><th scope="col">Honorarios</th></tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </div>
        <section class="content-section"><h2>Qué debe figurar en una propuesta</h2><p>Identidad del asunto, tareas incluidas y excluidas, responsables, gastos ajenos al despacho y forma de pago. No se garantiza una decisión judicial o administrativa por la contratación de un servicio.</p>
          <ul class="check-list"><li>Delimitación del encargo y entregables.</li><li>Honorarios, anticipos y gastos externos.</li><li>Supuestos y documentos que debe aportar el cliente.</li><li>Condiciones de terminación y comunicación.</li></ul>
        </section>
        <div class="route-next"><h2>¿Necesita una propuesta?</h2><p>Describa el asunto y los documentos disponibles. Con esa información el despacho puede indicar si acepta el encargo y en qué condiciones.</p><a class="button-primary" href="contacto.html">Solicitar propuesta <span aria-hidden="true">→</span></a></div>
      </article>
      {sidebar("Áreas de práctica")}
    </div>'''


def resources():
    notes = "\n".join([
        '''<a href="propiedad-horizontal.html"><span>Propiedad horizontal</span><strong>Prevenir el conflicto en un edificio.</strong><small>Reglamento, asambleas, actas, morosidad y responsabilidad de la junta directiva bajo la Ley 284.</small></a>''',
        '''<a href="empresas.html#contratos-negociacion"><span>Contratos</span><strong>Qué revisar antes de firmar un acuerdo.</strong><small>Objeto, obligaciones, plazos, terminación y vías para resolver diferencias.</small></a>''',
        '''<a href="litigios.html#resolucion-disputas"><span>Disputas</span><strong>Negociación antes de litigio.</strong><small>Los documentos y los objetivos del cliente ayudan a elegir una ruta proporcional.</small></a>''',
        f'''<a href="{GUIDE}" target="_blank" rel="noopener noreferrer"><span>Migración</span><strong>Ordenar un expediente de nacionalidad.</strong><small>La submarca Naturalízate.pa ofrece una guía específica sobre residencia y solvencia.</small></a>''',
    ])
    steps = "\n".join([
        '''<li><span>01</span><div><strong>Consulta y clasificación</strong><p>Se identifica el área, el objetivo y si existe un plazo próximo.</p></div></li>''',
        '''<li><span>02</span><div><strong>Revisión documental</strong><p>Se comprueban hechos, títulos, contratos y comunicaciones relevantes.</p></div></li>''',
        '''<li><span>03</span><div><strong>Propuesta por escrito</strong><p>Alcance, honorarios, gastos y condiciones antes de contratar.</p></div></li>''',
        '''<li><span>04</span><div><strong>Ejecución y seguimiento</strong><p>Negociación, presentación o gestión según el mandato acordado.</p></div></li>''',
    ])
    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <span class="eyebrow">Información legal</span>
      <h1>Información útil para tomar decisiones.</h1>
      <p>Recursos de carácter general. No sustituyen la revisión de documentos ni una opinión jurídica sobre un caso específico.</p>
        </div>
        {orientation_note()}
        <section class="content-section" id="articulos"><span class="eyebrow">Notas de práctica</span><h2>Antes de actuar</h2>
          <div class="article-list">{notes}</div>
        </section>
        <section class="content-section" id="proceso"><span class="eyebrow">Etapas del trabajo</span><h2>Cómo se ordena un encargo</h2>
          <ol class="process-steps">{steps}</ol>
        </section>
        <section class="content-section" id="enlaces-oficiales"><span class="eyebrow">Fuentes institucionales</span><h2>Enlaces del Gobierno</h2><p>Verifique los procedimientos vigentes directamente con las autoridades competentes.</p>
          <ul class="official-links"><li><a href="https://www.tribunal-electoral.gob.pa/" target="_blank" rel="noopener noreferrer">Tribunal Electoral de Panamá ↗</a></li><li><a href="https://www.migracion.gob.pa/" target="_blank" rel="noopener noreferrer">Servicio Nacional de Migración ↗</a></li><li><a href="https://www.panamadigital.gob.pa/" target="_blank" rel="noopener noreferrer">Panamá Digital ↗</a></li></ul>
        </section>
        <section class="content-section" id="guia"><span class="eyebrow">Guías del despacho</span><h2>Naturalización panameña</h2><p>Consulte la guía pública de Naturalízate.pa sobre residencia, vínculos familiares y documentación, o revise la ficha de <a href="migracion.html#naturalizacion-panama">naturalización</a> dentro del catálogo.</p><div class="inline-actions"><a class="button-primary" href="{GUIDE}" target="_blank" rel="noopener noreferrer">Abrir la guía ↗</a><a class="text-action" href="migracion.html">Ver servicios migratorios</a></div>
        </section>
        <div class="article-callout"><span class="callout-mark" aria-hidden="true">§</span><div><h2>Una nota general no resuelve un caso.</h2><p>Si el asunto tiene plazos, documentos o una contraparte identificada, conviene una revisión individual.</p><a class="button-primary" href="contacto.html">Solicitar orientación <span aria-hidden="true">→</span></a></div></div>
      </article>
      {sidebar("Temas relacionados")}
    </div>'''


def tool():
    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <span class="eyebrow">Herramienta de preparación</span>
      <h1>Empiece con el problema, no con un formulario interminable.</h1>
      <p>Seleccione un área y complete cinco datos para preparar un mensaje. Esta herramienta no calcula impuestos, no almacena datos y no emite un dictamen.</p>
        </div>
        <form class="qual-form" data-qual-form>
          <div class="qual-progress"><span id="qual-count">0 de 5 respondidas</span><div class="progress-track" role="progressbar" aria-valuemin="0" aria-valuemax="5" aria-valuenow="0"><span id="qual-progress"></span></div></div>
          <div class="qual-grid">
            <p class="qual-field"><label for="t-area">Área de práctica <span>*</span></label><select id="t-area" name="Área" data-qual-field required><option value="">Seleccione un área</option>{category_options()}</select></p>
            <p class="qual-field"><label for="t-servicio">Servicio o tema <span>*</span></label><input id="t-servicio" name="Servicio" data-qual-field type="text" required placeholder="Ej. revisión de contrato" /></p>
            <p class="qual-field"><label for="t-perfil">Quién consulta</label><select id="t-perfil" name="Perfil" data-qual-field><option value="">Seleccione</option><option>Persona natural</option><option>Empresa o sociedad</option><option>Fundación o administración</option></select></p>
            <p class="qual-field"><label for="t-urgencia">¿Existe un plazo próximo?</label><select id="t-urgencia" name="Plazo" data-qual-field><option value="">Seleccione</option><option>No, estoy evaluando</option><option>Sí, en los próximos días</option><option>Sí, ya venció</option></select></p>
            <p class="qual-field"><label for="t-resumen">Resuma su pregunta (opcional)</label><textarea id="t-resumen" name="Resumen" data-qual-field rows="4" maxlength="320" placeholder="Indique qué necesita resolver, sin datos sensibles."></textarea></p>
          </div>
          <div class="qual-actions"><button class="button-primary" type="submit">Preparar consulta <span aria-hidden="true">→</span></button><a class="text-action" href="contacto.html">Usar el formulario de correo</a></div>
          <p class="form-note" data-qual-status role="status">El mensaje se abrirá en WhatsApp para que usted decida si lo envía. Ninguna respuesta se guarda en la página.</p>
        </form>
        <div class="article-callout"><span class="callout-mark" aria-hidden="true">§</span><div><h2>¿Buscaba una calculadora de impuestos?</h2><p>Las tasas y reglas pueden cambiar. No mostramos un cálculo sin datos oficiales actualizados; solicite una revisión de la operación para obtener una estimación fundada.</p><a class="text-action" href="propiedades.html">Ver operaciones inmobiliarias →</a></div></div>
      </article>
      {sidebar("Áreas del despacho")}
    </div>'''


def disclaimer():
    sections = [
        ("Ámbito de la práctica", "Alfonso Villarreal es abogado en la República de Panamá. Los temas enumerados en el sitio describen áreas de atención, pero cada encargo requiere confirmar hechos, alcance profesional y condiciones de representación. Para derecho extranjero o asesoría contable, consulte a la persona profesional correspondiente.", ""),
        ("Información general, no un dictamen", "Textos, guías, notas y herramientas son informativos. No constituyen una recomendación para una persona concreta, no reemplazan una revisión de documentos y pueden requerir actualización. No se garantizan resultados, montos de recuperación, decisiones de autoridades ni plazos.", ""),
        ("Mensajes y relación profesional", "El envío de un correo, un mensaje de WhatsApp o un formulario no establece por sí solo una relación de representación. Evite compartir datos sensibles antes de que se acuerde un canal y un alcance de atención. El despacho puede solicitar información adicional y evaluar si acepta un asunto.", ""),
        ("Orientación gratuita y auditoría con costo", "El primer contacto y la orientación inicial son gratuitos: consisten en escuchar el planteamiento y señalar si requiere una revisión formal. No incluyen lectura de documentos ni un dictamen. La auditoría de cada caso tiene costo, se cotiza antes de comenzar y puede incluir revisión documental, contraste normativo e informe escrito. Los rangos publicados del retainer de propiedad horizontal son referenciales y no constituyen una oferta vinculante.", "orientacion-auditoria"),
        ("Relaciones comerciales y enlaces externos", "Los enlaces a portales públicos, mapas, redes y aplicaciones de mensajería conducen a sitios gestionados por terceros. El despacho no controla su contenido, disponibilidad o prácticas de privacidad. Incluirlos no equivale a avalarlos.", "relaciones-comerciales"),
        ("Formularios y datos", "El buscador y la herramienta de preparación operan en el navegador. Los formularios de este sitio preparan un mensaje de WhatsApp o un correo mailto: la persona usuaria confirma el envío en su aplicación. El enlace a WhatsApp transmite el texto al servicio externo cuando se abre y al despacho solo si se envía. No hay una bandeja de entrada ni suscripción automática a boletines.", ""),
    ]
    body = "\n".join(
        '<section class="content-section"{ident}><h2>{title}</h2><p>{text}</p></section>'.format(
            ident=f' id="{anchor}"' if anchor else "",
            title=escape(title),
            text=escape(text),
        )
        for title, text, anchor in sections
    )
    return f'''<div class="content-columns">
      <article class="article-main legal-content">
        <div class="page-heading">
      <span class="eyebrow">Descargo</span>
      <h1>Aviso legal.</h1>
      <p>El contenido de esta web es general. Antes de tomar decisiones sobre un asunto, consulte su situación y documentos con un profesional.</p>
        </div>
        {body}
        <div class="article-callout"><span class="callout-mark" aria-hidden="true">§</span><div><h2>¿Necesita orientación individual?</h2><p>Describa su asunto sin enviar documentación sensible por el primer mensaje.</p><a class="button-primary" href="contacto.html">Contactar al despacho <span aria-hidden="true">→</span></a></div></div>
      </article>
      {sidebar("Temas relacionados")}
    </div>'''


def contact():
    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <span class="eyebrow">Contáctenos</span>
      <h1>Conversemos con los documentos sobre la mesa.</h1>
      <p>Cuéntenos qué sucede y cuál es su objetivo. No incluya números de pasaporte, datos bancarios o documentos completos en el primer mensaje.</p>
        </div>
        {orientation_note(" Si su asunto requiere revisión documental, la auditoría se cotiza antes de abrir expediente.")}
        <form class="contact-form contact-main-form" data-wa-form>
          <div class="form-row"><label for="main-name">Nombre <span>*</span></label><input id="main-name" name="nombre" type="text" autocomplete="name" placeholder="Nombre completo" required /></div>
          <div class="form-row"><label for="main-email">Correo electrónico <span>*</span></label><input id="main-email" name="correo" type="email" autocomplete="email" placeholder="nombre@dominio.com" required /></div>
          <div class="form-row"><label for="main-phone">WhatsApp o teléfono</label><input id="main-phone" name="telefono" type="tel" autocomplete="tel" placeholder="+507" /></div>
          <div class="form-row"><label for="main-area">Área de interés</label><select id="main-area" name="area"><option value="">Seleccione un área</option>{category_options()}</select></div>
          <div class="form-row"><label for="main-service">Servicio o tema</label><input id="main-service" name="servicio" type="text" placeholder="Ej. revisión de contrato de compraventa" /></div>
          <div class="form-row"><label for="main-message">Mensaje <span>*</span></label><textarea id="main-message" name="mensaje" rows="6" placeholder="Describa el asunto y su objetivo, sin datos sensibles." required></textarea></div>
          <label class="check-line"><input type="checkbox" name="novedades" value="Sí" /> Me interesa recibir notas legales</label>
          <div class="contact-form-actions"><button class="form-submit" type="submit">Preparar mensaje <span aria-hidden="true">→</span></button><a class="text-action" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">Prefiero WhatsApp ↗</a></div>
          <p class="form-note" data-form-status role="status">Se abrirá WhatsApp con sus datos para que revise y confirme el mensaje. No guardamos datos en esta página. <a href="descargo.html">Lea el descargo</a>.</p>
        </form>
        <section class="content-section" style="margin-top:26px"><h2>Contacto directo</h2>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">◔</span><div><strong>WhatsApp</strong><a href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">+507 6255-7583</a></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">✉</span><div><strong>Correo electrónico</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">⌖</span><div><strong>Atención</strong><address>Ciudad de Panamá<br />Asuntos en toda la República</address></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">§</span><div><strong>Idoneidad</strong><address>No. 25795<br />Corte Suprema de Justicia de Panamá</address></div></div>
        </section>
        <div class="map-load" data-map-container><div class="map-load-inner"><span aria-hidden="true">⌖</span><p>Ciudad de Panamá</p><button type="button" data-load-map>Cargar mapa</button><small>Mapa de Google. Al cargarlo se conecta con un servicio externo.</small></div></div>
      </article>
      {sidebar("Servicios del despacho")}
    </div>'''


def propiedad_horizontal():
    category = CATEGORY_BY_SLUG["propiedad-horizontal"]
    pain_points = [
        ("Un reglamento que ya no coincide con la ley", "El reglamento anterior a la Ley 284 sigue rigiendo en lo que no se le oponga, pero lo que la contradice quedó sin efecto. Muchos edificios siguen votando con reglas vencidas y producen acuerdos que después no se sostienen."),
        ("Convocatorias y quórum calculados de memoria", "Una asamblea mal convocada o votada puede dejar sin base el aumento de cuota, la obra o el cambio de administrador. El costo aparece meses después, cuando hay que repetir todo y explicar por qué."),
        ("Actas que no prueban nada", "Actas sin firmas, sin anexos o sin la votación por unidad convierten una decisión legítima en una discusión. La junta queda sin evidencia de lo que aprobó y de cuándo lo comunicó."),
        ("Morosidad cobrada sin criterio uniforme", "Cobrar solo a algunos, tolerar años de deuda o iniciar procesos sin expediente produce trato desigual. La Ley 467 de 2025 reformó el cobro de gastos comunes ante jueces comunitarios: conviene revisar cómo se está usando esa vía."),
        ("Sanciones sin debido proceso", "Multas por ruido, mascotas, filtraciones u obras aplicadas sin notificación ni oportunidad de defensa son el terreno típico de reclamos, medidas cautelares y cuestionamientos a la administración."),
        ("Contratos de los que no se puede salir", "Contratos de administración, seguridad o mantenimiento sin niveles de servicio, sin causales de terminación y sin control de gastos dejan a la junta atada justo cuando necesita herramientas."),
        ("Conflictos de interés y renuncias sin documentar", "Directivos que deciden sobre su propia unidad, contratistas vinculados a un miembro de la junta o renuncias que nunca se inscribieron exponen a las personas y contaminan la validez de los acuerdos."),
        ("Cada junta empieza de cero", "La nueva junta recibe el edificio sin inventario de contratos, litigios, actas, seguros y obligaciones. Lo que no se documenta se repite como problema y como costo para todos los propietarios."),
    ]
    pains = "".join(
        f"<li><strong>{escape(title)}</strong><p>{escape(text)}</p></li>"
        for title, text in pain_points
    )

    packages = [
        {
            "id": "esencial",
            "tag": "Nivel 1",
            "name": "Reina Legal Esencial",
            "target": "PH de hasta 40 unidades con administración interna o un administrador con poco respaldo jurídico.",
            "summary": "Ordenar lo básico para que las decisiones del año no dependan de modelos copiados de otro edificio.",
            "price": "B/. 350",
            "items": [
                "Revisión de 2 convocatorias y 2 actas al año (ordinaria y extraordinaria).",
                "Hasta 2 consultas legales al mes por correo o WhatsApp, con respuesta en 5 días hábiles.",
                "Revisión de hasta 3 contratos de proveedores al año.",
                "Plantillas de convocatoria, acta, notificación y sanción con debido proceso.",
                "Alertas normativas y guía de abstenciones para la junta directiva.",
            ],
            "excludes": "No incluye asistencia a asambleas, litigios, cobro judicial ni trámites registrales.",
            "featured": False,
        },
        {
            "id": "preventivo",
            "tag": "Nivel 2 · Más solicitado",
            "name": "Reina Legal Preventivo",
            "target": "PH de 41 a 120 unidades con administradora externa y junta directiva activa.",
            "summary": "El nivel para edificios que ya tienen conflictos recurrentes y necesitan criterio antes de cada asamblea.",
            "price": "B/. 750",
            "items": [
                "Todo lo del nivel Esencial, sin límite de consultas ordinarias.",
                "Acompañamiento en 1 asamblea ordinaria y 1 extraordinaria al año.",
                "Revisión de hasta 8 contratos al año, incluido el contrato de administración.",
                "Revisión del reglamento y plan de adecuación a la Ley 284 para someterlo a la asamblea.",
                "Estrategia trimestral de morosidad y revisión de estados de cuenta modelo.",
                "Informe trimestral de riesgos para la junta directiva, con respuesta en 72 horas.",
            ],
            "excludes": "No incluye procesos judiciales, cobro con abogado externo ni gastos de notaría o registro.",
            "featured": True,
        },
        {
            "id": "integral",
            "tag": "Nivel 3",
            "name": "Reina Legal Integral",
            "target": "PH de más de 120 unidades, uso mixto, varias torres o comunidades con conflicto persistente.",
            "summary": "Gobierno del edificio completo: juntas, contratos, cobro prejudicial y exposición de directivos bajo control.",
            "price": "B/. 1,450",
            "items": [
                "Todo lo del nivel Preventivo, con hasta 4 asambleas acompañadas al año.",
                "Revisión de contratos y pliegos de licitación sin límite razonable de alcance.",
                "Manual de gobierno: sanciones, cobro, compras, conflictos de interés y traspaso de junta.",
                "Reunión mensual con la junta directiva y capacitación anual a directivos y propietarios.",
                "Coordinación de cobro prejudicial y apoyo en impugnaciones de acuerdos.",
                "Canal prioritario con respuesta en 48 horas y atención el mismo día para medidas urgentes.",
            ],
            "excludes": "No incluye honorarios judiciales, peritajes, caución ni erogaciones de terceros.",
            "featured": False,
        },
    ]
    cards = "".join(
        f'''<article class="package-card{' featured' if pkg['featured'] else ''}" id="{pkg['id']}">
          <span class="package-tag">{pkg['tag']}</span>
          <h3>{pkg['name']}</h3>
          <p class="package-target"><strong>Para quién:</strong> {escape(pkg['target'])}</p>
          <p class="package-price">{pkg['price']}<small>desde / mes</small></p>
          <p class="package-summary">{escape(pkg['summary'])}</p>
          <p class="package-subhead">Incluye</p>
          <ul class="check-list">{''.join(f'<li>{escape(item)}</li>' for item in pkg['items'])}</ul>
          <p class="package-excludes">{escape(pkg['excludes'])}</p>
          <a class="button-primary package-cta" href="contacto.html?area=Propiedad%20horizontal&amp;servicio={quote(pkg['name'])}">Consultar este paquete <span aria-hidden="true">→</span></a>
        </article>'''
        for pkg in packages
    )

    ph_services = "".join(
        f'''<a href="contacto.html?area=Propiedad%20horizontal&amp;servicio={quote(item['title'])}" id="{item['slug']}"><span>Servicio PH · {index:02d}</span><strong>{escape(item['title'])}</strong><small>{escape(item['description'])}</small><small class="persona-line"><strong>Para quién:</strong> {escape(item['persona'])}</small></a>'''
        for index, item in enumerate(category["services"], 1)
        if item["slug"] != "retainer-ph"
    )

    audit_items = [
        "Reglamento de copropiedad vigente y contraste con la Ley 284 de 2022.",
        "Actas y acuerdos de los últimos 24 meses: convocatoria, quórum, mayorías y ejecución.",
        "Contratos vigentes con administradora, seguridad, mantenimiento y proveedores críticos.",
        "Estado de morosidad, criterios de cobro y expedientes en curso.",
        "Integración de la junta directiva, abstenciones, renuncias y conflictos de interés.",
        "Seguros, fondo de imprevistos, reservas y gastos extraordinarios aprobados.",
        "Litigios, reclamos y comunicaciones relevantes de propietarios o autoridades.",
    ]
    audit_list = "".join(f"<li>{escape(item)}</li>" for item in audit_items)

    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <span class="eyebrow">Retainer legal · Propiedad horizontal</span>
      <h1>Prevenir el conflicto cuesta menos que administrarlo.</h1>
      <p>Retainer legal Reina Legal para administradores y juntas directivas de edificios y condominios. Reglamento, asambleas, actas, contratos y cobro revisados antes de que se conviertan en demanda.</p>
      <span class="count-chip">3 paquetes · Ley 284 de 2022</span>
        </div>
        {orientation_note()}

        <section class="content-section" id="problema">
          <span class="eyebrow">El problema</span>
          <h2>El administrador y el presidente no pierden por falta de voluntad. Pierden por falta de respaldo.</h2>
          <p>En propiedad horizontal, casi ningún conflicto empieza en un juzgado. Empieza en una convocatoria enviada tarde, un acta incompleta, una multa sin notificación o un contrato que nadie leyó completo. Cuando el problema llega al abogado, el costo ya se multiplicó: hay que reconstruir documentos, repetir asambleas y responder ante propietarios que exigen resultados.</p>
          <p>Estos son los dolores que se repiten en las administraciones que buscan ayuda:</p>
          <ul class="risk-list">{pains}</ul>
        </section>

        <section class="content-section" id="a-quien-ayudamos">
          <span class="eyebrow">A quién ayudamos</span>
          <h2>Dos personas cargan con la decisión. Las dos necesitan lo mismo: criterio documentado.</h2>
          <p>El retainer no se vende a "un edificio". Se diseña para las dos personas que firman, convocan y responden. Por eso el contenido, los tiempos de respuesta y los entregables se definen según su realidad, no según un catálogo genérico.</p>
          <div class="persona-grid">
            <article class="persona-card">
              <span class="persona-tag">Perfil 1 · Quien ejecuta</span>
              <h3>Administrador o administradora de PH</h3>
              <dl class="persona-meta">
                <div><dt>Edad y rol</dt><dd>34–58 años. Administra entre 2 y 8 edificios, propios o de una administradora externa. Reporta a varias juntas a la vez.</dd></div>
                <div><dt>Su día</dt><dd>Atiende quejas, cobra, coordina mantenimiento, arma la convocatoria y responde mensajes de propietarios que lo culpan de todo.</dd></div>
                <div><dt>Lo que quiere</dt><dd>Que el edificio funcione, que la morosidad baje y que nadie lo cuestione por una decisión que tomó sin respaldo.</dd></div>
                <div><dt>Lo que teme</dt><dd>Ser demandado personalmente, perder el contrato de administración o quedar expuesto ante la junta por un error documental.</dd></div>
                <div><dt>Lo que dice</dt><dd>«No puedo pagar un abogado por cada duda» · «Me piden una decisión para ayer» · «Eso siempre se hizo así».</dd></div>
                <div><dt>Qué necesita</dt><dd>Respuestas rápidas, plantillas utilizables y un respaldo escrito que pueda mostrar cuando la decisión se cuestione.</dd></div>
              </dl>
            </article>
            <article class="persona-card">
              <span class="persona-tag">Perfil 2 · Quien responde</span>
              <h3>Presidente o presidenta de la junta directiva</h3>
              <dl class="persona-meta">
                <div><dt>Edad y rol</dt><dd>40–65 años. Propietario elegido en asamblea. Su cargo es ad honorem y le consume entre 6 y 15 horas al mes.</dd></div>
                <div><dt>Su día</dt><dd>Firma actas, autoriza gastos, media entre vecinos y recibe reclamos que no siempre puede resolver.</dd></div>
                <div><dt>Lo que quiere</dt><dd>Cumplir el cargo sin exponerse, dejar el edificio ordenado y evitar que una discusión de pasillo termine en demanda.</dd></div>
                <div><dt>Lo que teme</dt><dd>Responsabilidad personal por decisiones de la junta, asambleas conflictivas, impugnaciones y exposición en redes sociales.</dd></div>
                <div><dt>Lo que dice</dt><dd>«Firmé lo que me pusieron» · «No soy abogado» · «Para qué pagar si el reglamento ya lo dice».</dd></div>
                <div><dt>Qué necesita</dt><dd>Saber qué puede decidir, qué debe consultar y cómo documentar el acuerdo para que la junta no quede sola.</dd></div>
              </dl>
            </article>
          </div>
        </section>

        <section class="content-section" id="mercado">
          <span class="eyebrow">Lectura del mercado</span>
          <h2>Por qué la prevención en PH dejó de ser un lujo.</h2>
          <p>El mercado panameño de propiedad horizontal creció en altura y en complejidad. Un edificio dejó de ser un grupo de vecinos con un reglamento: es una operación con presupuesto, personal, contratistas, seguros, datos personales y decisiones que pueden terminar ante la autoridad o en tribunales. La administración se profesionalizó, pero el respaldo jurídico de la junta no siempre creció al mismo ritmo.</p>
          <p>Cuatro fuerzas explican la demanda actual de acompañamiento preventivo:</p>
          <div class="market-forces">
            <div><strong>1. La Ley 284 creó un régimen nuevo.</strong><p>Subrogó la Ley 31 de 2010 con 125 artículos, reglas propias de quórum, mayorías, junta directiva y administrador, y una Dirección de Propiedad Horizontal con decisiones vinculantes. La transición dejó reglamentos desactualizados y juntas interpretando normas que no conocen.</p></div>
            <div><strong>2. El reglamento de la ley sigue pendiente.</strong><p>Sin reglamento detallado, la interpretación cotidiana recae en la administración y en la junta. Ese vacío es exactamente donde aparece el riesgo: cada decisión se toma sin una guía única.</p></div>
            <div><strong>3. El costo operativo presiona la cuota.</strong><p>Seguridad, mantenimiento, energía y seguros suben. Con caja ajustada, la morosidad y el uso del fondo de reserva se vuelven decisiones sensibles que deben estar bien documentadas.</p></div>
            <div><strong>4. La junta responde con su nombre.</strong><p>Propietarios, administradoras y autoridades piden explicaciones a personas que ocupan el cargo por elección, no por profesión. La diferencia entre un acuerdo válido y uno impugnable suele ser un acta y una convocatoria bien hechas.</p></div>
          </div>
          <div class="table-scroll" tabindex="0" role="region" aria-label="Segmentos de propiedad horizontal y paquete sugerido">
            <table class="fees-table market-table"><caption>Segmentos de mercado y necesidad dominante</caption>
              <thead><tr><th scope="col">Segmento</th><th scope="col">Dolor dominante</th><th scope="col">Paquete sugerido</th></tr></thead>
              <tbody>
                <tr><th scope="row">Hasta 40 unidades</th><td>Decisiones sin respaldo jurídico, presupuesto ajustado y junta sin experiencia.</td><td>Reina Legal Esencial</td></tr>
                <tr><th scope="row">41–120 unidades</th><td>Morosidad, asambleas disputadas y contratos heredados sin salida.</td><td>Reina Legal Preventivo</td></tr>
                <tr><th scope="row">Más de 120 unidades o uso mixto</th><td>Gobernanza compleja, varias torres, contratos grandes y exposición de directivos.</td><td>Reina Legal Integral</td></tr>
              </tbody>
            </table>
          </div>
          <p class="legal-small">Esta lectura es cualitativa y no cita cifras de mercado. Antes de publicar estadísticas conviene verificarlas con MIVIOT, el INEC o el Registro Público. La información sobre la Ley 284 y la Ley 467 es general y no sustituye una revisión del caso.</p>
        </section>

        <section class="content-section" id="paquetes">
          <span id="retainer-ph" aria-hidden="true"></span>
          <span class="eyebrow">Los tres paquetes</span>
          <h2>Elija por complejidad, no por precio.</h2>
          <p>Los tres niveles comparten el mismo estándar: revisión documental, criterio escrito y respuesta dentro de un plazo comprometido. Cambia la intensidad del acompañamiento y el número de frentes que se cubren. Los montos son referenciales y se confirman después de la auditoría del edificio.</p>
          <div class="package-grid">{cards}</div>
          <p class="legal-small">Precios en balboas (B/.), a la par del dólar estadounidense. Todo paquete exige una auditoría legal inicial cotizada aparte y un contrato escrito con alcance, exclusiones y condiciones de terminación. La disponibilidad se confirma después de revisar el edificio.</p>
        </section>

        <section class="content-section" id="servicios-ph">
          <span class="eyebrow">Frentes de trabajo</span>
          <h2>Diez frentes que se atienden dentro del retainer.</h2>
          <p>El paquete mensual no es una bolsa de horas indeterminada: cada frente tiene un entregable y un límite. Estos son los servicios que se activan según el nivel contratado y la prioridad que fije la junta.</p>
          <div class="article-list">{ph_services}</div>
        </section>

        <section class="content-section" id="auditoria">
          <span class="eyebrow">Antes del retainer</span>
          <h2>La auditoría legal del PH: se cobra y se explica.</h2>
          <p>No se puede prometer prevención sin saber qué hay dentro del edificio. La auditoría es el paso previo obligatorio y tiene costo propio, porque implica leer documentos, contrastarlos con la ley y entregar un diagnóstico por escrito. Es un trabajo profesional, no una conversación exploratoria.</p>
          <p class="package-subhead">Qué revisa</p>
          <ul class="check-list services-columns">{audit_list}</ul>
          <p class="package-subhead">Qué entrega</p>
          <ul class="check-list"><li>Informe con matriz de riesgo por tema (alto, medio, bajo) y norma aplicable.</li><li>Plan de trabajo a 90 días con prioridades y responsables.</li><li>Sesión de presentación ante la junta directiva y propuesta del paquete que corresponde.</li></ul>
          <p><strong>Referencia:</strong> desde B/. 750. El monto final depende de unidades, torres, uso mixto, años de documentación y estado de los expedientes. Se informa por escrito antes de comenzar y no se descuenta del retainer salvo que la propuesta lo indique.</p>
        </section>

        <section class="content-section" id="como-empieza">
          <span class="eyebrow">Ruta de entrada</span>
          <h2>Primero se conversa. Después se audita. Después se acompaña.</h2>
          <ol class="process-steps">
            <li><span>01</span><div><strong>Orientación inicial gratuita</strong><p>Escuchamos el problema, identificamos el tipo de PH y señalamos si hace falta revisión documental. Sin costo y sin dictamen.</p></div></li>
            <li><span>02</span><div><strong>Auditoría del caso, con costo</strong><p>Se revisan reglamento, actas, contratos, morosidad y riesgos de la junta. Se cotiza antes de iniciar y se entrega informe escrito.</p></div></li>
            <li><span>03</span><div><strong>Retainer mensual</strong><p>Con el diagnóstico, se propone el paquete Esencial, Preventivo o Integral, con alcance, exclusiones y honorarios por escrito.</p></div></li>
          </ol>
        </section>

        <div class="orientation-inline"><span aria-hidden="true">§</span><p>{ORIENTATION_NOTE}</p></div>

        <div class="route-next"><h2>¿Su edificio tiene una asamblea o un conflicto próximo?</h2><p>Empiece por la orientación gratuita. Si el caso requiere revisión documental, le indicaremos el costo de la auditoría antes de abrir expediente. No se prometen resultados ni plazos que dependan de la asamblea, de la autoridad o de la contraparte.</p><a class="button-primary" href="contacto.html?area=Propiedad%20horizontal&amp;servicio=Retainer%20Reina%20Legal">Solicitar orientación <span aria-hidden="true">→</span></a></div>
        <p class="legal-small">Fuentes generales: Ley 284 de 14 de febrero de 2022, Gaceta Oficial 29476-C, que subroga la Ley 31 de 2010; Ley 467 de 24 de abril de 2025, Gaceta Oficial 30265. Verifique siempre el texto vigente y su aplicación al caso concreto.</p>
      </article>
      <aside class="related-sidebar" aria-label="Contenido del retainer">
        <h2>En esta página</h2>
        <ul><li><a href="propiedad-horizontal.html#problema">El problema</a></li><li><a href="propiedad-horizontal.html#a-quien-ayudamos">A quién ayudamos</a></li><li><a href="propiedad-horizontal.html#mercado">Lectura del mercado</a></li><li><a href="propiedad-horizontal.html#paquetes">Los tres paquetes</a></li><li><a href="propiedad-horizontal.html#servicios-ph">Frentes de trabajo</a></li><li><a href="propiedad-horizontal.html#auditoria">La auditoría</a></li><li><a href="propiedad-horizontal.html#como-empieza">Cómo empieza</a></li></ul>
        <div class="legal-precision"><p>El primer contacto es gratuito. La auditoría de cada caso tiene costo y se cotiza antes de iniciar.</p><a class="text-action" href="contacto.html">Solicitar una conversación →</a></div>
      </aside>
    </div>'''


def not_found():
    return f'''<div class="content-columns">
      <article class="article-main">
        <div class="page-heading">
      <span class="eyebrow">Error 404</span>
      <h1>Esta página no existe, pero su asunto sí tiene inicio.</h1>
      <p>La dirección que abrió pudo cambiar o escribirse con error. Vuelva al inicio o escriba directamente al despacho.</p>
      <div class="inline-actions" style="margin-top:18px"><a class="button-primary" href="index.html">Ir al inicio <span aria-hidden="true">→</span></a><a class="text-action" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">Hablar con un asesor <span aria-hidden="true">↗</span></a></div>
    </div>
        <section class="content-section"><h2>Quizá buscaba</h2>
        <div class="article-list"><a href="areas-de-practica.html"><span>Catálogo</span><strong>Áreas de práctica</strong><small>Los diez ámbitos y sus trámites.</small></a><a href="propiedad-horizontal.html"><span>Retainer</span><strong>Propiedad horizontal</strong><small>Prevención para administradores y juntas directivas.</small></a><a href="honorarios.html"><span>Propuestas</span><strong>Honorarios</strong><small>Cómo se define el alcance y el costo.</small></a><a href="contacto.html"><span>Contacto</span><strong>Escríbanos</strong><small>WhatsApp, correo y formulario.</small></a></div>
      </section>
      </article>
      {sidebar("Áreas de práctica")}
    </div>'''


PAGES = {
    "index.html": {
        "title": "Alfonso Villarreal · Abogado en Panamá",
        "description": "Estrategia legal, negociación y representación en Panamá. Áreas de práctica, criterios de honorarios y contacto con el Lic. Alfonso Villarreal.",
        "active": "inicio",
        "home": True,
        "body": home(),
    },
    "areas-de-practica.html": {
        "title": "Áreas de práctica | Alfonso Villarreal",
        "description": "Catálogo de servicios civiles, corporativos, inmobiliarios, familiares, migratorios y laborales del despacho Alfonso Villarreal.",
        "active": "areas",
        "body": practice_index(),
    },
    "propiedades.html": {
        "title": "Operaciones inmobiliarias | Alfonso Villarreal",
        "description": "Revisión jurídica de compraventas inmobiliarias en Panamá para personas y sociedades.",
        "active": "propiedades",
        "body": properties(),
    },
    "propiedad-horizontal.html": {
        "title": "Retainer legal para propiedad horizontal | Alfonso Villarreal",
        "description": "Retainer legal Reina Legal para administradores y juntas directivas de PH: reglamento, asambleas, actas, contratos y cobro. Tres paquetes y auditoría con costo.",
        "active": "ph",
        "body": propiedad_horizontal(),
        "jsonld": '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "name": "Retainer legal Reina Legal para propiedad horizontal",
            "serviceType": "Asesoría legal preventiva en propiedad horizontal",
            "areaServed": "PA",
            "provider": {"@type": "Attorney", "name": "Alfonso Villarreal"},
            "description": "Acompañamiento mensual a administradores y juntas directivas de edificios y condominios bajo la Ley 284 de 2022. La orientación inicial es gratuita; la auditoría de cada caso se cotiza aparte.",
            "hasOfferCatalog": {
                "@type": "OfferCatalog",
                "name": "Paquetes Reina Legal",
                "itemListElement": [
                    {"@type": "Offer", "name": "Reina Legal Esencial", "description": "Hasta 40 unidades. Convocatorias, actas y contratos básicos."},
                    {"@type": "Offer", "name": "Reina Legal Preventivo", "description": "41 a 120 unidades. Asambleas, morosidad, reglamento e informe trimestral."},
                    {"@type": "Offer", "name": "Reina Legal Integral", "description": "Más de 120 unidades o uso mixto. Gobierno, contratos, cobro prejudicial y acompañamiento permanente."},
                ],
            },
        }, ensure_ascii=False, separators=(",", ":")) + "</script>",
    },
    "honorarios.html": {
        "title": "Honorarios y propuestas | Alfonso Villarreal",
        "description": "Orientación inicial gratuita y auditoría del caso con costo. Alcance y honorarios definidos por escrito, incluido el retainer de propiedad horizontal.",
        "active": "honorarios",
        "body": fees(),
    },
    "descargo.html": {
        "title": "Descargo y aviso legal | Alfonso Villarreal",
        "description": "Alcance del contenido, relación profesional, terceros, datos y comunicaciones del despacho Alfonso Villarreal.",
        "active": "descargo",
        "body": disclaimer(),
    },
    "informacion-legal.html": {
        "title": "Información legal gratuita | Alfonso Villarreal",
        "description": "Notas de práctica, etapas del trabajo, guía de Naturalízate.pa y enlaces oficiales para consultas en Panamá.",
        "active": "informacion",
        "body": resources(),
    },
    "herramientas.html": {
        "title": "Preparar una consulta | Alfonso Villarreal",
        "description": "Seleccione un área y prepare una consulta sin diagnósticos automáticos ni cálculos tributarios sin base actualizada.",
        "active": "herramientas",
        "body": tool(),
    },
    "contacto.html": {
        "title": "Contáctenos | Alfonso Villarreal",
        "description": "Escriba al Lic. Alfonso Villarreal en Ciudad de Panamá. WhatsApp +507 6255-7583 y Villarreallawyers@proton.me.",
        "active": "contacto",
        "body": contact(),
    },
    "404.html": {
        "title": "Página no encontrada | Alfonso Villarreal",
        "description": "Vuelva a los servicios y recursos del despacho Alfonso Villarreal.",
        "active": "404",
        "robots": "noindex, nofollow",
        "body": not_found(),
    },
}

for _category in CATEGORIES:
    if _category["slug"] == "propiedad-horizontal":
        continue
    PAGES[f"{_category['slug']}.html"] = {
        "title": f"{_category['title']} | Alfonso Villarreal",
        "description": _category["intro"],
        "active": "category",
        "body": category_page(_category),
    }
