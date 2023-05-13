import socket
import os
import sys
import time
bufferSize = 4096

def esPalindromo(cadena):
    cadena = cadena.decode("utf-8")
    if cadena == ''.join(reversed(cadena)):
        return True
    else:
        return False

def server(server_address, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_address, server_port))
    #numero maximo de conexiones en espera que se pueden encolar
    s.listen(2)  # backlog

    print("Escuchando ...")

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        child_pid = os.fork()
        if child_pid == 0:
            nombre_fichero = conn.recv(1024).decode("utf-8").strip()
            try:
                fichero = open(nombre_fichero, "rb")
                while True:
                    data = fichero.read(bufferSize)
                    print(data)
                    #palindromo
                    print("ijnefij")
                    palabras = data.split()
                    print(palabras)
                    print("hola")
                    soloPalindromos = []
                    print("fro")
                    for e in palabras:
                        print(e)
                        if esPalindromo(e):
                            soloPalindromos.append(e)
                    print(soloPalindromos)
                    if not data:
                        time.sleep(1)
                        #fragmenta los datos y los envia de manera secuencial a un cliente conectado
                        conn.sendall("fin_de_fichero")
                        break
                    print("onwefio")
                    for p in soloPalindromos:
                        conn.sendall(p+ b'\n')
                    #conn.sendall(data)
                    #palindromo()
            except FileNotFoundError:
                conn.sendall("Error al abrir el fichero\n".encode('utf-8'))

            finally:
                conn.close()
                break

if __name__ == "__main__":

    if len(sys.argv) == 1:
        address = "0.0.0.0"
        port = 6553
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    server(address, port)
