# -*- coding: utf-8 -*-
"""WSGI para PyChoice. Vercel importa la variable `app`."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
app = application   # Vercel (@vercel/python) espera `app`
