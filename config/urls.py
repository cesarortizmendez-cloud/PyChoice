# -*- coding: utf-8 -*-
"""Rutas raiz del proyecto PyChoice."""
from django.urls import path
from core import views as core_views

urlpatterns = [
    path("", core_views.home, name="home"),
    path("consola/", core_views.console, name="console"),
    path("referencia/", core_views.cheatsheet, name="cheatsheet"),
    path("manifest.json", core_views.manifest, name="manifest"),
    path("service-worker.js", core_views.service_worker, name="service_worker"),

    # Rutas de aprendizaje (tracks) y lecciones
    path("ruta/<slug:slug>/", core_views.route, name="route"),
    path("leccion/<int:num>/", core_views.lesson, name="lesson"),
]
