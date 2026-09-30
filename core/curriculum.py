# -*- coding: utf-8 -*-
"""
Indice central del curriculo de PyChoice.

- CHAPTERS: todas las lecciones (capitulos), formato EstadisticaR.
- MODULES:  agrupan lecciones en modulos tematicos.
- ROUTES:   rutas de aprendizaje (tracks). Cada ruta agrupa modulos.
            Hoy existe "Ruta para ser Cientifico de datos"; mas adelante
            se sumaran otras (p. ej. Desarrollador de aplicaciones).
"""
from .curriculum_a import CHAPTERS_A
from .curriculum_b import CHAPTERS_B
from .curriculum_c import CHAPTERS_C
from .curriculum_d import CHAPTERS_D
from .curriculum_e import CHAPTERS_E
from .curriculum_f import CHAPTERS_F
from .curriculum_g import CHAPTERS_G
from .curriculum_h import CHAPTERS_H
from .curriculum_h2 import CHAPTERS_H2
from .curriculum_j import CHAPTERS_J
from .curriculum_k import CHAPTERS_K
from .curriculum_datasets import datasets_for, dataset_list  # noqa: F401

CHAPTERS = (CHAPTERS_A + CHAPTERS_B + CHAPTERS_C + CHAPTERS_D
            + CHAPTERS_E + CHAPTERS_F + CHAPTERS_G + CHAPTERS_H + CHAPTERS_H2
            + CHAPTERS_J + CHAPTERS_K)
BY_NUM = {c["num"]: c for c in CHAPTERS}
BY_SLUG = {c["slug"]: c for c in CHAPTERS}


def get_chapter(num):
    """Devuelve el dict del capitulo por su numero (1..N)."""
    return BY_NUM[num]


def nav_list():
    """Lista ligera de lecciones para el menu lateral / home."""
    return [
        {"num": c["num"], "slug": c["slug"], "code": c["code"],
         "title": c["title"], "subtitle": c["subtitle"]}
        for c in CHAPTERS
    ]


# ====================================================================
#  MODULOS: agrupan lecciones. status = "listo" | "proximamente"
#  Un modulo "listo" referencia lecciones existentes (lessons=[nums]).
#  Un modulo "proximamente" lista los titulos planificados (planned=[...]).
# ====================================================================
MODULES = [
    {"code": "A", "title": "Fundamentos de Python", "status": "listo",
     "desc": "Instalar Python, sintaxis básica, variables, tipos, librerías y condicionales.",
     "lessons": [1, 2, 3, 4]},
    {"code": "B", "title": "Datos y control", "status": "listo",
     "desc": "Cargar Excel, bucles for/while y tu primera estadística con pandas.",
     "lessons": [5, 6, 7, 8]},
    {"code": "C", "title": "Python intermedio", "status": "listo",
     "desc": "Estructuras de datos, funciones, comprensiones, errores y archivos.",
     "lessons": [9, 10, 11, 12]},
    {"code": "D", "title": "Manipulación de datos", "status": "listo",
     "desc": "NumPy a fondo y pandas avanzado: selección, limpieza, combinar y reformar tablas.",
     "lessons": [13, 14, 15, 16, 17]},
    {"code": "E", "title": "Análisis exploratorio (EDA)", "status": "listo",
     "desc": "Hacer preguntas a los datos: estadística aplicada, atípicos y relaciones.",
     "lessons": [18, 19, 20]},
    {"code": "F", "title": "Visualización de datos", "status": "listo",
     "desc": "Comunicar con gráficos: matplotlib a fondo, seaborn y storytelling.",
     "lessons": [21, 22, 23]},
    {"code": "G", "title": "Estadística y probabilidad", "status": "listo",
     "desc": "El sustento para afirmar cosas con datos: probabilidad, distribuciones e inferencia.",
     "lessons": [24, 25, 26]},
    {"code": "H", "title": "Machine Learning (nivel pro)", "status": "listo",
     "desc": "Flujo completo con scikit-learn: preparación, regresión, clasificación, "
             "evaluación, ensembles, validación cruzada, no supervisado y proyecto end-to-end.",
     "lessons": [27, 28, 29, 30, 31, 32, 33, 34, 35, 36]},
    {"code": "I", "title": "Proyecto y cierre", "status": "proximamente",
     "desc": "Integrar todo en un proyecto de ciencia de datos y comunicar resultados.",
     "planned": ["Proyecto integrador de data science", "Comunicar resultados y siguientes pasos"]},
]


