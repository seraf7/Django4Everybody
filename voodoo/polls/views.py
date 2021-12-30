# Biblioteca para respuestas de HTTP
from django.http import HttpResponse, HttpResponseRedirect
# Biblioteca para plantillas de renderizado
from django.template import loader
# Biblioteca para renderizado con atajos
from django.shortcuts import render, get_object_or_404
# Bibliotecas para error 404
from django.http import Http404
# Biblioteca para reconstruir URL
from django.urls import reverse
# Biblioteca para manejo de SQL
from django.db.models import F
# Biblioteca para usar vistas genéricas
from django.views import generic

# Se importa el modelo de preguntas
from .models import Question, Choice

# Clase con herencia para usar vistas genéricas de Django
class IndexView(generic.ListView):
    # Indica la plantilla a renderizar
    template_name = 'polls/index.html'
    # Se indica el objeto de contexto usado en la plantilla
    context_object_name = 'lista_preguntas'

    def get_queryset(self):
        # Recupera las 5 últimas preguntas publicadas
        return Question.objects.order_by('-pub_date')[:5]

# Uso de vista de detalles genérica de Django
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""
Definición antigua de las vistas, es codigo repetitivo

# Definición de una respuesta
def index(Request):
	#return HttpResponse("Hello, world. 201d7a97 is the polls index.")

	# Se obtienen las cinco preguntas más recientes
	lista_preguntas = Question.objects.order_by('-pub_date')[:5]
	# Se crea una cadena con los elementos de la lista unidos por coma
	#respuesta = ', '.join([q.question_text for q in lista_preguntas])
	#return HttpResponse(respuesta)

	# Se obtiene la plantilla de despliegue
	template = loader.get_template('polls/index.html')
	# Se crea un nuevo contexto, diccionario de los objetos a cargar
	context = {'lista_preguntas': lista_preguntas,}
	# Se devuelve la respuesta con formato
	return HttpResponse(template.render(context, Request))

# Vista con los detalles de una pregunta
def detail(Request, question_id):
    try:
        # Obtiene la pregunta con el ID del URL
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # Se levanta una excepción por pregunta no encontrada
        raise Http404("La pregunta no existe")
    # Se envía la respuesta HTTP con formato
    return render(Request, 'polls/detail.html', {'question': question})

# Vista con los resultados de una pregunta
def results(Request, question_id):
    # Obtiene la pregunta en caso de existir
    question = get_object_or_404(Question, pk=question_id)
    # Muestra una plantilla con los resultados de la pregunta
    return render(Request, 'polls/results.html',
    {'question': question})
"""

# Vista para realizar votaciones
def vote(Request, question_id):
    # Se obtiene el objeto en caso de existir
    question = get_object_or_404(Question, pk=question_id)

    try:
        # Obtiene el valor de la opción seleccionada
        selected_choice = question.choice_set.get(pk=Request.POST['choice'])
    # Maneja error cuando no se ha seleccionado nada
    except (KeyError, Choice.DoesNotExist):
        # Se muestra el formulario de votación con un mensaje de error
        return render(Request, 'polls/detail.html', {
            'question': question,
            'error_message': "No seleccionaste una opción",})
    # Acción cuando se seleccionó una opción
    else:
        #selected_choice.votes += 1
        # Actualizacion con una consulta encapsulada, se evitan las condiciones de carrera
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        # Se redirecciona a la pagina de resultados de la pregunta
        # para evitar acciones duplicadas
        return HttpResponseRedirect(reverse('polls:results',
        args=(question.id, )))

# Vista de validación
def owner(request):
       return HttpResponse("Hello, world. a8757ce9 is the polls index.")