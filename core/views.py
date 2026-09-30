# -*- coding: utf-8 -*-
"""Vistas del nucleo: portada, consola libre y hoja de referencia Python."""
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.cache import never_cache
from .curriculum import (nav_list, BY_NUM, get_route, route_list, route_modules,
                         datasets_for, dataset_list)


def home(request):
    return render(request, "core/home.html", {
        "chapters": nav_list(),
        "routes": route_list(),
        "active": "home",
    })


def lesson(request, num):
    """Vista unica para todas las lecciones (capitulos)."""
    ch = BY_NUM.get(num)
    if ch is None:
        raise Http404("Lección no encontrada")
    return render(request, "core/chapter.html", {
        "ch": ch,
        "chapters": nav_list(),
        "routes": route_list(),
        "datasets": datasets_for(num),
        "active": ch["slug"],
    })


def route(request, slug):
    """Pagina de una ruta de aprendizaje (track): sus modulos y lecciones."""
    r = get_route(slug)
    if r is None:
        raise Http404("Ruta no encontrada")
    modules, done, total = route_modules(r)
    return render(request, "core/route.html", {
        "route": r,
        "modules": modules,
        "done": done,
        "total": total,
        "chapters": nav_list(),
        "routes": route_list(),
        "active": r["slug"],
    })


CONSOLE_SEED = """# Consola Python libre - escribe y presiona Ctrl+Enter
# Ya tienes cargados: numpy (np), pandas (pd), matplotlib.pyplot (plt)
# y los datos de ejemplo: notas (lista) y datos (DataFrame).

print("promedio de notas:", round(sum(notas) / len(notas), 2))

# Un vistazo al DataFrame de ejemplo:
print(datos)
print(datos["ventas"].describe())

# ¿Que datasets tienes para practicar?
catalogo()          # lista todos los datasets disponibles
# df = cargar("propinas")   # cargalo en `datos` y practica
"""


def console(request):
    """Consola Python libre, sin contenido de leccion."""
    return render(request, "core/console.html", {
        "chapters": nav_list(),
        "routes": route_list(),
        "active": "console",
        "seed": CONSOLE_SEED,
    })


CHEATSHEET = [
    {"titulo": "Fundamentos de Python", "filas": [
        ("print()", "Muestra valores por pantalla", 'print("Hola", 2026)'),
        ("=", "Asigna un valor a una variable", 'x = 42'),
        ("type()", "Tipo de un objeto", 'type(3.14)'),
        ("len()", "Longitud de una secuencia", 'len([1, 2, 3])'),
        ("input()", "Lee texto (no interactivo aqui)", 'nombre = "Ana"'),
        ("f-string", "Interpola valores en texto", 'f"total: {x}"'),
    ]},
    {"titulo": "Estructuras de datos", "filas": [
        ("list", "Coleccion ordenada y mutable", 'xs = [4, 8, 15, 16]'),
        ("dict", "Pares clave-valor", 'd = {"a": 1, "b": 2}'),
        ("tuple", "Coleccion ordenada inmutable", 'p = (10, 20)'),
        ("set", "Conjunto sin duplicados", 's = {1, 2, 2, 3}'),
        ("slicing", "Sub-secuencia", 'xs[1:3]'),
        ("comprension", "Construye listas al vuelo", '[n*2 for n in xs]'),
    ]},
    {"titulo": "Control de flujo", "filas": [
        ("if / elif / else", "Decisiones", 'if x > 0: print("pos")'),
        ("for", "Repite sobre una secuencia", 'for n in xs: print(n)'),
        ("while", "Repite mientras se cumpla", 'while x > 0: x -= 1'),
        ("def", "Define una funcion", 'def doble(n): return n*2'),
        ("return", "Devuelve un resultado", 'return total'),
        ("in", "Pertenencia", '"a" in d'),
    ]},
    {"titulo": "Numeros y estadistica base", "filas": [
        ("sum()", "Suma de una secuencia", 'sum(xs)'),
        ("min() / max()", "Minimo y maximo", 'max(xs)'),
        ("round()", "Redondea", 'round(3.14159, 2)'),
        ("statistics.mean()", "Promedio", 'st.mean(xs)'),
        ("statistics.median()", "Mediana", 'st.median(xs)'),
        ("statistics.pstdev()", "Desviacion estandar", 'st.pstdev(xs)'),
    ]},
    {"titulo": "pandas (analisis de datos)", "filas": [
        ("pd.DataFrame()", "Crea una tabla", 'pd.DataFrame({"a": [1,2]})'),
        ("df.head()", "Primeras filas", 'df.head(3)'),
        ("df.describe()", "Resumen estadistico", 'df.describe()'),
        ("df['col']", "Selecciona una columna", 'df["edad"]'),
        ("df[df.x > 5]", "Filtra filas", 'df[df["edad"] > 30]'),
        ("df.groupby()", "Agrupa y resume", 'df.groupby("area").mean()'),
    ]},
    {"titulo": "Visualizacion (matplotlib)", "filas": [
        ("plt.plot()", "Linea / dispersion", 'plt.plot(x, y)'),
        ("plt.hist()", "Histograma", 'plt.hist(datos)'),
        ("plt.bar()", "Barras", 'plt.bar(cat, val)'),
        ("plt.scatter()", "Nube de puntos", 'plt.scatter(x, y)'),
        ("plt.title()", "Titulo del grafico", 'plt.title("Ventas")'),
        ("plt.show()", "Renderiza el grafico", 'plt.show()'),
    ]},
]


