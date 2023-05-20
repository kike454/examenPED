import socket
import sys
from datetime import datetime
import  os
import time

now = datetime.now()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dirServer = input("Introduce la direccion del servidor: ")
server_address = (dirServer, 2224)
sock.connect(server_address)

queQuiereElCLiente = input("Si desea obtener la hora, introduzca 'hora', si desea obtener la fecha, introduzca 'fecha': ")

try:

    if queQuiereElCLiente.lower()== "hora":

        solicitudHora = "HORA".encode('utf8')
        sock.sendall(solicitudHora)
        #time.sleep(1)
    elif queQuiereElCLiente.lower()=="fecha":

        solicitudFecha = "FECHA".encode('utf8')
        sock.sendall(solicitudFecha)
        #time.sleep(1)
    elif queQuiereElCLiente != "fecha" or "hora":
        solicitudErronea = "ERROR".encode('utf8')
        sock.sendall(solicitudErronea)
    
    data = sock.recv(1024)
       
    os.write(1,data)
   

finally:
    print('\nCerrando socket...')
    sock.close()
