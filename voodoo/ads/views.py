from ads.models import Ad
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

# Vista para listar los anuncios
class AdListView(OwnerListView):
    # Define el modelo a renderizar
    model = Ad

# Vista de detalles del anuncio
class AdDetailView(OwnerDetailView):
    model = Ad

# Vista de creación de un anuncio
class AdCreateView(OwnerCreateView):
    model = Ad
    # Definición de campos del formulario
    fields = ['title', 'price', 'text']

# Vista para la edición de un anuncio
class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdDeleteView(OwnerDeleteView):
    model = Ad
