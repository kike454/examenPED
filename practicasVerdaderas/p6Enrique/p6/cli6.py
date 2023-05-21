import socket
import os
import sys
import setproctitle
bufferSize = 100

setproctitle.setproctitle("cli6")
server_address = "127.0.0.1"
port = 6548
file_name = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_address, port))
s.sendto(file_name.encode("utf-8"), (server_address, port))
try:
    while True:
        data = s.recv(bufferSize)
        if data == "fin_de_fichero":
            break

        os.write(1, data)
        #s.close()
finally:
    resp1 = '\nCerrando socket\n'
    encode1 = resp1.encode()
    os.write(2,encode1)
    s.close()

