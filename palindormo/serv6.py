import socket
import os
import sys
import time
import struct
bufferSize = 4096

TotalNumeroVocales=0

def esPalindromo(cadena):
    cadena = cadena.decode("utf-8")
    #print("cadena", cadena )
    if cadena == ''.join(reversed(cadena)):
        return True
    else:
        return False
def esVocal(cadena):
    contador=0
    total =0
    vocales = "aeiouAEIOU"
    cadena = cadena.decode("utf-8")
    #print("cadenavoc",cadena)
    #if cadena in "aeiouAEIOU":
    for vocal in cadena:
        
        if vocal in vocales:
            print("cadena", cadena, "vocal",vocal)
            #print("cadena vocal")
            contador += 1
     #   total += contador
    print(contador)
    #print(total)
    return contador
        

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
                 #   print("read\n",data)
                    #palindromo
                    palabras = data.split()
                    print(palabras)
#                    print("hola")
                    soloPalindromos = []
#                    print("fro")
                    for e in palabras:
                  #      print(e)
                    #    #contador += cadena.count(caracter)
                        if esPalindromo(e):
                            #print("espalin")
                            soloPalindromos.append(e)
                   # print("array",soloPalindromos)
                    for p in soloPalindromos:
                    #    print("envio cliente", p)
                        conn.sendall(p + b'\n')
                    #VOCALES
                    #conn.sendall(b'envio_vocales')
                    j =0
                    for letter in palabras:
                        #print("letter", letter)
                        #numeroVocales = esVocal(letter)
                        #j =0
                        print(TotalNumeroVocales)
                        vocalTotal=esVocal(letter)
                        j += vocalTotal
                        print("total vocales leidas",j)
                    #print("envio vocales")
                    #weo = bytes(j)
                    weo = bytearray(struct.pack('f',j))
                    conn.sendall(weo + b'\n')
                    print("postenvio")
                    if not data:
                        time.sleep(1)
                        #fragmenta los datos y los envia de manera secuencial a un cliente conectado
                        conn.sendall(b"fin_de_fichero")
                        break
                    #print("onwefio")
                    #for p in soloPalindromos:
                     #   print("envio cliente", p)
                      #  conn.sendall(p + b'\n')
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
        port = 5119
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    server(address, port)
