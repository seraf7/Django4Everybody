# Biblioteca para crear respuestas HTTP
from django.http import HttpResponse

# Función para el manejo de cookies de sesión
def helloView(request):
    # Se obtiene el numero de visitas de la sesión actual
    # si no existe se establece en 1
    num_visitas = request.session.get('num_visits', 0) + 1
    # Se define la cookie de sesion con el valor obtenido
    request.session['num_visits'] = num_visitas

    # Valida la cantidad de visitas
    if num_visitas > 4:
        # Borra los datos de la sesión
        del(request.session['num_visits'])

    # Cadena de respuesta a visualizar
    mensaje = "<p>"
    mensaje += "view count=" + str(num_visitas)
    mensaje += "</p> <p>"
    mensaje += "Para validar: a8757ce9"
    mensaje += "</p>"

    # Define la nueva respuesta a visualizar
    resp = HttpResponse(mensaje)

    # Se define una nueva cookie con vida de 1000s
    resp.set_cookie('dj4e_cookie', 'a8757ce9', max_age = 1000)

    return resp