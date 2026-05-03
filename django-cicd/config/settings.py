# Minimal Django configuration for the CI/CD practice project

SECRET_KEY = 'django-insecure-homelab-learning-cicd-practice-key'

DEBUG = True

# Allow connections from any host (for testing purposes)
ALLOWED_HOSTS = ['*']

# File that defines the application URL routes
ROOT_URLCONF = 'config.urls'

# WSGI application entry point
WSGI_APPLICATION = 'config.wsgi.application'

# Default Django apps
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
]

# SQLite database — simplest option, no separate container needed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/db.sqlite3',
    }
}

# Static files URL
STATIC_URL = '/static/'

# Timezone
TIME_ZONE = 'Europe/Madrid'