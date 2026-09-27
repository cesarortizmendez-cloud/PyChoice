# -*- coding: utf-8 -*-
"""
Indice central del curriculo de PyChoice.
Formato identico a EstadisticaR: cada leccion es un capitulo con
  num, slug, code, title, subtitle, apunte
  concepts  -> lista de (termino, definicion)
  theory    -> HTML didactico
  examples  -> lista de {title, explain, code}  (Python ejecutable en Pyodide)
  dataset   -> texto breve (datos de ejemplo disponibles)
  exercises -> lista de retos para el alumno
"""
from .curriculum_a import CHAPTERS_A
from .curriculum_b import CHAPTERS_B

CHAPTERS = CHAPTERS_A + CHAPTERS_B
BY_NUM = {c["num"]: c for c in CHAPTERS}
BY_SLUG = {c["slug"]: c for c in CHAPTERS}


def get_chapter(num):
    """Devuelve el dict del capitulo por su numero (1..N)."""
    return BY_NUM[num]


def nav_list():
    """Lista ligera para el menu lateral / home."""
    return [
        {"num": c["num"], "slug": c["slug"], "code": c["code"],
         "title": c["title"], "subtitle": c["subtitle"]}
        for c in CHAPTERS
    ]
