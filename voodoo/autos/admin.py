from django.contrib import admin
from autos.models import Make, Auto

# Añade modelos a página de administración
admin.site.register(Make)
admin.site.register(Auto)
