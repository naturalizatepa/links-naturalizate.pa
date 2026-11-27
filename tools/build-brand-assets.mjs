/* Genera todos los activos de marca de Alfonso Villarreal · Abogado.
   Uso: node tools/build-brand-assets.mjs
   Requiere: sharp (npm install sharp). Todo parte de los SVG reales de la marca. */
import sharp from "sharp";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const ROOT = process.cwd();
const A = (p) => join(ROOT, "assets", p);
const B = (p) => join(ROOT, "assets", "brand", p);
for (const d of ["logos", "icons", "watermarks", "social", "print", "brandbook"]) mkdirSync(B(d), { recursive: true });

// ── Paleta de marca (regla 60·30·10) ──────────────────────────────
const C = {
  navy: "#0D1B2A", navyMid: "#1B3A57", navySoft: "#284B68",
  gold: "#C5A572", goldDark: "#A5814D",
  ivory: "#F5F1E8", white: "#FFFFFF", slate: "#5C6772", ink: "#212529",
};
const SERIF = "Georgia, 'Times New Roman', serif";
const SANS = "Arial, Helvetica, sans-serif";
const manifest = [];
const log = (p) => { manifest.push(p.replace(ROOT + "/", "")); };

const svg = (name) => readFileSync(A(name), "utf8");
const recolor = (s, map) => { for (const [from, to] of Object.entries(map)) s = s.split(from).join(to); return s; };
const withOpacity = (s, o) => s.replace(/<svg([^>]*)>/, `<svg$1><g opacity="${o}">`).replace("</svg>", "</g></svg>");
const render = (s, width) => sharp(Buffer.from(s), { density: 300 }).resize({ width }).png().toBuffer();

async function save(buf, path) { writeFileSync(path, buf); log(path); }

// ── 1. LOGOS (PNG transparente, varios tamaños) ───────────────────
async function logos() {
  const sets = [
    ["logo_principal.svg", "logo-principal", [1600, 800, 400]],
    ["logo_horizontal.svg", "logo-horizontal", [1600, 800, 400]],
    ["logo_blanco.svg", "logo-blanco", [1600, 800]],
    ["logo_dark.svg", "logo-dark", [1600, 800]],
    ["logo_naturalizate.svg", "logo-naturalizate", [1600, 800]],
  ];
  for (const [file, name, widths] of sets)
    for (const w of widths) await save(await render(svg(file), w), B(`logos/${name}-${w}.png`));

  // Variantes monocromáticas del isotipo (V + balanza)
  const icon = svg("icono_v_balanza.svg");
  const variants = {
    "icono-navy": icon,
    "icono-blanco": recolor(icon, { "#0D1B2A": "#FFFFFF", "#C5A572": "#FFFFFF" }),
    "icono-dorado": recolor(icon, { "#0D1B2A": "#C5A572" }),
    "icono-negro": recolor(icon, { "#0D1B2A": "#111111", "#C5A572": "#111111" }),
    "icono-navy-dorado": icon,
  };
  for (const [name, s] of Object.entries(variants))
    for (const w of [1000, 512, 256]) await save(await render(s, w), B(`logos/${name}-${w}.png`));

  // Logotipo principal invertido (todo blanco) y dorado sobre navy
  const prin = svg("logo_principal.svg");
  await save(await render(recolor(prin, { "#0D1B2A": "#FFFFFF", "#1B3A57": "#FFFFFF" }), 1600), B("logos/logo-principal-blanco-1600.png"));
  await save(await render(recolor(prin, { "#0D1B2A": "#C5A572", "#1B3A57": "#C5A572" }), 1600), B("logos/logo-principal-dorado-1600.png"));
}

