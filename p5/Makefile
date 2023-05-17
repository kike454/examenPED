socketsUDP:
	@echo "Compilando y ejecutando socketsUDP"
	python3 serv5.py & 
	python3 cli5.py prueba.txt
	pkill -f serv5.py

binary:
	@echo "Compilando y ejecutando fifos con binarios: /bin/sh"
	python3  serv5.py & python3 cli5.py /bin/sh
	pkill -f serv5.py

date:
	@echo "Compilando y ejecutando la hora"
	python3 serverHour.py & python3 clientHour.py
	pkill -f serverHour.py


services:
	@echo "Ejecutando con fichero /etc/services"
	python3  serv5.py & python3 cli5.py /etc/services
	pkill -f serv5.py

clean:
	@echo "Limpiando..."
