from django.contrib import admin
from .models import Question

# Se agrgan los modelos a la pantalla de administración
admin.site.register(Question)
