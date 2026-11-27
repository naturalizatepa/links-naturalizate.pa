/* Interacciones del sitio Alfonso Villarreal.
   Misma lógica que naturalizate-pa-main-v5: menú, submenús, buscador,
   formularios que preparan WhatsApp, FAQ y carga diferida del mapa. */

const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.getElementById("nav-links");
const dropdowns = [...document.querySelectorAll("[data-dropdown]")];
const subdropdowns = [...document.querySelectorAll("[data-subdropdown]")];
const mobileView = window.matchMedia("(max-width: 860px)");

function caretOf(item) {
  return item.querySelector(":scope > .nav-caret") || item.querySelector(":scope > .nav-subrow > .nav-subcaret");
}

function setItemState(item, open) {
  item.classList.toggle("is-open", open);
  const caret = caretOf(item);
  if (!caret) return;
  caret.setAttribute("aria-expanded", String(open));
  const label = caret.getAttribute("aria-label") || "";
  caret.setAttribute("aria-label", label.replace(open ? "Abrir" : "Cerrar", open ? "Cerrar" : "Abrir"));
}

function closeSubdropdowns(except = null) {
  subdropdowns.forEach((item) => { if (item !== except) setItemState(item, false); });
}

function closeDropdowns(except = null) {
  dropdowns.forEach((item) => { if (item !== except) setItemState(item, false); });
  closeSubdropdowns();
}

function closeMenu() {
  if (!navLinks || !menuToggle) return;
  navLinks.classList.remove("is-open");
  document.body.classList.remove("menu-open");
  menuToggle.setAttribute("aria-expanded", "false");
  menuToggle.setAttribute("aria-label", "Abrir menú");
  closeDropdowns();
}

function toggleSubdropdown(item) {
  const open = !item.classList.contains("is-open");
  [...item.parentElement.querySelectorAll(":scope > [data-subdropdown]")].forEach((sibling) => {
    if (sibling !== item) setItemState(sibling, false);
  });
  setItemState(item, open);
}

if (menuToggle && navLinks) {
  menuToggle.addEventListener("click", () => {
    const open = navLinks.classList.toggle("is-open");
    document.body.classList.toggle("menu-open", open && mobileView.matches);
    menuToggle.setAttribute("aria-expanded", String(open));
    menuToggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
    if (!open) closeDropdowns();
  });
  mobileView.addEventListener("change", () => closeMenu());
}

/* Escritorio: el despliegue al pasar el cursor lo resuelve el CSS (fundido +
   flyout). El clic en la flecha fija el panel para teclado / pantalla táctil. */
dropdowns.forEach((item) => {
  const caret = item.querySelector(":scope > .nav-caret");
  if (!caret) return;
  caret.addEventListener("click", (event) => {
    event.stopPropagation();
    const open = !item.classList.contains("is-open");
    closeDropdowns(item);
    setItemState(item, open);
  });
});

subdropdowns.forEach((item) => {
  const caret = item.querySelector(":scope > .nav-subrow > .nav-subcaret");
  if (!caret) return;
  caret.addEventListener("click", (event) => {
    event.stopPropagation();
    toggleSubdropdown(item);
  });
});

/* Los submenús largos (p. ej. migración) se reubican hacia arriba para que
   siempre quepan en la pantalla; el desplazamiento interno lo resuelve el CSS. */
function positionFlyout(item) {
  const panel = item.querySelector(":scope > .nav-subpanel");
  if (!panel || mobileView.matches) return;
  panel.style.top = "";
  const overflow = panel.getBoundingClientRect().bottom - (window.innerHeight - 12);
  if (overflow > 0) panel.style.top = `${-overflow}px`;
}

subdropdowns.forEach((item) => {
  item.addEventListener("mouseenter", () => positionFlyout(item));
  item.addEventListener("mouseleave", () => {
    const panel = item.querySelector(":scope > .nav-subpanel");
    if (panel) panel.style.top = "";
  });
});

/* Móvil: acordeón. Los enlaces con hijos despliegan su nivel en lugar de
   navegar; los enlaces hoja cierran el menú y navegan. */
if (navLinks) {
  navLinks.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link) return;
    if (mobileView.matches) {
      const subrow = link.closest(".nav-subrow");
      if (subrow) {
        event.preventDefault();
        toggleSubdropdown(subrow.closest("[data-subdropdown]"));
        return;
      }
      const topItem = link.closest("[data-dropdown]");
      if (topItem && link.classList.contains("nav-link")) {
        event.preventDefault();
        const open = !topItem.classList.contains("is-open");
        closeDropdowns(topItem);
        setItemState(topItem, open);
        return;
      }
      closeMenu();
    } else {
      closeDropdowns();
    }
  });
}

