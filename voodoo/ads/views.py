from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q

from django.core.files.uploadedfile import InMemoryUploadedFile

from ads.models import Ad, Comment, Fav
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from ads.forms import CreateForm, CommentForm

# Vista para listar los anuncios
class AdListView(OwnerListView):
    # Define el modelo a renderizar
    model = Ad
    template_name = 'ads/ad_list.html'

    # Sobreescritura para solicitudes GET
    def get(self, request):
        favorites = []

        # Recupera valores recibidos en solicitud GET
        strval = request.GET.get("search", False)

        # Valida si hay un valor de busqueda
        if strval:
            # Crea filtros con valor de busqueda
            query = Q(title__icontains=strval)
            query.add(Q(text__icontains=strval), Q.OR)
            query.add(Q(tags__name__in=[strval]), Q.OR)
            # Recupera lista de anuncios filtrada
            ad_list = Ad.objects.filter(query)
        else:
            # Obtiene todos los anuncios
            ad_list = Ad.objects.all()

        # Valida si el usuario ha iniciado sesión
        if request.user.is_authenticated:
            # Recupera el diccionario los ID de anuncios favoritos
            rows = request.user.favorite_ads.values('id')
            # Crea una lista de los ID recuperados
            favorites = [row['id'] for row in rows]

        # Crea el contexto
        ctx = {'ad_list': ad_list, 'favorites': favorites}
        return render(request, self.template_name, ctx)

# Vista de detalles del anuncio
class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'

    # Sobreescritura del método get
    def get(self, request, pk):
        # Obtiene el anuncio solicitado
        ad = Ad.objects.get(id=pk)
        # Obtiene los comentarios del anuncio, ordenados por el mas reciente
        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        # Crea objeto de formulario de comentarios
        comment_form = CommentForm()
        # Creación del contexto
        ctx = {'ad': ad, 'comments': comments, 'comment_form': comment_form}
        # Devuelve respuesta a renderizar
        return render(request, self.template_name, ctx)

# Vista de creación de un anuncio, requiere inicio de sesión
class AdCreateView(LoginRequiredMixin, View):
    # Definición de la plantilla
    template_name = 'ads/ad_form.html'
    # URL de éxito
    success_url = reverse_lazy('pics:all')

    # Sobreescritura para resolver peticiones GET
    def get(self, request, pk=None):
        # Establece objeto del formulario
        form = CreateForm()
        ctx = {'form': form}
        # Devuelve vista a renderizar
        return render(request, self.template_name, ctx)

    # Sobreescritura para resolver peticiones POST
    def post(self, request, pk=None):
        # Crea instancia del formulario recibido y archivos
        form = CreateForm(request.POST, request.FILES or None)

        # Verifica si los datos del formulario no son válidos
        if not form.is_valid():
            ctx = {'form', form}
            # Devuelve vista con los errores encontrados
            return render(request, self.template_name, ctx)

        # Crea un nuevo objeto del anuncio
        ad = form.save(commit=False)
        # Establece valor del campo del dueño con el usuario en sesión
        ad.owner = self.request.user
        # Guarda objeto en la BD
        ad.save()
        # Guarda la relación de TAGS del anuncio
        form.save_m2m()

        # Redirije a la URL de éxito
        return redirect(self.success_url)

# Vista para la edición de un anuncio, requiere inicio de sesión
class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('pics:all')

    def get(self, request, pk):
        # Recupera registro de la BD con ID y dueño solicitados
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        # Crea formulario con datos del registro
        form = CreateForm(instance=ad)
        ctx = {'form': form}
        # Devuelve vista formulario con información
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        # Valida si los cambios en el formulario no son válidos
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Actualiza cambios en la BD
        ad = form.save(commit=False)
        ad.save()

        # Guarda relación de TAGS del anuncio
        form.save_m2m()

        return redirect(self.success_url)

class AdDeleteView(OwnerDeleteView):
    model = Ad

# Método para envío de imagenes
def stream_file(request, pk):
    # Obtiene objeto con ID indicado
    ad = get_object_or_404(Ad, id=pk)
    # Construcción de respuesta HTTP
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    # Escribe imagen en la respuesta
    response.write(ad.picture)
    # Envía la respuesta generada
    return response

# Vista para la creación de un comentario, requiere inicio de sesión
class CommentCreateView(LoginRequiredMixin, View):
    # Sobreescritura del método POST
    def post(self, request, pk):
        # Obtiene el anuncio con id recibido
        ad = get_object_or_404(Ad, id=pk)
        # Crea objeto con datos del formulario recibido
        comment = Comment(text=request.POST['comment'],
            owner=request.user, ad=ad)
        # Guarda en la BD
        comment.save()
        # Redirecciona a la página de detalles del anuncio
        return redirect(reverse('ads:ad_detail', args=[pk]))

# Vista para borrar un comentario del autor en sesión
class CommentDeleteView(OwnerDeleteView):
    model = Comment

    # Sobreescritura del método para ir a URL de éxito
    def get_success_url(self):
        # Obtiene el anuncio actual
        ad = self.object.ad
        # Redirecciona al anuncio del ID indicado
        return reverse('ads:ad_detail', args=[ad.id])

# Vista para añadir favoritos, se ignora el token csrf y se gestionan
# las solicitudes recibidas por su tipo
@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    # Método para atender solicitud POST
    def post(self, request, pk):
        # Obtiene el anuncio indicado
        ad = get_object_or_404(Ad, id=pk)
        # Crear registro en tabla de favoritos
        fav = Fav(user=request.user, ad=ad)

        try:
            # Intenta guardar el registro
            fav.save()
        except IntegrityError as e:
            # No guarda en caso de duplicidad
            pass

        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        try:
            # Intenta borrar registro de tabla de favoritos
            fav = Fav.objects.get(user=request.user, ad=ad).delete()
        except Fav.DoesNotExist as e:
            # El registro no existia en la tabla
            pass

        return HttpResponse()
