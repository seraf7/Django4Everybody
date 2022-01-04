from django.urls import path, reverse_lazy
from . import views

# Definición del nombre de la aplicación
app_name = 'ads'

# Definición de las urls
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('ad/<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    # Se define el redireccionamiento sobre la url
    path('ad/create/',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')),
        name='ad_create'),
    path('ad/<int:pk>/update/',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')),
        name='ad_update'),
    path('ad/<int:pk>/delete/',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')),
        name='ad_delete'),
]
