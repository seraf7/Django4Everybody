from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Clase para devolver el listado de objetos
class OwnerListView(ListView):
    """
    Clase que hereda de ListView, envía solicitud al formulario
    """

# Clase para obtener los detalles del objeto
class OwnerDetailView(DetailView):
    """
    Clase que hereda de DetailView, evía solicitud al formulario
    """

# Clase para crear un nuevo objeto
class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    Clase que hereda de CreateView, envía la solicitud al formulario y añde
    el autor al objeto guardado
    """
    # Sobreescritura del método de validación del formulario
    def form_valid(self, form):
        print("Llamada a form_valid")
        # Crea objeto pero no lo guarda en la BD
        object = form.save(commit=False)
        # Establece el autor con el usuario en la sesión actual
        object.owner = self.request.user
        # Guarda el registro en la BD
        object.save()
        # Invoca al método del padre para validar el formulario
        return super(OwnerCreateView, self).form_valid(form)

# Clase para modificar un objeto
class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Clase que hereda de UpdateView, envía solicitud al formulario y filtra
    anuncios con el usuario de la solicitud
    """

    # Sobreescritura del método para obtener los registros
    def get_queryset(self):
        print('Llamada a  Update.get_queryset')
        # Obtiene todos los registros con el método del padre
        qs = super(OwnerUpdateView, self).get_queryset()
        # Devuelve resultados filtrdos con el usuario
        return qs.filter(owner=self.request.user)

# Clase para borrar un objeto
class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Clase que hereda de DeleteView, restringe a los usuarios para borrar los
    objetos que no son propios
    """

    # Sobreescritura del método para obtener los registros
    def get_queryset(self):
        print('Llamada a  Update.get_queryset')
        # Obtiene todos los registros con el método del padre
        qs = super(OwnerDeleteView, self).get_queryset()
        # Devuelve resultados filtrdos con el usuario
        return qs.filter(owner=self.request.user)

# References
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid

# https://stackoverflow.com/questions/862522/django-populate-user-id-when-saving-a-model

# https://stackoverflow.com/a/15540149

# https://stackoverflow.com/questions/5531258/example-of-django-class-based-deleteview
