fifo:
	@echo "Compilando y ejecutando fifos"
	python3 serv3.py & 
	python3 cli3.py prueba.txt
	pkill -f serv3.py

binary:
	@echo "Compilando y ejecutando fifos con binarios: /bin/sh"
	python3  cli3.py & python3 serv3.py /bin/sh
	pkill -f serv3.py

date:
	@echo "Compilando y ejecutando la hora con fechaHora.py"
	python3 fechaHora.py 


services:
	@echo "Ejecutando con fichero /etc/services"
	python3  serv3.py & python3 cli3.py /etc/services

clean:
	@echo "Limpiando..."
