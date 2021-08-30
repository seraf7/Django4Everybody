# @Autor:           Seraf
# @Fecha:           27/08/2021
# @Descripcion:     Definición de la primer vista de la aplicación

from django.http import HttpResponse

# Se definine el sitio raíz
def index(request):
    return HttpResponse("¡¡Hola Mundo!! Llegaste al index de la aplicación")