// ── 2. ICONOS / FAVICON / APP ─────────────────────────────────────
async function icons() {
  const icon = svg("icono_v_balanza.svg");
  for (const s of [512, 192, 180, 64, 32, 16]) await save(await render(icon, s), B(`icons/favicon-${s}.png`));
  // Apple touch (fondo navy, isotipo blanco+dorado)
  const bg = Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="180" height="180"><rect width="180" height="180" fill="${C.navy}"/></svg>`);
  const iso = await render(recolor(icon, { "#0D1B2A": "#FFFFFF" }), 120);
  await save(await sharp(bg).composite([{ input: iso, gravity: "center" }]).png().toBuffer(), B("icons/apple-touch-180.png"));
  await save(await render(icon, 512), B("icons/app-icon-512.png"));
}

// ── 3. MARCAS DE AGUA (PNG transparente) ──────────────────────────
async function watermarks() {
  const icon = svg("icono_v_balanza.svg");
  const prin = svg("logo_principal.svg");
  // Isotipo tenue (para fotos y documentos)
  await save(await render(withOpacity(icon, 0.12), 1000), B("watermarks/marca-agua-icono-1000.png"));
  await save(await render(withOpacity(recolor(icon, { "#0D1B2A": "#FFFFFF", "#C5A572": "#FFFFFF" }), 0.16), 1000), B("watermarks/marca-agua-icono-blanco-1000.png"));
  // Logotipo completo tenue
  await save(await render(withOpacity(prin, 0.10), 1600), B("watermarks/marca-agua-logo-1600.png"));

  // Patrón diagonal repetido (documento / foto)
  const tile = await render(withOpacity(icon, 0.08), 240);
  const rot = await sharp(tile).rotate(-28, { background: { r: 0, g: 0, b: 0, alpha: 0 } }).png().toBuffer();
  const meta = await sharp(rot).metadata();
  const W = 1600, H = 1200, comps = [];
  for (let y = -100; y < H + 100; y += 300)
    for (let x = -100; x < W + 100; x += 360)
      comps.push({ input: rot, left: x + ((y / 300) % 2 ? 180 : 0), top: y });
  await save(await sharp({ create: { width: W, height: H, channels: 4, background: { r: 0, g: 0, b: 0, alpha: 0 } } }).composite(comps).png().toBuffer(), B("watermarks/marca-agua-patron-1600x1200.png"));

  // Texto diagonal repetido (documentos legales)
  const txt = "ALFONSO VILLARREAL · ABOGADO · PANAMÁ";
  let rows = "";
  for (let y = 0; y < 1400; y += 180)
    rows += `<text x="-200" y="${y}" font-family="${SANS}" font-size="34" letter-spacing="6" fill="${C.navy}" fill-opacity="0.09">${txt}  ${txt}</text>`;
  const tsvg = `<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1200"><g transform="rotate(-24 800 600)">${rows}</g></svg>`;
  await save(await sharp(Buffer.from(tsvg)).png().toBuffer(), B("watermarks/marca-agua-texto-1600x1200.png"));
}

// ── 4. TARJETAS WEB / REDES (navy + logo + dorado) ────────────────
function cardBG(w, h, { frame = true } = {}) {
  const m = Math.round(Math.min(w, h) * 0.055);
  const fr = frame ? `<rect x="${m}" y="${m}" width="${w - 2 * m}" height="${h - 2 * m}" fill="none" stroke="${C.gold}" stroke-opacity="0.55" stroke-width="2"/>` : "";
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}">
    <defs><radialGradient id="g" cx="50%" cy="0%" r="90%">
      <stop offset="0%" stop-color="${C.navyMid}"/><stop offset="60%" stop-color="${C.navy}"/><stop offset="100%" stop-color="#060F17"/>
    </radialGradient></defs>
    <rect width="${w}" height="${h}" fill="url(#g)"/>${fr}</svg>`;
}
async function card(name, w, h, { logoW, logoY, tagline, sub, gravity = "center", frame = true }) {
  const bg = await sharp(Buffer.from(cardBG(w, h, { frame }))).png().toBuffer();
  const logo = await render(svg("logo_dark.svg"), logoW);
  const lm = await sharp(logo).metadata();
  const left = gravity === "center" ? Math.round((w - lm.width) / 2) : gravity.left;
  const comps = [{ input: logo, left, top: logoY }];
  let extra = "";
  if (tagline) {
    const base = Math.min(w, h);
    const ty = logoY + lm.height + Math.round(base * 0.07);
    extra += `<text x="${w / 2}" y="${ty}" font-family="${SERIF}" font-size="${Math.round(base * 0.05)}" fill="${C.gold}" text-anchor="middle" letter-spacing="2">${tagline}</text>`;
    if (sub) extra += `<text x="${w / 2}" y="${ty + Math.round(base * 0.06)}" font-family="${SANS}" font-size="${Math.round(base * 0.027)}" fill="${C.white}" fill-opacity="0.85" text-anchor="middle" letter-spacing="2">${sub}</text>`;
  }
  if (extra) {
    const overlay = await sharp(Buffer.from(`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}">${extra}</svg>`)).png().toBuffer();
    comps.push({ input: overlay, left: 0, top: 0 });
  }
  await save(await sharp(bg).composite(comps).png().toBuffer(), B(`social/${name}.png`));
}
async function social() {
  await card("og-image-1200x630", 1200, 630, { logoW: 620, logoY: 120, tagline: "Estrategia legal · Panamá", sub: "NATURALIZACIÓN · SOCIEDADES · INMUEBLES · FAMILIA" });
  await card("twitter-cover-1500x500", 1500, 500, { logoW: 560, logoY: 70, tagline: "Abogado · Idoneidad 25795", sub: "CIUDAD DE PANAMÁ" });
  await card("instagram-post-1080x1080", 1080, 1080, { logoW: 640, logoY: 300, tagline: "Su asunto, con estrategia.", sub: "+507 6255-7583" });
  await card("instagram-story-1080x1920", 1080, 1920, { logoW: 660, logoY: 660, tagline: "Naturalízate.pa", sub: "GUÍA DE NATURALIZACIÓN PANAMEÑA" });
  await card("linkedin-cover-1584x396", 1584, 396, { logoW: 470, logoY: 55, tagline: "", sub: "" });
  await card("facebook-cover-820x312", 820, 312, { logoW: 380, logoY: 40, tagline: "", sub: "" });
  await card("whatsapp-perfil-500x500", 500, 500, { logoW: 300, logoY: 120, tagline: "", sub: "", frame: false });
  await card("youtube-banner-2560x1440", 2560, 1440, { logoW: 760, logoY: 500, tagline: "Derecho migratorio y corporativo", sub: "PANAMÁ" });
}

