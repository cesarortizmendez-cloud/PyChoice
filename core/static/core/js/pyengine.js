/* ============================================================
   pyengine.js - Motor Python real en el navegador (Pyodide / WebAssembly)
   + consolas educativas + carga/descarga Excel (SheetJS)
   Sin servidor de Python: todo corre en la maquina del alumno.
   PyChoice - Aprende Python con datos.
   ============================================================ */
import { loadPyodide } from 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.mjs';

const PYODIDE_VERSION = 'v0.26.4';
const INDEX_URL = `https://cdn.jsdelivr.net/pyodide/${PYODIDE_VERSION}/full/`;

const STATUS = document.getElementById('engine-status');
const DOT = document.getElementById('engine-dot');

function setStatus(txt, state) {
  if (STATUS) STATUS.textContent = txt;
  if (DOT) { DOT.className = 'dot' + (state ? ' ' + state : ''); }
}

/* --- Harness: se ejecuta una vez al arrancar. Define el espacio de
   nombres compartido (con datos de ejemplo) y la funcion de ejecucion. --- */
const HARNESS = `
import sys, io, os, base64, json, traceback
os.environ["MPLBACKEND"] = "AGG"
import numpy as np
import pandas as pd

# matplotlib se carga de forma diferida (en el primer grafico) para que el
# arranque sea mas rapido. Hasta entonces, plt no existe.
plt = None

# Espacio de nombres compartido por todas las consolas (como el entorno global de R)
NS = {"__name__": "__main__", "np": np, "pd": pd}

# ------------------------------------------------------------------
# Catalogo de datasets de practica. Cada funcion devuelve un DataFrame
# reproducible (semilla fija) para que el alumno "aprenda haciendo".
# ------------------------------------------------------------------
def _rng(seed=7):
    return np.random.default_rng(seed)

def _ds_negocio():
    return pd.DataFrame({
        "mes":    ["ene", "feb", "mar", "abr", "may", "jun"],
        "region": ["norte", "sur", "norte", "centro", "sur", "centro"],
        "ventas": [120, 95, 130, 110, 88, 145],
        "unidades": [12, 9, 13, 11, 8, 15],
        "costo":   [70, 60, 78, 66, 55, 82],
    })

def _ds_propinas(n=120):
    r = _rng(11)
    cuenta = np.round(r.gamma(6.0, 3.4, n) + 5, 2)
    momento = r.choice(["almuerzo", "cena"], n, p=[0.35, 0.65])
    pct = np.where(momento == "cena", 0.17, 0.15) + r.normal(0, 0.03, n)
    pct = np.clip(pct, 0.05, 0.30)
    return pd.DataFrame({
        "cuenta": cuenta,
        "propina": np.round(cuenta * pct, 2),
        "sexo": r.choice(["Mujer", "Hombre"], n),
        "fumador": r.choice(["si", "no"], n, p=[0.38, 0.62]),
        "dia": r.choice(["jue", "vie", "sab", "dom"], n),
        "momento": momento,
        "personas": r.integers(1, 6, n),
    })

def _ds_estudiantes(n=100):
    r = _rng(23)
    horas = np.round(np.clip(r.normal(6, 2.5, n), 0.5, 14), 1)
    asist = np.round(np.clip(r.normal(0.80, 0.14, n), 0.3, 1.0), 2)
    base = 0.8 + 0.32 * horas + 1.9 * asist + r.normal(0, 0.9, n)
    nota = np.round(np.clip(base, 1.0, 7.0), 1)
    return pd.DataFrame({
        "edad": r.integers(17, 27, n),
        "genero": r.choice(["F", "M"], n),
        "horas_estudio": horas,
        "asistencia": asist,
        "nota_final": nota,
        "aprobado": nota >= 4.0,
    })

def _ds_viviendas(n=150):
    r = _rng(41)
    superficie = np.round(np.clip(r.normal(90, 35, n), 25, 260), 0)
    habitaciones = np.clip((superficie // 30).astype(int) + r.integers(0, 2, n), 1, 6)
    antiguedad = r.integers(0, 60, n)
    barrio = r.choice(["centro", "norte", "sur", "oriente"], n)
    factor = pd.Series(barrio).map({"centro": 1.35, "oriente": 1.2, "norte": 1.0, "sur": 0.85}).values
    precio = (superficie * 28 + habitaciones * 250 - antiguedad * 45) * factor
    precio = np.round(np.clip(precio + r.normal(0, 400, n), 800, None), 0)
    return pd.DataFrame({
        "superficie": superficie,
        "habitaciones": habitaciones,
        "antiguedad": antiguedad,
        "barrio": barrio,
        "precio": precio,
    })

def _ds_clientes(n=200):
    r = _rng(59)
    edad = r.integers(18, 75, n)
    ingresos = np.round(np.clip(r.normal(750, 260, n), 250, 2200), 0)
    antig = r.integers(1, 72, n)
    gasto = np.round(np.clip(ingresos * 0.12 + r.normal(0, 25, n), 5, None), 1)
    logit = -1.0 - 0.025 * (antig - 24) + 0.003 * (700 - ingresos)
    p_fuga = 1 / (1 + np.exp(-logit))
    churn = (r.random(n) < np.clip(p_fuga, 0.02, 0.95)).astype(int)
    return pd.DataFrame({
        "edad": edad,
        "genero": r.choice(["F", "M"], n),
        "ciudad": r.choice(["Santiago", "Valpo", "Concepcion", "Temuco"], n),
        "ingresos": ingresos,
        "antiguedad_meses": antig,
        "gasto_mensual": gasto,
        "churn": churn,
    })

def _ds_empleados(n=120):
    r = _rng(73)
    depto = r.choice(["Ventas", "TI", "RRHH", "Finanzas", "Operaciones"], n)
    antig = r.integers(0, 25, n)
    base = pd.Series(depto).map({"TI": 1500, "Finanzas": 1400, "Ventas": 1100,
                                 "Operaciones": 1000, "RRHH": 1050}).values
    salario = np.round(base + antig * 32 + r.normal(0, 120, n), 0)
    return pd.DataFrame({
        "departamento": depto,
        "edad": r.integers(22, 63, n),
        "genero": r.choice(["F", "M"], n),
        "antiguedad": antig,
        "salario": salario,
        "satisfaccion": np.round(np.clip(r.normal(3.6, 0.9, n), 1, 5), 1),
    })

def _ds_clima(dias=90):
    r = _rng(89)
    fechas = pd.date_range("2024-06-01", periods=dias, freq="D")
    t = np.arange(dias)
    temp = np.round(12 + 6 * np.sin(2 * np.pi * t / 30) + r.normal(0, 1.5, dias), 1)
    lluvia = np.round(np.clip(r.gamma(1.2, 2.0, dias) * (r.random(dias) < 0.4), 0, None), 1)
    return pd.DataFrame({
        "fecha": fechas,
        "ciudad": "Santiago",
        "temp_c": temp,
        "humedad": np.clip((70 - temp + r.normal(0, 5, dias)).round(0), 20, 100),
        "lluvia_mm": lluvia,
    })

# nombre -> (funcion, descripcion corta)
_CATALOGO = {
    "negocio":     (_ds_negocio,    "Ventas por mes y region (tabla base pequena)."),
    "propinas":    (_ds_propinas,   "Cuentas y propinas de un restaurante (120 filas)."),
    "estudiantes": (_ds_estudiantes,"Horas de estudio, asistencia y nota final (100)."),
    "viviendas":   (_ds_viviendas,  "Superficie, barrio y precio de viviendas (150)."),
    "clientes":    (_ds_clientes,   "Clientes, gasto y fuga/churn (200 filas)."),
    "empleados":   (_ds_empleados,  "RRHH: departamento, salario, satisfaccion (120)."),
    "clima":       (_ds_clima,      "Serie diaria de temperatura y lluvia (90 dias)."),
}

def catalogo():
    "Imprime los datasets disponibles para practicar."
    print("Datasets disponibles (usa: cargar('nombre')):")
    for k, (_, d) in _CATALOGO.items():
        print(f"  - {k:<12} {d}")
    print("\\nTambien tienes: notas (lista) y datos (DataFrame base).")

def cargar(nombre):
    "Devuelve una copia fresca del dataset y lo deja tambien en 'datos'."
    if nombre not in _CATALOGO:
        raise KeyError(f"'{nombre}' no existe. Usa catalogo() para ver las opciones.")
    df = _CATALOGO[nombre][0]().copy()
    NS["datos"] = df
    return df

# ------------------------------------------------------------------
# Generadores de PROBLEMAS para la ruta "Ingeniero de IA" (metaheuristicas).
# Son ligeros y reproducibles; se calculan solo al llamarlos (no en el
# arranque), asi no afectan la velocidad de carga. Tamanos pequenos a
# proposito para que los algoritmos corran rapido en el navegador.
# ------------------------------------------------------------------
def ciudades(n=12, seed=7):
    "DataFrame de n ciudades con coordenadas x, y (para el problema del viajante, TSP)."
    r = _rng(seed)
    return pd.DataFrame({
        "ciudad": [f"C{i}" for i in range(n)],
        "x": r.integers(0, 100, n),
        "y": r.integers(0, 100, n),
    })

def distancias(coords):
    "Matriz (numpy) de distancias euclidianas desde un DataFrame con columnas x, y."
    xy = coords[["x", "y"]].to_numpy(dtype=float)
    return np.sqrt(((xy[:, None, :] - xy[None, :, :]) ** 2).sum(axis=2))

def mochila(n=15, seed=7):
    "DataFrame de n objetos con peso y valor (problema de la mochila / knapsack)."
    r = _rng(seed)
    return pd.DataFrame({
        "objeto": [f"obj{i}" for i in range(n)],
        "peso": r.integers(1, 20, n),
        "valor": r.integers(5, 50, n),
    })

def _seed():
    NS["notas"] = [4.2, 5.8, 6.1, 3.9, 5.0, 6.7, 4.5, 5.3]
    NS["datos"] = _ds_negocio()
    # datasets de practica siempre disponibles por su nombre
    for _n, (_f, _d) in _CATALOGO.items():
        NS[_n] = _f()
    NS["catalogo"] = catalogo
    NS["cargar"] = cargar
    # generadores de problemas de IA (metaheuristicas)
    NS["ciudades"] = ciudades
    NS["distancias"] = distancias
    NS["mochila"] = mochila

_seed()

def _capture_plots():
    imgs = []
    try:
        for num in plt.get_fignums():
            fig = plt.figure(num)
            buf = io.BytesIO()
            fig.savefig(buf, format="png", dpi=100, bbox_inches="tight", facecolor="white")
            imgs.append(base64.b64encode(buf.getvalue()).decode("ascii"))
        plt.close("all")
    except Exception:
        pass
    return imgs

def __run(code):
    out = io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout = out
    sys.stderr = out
    result = {"out": "", "error": None, "images": []}
    try:
        try:
            exec(code, NS)
        except Exception:
            tb = traceback.format_exc()
            clean = [l for l in tb.split(chr(10)) if "in __run" not in l and "exec(code" not in l]
            result["error"] = chr(10).join(clean).strip()
        result["images"] = _capture_plots()
        result["out"] = out.getvalue()
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return json.dumps(result)
`;

