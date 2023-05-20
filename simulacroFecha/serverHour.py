import socket
import sys
from FechaHora import FechaHora

p1 = FechaHora()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 2224)
print('Estableciendo conexión con {} en el puerto {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(1024)    
            #print(data)
            decodeData = data.decode("utf8")
            #print(decodeData)

            if decodeData == "HORA":

                mensaje=p1.obtenerHora()
                #print("mensajeHOra",mensaje)
                
                #print("mensajeEncode", mensaje.encode("utf8"))
                connection.sendall(mensaje.encode("utf8") + b'\n')

            elif decodeData == "FECHA":
                mensaje1 = p1.obtenerFecha()
                #print("fechain")
                connection.sendall(mensaje1.encode("utf8"))
            elif decodeData=="ERROR":
                mensaje2 = "ERROR"
                connection.sendall(mensaje2.encode("utf8"))

            else:
                
                break

    finally:
        connection.close()