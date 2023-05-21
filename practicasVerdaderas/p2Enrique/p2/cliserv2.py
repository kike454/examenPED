import os
import sys
import setproctitle
import json

if len(sys.argv) != 2:
    #print("Introduzca la ruta del fichero del cual desea leer su contenido: " )
    resp1 = " Introduzca la ruta del fichero del cual desea leer su contenido \n"
    encode1 = resp1.encode()
    os.write(2, encode1)
    exit(1)



#lo que escribe el cliente se lee en el servidor
servidor_lee, cliente_escribe = os.pipe()
#lo que escribe el servidor se lee en el cliente
cliente_lee, servidor_escribe = os.pipe()
#setproctitle.setproctitle("serv2")

pid = os.fork()
if pid:
    
    setproctitle.setproctitle("serv2")
    #print("nombre proceso servidor:", setproctitle.getproctitle())
    resp2 = "nombre proceso padre (servidor): ", setproctitle.getproctitle() 
    resp3 = json.dumps(resp2)
    encode2 = resp3.encode()
    os.write(2, encode2)
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
    resp4 = "nombre proceso hijo (servidor): ", setproctitle.getproctitle()
    resp5 = json.dumps(resp4)
    encode3 = resp5.encode()
    os.write(2, encode3)

    os.close(servidor_escribe)
    os.close(servidor_lee)
    cliente_escribeFichero = os.fdopen(cliente_escribe, 'w')

    file_name = sys.argv[1]

    cliente_escribeFichero.write(file_name)
    cliente_escribeFichero.close()
    client_leeFichero = os.fdopen(cliente_lee, 'r')
    contenidoFichero = client_leeFichero.read()
    bytesFile = contenidoFichero.encode()
    os.write(1,bytesFile)
    #print(contenidoFichero)

    
