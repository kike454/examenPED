import socket
import sys, os

server_address = sys.argv[1]

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print('Servidor empezando en {}'.format(server_address))
sock.bind(server_address)

sock.listen(2)

while True:
    
    connection, client_address = sock.accept()
    direct = str(client_address)
    try:
        print('Conexión desde: {}'.format(direct))

        while True:
            data = connection.recv(1024)
            #print('Recibido {!r}'.format(data))
            if data:
                connection.sendall(data)
            else:
                break

    finally:
        connection.close()
