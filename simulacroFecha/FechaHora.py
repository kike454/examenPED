
from datetime import datetime

class FechaHora:

    now = datetime.now() 
    date =0
    hour =0

    def obtenerFecha(self):
       
        date = self.now.strftime('%Y %m %d')
        return date

    def obtenerHora(self):
         hour = self.now.strftime('%H:%M:%S')
         return hour