/* --- Singleton de Pyodide --- */
let pyodide = null;
let bootPromise = null;

async function boot() {
  if (bootPromise) return bootPromise;
  setStatus('Python · descargando WASM…', '');
  bootPromise = (async () => {
    const py = await loadPyodide({ indexURL: INDEX_URL });
    setStatus('Python · cargando numpy y pandas…', '');
    // Solo numpy + pandas al arrancar. matplotlib (mas pesado) se carga
    // la primera vez que se necesita un grafico -> arranque mas rapido.
    await py.loadPackage(['numpy', 'pandas']);
    await py.runPythonAsync(HARNESS);
    pyodide = py;
    setStatus('Python 3.12 · WASM · LISTO', 'ready');
    return py;
  })();
  return bootPromise;
}

/* matplotlib se carga solo cuando hace falta (primer grafico). */
let mplReady = false;
const PLOT_HINT = /\b(plt|matplotlib|seaborn|sns|pyplot)\b|\.plot\b|\.hist\s*\(|\.boxplot\s*\(|\.plot\./;

async function ensureMatplotlib(py) {
  if (mplReady) return;
  setStatus('Python · cargando matplotlib…', 'ready');
  await py.loadPackage('matplotlib');
  await py.runPythonAsync(
    'import matplotlib; matplotlib.use("AGG"); import matplotlib.pyplot as plt; NS["plt"] = plt'
  );
  mplReady = true;
}

/* Ejecuta codigo y devuelve {out, error, images}.
   Antes de ejecutar, autocarga los paquetes que el codigo importe
   (seaborn, scipy, scikit-learn, etc.) la primera vez que se usan. */
async function runPython(code) {
  const py = await boot();
  // Si el codigo dibuja algo, asegura matplotlib antes de ejecutar.
  if (!mplReady && PLOT_HINT.test(code)) {
    try { await ensureMatplotlib(py); } catch (e) { /* mostrara ImportError */ }
  }
  try {
    setStatus('Python · preparando paquetes…', 'ready');
    await py.loadPackagesFromImports(code);
  } catch (e) { /* si falta un paquete, Python mostrara el ImportError */ }
  setStatus('Python 3.12 · WASM · LISTO', 'ready');
  py.globals.set('__user_code', code);
  let jsonStr = await py.runPythonAsync('__run(__user_code)');
  let result;
  try { result = JSON.parse(jsonStr); }
  catch (e) { return { out: '', error: String(e), images: [] }; }

  // Red de seguridad: si fallo por falta de matplotlib, lo carga y reintenta 1 vez.
  if (result.error && !mplReady && /matplotlib|No module named 'matplotlib'|pyplot/.test(result.error)) {
    try {
      await ensureMatplotlib(py);
      jsonStr = await py.runPythonAsync('__run(__user_code)');
      result = JSON.parse(jsonStr);
    } catch (e) { /* conserva el error original */ }
    setStatus('Python 3.12 · WASM · LISTO', 'ready');
  }
  return result;
}

/* --- Pintar salida --- */
function renderOutput(panel, result) {
  panel.innerHTML = '';
  if (result.error) {
    const span = document.createElement('span');
    span.className = 'err';
    span.textContent = result.error + '\n';
    panel.appendChild(span);
  }
  if (result.out) {
    const span = document.createElement('span');
    span.textContent = result.out;
    panel.appendChild(span);
  }
  if (!result.error && !result.out && (!result.images || !result.images.length)) {
    panel.innerHTML = '<span class="prompt">[sin salida de texto]</span>';
  }
}

function renderPlots(box, images) {
  if (!box) return;
  if (!images || !images.length) {
    box.innerHTML = '<div class="empty">Sin gráfico. Usa matplotlib: plt.plot(), plt.hist()…</div>';
    return;
  }
  box.innerHTML = '';
  for (const b64 of images) {
    const img = document.createElement('img');
    img.src = 'data:image/png;base64,' + b64;
    img.alt = 'gráfico';
    img.style.maxWidth = '100%';
    box.appendChild(img);
  }
}

/* ============================================================
   Enlaza cada bloque .rconsole
   ============================================================ */
function bindConsole(el) {
  const ta   = el.querySelector('textarea');
  const out  = el.querySelector('.output');
  const plot = el.querySelector('.plotbox');
  const runBtn   = el.querySelector('[data-act=run]');
  const clearBtn = el.querySelector('[data-act=clear]');
  const resetBtn = el.querySelector('[data-act=reset]');
  const xlsxIn   = el.querySelector('[data-act=loadxlsx]');
  const xlsxOut  = el.querySelector('[data-act=savexlsx]');
  const chip     = el.querySelector('.filechip');
  const original = ta ? ta.value : '';

  async function execute() {
    if (!ta) return;
    runBtn.disabled = true;
    const prev = runBtn.textContent;
    runBtn.textContent = '⟳ ejecutando…';
    if (out) out.innerHTML = '<span class="prompt">Corriendo Python…</span>';
    const result = await runPython(ta.value);
    renderOutput(out, result);
    renderPlots(plot, result.images);
    runBtn.disabled = false;
    runBtn.textContent = prev;
  }

  if (runBtn) runBtn.addEventListener('click', execute);
  if (clearBtn) clearBtn.addEventListener('click', () => {
    if (out) out.innerHTML = '';
    if (plot) plot.innerHTML = '<div class="empty">Sin gráfico.</div>';
  });
  if (resetBtn) resetBtn.addEventListener('click', () => { ta.value = original; });

  // Ctrl/Cmd + Enter para ejecutar; Tab inserta 4 espacios
  if (ta) ta.addEventListener('keydown', (ev) => {
    if ((ev.ctrlKey || ev.metaKey) && ev.key === 'Enter') { ev.preventDefault(); execute(); }
    if (ev.key === 'Tab') {
      ev.preventDefault();
      const s = ta.selectionStart, e = ta.selectionEnd;
      ta.value = ta.value.slice(0, s) + '    ' + ta.value.slice(e);
      ta.selectionStart = ta.selectionEnd = s + 4;
    }
  });

  /* --- Cargar Excel/CSV -> DataFrame `datos` --- */
  if (xlsxIn) {
    const fileEl = el.querySelector('input[type=file]');
    xlsxIn.addEventListener('click', () => fileEl && fileEl.click());
    if (fileEl) fileEl.addEventListener('change', async (ev) => {
      const file = ev.target.files[0];
      if (!file) return;
      if (chip) chip.textContent = '⟳ cargando ' + file.name + '…';
      try {
        const buf = await file.arrayBuffer();
        const wb = XLSX.read(buf, { type: 'array' });
        const ws = wb.Sheets[wb.SheetNames[0]];
        const csv = XLSX.utils.sheet_to_csv(ws);
        const py = await boot();
        py.FS.writeFile('/tmp/datos.csv', csv);
        await py.runPythonAsync('NS["datos"] = pd.read_csv("/tmp/datos.csv")');
        if (chip) chip.textContent = '✓ ' + file.name + ' → DataFrame `datos`';
        const result = await runPython('print("Datos cargados en `datos`:")\nprint(datos.head())\nprint("filas x columnas:", datos.shape)');
        renderOutput(out, result);
      } catch (e) {
        if (chip) chip.textContent = '✗ error: ' + (e.message || e);
      }
    });
  }

  /* --- Exportar un DataFrame a Excel --- */
  if (xlsxOut) {
    xlsxOut.addEventListener('click', async () => {
      const name = (prompt('¿Qué objeto exportar a Excel? (DataFrame)', 'datos') || '').trim();
      if (!name) return;
      try {
        const py = await boot();
        const csv = await py.runPythonAsync(
          `_o = NS.get(${JSON.stringify(name)})\n` +
          `"" if _o is None else (_o if isinstance(_o, str) else pd.DataFrame(_o).to_csv(index=False))`
        );
        if (!csv) { alert("'" + name + "' no existe o no es una tabla. Ejecuta primero el código que lo crea."); return; }
        const wb = XLSX.read(csv, { type: 'string' });
        XLSX.writeFile(wb, name + '_pychoice.xlsx');
      } catch (e) {
        alert('No se pudo exportar: ' + (e.message || e));
      }
    });
  }
}

/* ============================================================
   Navegacion sin recargar (SPA ligera).
   Mantiene el motor Pyodide VIVO al pasar de una leccion a otra:
   asi el motor arranca UNA sola vez y la primera ejecucion de cada
   leccion ya no espera el reinicio del interprete.
   ============================================================ */
function bindConsolesIn(root) {
  root.querySelectorAll('.rconsole').forEach(bindConsole);
}

/* Re-ejecuta los <script> que vengan dentro del contenido intercambiado
   (innerHTML no ejecuta scripts por si solo). */
function runScriptsIn(root) {
  root.querySelectorAll('script').forEach((old) => {
    const s = document.createElement('script');
    for (const attr of old.attributes) s.setAttribute(attr.name, attr.value);
    s.textContent = old.textContent;
    old.replaceWith(s);
  });
}

function updateSidebarActive(pathname) {
  document.querySelectorAll('.sidebar .tree a').forEach((a) => {
    let ap;
    try { ap = new URL(a.href).pathname; } catch (e) { ap = a.getAttribute('href'); }
    a.classList.toggle('on', ap === pathname);
  });
}

function isInternalNav(a) {
  if (!a) return false;
  if (a.target === '_blank' || a.hasAttribute('download')) return false;
  const href = a.getAttribute('href');
  if (!href || href.charAt(0) === '#') return false;         // ancla en la misma pagina
  if (/^(https?:|mailto:|tel:)/i.test(href)) {               // externos
    return a.origin === location.origin;                     // salvo mismo origen absoluto
  }
  return true;                                               // rutas relativas internas
}

let navToken = 0;
async function navigateTo(url, push) {
  const my = ++navToken;
  const target = new URL(url, location.origin);
  try {
    const resp = await fetch(target.href, { headers: { 'X-Requested-With': 'fetch' } });
    if (!resp.ok) { location.href = target.href; return; }
    const html = await resp.text();
    if (my !== navToken) return;                             // otra navegacion la reemplazo
    const doc = new DOMParser().parseFromString(html, 'text/html');
    const newMain = doc.querySelector('main.main');
    const curMain = document.querySelector('main.main');
    if (!newMain || !curMain) { location.href = target.href; return; }

    curMain.className = newMain.className;
    curMain.innerHTML = newMain.innerHTML;
    document.title = doc.title || document.title;
    updateSidebarActive(target.pathname);
    bindConsolesIn(curMain);
    runScriptsIn(curMain);
    window.scrollTo(0, 0);
    if (push) history.pushState({ spa: true }, '', target.href);

    // El motor casi siempre ya esta listo (arranco una sola vez). Reinicia los
    // datos de ejemplo para que cada leccion empiece limpia y reproducible.
    boot()
      .then((py) => py.runPythonAsync('_seed()'))
      .then(() => { if (my === navToken) setStatus('Python 3.12 · WASM · LISTO', 'ready'); })
      .catch(() => {});
  } catch (e) {
    location.href = target.href;                             // ante cualquier fallo, navegacion normal
  }
}

document.addEventListener('click', (ev) => {
  if (ev.defaultPrevented || ev.button !== 0 || ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return;
  const a = ev.target.closest('a');
  if (!isInternalNav(a)) return;
  ev.preventDefault();
  document.body.classList.remove('nav-open');
  navigateTo(a.getAttribute('href'), true);
});

window.addEventListener('popstate', () => navigateTo(location.pathname + location.search, false));

/* --- Init global --- */
document.addEventListener('DOMContentLoaded', () => {
  bindConsolesIn(document);
  boot().catch(() => setStatus('Python · error de carga', 'err'));
});

window.__runPython = runPython;
window.__bootPy = boot;
window.__navigateTo = navigateTo;
