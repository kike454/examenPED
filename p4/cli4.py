import socket
import os
import sys
import setproctitle


setproctitle.setproctitle("cli4")

def cliente(server_address, fichero):
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(server_address)

    try:
        mensaje = fichero
        resp1 = 'Dirección fichero: {!r}'.format(mensaje)
        encode1 = resp1.encode()
        #print('Dirección fichero: {!r}'.format(mensaje))
        os.write(2,encode1)
        s.sendall(mensaje.encode('utf8'))

        while True:
            data = s.recv(1024)
            if not data:
                break

            os.write(1, data)

    finally:
        resp2 = 'Cerrando socket ...'
        encode2 = resp2.encode()
        os.write(2,encode2)
        #print("Cerrando socket...")
        s.close()


if __name__ == "__main__":

    if len(sys.argv) == 2:
        address = "/tmp/ped1_group1"
        file = sys.argv[1]
    else:
        resp3 = "Introduzca la ruta del fichero: \n"
        encode3 = resp3.encode()
        os.write(2,encode3)
        #print("Introduzca la ruta del fichero: ")
        exit(1)

    cliente(address, file)
