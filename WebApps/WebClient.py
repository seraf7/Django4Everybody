# @Autor:           Seraf
# @Fecha:           26/08/2021
# @Descripcion:     Simulación de un navegador web simple

# Librería para manejo de URL
import urllib.request

# Se realiza una petición con la URL
fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')

# Se lee la respuesta obtenida
for l in fhand:
    print(l.decode().strip())
