import socket
import os
import sys
import setproctitle
bufferSize = 100

setproctitle.setproctitle("cli6")

def client(server_address, server_port, file_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_address, server_port))
    s.sendto(file_name.encode("utf-8"), (server_address, port))
    try:
        while True:
            data = s.recv(bufferSize)
            if data == "fin_de_fichero":
                break
            os.write(1, data)
    finally:
        resp1 = 'Cerrando socket'
        os.write(2,b'resp1')
        s.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        address = "127.0.0.1"
        port = 6544
        file = sys.argv[1]
    elif len(sys.argv) == 4:
        address = sys.argv[1]
        port = int(sys.argv[2])
        file = sys.argv[3]
    else:
        print("Error en los argumentos")
        exit(1)

    client(address, port, file)
