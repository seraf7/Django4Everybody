# @Autor:           Seraf
# @Fecha:           26/08/2021
# @Descripcion:     Simulación de un navegador web simple

# Biblioteca de sockets
import socket

# Declaración de un socket de internet
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se establece la conexión a una URL por el puerto 80
mysocket.connect(('data.pr4e.org', 80))

# Se define una peticicion en UTF-8 con operación GET
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# Se envía la petición al servidor
mysocket.send(cmd)

# Impresión de los datos en bloques de 512 bytes
while True:
    # Se almacena el flujo de datos recibidos
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Se cierra la conexión
mysocket.close()
