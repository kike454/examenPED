import os, time, sys
from datetime import datetime

def server():
    sc_w = os.open(sc, os.O_WRONLY)
    while True:
        hora = datetime.now()
        mensaje = hora.strftime("%d/%m/%Y %H:%M:%S\n")
        os.write(sc_w, mensaje.encode('utf8'))
        time.sleep(1)

if __name__ == '__main__':
    sc = '/tmp/ped1_group1Date'
    
    if not os.path.exists(sc):
	    os.mkfifo(sc)
    try:
        server()
    except KeyboardInterrupt:
        print("\nCerrando Servidor...\n")
