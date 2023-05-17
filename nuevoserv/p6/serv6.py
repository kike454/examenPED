import socket
import os
import sys
import time
import setproctitle
bufferSize = 4096

setproctitle.setproctitle("serv6")


server_address = "0.0.0.0"
port = 6548

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_address,port))
s.listen(5)  # backlog


while True:
    conn, addr = s.accept()
    print('Conexion existosa', addr)
    child_pid = os.fork()
    if child_pid == 0:
        nombre_fichero = conn.recv(1024).decode("utf-8").strip()
        try:
            fichero = open(nombre_fichero, "rb")
            while True:
                data = fichero.read(bufferSize)
                if not data:
                    time.sleep(1)
                        #fragmenta los datos y los envia de manera secuencial a un cliente conectado
                    conn.sendall(b"fin_de_fichero")
                    break
                conn.sendall(data)

        except FileNotFoundError:
            conn.sendall("Error al abrir el fichero\n".encode('utf-8'))



