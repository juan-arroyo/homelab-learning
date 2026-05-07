# URL definitions for the project

from django.http import HttpResponse
from django.urls import path

# Minimal view — returns a simple HTML response
def home(request):
    return HttpResponse("""
        <h1>Django CI/CD - Homelab Learning</h1>
        <p>Automatically deployed from GitHub Actions</p>
        <p>Runner: rpi-server (Raspberry Pi 5)</p>
    """)

# Available URL patterns
urlpatterns = [
    path('', home),   # Root URL → home view
]