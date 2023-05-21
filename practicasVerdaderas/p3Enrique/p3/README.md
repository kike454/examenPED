<em> Manual de usuario </em>

## :hammer:Funcionalidades del proyecto

- `Ejecutar la aplicacion con el comando make usando el fichero ubicado dentro del directorio `: make fifo 
- `Ejecutar la aplicacion con el fichero /etc/services`: make services 
- `Ejecutar la aplicacion con el fichero /bin/sh`: make binary 
- `Ejecutar la aplicacion para que de la hora`: make date

<blockquote><p> Una aplicación cliente-servidor mediante FIFOs consiste en que dos procesos separados se comunican a través de FIFOs (First In First Out), también conocidos como tuberías nombradas. El programa servidor es responsable de crear y escuchar en el FIFO del servidor para recibir datos del cliente, procesar los datos y enviar una respuesta a través de otro FIFO. Por otro lado, el programa cliente, crea y escribe datos en el FIFO del servidor y espera una respuesta a través de otro FIFO para luego mostrar el contenido de dicha respuesta. Además, se puede visualizar el nombre de los procesos con el comando ps -ef  </p> </blockquote>






