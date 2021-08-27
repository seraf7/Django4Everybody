# @Autor:           Seraf
# @Fecha:           26/08/2021
# @Descripcion:     Simulación de un servidor web simple

# Biblioteca de sockets
from socket import *

# Definición de la función que simular el servidor
def createServer():
    # Se define un nuevo socket de internet
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Bloque para intentar conexiones
    try:
        # Se liga el socket a un puerto y una dirección IP
        serverSocket.bind(('localhost', 9000))
        # Se indica el máximo de conexiones que se pueden encolar
        serverSocket.listen(5)

        # Ciclo infinito para esperar conexiones
        while(1):
            # Se acepta una nueva conexión
            (clientSocket, address) = serverSocket.accept()

            # Se recibe la petición del cliente y se decodifica en UNICODE
            rd = clientSocket.recv(5000).decode()
            # Se separa el mensaje recibido
            pieces = rd.split("\n")
            # Se valida que se haya recibido un mensaje
            if (len(pieces) > 0) : print(pieces[0])

            # Se construye la respuesta a enviar
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>¡¡Hola Mundo!!</body></html>\r\n\r\n"
            # Se envia la respuesta codificada
            clientSocket.sendall(data.encode())
            # Se cierra la conexión con el cliente
            clientSocket.shutdown(SHUT_WR)

    # Manejo de excepción por interrupción con teclado
    except KeyboardInterrupt:
        print("\nCerrando servicio...\n")
    # Excepción general
    except Exception as exc:
        print("Error: \n")
        print(exc)

    # Se cierra el socket
    serverSocket.close()

# Se invoca al servidor
print("Access http://localhost:9000")
createServer()