/* ---------------------------------------------------------------- buscador */

const searchForm = document.getElementById("site-search");
const searchInput = document.getElementById("search-input");
const searchResults = document.getElementById("search-results");

const fallbackEntries = [
  { title: "Áreas de práctica", detail: "Catálogo del despacho", href: "areas-de-practica.html", terms: "servicios tramites areas" },
  { title: "Honorarios", detail: "Alcance y propuesta por escrito", href: "honorarios.html", terms: "precio costo tarifa" },
  { title: "Contáctenos", detail: "WhatsApp, correo y ubicación", href: "contacto.html", terms: "telefono email" },
  { title: "Preparar una consulta", detail: "Herramienta", href: "herramientas.html", terms: "formulario" },
];

const searchEntries = Array.isArray(window.AV_SERVICE_INDEX) && window.AV_SERVICE_INDEX.length
  ? window.AV_SERVICE_INDEX
  : fallbackEntries;

function normalize(text) {
  return String(text).normalize("NFD").replace(/\p{M}/gu, "").toLowerCase();
}

function hideSearch() {
  if (!searchResults) return;
  searchResults.hidden = true;
  searchResults.replaceChildren();
}

function renderSearch() {
  if (!searchInput || !searchResults) return;
  const query = searchInput.value.trim();
  if (query.length < 2) return hideSearch();
  const words = normalize(query).split(/\s+/).filter(Boolean);
  const matches = searchEntries.filter((entry) => {
    const text = normalize(`${entry.title} ${entry.detail} ${entry.terms}`);
    return words.every((word) => text.includes(word));
  });
  searchResults.replaceChildren();
  if (!matches.length) {
    const empty = document.createElement("p");
    empty.textContent = "Sin resultados. Pruebe con “contrato”, “naturalización” o “honorarios”.";
    searchResults.append(empty);
  } else {
    matches.slice(0, 12).forEach((entry) => {
      const link = document.createElement("a");
      link.href = entry.href;
      const label = document.createElement("span");
      const title = document.createElement("strong");
      const detail = document.createElement("small");
      title.textContent = entry.title;
      detail.textContent = entry.detail;
      label.append(title, detail);
      const arrow = document.createElement("span");
      arrow.textContent = "↗";
      arrow.setAttribute("aria-hidden", "true");
      link.append(label, arrow);
      link.addEventListener("click", hideSearch);
      searchResults.append(link);
    });
  }
  searchResults.hidden = false;
}

if (searchForm && searchInput) {
  searchInput.addEventListener("input", renderSearch);
  searchInput.addEventListener("focus", renderSearch);
  searchInput.addEventListener("keydown", (event) => {
    if (event.key === "ArrowDown" && !searchResults.hidden) {
      const first = searchResults.querySelector("a");
      if (first) {
        event.preventDefault();
        first.focus();
      }
    }
    if (event.key === "Escape") hideSearch();
  });
  searchForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const first = searchResults.querySelector("a");
    if (first) first.click();
    else renderSearch();
  });
}

document.addEventListener("click", (event) => {
  if (searchForm && !searchForm.contains(event.target) && !searchResults.contains(event.target)) hideSearch();
  if (!event.target.closest("[data-dropdown]")) closeDropdowns();
  if (mobileView.matches && !event.target.closest(".site-nav")) closeMenu();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    hideSearch();
    closeMenu();
  }
  if (event.key === "/" && !/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName)) {
    if (!searchInput) return;
    event.preventDefault();
    searchInput.focus();
  }
});

/* --------------------------------------------------------------- WhatsApp */

const WA_NUMBER = "50762557583";

