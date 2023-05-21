import os, time, sys
nombre_fifo = '/tmp/ped1_group1Send'
nombre_fifo2 = '/tmp/ped1_group1Receive'

# devuelve un fd de bajo nivel, y no convierte automaticamente el contenido del archivo a unicode, es decir, puedes trabajar con archivos que no sean de texto, por ejemplo, los binarios
fifo_escritura = os.open(nombre_fifo, os.O_WRONLY)
rutafichero = sys.argv[1]
os.write(fifo_escritura, rutafichero.encode('utf8'))

print("Se ha enviado el fichero: " + rutafichero)
os.close(fifo_escritura)

fifo_lectura = open(nombre_fifo2, 'r')
leido = fifo_lectura.read()
os.write(1,leido.encode('utf-8'))

