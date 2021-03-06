from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
from taggit.managers import TaggableManager

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

    # Relación muchos a muchos para marcar favoritos
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Fav',
        related_name='favorite_ads')

    # Campos para guardar imagen
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True,
        help_text='The MIMEType of the file')

    # Relación M:M para añadir comentarios, usa la entidad Comment
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Comment', related_name='comments_owner')

    # Campo para TAGS en los anuncios, no es obligatorio
    tags = TaggableManager(blank=True)

    # Método para imprimir objeto como cadena
    def __str__(self):
        return self.title

# Clase para modelar comentarios
class Comment(models.Model):
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )

    # Llaves foráneas de la entidad intermedia
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Campos de tiempo autollenados
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.text) < 15:
            return self.text
        else:
            # Devuelve primeros 11 caracteres del comentario
            return self.text[:11] + '...'

# Clase para guardar relación de anuncios favoritos
class Fav(models.Model):
    # Definición de llaves foráneas
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Definición de campos únicos
    class Meta:
        unique_together = ('ad', 'user')

    # Representación como cadena
    def __str__(self):
        return "%s likes %s"%(self.user.username, self.ad.title[:10])
