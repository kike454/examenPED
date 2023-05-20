import socket
import sys
from datetime import datetime
import  os
import time

now = datetime.now()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dirServer = input("Introduce la direccion del servidor: ")
server_address = (dirServer, 2225)
sock.connect(server_address)

queQuiereElCLiente = input("introduzca el numero que desea traducir: ")

try:
    
        
    solicitudEnBytes=queQuiereElCLiente.encode("utf8")
        
    sock.sendall(solicitudEnBytes)
    
    data = sock.recv(1024)
       
    os.write(1,data)
   

finally:
    time.sleep(1)
    print('\nCerrando socket...')
    sock.close()
