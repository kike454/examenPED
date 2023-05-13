import socket
import sys
import os
import setproctitle

setproctitle.setproctitle("cli5")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 1030)

try:

    #Enviar la data
    #rutafichero = "/etc/services"
    rutafichero = sys.argv[1]
    resp1= "Enviando {!r}".format(rutafichero) + "\n"
    encode1 = resp1.encode()
    os.write(2,encode1)
    #print('Enviando {!r}'.format(rutafichero))
    sent = sock.sendto(rutafichero.encode('utf8'), server_address)
    resp2 = 'Sent {} bytes'.format(sent) + "\n"
    encode2 = resp2.encode()
    os.write(2,encode2)
    #print('Sent {} bytes'.format(sent))
    
    # respuesta
    resp3 = 'Esperando para recibir \n'
    encode3 = resp3.encode()
    os.write(2,encode3)
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
    resp4 = 'Cerrando socket \n'
    encode4 = resp4.encode()
    os.write(2,encode4)
    #print('Cerrando socket')
    sock.close()