// ── 5. PLANTILLAS DE IMPRESIÓN / APLICACIONES ─────────────────────
async function print() {
  // Tarjeta de presentación 90×50 mm @300dpi = 1063×591
  const cw = 1063, ch = 591;
  const frontBG = Buffer.from(cardBG(cw, ch, { frame: true }));
  const flogo = await render(svg("logo_dark.svg"), 560);
  await save(await sharp(frontBG).composite([{ input: flogo, gravity: "center" }]).png().toBuffer(), B("print/tarjeta-frente-1063x591.png"));

  const backSVG = `<svg xmlns="http://www.w3.org/2000/svg" width="${cw}" height="${ch}">
    <rect width="${cw}" height="${ch}" fill="${C.ivory}"/>
    <rect x="0" y="0" width="14" height="${ch}" fill="${C.gold}"/>
    <text x="70" y="150" font-family="${SERIF}" font-size="46" fill="${C.navy}">Alfonso Villarreal</text>
    <text x="70" y="195" font-family="${SANS}" font-size="22" letter-spacing="4" fill="${C.goldDark}">ABOGADO · IDONEIDAD 25795</text>
    <line x1="70" y1="235" x2="990" y2="235" stroke="${C.gold}" stroke-width="2"/>
    <text x="70" y="300" font-family="${SANS}" font-size="26" fill="${C.ink}">WhatsApp  +507 6255-7583</text>
    <text x="70" y="350" font-family="${SANS}" font-size="26" fill="${C.ink}">Villarreallawyers@proton.me</text>
    <text x="70" y="400" font-family="${SANS}" font-size="26" fill="${C.ink}">Ciudad de Panamá · República de Panamá</text>
    <text x="70" y="450" font-family="${SANS}" font-size="26" fill="${C.navyMid}">naturalizate.pa</text>
  </svg>`;
  const biso = await render(svg("icono_v_balanza.svg"), 150);
  await save(await sharp(Buffer.from(backSVG)).composite([{ input: biso, left: cw - 220, top: ch - 220 }]).png().toBuffer(), B("print/tarjeta-reverso-1063x591.png"));

  // Membrete A4 @150dpi = 1240×1754 (encabezado + pie)
  const lw = 1240, lh = 1754;
  const lsvg = `<svg xmlns="http://www.w3.org/2000/svg" width="${lw}" height="${lh}">
    <rect width="${lw}" height="${lh}" fill="#FFFFFF"/>
    <rect x="0" y="0" width="${lw}" height="10" fill="${C.navy}"/>
    <rect x="0" y="10" width="${lw}" height="4" fill="${C.gold}"/>
    <line x1="90" y1="${lh - 150}" x2="${lw - 90}" y2="${lh - 150}" stroke="${C.gold}" stroke-width="2"/>
    <text x="90" y="${lh - 105}" font-family="${SANS}" font-size="22" fill="${C.slate}">+507 6255-7583 · Villarreallawyers@proton.me</text>
    <text x="90" y="${lh - 70}" font-family="${SANS}" font-size="22" fill="${C.slate}">Ciudad de Panamá · naturalizate.pa</text>
  </svg>`;
  const llogo = await render(svg("logo_horizontal.svg"), 520);
  await save(await sharp(Buffer.from(lsvg)).composite([{ input: llogo, left: 90, top: 70 }]).png().toBuffer(), B("print/membrete-a4-1240x1754.png"));

  // Firma de correo 600×220
  const esvg = `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="220">
    <rect width="600" height="220" fill="#FFFFFF"/>
    <rect x="0" y="0" width="6" height="220" fill="${C.gold}"/>
    <text x="200" y="70" font-family="${SERIF}" font-size="34" fill="${C.navy}">Alfonso Villarreal</text>
    <text x="200" y="100" font-family="${SANS}" font-size="15" letter-spacing="3" fill="${C.goldDark}">ABOGADO · PANAMÁ</text>
    <text x="200" y="135" font-family="${SANS}" font-size="16" fill="${C.ink}">+507 6255-7583</text>
    <text x="200" y="160" font-family="${SANS}" font-size="16" fill="${C.ink}">Villarreallawyers@proton.me</text>
    <text x="200" y="185" font-family="${SANS}" font-size="16" fill="${C.navyMid}">naturalizate.pa</text>
  </svg>`;
  const eiso = await render(svg("icono_v_balanza.svg"), 150);
  await save(await sharp(Buffer.from(esvg)).composite([{ input: eiso, left: 25, top: 35 }]).png().toBuffer(), B("print/firma-correo-600x220.png"));
}

