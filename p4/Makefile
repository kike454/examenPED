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
	@echo "Compilando y ejecutando la hora con fechaHora.py"
	python3 fechaHora.py 


services:
	@echo "Ejecutando con fichero /etc/services"
	python3  serv4.py & python3 cli4.py /etc/services
	pkill -f serv4.py

clean:
	@echo "Limpiando..."
