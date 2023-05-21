import os, time, sys
nombre_fifo = '/tmp/ped1_group1Send'
nombre_fifo2 = '/tmp/ped1_group1Receive'

if not os.path.exists(nombre_fifo):
        os.mkfifo(nombre_fifo)
if not os.path.exists(nombre_fifo2):
        os.mkfifo(nombre_fifo2)

#funcion incorporada que  devuelve un objeto de archivo
fifo_lectura = open(nombre_fifo, 'r')
mensaje = fifo_lectura.read()

info = open(mensaje, 'r')
data = info.read()

fifo_escritura = os.open(nombre_fifo2, os.O_WRONLY)
os.write(fifo_escritura, data.encode('utf-8'))  
        

