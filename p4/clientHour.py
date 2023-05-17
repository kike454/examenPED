import socket
import sys
import os
from datetime import datetime
now = datetime.now()

#Crear el UDS socket del cliente
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = sys.argv[1]
print('Conectándo a {}'.format(server_address))
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

try:
    #Enviar los datos
    mensaje = now.strftime('%Y %m %d, %H:%M:%S')
    #print('Enviando {!r}'.format(mensaje))
    sock.sendall(mensaje.encode('utf8'))

    data = sock.recv(1024)
    os.write(1,data)
    #print('Received {!r}'.format(data))

finally:
    print('\nCerrando socket')
    sock.close()
