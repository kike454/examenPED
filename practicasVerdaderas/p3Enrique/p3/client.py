import os, time, sys
from datetime import datetime
from time import sleep

nombre_fifo = '/tmp/ped1_group1Date'

fifo_lectura = open(nombre_fifo, "r")
message = fifo_lectura.readline()
print(message)

