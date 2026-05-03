# Punto de entrada WSGI — gunicorn usa este archivo para arrancar Django

import os
from django.core.wsgi import get_wsgi_application

# Le dice a Django qué archivo de settings usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()