import socket
import select


dir_serv = input('Dirección del servidor: ')
puerto_serv = input('Puerto del servidor: ')

if not dir_serv:
    dir_serv = '127.0.0.1'

if not puerto_serv:
    puerto_serv = '8888'

socket_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_serv.bind((dir_serv, int(puerto_serv)))
socket_serv.listen(1)

lista_sockets = [socket_serv]

clientes = {}
lista_usuarios= []

def recibir_mensaje(socket_cli):
    try:
        mensaje = socket_cli.recv(1024)
        if mensaje:
            return mensaje
        else:
            return False

    except:
        return False
    

while True:
    ready_list, _, _ = select.select(lista_sockets, [], [])

    for s in ready_list:
        usr_repetido = False
        if s == socket_serv:
            socket_cli, dir_cli = socket_serv.accept()

            usuario = recibir_mensaje(socket_cli)
            if usuario is False:
                continue
            
            if len(lista_usuarios) != 0:
                for usr in lista_usuarios:
                    if usr == usuario.decode():
                        print('usuario ya está en uso')
                        socket_cli.send('ERROR Ese usuario ya está en uso, prueba con otro nombre.'.encode('utf8'))
                        usr_repetido = True

            if not usr_repetido:
                lista_sockets.append(socket_cli)
                clientes[socket_cli] = usuario
                lista_usuarios.append(usuario.decode('utf-8'))
                usr = usuario.decode('utf-8')

                print(f'Nueva conexión aceptada desde: {dir_cli[0]}:{dir_cli[1]}, usuario: {usr}')

        else:

            mensaje = recibir_mensaje(s)

            if mensaje is False:
                usr = clientes[s].decode('utf-8')
                print(f'Conexión cerrada del usuario {usr}')
                lista_sockets.remove(s)
                lista_usuarios.remove(usr)
                del clientes[s]
                continue

            usuario = clientes[s]

            for socket_cli in clientes:
                if socket_cli != s:
                    try:
                        socket_cli.send(usuario + b' ' + mensaje) 

                    except ConnectionResetError:
                        print('Error: La conexión con el cliente se ha restablecido.')
                        lista_usuarios.remove(usuario)
