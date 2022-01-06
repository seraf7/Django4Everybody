from django.contrib import admin
from unesco.models import Site, Category, Iso, Region, State

# Añade modelos al sitio de administración
admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Iso)
admin.site.register(Region)
admin.site.register(State)
