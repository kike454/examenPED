import os
from time import sleep
import setproctitle
fifo_path = "/tmp/ped1_p3"

setproctitle.setproctitle("serv3")

def servidor():
	fifo_lectura = open(fifo_path, "r")
	while True:
		mensaje_cliente = fifo_lectura.readline().split()
		if len(mensaje_cliente) == 0:
			continue
		elif len(mensaje_cliente) > 2:
			print("error en el input")
			continue

		pid_cliente = str(mensaje_cliente[0])
		try:
			fichero_requerido = open(mensaje_cliente[1], "rb")
			texto = fichero_requerido.read()
			fichero_requerido.close()

			fifo_escritura = open(fifo_path + "_{}".format(pid_cliente), "wb")
			fifo_escritura.write(texto)
			fifo_escritura.close()

			sleep(5)

		except FileNotFoundError:
			fifo_escritura = open(fifo_path + "_{}".format(pid_cliente), "w")
			fifo_escritura.write("error al abrir el fichero")
			fifo_escritura.close()


if __name__ == "__main__":
	try:
		os.mkfifo(fifo_path)
	except FileExistsError:
		pass
	servidor()

