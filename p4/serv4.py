import socket
from time import sleep
import os
import sys
import setproctitle

setproctitle.setproctitle("serv4")

def servidor(server_address):
    while True:

        try:
            os.unlink(server_address)
        except OSError:
            if os.path.exists(server_address):
                raise

        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(server_address)
        s.listen()
        print("Escuchando")
        conn, addr = s.accept()
        print('Connected by {}'.format(addr))

        nombre_fichero = conn.recv(1024).decode("utf-8").strip()

        try:
            fichero = open(nombre_fichero, "rb")
            texto = fichero.read()
            conn.sendall(texto)

        except FileNotFoundError:
            conn.sendall("Error al abrir el fichero\n".encode('utf-8'))

        conn.close()
        s.close()


if __name__ == "__main__":

    if len(sys.argv) == 1:
        address = "/tmp/ped1_group1"
    else:
        print("Introduza la ruta del fichero:" )
        exit(1)
    servidor(address)
