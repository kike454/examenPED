import socket
import os
import sys
import setproctitle


setproctitle.setproctitle("cli4")
fichero = sys.argv[1]

if len(sys.argv) == 2:
    address = "/tmp/ped1_group1"
    file = sys.argv[1]
else:
    resp3 = "Introduzca la ruta del fichero: \n"
    encode3 = resp3.encode()
    os.write(2,encode3)
    exit(1)

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(address)

try:
    mensaje = fichero
    resp1 = 'Dirección fichero: {!r}'.format(mensaje)
    encode1 = resp1.encode()
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
    s.close()


