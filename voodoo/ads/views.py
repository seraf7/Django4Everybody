from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.uploadedfile import InMemoryUploadedFile

from ads.models import Ad
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from ads.forms import CreateForm

# Vista para listar los anuncios
class AdListView(OwnerListView):
    # Define el modelo a renderizar
    model = Ad

# Vista de detalles del anuncio
class AdDetailView(OwnerDetailView):
    model = Ad

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

        return redirect(self.success_url)

class AdDeleteView(OwnerDeleteView):
    model = Ad
