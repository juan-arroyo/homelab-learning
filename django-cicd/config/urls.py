# Definición de URLs del proyecto

from django.http import HttpResponse
from django.urls import path

# Vista mínima — devuelve un HTML simple
def home(request):
    return HttpResponse("""
        <h1>Django CI/CD - Homelab Learning</h1>
        <p>Desplegado automáticamente desde GitHub Actions</p>
        <p>Runner: rpi-server (Raspberry Pi 5)</p>
    """)

# Lista de URLs disponibles
urlpatterns = [
    path('', home),   # URL raíz → vista home
]