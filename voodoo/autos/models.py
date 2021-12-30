from django.db import models
from django.core.validators import MinLengthValidator

class Make(models.Model):
    # Se define un campo de texto
    name = models.CharField(
        max_length = 200,
        # Texto de ayuda para errores
        help_text = 'Enter a make (e.g. Dodge)',
        # Valida la longitud mínima
        validators = [MinLengthValidator(2, "Make must be greater than 1 character")]
    )

    # Método para representar como cadena
    def __str__(self):
        return self.name

class Auto(models.Model):
    nickname = models.CharField(
        max_length = 200,
        validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname


