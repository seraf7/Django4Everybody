from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Clase para modelar un anuncio
class Ad(models.Model):
    title = models.CharField(
        max_length = 200,
        validators = [MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Establece atomáticamente fecha/hora al crear el objeto
    created_at = models.DateTimeField(auto_now_add=True)
    # Guarda atomáticamente fecha/hora de la ultima modificación
    updated_at = models.DateTimeField(auto_now=True)

    # Método para imprimir objeto como cadena
    def __str__(self):
        return self.title
