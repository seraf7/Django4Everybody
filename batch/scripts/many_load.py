from unesco.models import Site, Category, Iso, Region, State
import csv

# Función principal de ejecución
def run():
    # Abre el archivo
    f = open('unesco/whc-sites-2018-clean.csv')
    # Crea objeto lector
    reader = csv.reader(f)
    # Salta fila de encabezados
    next(reader)

    # Limpieza de las tablas
    Site.objects.all().delete()
    Category.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()

    # Formato
    # name, description, justification, year, longitude,
    # latitude, area_hectares, category, state, region,
    # iso

    # Ciclo para recorrer el archivo
    for row in reader:
        print(row)

        # Recpera registro de la BD y crea objetos independientes en
        # caso de no existir
        c, creado = Category.objects.get_or_create(name=row[7])
        i, creado = Iso.objects.get_or_create(code=row[10])
        r, creado = Region.objects.get_or_create(name=row[9])
        st, creado = State.objects.get_or_create(name=row[8])

        # Validación de valores nulos
        try:
            y = int(row[3])
        except:
            y = None

        try:
            a = float(row[6])
        except:
            a = None

        # Creación del sitio con sus dependencias
        site = Site(name=row[0], description=row[1], justification=row[2], \
            year=y, longitude=row[4], latitude=row[5], area_hectares=a, \
            category=c, state=st, region=r, iso=i)

        # Guarda el registro
        site.save()
