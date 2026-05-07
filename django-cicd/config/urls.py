# URL definitions for the project

from django.http import HttpResponse
from django.urls import path

# Minimal view — returns a simple HTML response
def home(request):
    return HttpResponse("""
        <h1>Broken page</h1>
        <p>This text does not match what the test expects</p>
    """)

# Available URL patterns
urlpatterns = [
    path('', home),   # Root URL → home view
]