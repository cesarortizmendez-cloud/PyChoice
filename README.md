# PyChoice · Terminal de Python

> **Software abierto de aprendizaje de Python**, creado por el **Dr. César Ortiz Méndez** — [cv-cesarortiz.vercel.app](https://cv-cesarortiz.vercel.app)

Webapp educativa en **Django** para aprender **Python desde la base**, directamente en el
navegador. Cada lección combina **teoría**, **conceptos clave** y una serie de **ejemplos con una
consola de Python real, funcional**, capaz de **cargar Excel** y **exportar a Excel**. Mismo diseño
y arquitectura que EstadísticaR, con Python en lugar de R.

- **Python de verdad en el navegador** vía [Pyodide](https://pyodide.org/) (CPython compilado a WebAssembly). No hay servidor de Python.
- **numpy, pandas y matplotlib** cargados y listos, más datos de ejemplo (`notas`, `datos`).
- **Sin base de datos, sin usuarios, libre acceso.** Nada se almacena.
- **Excel I/O** con [SheetJS](https://sheetjs.com/): carga un `.xlsx/.csv` como el DataFrame `datos` y exporta a Excel.
- **Estética hacker / terminal** (fósforo verde, cian, magenta, ámbar).
- **Instalable como PWA** (Android, Windows, iPhone) y **desplegable en Vercel** desde GitHub.

---

## Contenido

| Ruta | Módulo |
|------|--------|
| `/` | Inicio |
| `/leccion/01/` | Primeros pasos en Python |
| `/leccion/02/` | Variables y tipos de datos |
| `/consola/` | Consola Python libre |
| `/referencia/` | Hoja de referencia de Python |

Cada lección es un **capítulo**: teoría, conceptos clave y ejemplos de código ejecutables que el
alumno corre y modifica. Este arranque incluye 2 lecciones; el resto del temario se agrega
escribiendo diccionarios en `core/curriculum_a.py` / `core/curriculum_b.py`.

## Cómo se agrega una lección

Todo el contenido vive en `core/curriculum_*.py`, separado del código. Una lección es un dict:

```python
{
  "num": 3, "slug": "...", "code": "leccion_03",
  "title": "...", "subtitle": "...", "apunte": "Leccion 3 - ...",
  "concepts": [("término", "definición"), ...],
  "theory": "<p>HTML didáctico...</p>",
  "examples": [{"title": "...", "explain": "<p>...</p>", "code": "print('...')"}, ...],
  "dataset": "notas, datos",
  "exercises": ["reto 1", "reto 2", ...],
}
```

Los `examples` son código Python ejecutable (en cada consola están disponibles `np`, `pd`, `plt` y
los datos `notas` y `datos`). Para sumar una lección: agrega el dict, crea una app en `apps/capNN/`
(copiando `cap01`) y registra su ruta en `config/urls.py` e `INSTALLED_APPS`.

---

## Desarrollo local (Windows · símbolo del sistema)

Necesitas **Python 3.10+** instalado.

```cmd
git clone https://github.com/<tu-usuario>/PyChoice.git
cd PyChoice
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Abre **http://127.0.0.1:8000/**.

> La **primera** vez que ejecutes código, el navegador descarga el motor Pyodide y los paquetes
> (numpy/pandas/matplotlib). Tarda unos segundos; luego queda en caché. La barra superior muestra
> `Python 3.12 · WASM · LISTO` cuando el motor está disponible.

---

## Despliegue en Vercel (desde GitHub)

1. Sube el proyecto a un repositorio de GitHub (`git init`, `add`, `commit`, `push`).
2. En [vercel.com](https://vercel.com): **Add New → Project → Import** tu repo.
3. Vercel detecta `vercel.json` automáticamente. (Opcional: define `DJANGO_DEBUG=False` en variables de entorno.)
4. **Deploy.** Cada `git push` vuelve a desplegar.

### Cómo está configurado el deploy

- `vercel.json` define un build **estático** (`build_files.sh` → `collectstatic` en `staticfiles/`) y
  una **función Python** (`config/wsgi.py`, que expone `app`).
- `/static/*` se sirve desde el CDN; el resto va a la función Django.
- `CompressedStaticFilesStorage` (sin manifest con hashes) para el filesystem de solo lectura de Vercel.
- **Sin base de datos**: la función Django solo sirve HTML. Todo el cómputo de Python del alumno
  ocurre en su navegador con Pyodide (cargado desde el CDN de jsDelivr), así que el despliegue es liviano.

---

## Estructura del proyecto

```
PyChoice/
├─ config/            # settings, urls, wsgi (sin BD)
├─ core/              # núcleo: vistas base, currículo, estáticos y plantillas
│  ├─ curriculum*.py  # contenido de las lecciones (teoría + conceptos + ejemplos)
│  ├─ static/core/    # app.css (diseño terminal) y pyengine.js (Pyodide + Excel)
│  └─ templates/core/ # chapter.html, home, consola, referencia, _console.html
├─ apps/cap01, cap02/ # una app Django por lección (enrutamiento)
├─ templates/base.html
├─ datos_ejemplo/     # ventas.csv para probar "cargar excel"
├─ requirements.txt · vercel.json · build_files.sh · manage.py
```

---

## Autor y licencia

Creado por el **Dr. César Ortiz Méndez** — [cv-cesarortiz.vercel.app](https://cv-cesarortiz.vercel.app).
Software abierto de aprendizaje: libre para estudiar, usar y compartir con fines educativos.
Si lo reutilizas o adaptas, por favor mantén la atribución a su autor.
