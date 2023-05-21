<em> Manual de usuario </em>

## :hammer:Funcionalidades del proyecto

- `Ejecutar la aplicacion con el comando make usando el fichero ubicado dentro del directorio `: make socketsTCP 
- `Ejecutar la aplicacion con el fichero /etc/services`: make services 
- `Ejecutar la aplicacion con el fichero /bin/sh`: make binary 

<blockquote><p>  El servidor crea un socket TCP utilizando la funcion socket() y espera a que un cliente se conecte. El cliente crea otro socket y se conecta al servidor mediante el metodo connect(). UNa vez establecida la conexion el cliente y el servidor pueden enviar y recibir datos utlizando los metodos send() y recv(). El protocolo TCP garantiza que los datos sean entregados sin errores y en orden, e incluye mecanismos de control de congestion para evitar la sobrecarga de la red.Además, se puede visualizar el nombre de los procesos con el comando ps -ef    </p></blockquote>






