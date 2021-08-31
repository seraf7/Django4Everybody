"""sitioPeque URL Configuration

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
from django.urls import include, path

# Biblioteca para funcionalidades del SO
import os
# Biblioteca para definición de URL
from django.conf.urls import url
# Biblioteca para manejo de archivos estáticos
from django.views.static import serve

# Se define la ruta del directorio base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Se define el sitio raíz, del directorio site
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    # Se define la dirección de las vistas
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    # Definición de una nueva URL para el directorio site
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name = 'site_path'),
]
