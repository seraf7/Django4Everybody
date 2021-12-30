from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make

# Vista para listar autos, requiere login
class MainView(LoginRequiredMixin, View):
    # Método para solicitudes GET
    def get(self, request):
        # Cuenta los fabricantes
        mc = Make.objects.all().count()
        # Obtiene lista de autos
        al = Auto.objects.all()

        # Define el contexto
        ctx = {'make_count': mc, 'auto_list': al}

        # Devuelve la vista con la información
        return render(request, 'autos/auto_list.html', ctx)

# Vista para listar fabricantes
class MakeView(LoginRequiredMixin, View):
    # Método para solicitudes GET
    def get(self, request):
        # Obtiene los fabricantes
        ml = Make.objects.all()
        # Define el contexto
        ctx = {'make_list': ml, }

        # Devuelve la vista
        return render(request, 'autos/make_list.html', ctx)

# Vista para crear un auto, hereda de clase para crear registros
class AutoCreate(LoginRequiredMixin, CreateView):
    # Define modelo a usar
    model = Auto
    # Indica que se usan todos los campos en el formulario
    fields = '__all__'
    # Indica URL para creación exitosa
    success_url = reverse_lazy('autos:all')

# Vista para editar un auto, hereda de clase para actualización
class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# Vista para eliminar un auto, hereda de clase para eliminar registros
class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# Vista para crear un fabricante
class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# Vista para editar un fabricante
class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# Vista para eliminar un fabricante
class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

