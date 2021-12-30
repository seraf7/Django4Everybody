"""voodoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Biblioteca para funcionalidades del SO
import os
# Biblioteca para la creación de URL
from django.conf.urls import url
# Biblioteca para la visualización de archivos estáticos
from django.views.static import serve
# Biblioteca para usar vistas genericas
from django.views.generic import TemplateView

# Definición del directorio base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Definición del sitio base
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    # Ruta para la vista principal
    path('', TemplateView.as_view(template_name='home/main.html')),
    # Se añade la ruta de aplicación creada
    path('polls/', include('polls.urls')),
    # Ruta para aplicación de cookies y sesiones
    path('hello/', include('hello.urls')),
    # Ruta de aplicación CRUD de autos
    path('autos/', include('autos.urls')),
    # Ruta de la aplicación CRUD de gatos
    path('cats/', include('cats.urls')),
    # Ruta para funcionalidades de sesión
    path('accounts/', include('django.contrib.auth.urls')),
    # Ruta del sitio de administración
    path('admin/', admin.site.urls),
    # Definición de un patrón de URL
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'),
]
