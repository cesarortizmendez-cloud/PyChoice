# -*- coding: utf-8 -*-
"""Context processors globales para las plantillas."""
from .projects import sidebar_projects


def projects_nav(request):
    """Expone los proyectos listos en todas las plantillas (menú lateral)."""
    return {"projects": sidebar_projects()}
