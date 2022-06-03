from django import forms
from ads.models import Ad
from django.core.files.uploadedfile import InMemoryUploadedFile
from ads.humanize import naturalsize

from django.core.exceptions import ValidationError
from django.core import validators

# Definición de clase para un formulario de anuncio
class CreateForm(forms.ModelForm):
    # Cálculo del tamaño límite de archivos
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Definición de campo para cargar archivo
    picture = forms.FileField(required=False, \
        label='File to Upload <= ' + max_upload_limit_text)
    upload_field_name = 'picture'

    # Clase de metadatos para crear el formulario
    class Meta:
        model = Ad
        fields = ['title', 'price', 'text', 'tags','picture']

    # Sobreescritura de método para validar y obtener datos del formulario
    def clean(self):
        # Llama método padre para obtener diccionario de dátos validados
        cleaned_data = super().clean()
        # Obtiene la imagen cargada
        pic = cleaned_data.get('picture')

        # Valida si se recibió una imagen
        if pic is None:
            return
        # Valida tamaño de la imagen
        if len(pic) > self.max_upload_limit:
            # Carga un mensaje de error a la pila
            self.add_error('picture',
                "File must be < " + self.max_upload_limit_text + " bytes")

    # Sobreescritura de método para guardar datos del formulario en BD
    def save(self, commit=True):
        # Crea nueva instancia del objeto recibido
        instance = super(CreateForm, self).save(commit=False)

        # Recupera imagen recibida
        f = instance.picture
        # Valida si la imagen se encuentra en memoria
        if isinstance(f, InMemoryUploadedFile):
            # Lee pixeles de la imagen
            bytearr = f.read()
            # Obtiene descripción del contenido
            instance.content_type = f.content_type
            # Escribre los pixeles de la imagen
            instance.picture = bytearr

        # Valida estado del commit
        if commit:
            instance.save()
            # Guarda los TAGS del formulario
            self.save_m2m()

        return instance

# Definición de clase para un comentario
class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3,
        strip=True)
