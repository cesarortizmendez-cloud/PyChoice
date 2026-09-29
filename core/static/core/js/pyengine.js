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
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Espacio de nombres compartido por todas las consolas (como el entorno global de R)
NS = {"__name__": "__main__", "np": np, "pd": pd, "plt": plt}

def _seed():
    NS["notas"] = [4.2, 5.8, 6.1, 3.9, 5.0, 6.7, 4.5, 5.3]
    NS["datos"] = pd.DataFrame({
        "mes":    ["ene", "feb", "mar", "abr", "may"],
        "region": ["norte", "sur", "norte", "centro", "sur"],
        "ventas": [120, 95, 130, 110, 88],
        "unidades": [12, 9, 13, 11, 8],
    })

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
    setStatus('Python · cargando numpy, pandas, matplotlib…', '');
    await py.loadPackage(['numpy', 'pandas', 'matplotlib']);
    await py.runPythonAsync(HARNESS);
    pyodide = py;
    setStatus('Python 3.12 · WASM · LISTO', 'ready');
    return py;
  })();
  return bootPromise;
}

/* Ejecuta codigo y devuelve {out, error, images}.
   Antes de ejecutar, autocarga los paquetes que el codigo importe
   (seaborn, scipy, scikit-learn, etc.) la primera vez que se usan. */
async function runPython(code) {
  const py = await boot();
  try {
    setStatus('Python · preparando paquetes…', 'ready');
    await py.loadPackagesFromImports(code);
  } catch (e) { /* si falta un paquete, Python mostrara el ImportError */ }
  setStatus('Python 3.12 · WASM · LISTO', 'ready');
  py.globals.set('__user_code', code);
  const jsonStr = await py.runPythonAsync('__run(__user_code)');
  try { return JSON.parse(jsonStr); }
  catch (e) { return { out: '', error: String(e), images: [] }; }
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

/* --- Init global --- */
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.rconsole').forEach(bindConsole);
  boot().catch(() => setStatus('Python · error de carga', 'err'));
});

window.__runPython = runPython;
window.__bootPy = boot;
