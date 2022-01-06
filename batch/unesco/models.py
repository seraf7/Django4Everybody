from django.db import models

# Clase para modelar una categoria
class Category(models.Model):
    name = models.CharField(max_length=128)

    # Método para devolver objeto como cadena
    def __str__(self):
        return self.name

# Clase para modelar los estados
class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Clase para modelar una región
class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Clase para modelar ISO
class Iso(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.code

# Clase para modelar los sitios
class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    justification = models.TextField(null=True)
    year = models.IntegerField(null=True)
    longitude = models.CharField(max_length=80)
    latitude = models.CharField(max_length=80)
    area_hectares = models.DecimalField(max_digits=15, decimal_places=5, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=False)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=False)
    iso = models.ForeignKey('Iso', on_delete=models.CASCADE, null=False)
