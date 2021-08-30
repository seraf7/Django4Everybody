# Biblioteca para fechas
import datetime

from django.db import models
from django.utils import timezone

# Definición de una clase para preguntas, se hereda de Model
class Question(models.Model):
    # Campo de texto con la pregunta
    question_text = models.CharField(max_length=200)
    # Campo de fecha con la publicación
    pub_date = models.DateTimeField('Fecha de publicación')

    # Se define el metodo para representar el objeto como cadena
    def __str__(self):
        return self.question_text

    # Método para indicar si la pregunta se publicó máximo hace un día
    def publicada_recientemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

# Definición de una clase para opciones
class Choice(models.Model):
    # Relación con el registro padre, se asocia a una pregunta
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # Campo con la cantidad de votos, inicializado en 0
    votes = models.IntegerField(default=0)

    # Método para representar el objeto como cadena
    def __str__(self):
        return self.choice_text
