import socket
import sys
from datetime import datetime
import os

now = datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('0.0.0.0', 1111)

message = now.strftime("%Y %m %d,  %H:%M:%S")

try:

    sent = sock.sendto(message.encode('utf8'), server_address)

    data, server = sock.recvfrom(4096)
    os.write(1,data)

finally:
    print('\nCerrando socket')
    sock.close()
