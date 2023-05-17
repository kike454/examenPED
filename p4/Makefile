socketsUDS:
	@echo "Compilando y ejecutando fifos"
	python3 serv4.py & 
	python3 cli4.py prueba.txt
	pkill -f serv4.py

binary:
	@echo "Compilando y ejecutando fifos con binarios: /bin/sh"
	python3  serv4.py & python3 cli4.py /bin/sh
	pkill -f serv4.py

date:
	@echo "Compilando y ejecutando la hora"
	python3 serverHour.py /tmp/ped1_group1_dateSocketsUDS & python3 clientHour.py /tmp/ped1_group1_dateSocketsUDS 


services:
	@echo "Ejecutando con fichero /etc/services"
	python3  serv4.py & python3 cli4.py /etc/services
	pkill -f serv4.py

clean:
	@echo "Limpiando..."
