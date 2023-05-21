import pytest
from Kata import Kata
import os
import sys

p1 = Kata()

def test1():
    #cadenaPrueba = "somos".encode("utf8")
    assert p1.esPalindromo("somos") 

def test2():
    #cadenaPrueba = "noPalindromo".encode("utf8")
    assert not p1.esPalindromo("noPalindromo")

def test3():
    #cadenaPrueba = "hola".encode("utf8")
    assert p1.esVocal("hola") == 2

def test4():
    #cadenaPrueba = "murcielago".encode("utf8")
    assert p1.esVocal("murcielago") == 5

def test5():
    #cadenaPrueba = "ana".encode("utf8")
    assert p1.esPalindromo("ana")

def test6():
    assert hasattr(Kata,"esPalindromo")

def test7():
    assert hasattr(Kata,"esVocal")

def test8():
    #cadenaPrueba = "Amanda".encode("utf8")
    assert p1.startsWithA("Amanda")

def test9():
    #cadenaPrueba = "tuyaaya".encode("utf8")
    assert not p1.startsWithA("tuyaya")
def test10():
    #cadenaPrueba = "ana".encode("utf8")
    assert p1.startsWithA("ana")
def test11():
    #cadenaPrueba = "maria".encode("utf8")
    assert p1.palabrasConVocalesImpares("maria") == "maria"
def test12():
    #cadenaPrueba = "raul".encode("utf8")
    assert not p1.palabrasConVocalesImpares("raul")

def test13():
    #cadenaPrueba = "mamaguevo".encode("utf8")
    assert p1.palabrasQueTenganTamañoMayorQue7("mamaguevo") == "mamaguevo"

def test14():
    #cadenaPrueba = "d3".encode("utf8")
    assert not p1.palabrasQueTenganTamañoMayorQue7("d3") 

def test15():
    #cadenaPrueba = "keloke".encode("utf8")
    assert p1.deletarVocalesDeUnaCadena("keloke") == "klk"

def test16():
    #cadenaPrueba = "klk".encode("utf8")
    assert p1.deletarVocalesDeUnaCadena("klk") == "klk"

def test17():
    #cadenaPrueba = "Alocado".encode("utf8")
    assert p1.annadirZDespuesDeUnaA("Alocado") == "azlocazdo"

def test18():
    #cadenaPrueba = "orco".encode("utf8")
    assert p1.annadirZDespuesDeUnaA("orco") == "orco"

def test19():
    #cadenaPrueba = "joder".encode("utf8")
    assert p1.annadirXTresPosicionesMasDeUnaJ("joder") == "jodxer"

def test20():
    #cadenaPrueba = "olla".encode("utf8")
    assert p1.annadirXTresPosicionesMasDeUnaJ("olla") == "olxla"

def test21():
    #cadenaPrueba = "MMXXI".encode("utf8")
    numero = 2021
    assert p1.entero_a_romano(numero) == "MMXXI"

def test22():
    numero = 1094
    assert p1.entero_a_romano(numero) == "MXCIV"

def test23():
    numero = 47
    assert p1.entero_a_romano(numero) == "XLVII"
#contar a's
def test24():
   filename = "fichero.txt"

    # Abrir el archivo en modo de escritura
   
   fichero = open(filename,"r")
   
   assert p1.contar_a_en_una_linea(fichero) == 2

def test_file_existence():
    filename = "fichero.txt"  

    assert os.path.isfile(filename) == True

def test_file_permissions():
    filename = "fichero.txt"

    assert os.access(filename, os.R_OK) == True  # Comprobar permisos de lectura
    assert os.access(filename, os.W_OK) == True  # Comprobar permisos de escritura
   




