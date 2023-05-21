import socket
import sys
import setproctitle

setproctitle.setproctitle("serv5")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 1030)

print('Empezando en la dirección {} con el puerto {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\Esperando a recibir mensajes')

    data, address = sock.recvfrom(1024)
    clientFile = open(data, 'rb')
    contentFile = clientFile.read()
    #decodeData = contentFile.decode('utf-8')

    print('Recibidos {} bytes desde {} y cuyo tamaño es {}'.format(len(data), address,len(contentFile)))
    #print(decodeData)

    #FRAGMENTACION
    max_size=1024
    size = len(contentFile)
    for i in range(0,len(contentFile), max_size):

        fragment = contentFile[i:i+max_size]
        
        sent = sock.sendto(fragment, address)
        size -= max_size
        if size < 0:

          #  print("size")
            sent = sock.sendto(b'fin_del_fichero', address)

        #print("size", size)
        print('Enviando {} bytes al cliente cuya direccion es  {}'.format(sent, address))

