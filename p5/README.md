<em> Manual de usuario </em>

## :hammer:Funcionalidades del proyecto

- `Ejecutar la aplicacion con el comando make usando el fichero ubicado dentro del directorio `: make socketsUDP 
- `Ejecutar la aplicacion con el fichero /etc/services`: make services 
- `Ejecutar la aplicacion con el fichero /bin/sh`: make binary 
- `Ejecutar la hora`: make date


<blockquote><p> Tanto el cliente como el servidor crean un socket udp y especifican un puerto para escuchar los datagramas entrantes. Luego, el cliente envia los datagramas a la direccion IP y el puerto del servidor, y el servidor los recibe y los procesa. Cada datagrama se envia de forma independiente y no se establece una conexion previa entre ambos extremos de la comunicacion,es decir, la comunicacion es no orientada a conexion.  </blockquote></p>

<h3>Para comprobar que no hay ninguna diferencia entre los 2 archivos, puedes ejecutar la clase serv5 y la clase cli5 en dos terminales independientes, primero ejecutas el servidor <strong> python3 serv5.py </strong> y en segundo lugar, en el otro terminal ejecutas el cliente <strong> python3 cli5.py /etc/services </strong> y sigues estos pasos: </h3>

<ol>
	<li> Redirigimos la salida de un archivo en otro archivo llamado "kk", sintaxis: python3 cli5.py /etc > kk </li>
	<li> Comparamos los dos archivos y mostramos que no hay ninguna diferencia entre ellos: diff /etc/services kk </li>
	<li> Listamos el contenido del directorio incluyendo los archivos ocultos y detalles de permisos, nos fijamos si poseen el mismo tamaño: ls -la /etc/services kk </li>
</ol>





