# Configuración mínima de Django para el proyecto de práctica CI/CD

SECRET_KEY = 'django-insecure-homelab-learning-cicd-practice-key'

DEBUG = True

# Permite conexiones desde cualquier host (para pruebas)
ALLOWED_HOSTS = ['*']

# Archivo que define las URLs de la aplicación
ROOT_URLCONF = 'config.urls'

# Archivo WSGI (ya lo tenemos)
WSGI_APPLICATION = 'config.wsgi.application'

# Apps instaladas por defecto de Django
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
]

# Base de datos SQLite — la más simple, no necesita contenedor aparte
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/db.sqlite3',
    }
}

# Configuración de archivos estáticos
STATIC_URL = '/static/'

# Zona horaria
TIME_ZONE = 'Europe/Madrid'