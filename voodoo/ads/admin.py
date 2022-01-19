from django.contrib import admin
from ads.models import Ad, Comment

# Añade los modelos a la página de administración
admin.site.register(Ad)
admin.site.register(Comment)
