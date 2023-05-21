socketsTCP:
	@echo "Compilando y ejecutando socketsTCP"
	python3 serv6.py & 
	python3 cli6.py prueba.txt
	pkill -f serv6.py

binary:
	@echo "Compilando y ejecutando fifos con binarios: /bin/sh"
	python3  serv6.py & python3 cli6.py /bin/sh
	pkill -f serv6.py

date:
	@echo "Compilando y ejecutando la hora"
	python3 serverHour.py & python3 clientHour.py
	pkill -f serverHour.py	


services:
	@echo "Ejecutando con fichero /etc/services"
	python3  serv6.py & python3 cli6.py /etc/services
	pkill -f serv6.py

clean:
	@echo "Limpiando..."
