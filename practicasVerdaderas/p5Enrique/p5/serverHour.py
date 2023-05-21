import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('0.0.0.0', 1111)

print('Dirección {} con el puerto {} del servidor'.format(*server_address))
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(1024)


    if data:
        sent = sock.sendto(data, address)
        print('Sent {} bytes back to  {}'.format(sent, address))
