import socket
import sys
import os
import setproctitle

setproctitle.setproctitle("cli5")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 10000)

try:

    #Enviar la data
    #rutafichero = "/etc/services"
    rutafichero = sys.argv[1]
    resp1= 'Enviando {!r}'.format(rutafichero)
    os.write(2,b'resp1')
    #print('Enviando {!r}'.format(rutafichero))
    sent = sock.sendto(rutafichero.encode('utf8'), server_address)
    resp2 = 'Sent {} bytes'.format(sent)
    os.write(2,b'resp2')
    #print('Sent {} bytes'.format(sent))
    
    # respuesta
    resp3 = 'Esperando para recibir'
    os.write(2,b'resp3')
    #print('Esperando para recibir')
    data = b''
    max_size = 1024
    #reensamblado
    while True:
        fragment, server = sock.recvfrom(max_size)

       # print("trocito $$$$$$$$$$$$$",len(fragment))

        if fragment==b'fin_del_fichero':
            #print("if ")
            break
        data += fragment
        #print("data",data.decode('utf-8'))
    #print('El fichero contiene: \n {}'.format(data2))

finally:
    #decodeData = data.decode('utf-8')
    os.write(1,data)
    #print(decodeData)
    resp4 = 'Cerrando socket'
    os.write(2,b'resp4')
    #print('Cerrando socket')
    sock.close()
