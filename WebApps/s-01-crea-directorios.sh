# @Autor:           Seraf
# @Fecha:           27/08/2021
# @Descripcion:     Script para la inicialización de directorios y archivos
#                   de la primer aplicación con Django

# Se crea el directorio raíz de la aplicación y scripts base
django-admin startproject sitioPeque

# Ingresa al directorio del proyecto
cd sitioPeque

# Se crea la estructura base de una aplicación
python3 manage.py startapp polls

# Se agregan las tablas de base de datos necesarias, de acuerdo a las
# aplicaciones agregadas en INSTALLED_APPS dentro de settings.py
python3 manage.py migrate

# Se agrega la nueva aplicación al esquema de la BD
python3 manage.py makemigrations polls

# Se consulta el código SQL que se encarga de generar los objetos en la BD
python3 manage.py sqlmigrate polls 0001

# Se comprueba si hay errores en el proyecto
python3 manage.py check

# Se aplican los nuevos cambios en la BD
python3 manage.py migrate

# Se levanta el servidor
python3 manage.py runserver

# Para usar una IP y puero específicos
# python3 manage.py runserver 192.168.1.79:8000
