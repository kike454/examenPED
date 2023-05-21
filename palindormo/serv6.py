import socket
import os
import sys
import time
import struct
from Kata import Kata
p1 = Kata()
bufferSize = 4096


"""
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
"""     

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
                    #palindromo
                    decodeData = data.decode("utf-8")
                    palabras = decodeData.split()
                    #print(palabras)
                   
                    soloPalindromos = []
                    #identificar palindromos
                   
                    for e in palabras:
                    
                        if p1.esPalindromo(e):
                            
                            soloPalindromos.append(e)
                   
                    #soloPalindromosEncode = soloPalindromos.encode("utf8")
                   
                   # print("array",soloPalindromos)
                   #envio palindromos
                    conn.sendall("los palindromos que contiene el acrhivo son: ".encode("utf8") + b'\n')
                    for p in soloPalindromos:
                    #    print("envio cliente", p)
                        conn.sendall(p.encode("utf8") + b'\n')
                    
                    #VOCALES
                    #
                    
                    totalVocales =0
                    for letter in palabras:
                        #print("letter", letter)
                        #numeroVocales = esVocal(letter)
                        #j =0
                        #print(TotalNumeroVocales)
                        vocalTotalCadena= p1.esVocal(letter)
                        totalVocales += vocalTotalCadena
                        #print("total vocales leidas",j)
                    
                    conn.sendall("las vocales que contiene el archivo son: ".encode("utf8") + b'\n') 
                    weo = str(totalVocales).encode("utf8")

                    conn.sendall(weo + b'\n')
                    #print("postenvio")
                    #numeros romanos
                    
                    if not data:
                        time.sleep(1)
                        #fragmenta los datos y los envia de manera secuencial a un cliente conectado
                        conn.sendall("fin_de_fichero".encode("utf8"))
                        break
                    
            except FileNotFoundError:
                conn.sendall("Error al abrir el fichero\n".encode('utf-8'))

            finally:
                conn.close()
                break

if __name__ == "__main__":

    if len(sys.argv) == 1:
        address = "0.0.0.0"
        port = 5113
    elif len(sys.argv) == 3:
        address = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Error en los argumentos")
        exit(1)

    server(address, port)
