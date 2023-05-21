import os, time, sys
from datetime import datetime

nombre_fifo = '/tmp/ped1_group1Date'

if not os.path.exists(nombre_fifo):
            os.mkfifo(nombre_fifo)

fifo_escritura = os.open(nombre_fifo, os.O_WRONLY)
while True:
    hora = datetime.now()
    mensaje = hora.strftime("%d/%m/%Y %H:%M:%S\n")
    os.write(fifo_escritura, mensaje.encode('utf8'))
    time.sleep(1)

