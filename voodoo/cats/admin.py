from django.contrib import admin
from cats.models import Breed, Cat

# Añade modelos a página de administración
admin.site.register(Breed)
admin.site.register(Cat)