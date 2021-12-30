from django.db import models
from django.core.validators import MinLengthValidator

# Clase para modelar las razas
class Breed(models.Model):
    name = models.CharField(
            max_length = 200,
            validators = [
                    MinLengthValidator(2, "Breed must be greater than 1 character"),
                ]
        )

    # Método para obtener objeto como cadena
    def __str__(self):
        return self.name

# Clase para modelar un gato
class Cat(models.Model):
    nickname = models.CharField(
            max_length = 200,
            validators = [
                    MinLengthValidator(2, "Nickname must be greater than 1 character"),
                ]
        )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length = 300)
    # Campo como llave foránea con borrado en cascada
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