# ====================================================================
#  MODULOS de la ruta "Ingeniero de IA con Python" (codigos J-O)
#  Metaheuristicas + redes neuronales desde la base + IA aplicada,
#  todo ejecutable en el navegador (numpy / scipy / scikit-learn).
#  Se iran publicando uno a uno (hoy: proximamente).
# ====================================================================
MODULES_IA = [
    {"code": "J", "title": "Fundamentos de IA y pensamiento algorítmico", "status": "listo",
     "desc": "El panorama de la IA con Python, problemas de búsqueda y optimización, y cómo evaluar algoritmos.",
     "lessons": [39, 40, 41]},
    {"code": "K", "title": "Metaheurísticas I: búsqueda local", "status": "listo",
     "desc": "Optimizar con SciPy y buscar soluciones con hill climbing, recocido simulado y búsqueda tabú.",
     "lessons": [42, 43, 44, 45]},
    {"code": "L", "title": "Metaheurísticas bioinspiradas", "status": "proximamente",
     "desc": "Algoritmos poblacionales: genéticos, enjambre de partículas (PSO) y colonia de hormigas (ACO).",
     "planned": ["Algoritmos genéticos I", "Algoritmos genéticos II (TSP)",
                 "Optimización por enjambre de partículas (PSO)", "Colonia de hormigas (ACO)"]},
    {"code": "M", "title": "Redes neuronales desde la base", "status": "proximamente",
     "desc": "Del perceptrón al backpropagation con numpy, y redes con scikit-learn (MLP).",
     "planned": ["La neurona y el perceptrón", "Perceptrón multicapa y forward pass",
                 "Backpropagation y descenso de gradiente", "Redes con scikit-learn (MLP)",
                 "Buenas prácticas y panorama del deep learning"]},
    {"code": "N", "title": "IA moderna aplicada", "status": "proximamente",
     "desc": "Aprendizaje por refuerzo, NLP clásico, recomendadores y metaheurísticas para ML + IA responsable.",
     "planned": ["Aprendizaje por refuerzo básico (Q-learning)", "NLP clásico (TF-IDF)",
                 "Sistemas de recomendación", "Metaheurísticas + ML e IA responsable"]},
    {"code": "O", "title": "Proyecto de Ingeniería de IA", "status": "proximamente",
     "desc": "Integrar todo en un proyecto de IA de punta a punta y planificar los siguientes pasos.",
     "planned": ["Proyecto integrador de IA", "Cierre y siguientes pasos"]},
]


# ====================================================================
#  RUTAS DE APRENDIZAJE (tracks)
# ====================================================================
ROUTES = [
    {
        "slug": "cientifico-datos",
        "title": "Ruta para ser Científico de datos",
        "short": "científico de datos",
        "subtitle": "De cero a analizar, visualizar y modelar datos con Python",
        "intro": """
<p>Esta ruta te lleva paso a paso desde los <b>fundamentos de Python</b> hasta el <b>análisis y la
ciencia de datos</b>. Avanza módulo por módulo: cada uno reúne varias lecciones con teoría, ejemplos
ejecutables y ejercicios. Los módulos marcados <b>listo</b> ya están disponibles; el resto se irá
publicando en orden.</p>
""",
        "modules": MODULES,
    },
    {
        "slug": "ingeniero-ia",
        "title": "Ruta para ser Ingeniero de IA con Python",
        "short": "ingeniero de IA",
        "subtitle": "Metaheurísticas, redes neuronales e IA moderna, programadas desde su base",
        "intro": """
<p>Esta ruta enseña a <b>construir sistemas de inteligencia artificial con Python</b>: optimización y
metaheurísticas (algoritmos genéticos, colonia de hormigas, recocido simulado, PSO), redes neuronales
programadas desde su mecánica interna y aplicaciones modernas (aprendizaje por refuerzo, NLP,
recomendadores). Todo se ejecuta en el navegador con <b>numpy, scipy y scikit-learn</b>; el deep
learning con frameworks se presenta como el siguiente paso. Recomendado tras dominar los fundamentos de
Python y numpy/pandas de la ruta de ciencia de datos.</p>
""",
        "modules": MODULES_IA,
    },
]

BY_ROUTE = {r["slug"]: r for r in ROUTES}


def get_route(slug):
    return BY_ROUTE.get(slug)


def route_list():
    """Lista ligera de rutas para el menu lateral / home."""
    return [{"slug": r["slug"], "title": r["title"], "short": r["short"],
             "subtitle": r["subtitle"]} for r in ROUTES]


def route_modules(route):
    """Resuelve los modulos de una ruta con los datos de sus lecciones."""
    out = []
    total = done = 0
    for m in route["modules"]:
        item = dict(m)
        if m.get("lessons"):
            item["items"] = [{"num": n, "title": BY_NUM[n]["title"],
                              "subtitle": BY_NUM[n]["subtitle"]} for n in m["lessons"]]
            total += len(m["lessons"])
            done += len(m["lessons"])
        else:
            item["items"] = [{"num": None, "title": t, "subtitle": ""}
                             for t in m.get("planned", [])]
            total += len(m.get("planned", []))
        out.append(item)
    return out, done, total
