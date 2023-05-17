<em> Manual de usuario </em>

## :hammer:Funcionalidades del proyecto

- `Ejecutar la aplicacion con el comando make usando el fichero ubicado dentro del directorio `: make socketsUDS 
- `Ejecutar la aplicacion con el fichero /etc/services`: make services 
- `Ejecutar la aplicacion con el fichero /bin/sh`: make binary 
- `Ejecutar la hora`: make date

<blockquote><p> El proceso servidor crea un socket UDS /tmp/ped1_group1 y espera a que el cliente se conecte a él. El cliente, a su vez, abre un socket UDS y se conecta al servidor. Una vez establecida la conexión, ambos procesos pueden enviar y recibir datos en ambos sentidos.Además, la comunicación mediante sockets UDS permite la comunicación bidireccional y se puede utilizar para la comunicación entre procesos que se ejecutan en diferentes directorios de un sistema de archivos </p></blockquote>







