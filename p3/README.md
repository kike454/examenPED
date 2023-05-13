<em> Manual de usuario </em>

## :hammer:Funcionalidades del proyecto

- `Ejecutar la aplicacion con el comando make usando el fichero ubicado dentro del directorio `: make fifo 
- `Ejecutar la aplicacion con el fichero /etc/services`: make services 
- `Ejecutar la aplicacion con el fichero /bin/sh`: make binary 

<blockquote><p> El servidor crea y lee el FIFO /tmp/ped1_p3, el cliente crea el FIFO /tmp/ped1_p3 y escribe su PID y el nombre del fichero que quiere abrir. Seguidamente, el servidor recibe el mensaje, abre el fichero proporcionado por el cliente y el FIFO que este creo. En definitiva, el cliente envia el nombre del fichero al servidor y este le devuelve su contenido. </p> </blockquote>






