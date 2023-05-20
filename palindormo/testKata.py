import pytest
from Kata import Kata

p1 = Kata()

def test1():
    cadenaPrueba = "somos".encode("utf8")
    assert p1.esPalindromo(cadenaPrueba) 

def test2():
    cadenaPrueba = "noPalindromo".encode("utf8")
    assert not p1.esPalindromo(cadenaPrueba)

def test3():
    cadenaPrueba = "hola".encode("utf8")
    assert p1.esVocal(cadenaPrueba) == 2

def test4():
    cadenaPrueba = "murcielago".encode("utf8")
    assert p1.esVocal(cadenaPrueba) == 5

def test5():
    cadenaPrueba = "ana".encode("utf8")
    assert p1.esPalindromo(cadenaPrueba)

def test6():
    assert hasattr(Kata,"esPalindromo")

def test7():
    assert hasattr(Kata,"esVocal")

def test8():
    cadenaPrueba = "Amanda".encode("utf8")
    assert p1.startsWithA(cadenaPrueba)

def test9():
    cadenaPrueba = "tuyaaya".encode("utf8")
    assert not p1.startsWithA(cadenaPrueba)
def test10():
    cadenaPrueba = "ana".encode("utf8")
    assert p1.startsWithA(cadenaPrueba)
def test11():
    cadenaPrueba = "maria".encode("utf8")
    assert p1.palabrasConVocalesImpares(cadenaPrueba) == "maria"
def test12():
    cadenaPrueba = "raul".encode("utf8")
    assert not p1.palabrasConVocalesImpares(cadenaPrueba)

def test13():
    cadenaPrueba = "mamaguevo".encode("utf8")
    assert p1.palabrasQueTenganTamañoMayorQue7(cadenaPrueba) == "mamaguevo"

def test14():
    cadenaPrueba = "d3".encode("utf8")
    assert not p1.palabrasQueTenganTamañoMayorQue7(cadenaPrueba) 

def test15():
    cadenaPrueba = "keloke".encode("utf8")
    assert p1.deletarVocalesDeUnaCadena(cadenaPrueba) == "klk"

def test16():
    cadenaPrueba = "klk".encode("utf8")
    assert p1.deletarVocalesDeUnaCadena(cadenaPrueba) == "klk"

def test17():
    cadenaPrueba = "Alocado".encode("utf8")
    assert p1.annadirZDespuesDeUnaA(cadenaPrueba) == "azlocazdo"

def test18():
    cadenaPrueba = "orco".encode("utf8")
    assert p1.annadirZDespuesDeUnaA(cadenaPrueba) == "orco"

def test19():
    cadenaPrueba = "joder".encode("utf8")
    assert p1.annadirXTresPosicionesMasDeUnaJ(cadenaPrueba) == "jodxer"

def test20():
    cadenaPrueba = "olla".encode("utf8")
    assert p1.annadirXTresPosicionesMasDeUnaJ(cadenaPrueba) == "olxla"

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






