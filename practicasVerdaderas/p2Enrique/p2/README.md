<em> Manual de usuario </em>

## :hammer:Funcionalidades del proyecto

- `Ejecutar la aplicacion con el comando make usando el fichero ubicado dentro del directorio `: make pipes 
- `Ejecutar la aplicacion con el fichero /etc/services`: make services 
- `Ejecutar la aplicacion con el fichero /bin/sh`: make binary 


<blockquote><p> La conexión mediante pipes entre un cliente y un servidor es un mecanismo de comunicación interproceso (IPC) que permite el intercambio de datos entre dos procesos diferentes que se ejecutan en la misma máquina. El proceso servidor crea un pipe con nombre o un pipe anónimo y espera a que el cliente se conecte a él. El cliente, a su vez, abre el pipe y se conecta al servidor. La comunicación a través de pipes es unidireccional, lo que significa que cada proceso debe tener su propio conjunto de pipes para enviar y recibir datos. A partir de este momento, ambos procesos pueden leer y escribir datos en el pipe de forma bidireccional. Además, se puede visualizar el nombre de los procesos con el comando ps -ef  </p> </blockquote>






