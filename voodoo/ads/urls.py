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
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')),
        name='ad_update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')),
        name='ad_delete'),
    # URL para la entrega de imagenes
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    # URL para comentarios
    path('ad/<int:pk>/comment', views.CommentCreateView.as_view(),
        name='ad_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('ads')),
        name='ad_comment_delete'),
    # URL para añadir favoritos
    path('ad/<int:pk>/favorite', views.AddFavoriteView.as_view(),
        name='ad_favorite'),
    path('ad/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(),
        name='ad_unfavorite'),
]
