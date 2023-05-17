import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 2223)
print('Estableciendo conexión con {} en el puerto {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(64)    
            
            if data:
                connection.sendall(data)
            else:
                break

    finally:
        connection.close()
            
