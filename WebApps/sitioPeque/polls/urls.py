# @Autor:           Seraf
# @Fecha:           27/08/2021
# @Descripcion:     Script para realizar el mapeo de la aplicación a una URL

# Biblioteca para el manejo de URL
from django.urls import path
# Se importa el archivo de la vista
from . import views

# Se crea la lista de las vistas
urlpatterns = [
    # Se nombra el index de la aplicación
    path('', views.index, name='index')
]
