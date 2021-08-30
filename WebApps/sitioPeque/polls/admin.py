from django.contrib import admin
# Se importa la clase de preguntas
from .models import Question

# Se indica que la clase tiene una interfaz de administración
admin.site.register(Question)
