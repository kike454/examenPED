import socket
import sys
import errno

dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '8888'

mi_usuario = input('Usuario: ')

socket_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cli.connect((dir_serv, int(puerto_serv)))
socket_cli.setblocking(False)

usuario = mi_usuario.encode('utf-8')
socket_cli.send(usuario)

while True:
    mensaje = input(f'{mi_usuario} > ')

    if mensaje:
        mensaje = mensaje.encode('utf-8')
        socket_cli.send(mensaje)
    
    try:
        while True:
            recibido = socket_cli.recv(1024).decode('utf-8')
            if recibido == 'ERROR Ese usuario ya está en uso, prueba con otro nombre.':
                print(recibido)
                sys.exit()
            usuario, mensaje = recibido.split(' ', 1)

            print(f'{usuario} > {mensaje}')

    except IOError as e:
        if e.errno != errno.EAGAIN or e.errno != errno.EWOULDBLOCK:
            print('reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('GENERAL ERROR', str(e))
        sys.exit()

    
    
