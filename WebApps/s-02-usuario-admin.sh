# @Autor:           Seraf
# @Fecha:           27/08/2021
# @Descripcion:     Creación de un usuario administrador

# Línea para crear super usuario
python3 manage.py createsuperuser

# Se ingresan los datos de loggin
# Username: admin
# Email address: sera@ejemplo.com
# Contraseña: seraf


# Se levanta el servidor
python3 manage.py runserver

# Para usar una IP y puero específicos
# python3 manage.py runserver 192.168.1.79:8000
