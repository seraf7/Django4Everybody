# Biblioteca para manejo de rutas
from django.urls import path
# Se importan las vistas
from . import views

# Se crea el nombre de la aplicación
app_name = 'polls'

# Se definen los patrones de URL
urlpatterns = [
	# Se define la URL de la aplicación polls
	# /polls/
	#path('', views.index, name='index'),

	path('', views.IndexView.as_view(), name='index'),

	# URL para solicitar detalles de una pregunta
	# /polls/5/
	#path('<int:question_id>/', views.detail, name='detail'),

	# Actualización para usar vistas genéricas
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),

	# URL para solicitar resultados de una pregunta
	# /polls/5/results/
	#path('<int:question_id>/results/', views.results, name='results'),

	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

	# URL para realizar votaciones
	# /polls/5/vote/
	path('<int:question_id>/vote/', views.vote, name='vote'),
	# URL de validación
	path('owner', views.owner, name='owner'),
]
