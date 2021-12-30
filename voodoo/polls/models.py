from django.db import models
from django.utils import timezone

import datetime

# Clase para modelar una pregunta
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Metodo para saber si se publicó hace un día o menos
    def publicada_recientemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # Representación como cadena
    def __str__(self):
        return self.question_text


# Clase para modelas una respuesta
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes =  models.IntegerField(default=0)

    # Representación como cadena
    def __str__(self):
        return self.choice_text
