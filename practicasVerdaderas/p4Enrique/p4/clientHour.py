import socket
import sys
import os
from datetime import datetime
now = datetime.now()

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = sys.argv[1]
print('Conectándose a {}'.format(server_address))
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)

try:
    mensaje = now.strftime('%Y %m %d, %H:%M:%S')
    sock.sendall(mensaje.encode('utf8'))

    data = sock.recv(1024)
    os.write(1,data)

finally:
    print('\nCerrando socket')
    sock.close()
