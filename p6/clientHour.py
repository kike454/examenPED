import socket
import sys
from datetime import datetime
import  os
now = datetime.now()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 2223)
sock.connect(server_address)

try:

    mensaje = now.strftime('%Y %m %d, %H:%M:%S').encode('utf8')
    sock.sendall(mensaje)

    #amount_received = 0
    #amount_expected = len(mensaje)

    #while amount_received < amount_expected:
    data = sock.recv(1024)
        #data2 = data.decode('utf8')
        #amount_received += len(data)
        #print('Recibido {!r}'.format(data2))
    os.write(1,data)

finally:
    print('\nCerrando socket...')
    sock.close()

