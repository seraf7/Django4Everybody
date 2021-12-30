# Biblioteca para manejo de rutas
from django.urls import path
# Importa las vistas de la aplicación
from . import views

# Nombre de la aplicación
app_name = 'hello'

# Define los patrones de la URL para la aplicación
urlpatterns = [
    path('', views.helloView, name='hello'),
]