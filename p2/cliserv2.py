import os
import sys
import setproctitle
if len(sys.argv) != 2:
    print("Introduzca la ruta del fichero del cual desea leer su contenido: " )
    exit(1)

#def setproctitle(title: str) -> None:
   # logger.debug("setproctitle C module not available")
    #return None


#lo que escribe el cliente se lee en el servidor
servidor_lee, cliente_escribe = os.pipe()
#lo que escribe el servidor se lee en el cliente
cliente_lee, servidor_escribe = os.pipe()
#setproctitle.setproctitle("serv2")

pid = os.fork()
if pid:
    
    setproctitle.setproctitle("serv2")
    print("nombre proceso:", setproctitle.getproctitle())
# padre
    os.close(cliente_lee)
    os.close(cliente_escribe)
    #fdopen devuelve un open file object conectado con el file descriptor del pipe y le añadimos el argumento opcional r de read
    servidor_leeFichero = os.fdopen(servidor_lee, 'r')
    
    file_name = servidor_leeFichero.read()
    servidor_leeFichero.close()

    fichero = open(file_name, 'r')
    contenidoFichero = fichero.read()
    fichero.close()
    servidor_escribeFichero = os.fdopen(servidor_escribe, 'w')
    servidor_escribeFichero.write(contenidoFichero)

        
else:
# hijo
    #setproctitle(cli)
    setproctitle.setproctitle("cli2")

    os.close(servidor_escribe)
    os.close(servidor_lee)
    cliente_escribeFichero = os.fdopen(cliente_escribe, 'w')

    file_name = sys.argv[1]

    cliente_escribeFichero.write(file_name)
    cliente_escribeFichero.close()
    client_leeFichero = os.fdopen(cliente_lee, 'r')
    contenidoFichero = client_leeFichero.read()
    print(contenidoFichero)

    
