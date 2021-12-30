from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Breed, Cat

# Vista para listar gatos, requiere login
class MainView(LoginRequiredMixin, View):
    # Método para solicitudes GET
    def get(self, request):
        # Cuenta las razas
        bc = Breed.objects.all().count()
        # Obtiene la lista de gatos
        cl = Cat.objects.all()

        # Define el contexto
        ctx = {'breed_count': bc, 'cat_list': cl}

        # Devuelve la vista con la información
        return render(request, 'cats/cat_list.html', ctx)

# Vista para listar razas
class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        # Obtiene lar razas
        bl = Breed.objects.all()
        # Define el contexto
        ctx = {'breed_list': bl}

        # Devuelve la vista
        return render(request, 'cats/breed_list.html', ctx)

# Vista para crear un gato, hereda de clase para crear registros
class CatCreate(LoginRequiredMixin, CreateView):
    # Define el modelo a usar
    model = Cat
    # Se indican los campos para el formulario
    fields = '__all__'
    # Indica URL para creación exitosa
    success_url = reverse_lazy('cats:cat_list')

# Vista para editar un gato, hereda de clase de actualización
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

# Vista para eliminar un gato, hereda de clase de eliminación
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

# Vista para crear una raza
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

# Vista para editar una raza
class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')

# Vista para eliminar una raza
class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:cat_list')