def cheatsheet(request):
    return render(request, "core/cheatsheet.html", {
        "chapters": nav_list(),
        "routes": route_list(),
        "active": "cheatsheet",
        "grupos": CHEATSHEET,
    })


DATASETS_SEED = """# 1) Ver todos los datasets disponibles
catalogo()

# 2) Usar uno directamente por su nombre
print(propinas.head())
print("filas x columnas:", propinas.shape)

# 3) O cargarlo en 'datos' para reutilizar el codigo de las lecciones
df = cargar("viviendas")
print(df.describe())
"""


def datasets(request):
    """Pagina de referencia con el catalogo completo de datasets de practica."""
    return render(request, "core/datasets.html", {
        "chapters": nav_list(),
        "routes": route_list(),
        "active": "datasets",
        "datasets": dataset_list(),
        "seed": DATASETS_SEED,
    })


def manifest(request):
    """Manifest PWA para instalar PyChoice en Android, Windows e iPhone."""
    data = {
        "id": "/",
        "name": "PyChoice - Aprende Python para decidir con datos",
        "short_name": "PyChoice",
        "description": "Plataforma interactiva para aprender Python desde la base, "
                       "ejecutando codigo real en el navegador.",
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "background_color": "#0d1117",
        "theme_color": "#3776AB",
        "orientation": "portrait-primary",
        "lang": "es-CL",
        "categories": ["education", "productivity"],
        "icons": [
            {"src": "/static/core/icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "/static/core/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "/static/core/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}
        ],
        "shortcuts": [
            {"name": "Consola Python", "short_name": "Consola", "description": "Abrir la consola libre para practicar Python.", "url": "/consola/", "icons": [{"src": "/static/core/icons/icon-192.png", "sizes": "192x192"}]},
            {"name": "Referencia Python", "short_name": "Referencia", "description": "Abrir la hoja de referencia rapida de Python.", "url": "/referencia/", "icons": [{"src": "/static/core/icons/icon-192.png", "sizes": "192x192"}]}
        ]
    }
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})


@never_cache
def service_worker(request):
    """Service worker en la raiz del sitio para habilitar instalacion PWA."""
    content = r'''
const CACHE_NAME = 'pychoice-pwa-v2';
const CDN_CACHE = 'pychoice-cdn-v1';   // Pyodide, wheels y SheetJS (URLs versionadas)
const CDN_HOSTS = ['cdn.jsdelivr.net', 'cdnjs.cloudflare.com'];
const APP_SHELL = [
  '/',
  '/manifest.json',
  '/static/core/css/app.css',
  '/static/core/js/pyengine.js',
  '/static/core/js/pwa-install.js',
  '/static/core/icons/icon-192.png',
  '/static/core/icons/icon-512.png',
  '/static/core/icons/icon-maskable-512.png',
  '/static/core/icons/apple-touch-icon.png',
  '/static/core/icons/favicon-32.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => Promise.all(APP_SHELL.map((url) => {
        return fetch(url).then((response) => {
          if (response.ok) return cache.put(url, response);
          return null;
        }).catch(() => null);
      })))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.map((key) => (key === CACHE_NAME || key === CDN_CACHE) ? null : caches.delete(key))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);

  // Cache-first para los grandes recursos de CDN (Pyodide + wheels + SheetJS).
  // Sus URLs llevan la version fija, asi que el contenido nunca cambia:
  // se descarga una sola vez y luego abre al instante (y sin conexion).
  if (CDN_HOSTS.indexOf(url.hostname) !== -1) {
    event.respondWith(
      caches.open(CDN_CACHE).then((cache) =>
        cache.match(request).then((hit) => hit || fetch(request).then((response) => {
          if (response && (response.ok || response.type === 'opaque')) {
            cache.put(request, response.clone());
          }
          return response;
        }))
      )
    );
    return;
  }

  if (url.origin !== self.location.origin) return;

  if (url.pathname.startsWith('/static/')) {
    event.respondWith(
      fetch(request).then((response) => {
        const copy = response.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(request, copy));
        return response;
      }).catch(() => caches.match(request))
    );
    return;
  }

  if (request.mode === 'navigate') {
    event.respondWith(fetch(request).catch(() => caches.match('/')));
  }
});
'''.strip()
    response = HttpResponse(content, content_type="application/javascript; charset=utf-8")
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response["Service-Worker-Allowed"] = "/"
    return response
