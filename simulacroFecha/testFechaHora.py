import pytest

from FechaHora import FechaHora
from datetime import datetime
p1 = FechaHora()

now = datetime.now()
fechaActual = now.strftime('%Y %m %d')
horaActual = now.strftime( '%H:%M:%S')

def test0():
    assert p1.obtenerFecha() == fechaActual 

def test1():
    assert p1.obtenerHora() == horaActual
#test que comprueba si la instancia de esta clase es de la otra clase
def test2():
    assert isinstance(p1,FechaHora)
#test que comprueba si existe la variable en la otra clase
def test3():
    assert hasattr(p1,"now")

def test4():
    assert hasattr(p1,"date")

def test5():
    assert hasattr(p1,"hour")
#test si existe el metodo en la otra clase
def tes6():
    assert hasattr(FechaHora,"obtenerFecha")
def test7():
    assert hasattr(FechaHora,"obtenerHora")

