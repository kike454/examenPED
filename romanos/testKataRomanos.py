import pytest
from KataRomanos import KataRomanos

p1 = KataRomanos()

def test0():
    assert hasattr(p1,"entero_a_romano")

def test1():
    #cadenaPrueba = "MMXXI".encode("utf8")
    numero = 2021
    assert p1.entero_a_romano(numero) == "MMXXI"

def test2():
    numero = 1094
    assert p1.entero_a_romano(numero) == "MXCIV"

def test3():
    numero = 47
    assert p1.entero_a_romano(numero) == "XLVII"

def test4():
    assert hasattr(p1,"romano_a_entero")

def test5():
    numero = "III"
    assert p1.romano_a_entero(numero) == 3

def test6():
    numero = "MMXXIII"
    assert p1.romano_a_entero(numero) == 2023