function openWhatsApp(message) {
  const anchor = document.createElement("a");
  anchor.href = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(message)}`;
  anchor.target = "_blank";
  anchor.rel = "noopener noreferrer";
  anchor.hidden = true;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
}

const formLabels = {
  nombre: "Nombre",
  correo: "Correo electrónico",
  telefono: "Teléfono o WhatsApp",
  area: "Área",
  servicio: "Servicio o tema",
  mensaje: "Mensaje",
};

for (const form of document.querySelectorAll("[data-wa-form]")) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const values = new FormData(form);
    const lines = ["Hola, escribo desde el sitio de Alfonso Villarreal."];
    for (const [key, value] of values.entries()) {
      if (key === "novedades") continue;
      const text = String(value).trim();
      if (text) lines.push(`${formLabels[key] || key}: ${text}`);
    }
    lines.push(`Notas legales: ${values.has("novedades") ? "Sí" : "No"}`);
    openWhatsApp(lines.join("\n"));
    const status = form.querySelector("[data-form-status]");
    if (status) status.textContent = "Se abrió WhatsApp con sus datos. Revise el mensaje y envíelo desde su aplicación; si no se abre, escriba al +507 6255-7583.";
  });
}

/* ------------------------------------------------------------------- FAQ */

for (const item of document.querySelectorAll(".faq-item")) {
  const button = item.querySelector(".faq-q");
  const panel = item.querySelector(".faq-a");
  if (!button || !panel) continue;
  button.addEventListener("click", () => {
    const open = button.getAttribute("aria-expanded") !== "true";
    button.setAttribute("aria-expanded", String(open));
    panel.hidden = !open;
  });
}

/* ------------------------------------------- formulario de calificación */

const qualForm = document.querySelector("[data-qual-form]");
if (qualForm) {
  const fields = [...qualForm.querySelectorAll("[data-qual-field]")];
  const countLabel = document.getElementById("qual-count");
  const bar = qualForm.querySelector(".progress-track");
  const fill = document.getElementById("qual-progress");
  const status = qualForm.querySelector("[data-qual-status]");
  const update = () => {
    const filled = fields.filter((field) => String(field.value).trim()).length;
    if (countLabel) countLabel.textContent = `${filled} de ${fields.length} respondidas`;
    if (bar) bar.setAttribute("aria-valuenow", String(filled));
    if (fill) fill.style.width = `${(filled / fields.length) * 100}%`;
  };
  fields.forEach((field) => {
    field.addEventListener("input", update);
    field.addEventListener("change", update);
  });
  update();
  qualForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!qualForm.reportValidity()) return;
    const lines = fields
      .filter((field) => String(field.value).trim())
      .map((field) => `${field.name}: ${field.value.trim()}`);
    openWhatsApp([
      "Hola, preparé una consulta desde el sitio de Alfonso Villarreal.",
      "",
      ...lines,
    ].join("\n"));
    if (status) status.textContent = "Se preparó el mensaje de WhatsApp con sus respuestas. Revíselo y envíelo desde su aplicación.";
  });
}

/* ------------------------------------------------------------------ mapa */

const mapButton = document.querySelector("[data-load-map]");
if (mapButton) {
  mapButton.addEventListener("click", () => {
    const iframe = document.createElement("iframe");
    iframe.title = "Mapa de Ciudad de Panamá";
    iframe.loading = "lazy";
    iframe.referrerPolicy = "no-referrer-when-downgrade";
    iframe.src = "https://www.google.com/maps?q=Ciudad+de+Panama&output=embed";
    mapButton.closest("[data-map-container]").replaceChildren(iframe);
  });
}

/* -------------------------------------------------------------- compartir */

for (const button of document.querySelectorAll("[data-share]")) {
  button.addEventListener("click", async () => {
    const status = button.parentElement.querySelector("[data-share-status]");
    if (navigator.share) {
      try {
        await navigator.share({ title: document.title, url: location.href });
        if (status) status.textContent = "Página compartida desde su dispositivo.";
        return;
      } catch (error) {
        if (error.name === "AbortError") return;
      }
    }
    try {
      await navigator.clipboard.writeText(location.href);
      if (status) status.textContent = "Enlace copiado al portapapeles.";
    } catch {
      if (status) status.textContent = "Copie el enlace desde la barra de direcciones.";
    }
  });
}

/* Áreas de práctica: al llegar con un #ancla, desplegar la sección apuntada
   (y cualquier subsección ancestro) para que el enlace del menú no quede oculto. */
function openHashDetails() {
  const id = decodeURIComponent(location.hash.slice(1));
  if (!id) return;
  const target = document.getElementById(id);
  if (!target) return;
  const own = target.matches("details") ? target : target.querySelector("details");
  if (own) own.open = true;
  let ancestor = target.closest("details");
  while (ancestor) { ancestor.open = true; ancestor = ancestor.parentElement.closest("details"); }
}
window.addEventListener("hashchange", openHashDetails);
openHashDetails();

const year = document.getElementById("year");
if (year) year.textContent = new Date().getFullYear();
