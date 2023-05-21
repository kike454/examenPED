import sys, os, time
from datetime import datetime

r, w = os.pipe()
info = datetime.now()
date_time = info.strftime("Año: %Y, Mes: %m Día: %d. Hora exacta:  %H:%M:%S")
pid = os.fork()

if pid:
    os.close(r)
    fd1 = os.fdopen(w, 'w')
  #  time.sleep(10)
    fd1.write(date_time)
    
else:
    os.close(w)
    fd2 = os.fdopen(r, 'r')
    fechaHora = fd2.read()
    print(fechaHora)