// ── 6. AYUDAS DEL BRANDBOOK (paleta 60·30·10) ─────────────────────
async function brandbookAids() {
  const w = 1200, h = 360;
  const s = `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}">
    <rect x="0" y="0" width="720" height="${h}" fill="${C.navy}"/>
    <rect x="720" y="0" width="360" height="${h}" fill="${C.ivory}"/>
    <rect x="1080" y="0" width="120" height="${h}" fill="${C.gold}"/>
    <text x="360" y="170" font-family="${SERIF}" font-size="64" fill="${C.white}" text-anchor="middle">60%</text>
    <text x="360" y="215" font-family="${SANS}" font-size="22" fill="${C.gold}" text-anchor="middle" letter-spacing="3">PRINCIPAL · NAVY</text>
    <text x="900" y="170" font-family="${SERIF}" font-size="52" fill="${C.navy}" text-anchor="middle">30%</text>
    <text x="900" y="215" font-family="${SANS}" font-size="20" fill="${C.slate}" text-anchor="middle" letter-spacing="2">SECUNDARIO · MARFIL</text>
    <text x="1140" y="170" font-family="${SERIF}" font-size="34" fill="${C.navy}" text-anchor="middle">10%</text>
    <text x="1140" y="205" font-family="${SANS}" font-size="13" fill="${C.navy}" text-anchor="middle" letter-spacing="1">ACENTO</text>
  </svg>`;
  await save(await sharp(Buffer.from(s)).png().toBuffer(), B("brandbook/paleta-60-30-10.png"));

  // Muestras de color individuales
  const swatches = { navy: C.navy, "navy-medio": C.navyMid, marfil: C.ivory, pizarra: C.slate, dorado: C.gold, "dorado-oscuro": C.goldDark };
  for (const [name, hex] of Object.entries(swatches)) {
    const txt = ["marfil"].includes(name) ? C.navy : C.white;
    const sw = `<svg xmlns="http://www.w3.org/2000/svg" width="400" height="240"><rect width="400" height="240" fill="${hex}"/><text x="24" y="200" font-family="${SANS}" font-size="26" fill="${txt}">${hex.toUpperCase()}</text></svg>`;
    await save(await sharp(Buffer.from(sw)).png().toBuffer(), B(`brandbook/swatch-${name}.png`));
  }
}

(async () => {
  await logos(); await icons(); await watermarks(); await social(); await print(); await brandbookAids();
  writeFileSync(B("manifest.json"), JSON.stringify(manifest, null, 2));
  console.log(`Generados ${manifest.length} activos de marca.`);
})().catch((e) => { console.error(e); process.exit(1); });
