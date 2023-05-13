from Kata import Kata
#from NumeroMenorQue10Exception import NumeroMenorQue10Exception
import pytest
p1=Kata()
#p2=NumeroMenorQue10Exception.NumeroMenorQue10Exception(Exception)

my_empty_dic={}
list_empty = []
############################################
#   LISTAS
############################################
def testcalcularPuntuacionTodo1():
    lista1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #p1.tirada(lista1)
    assert p1.puntuacion(lista1,10) == 20

def testcalcularPuntuacionTodo4():
   lista1 = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
   assert p1.puntuacion(lista1,10) == 80

def test1SpareAlPrincipio():
    lista1 = [5,5,4,4,4,4,4,4,5,3,2,1,2,1,2,1,2,1,2,1]
    assert p1.puntuacion(lista1,10) == 61

def test1SpareEntreMedias():
    lista1 = [3,3,3,3,3,3,3,3,6,4,7,2,9,0,4,2,1,1,2,2]
    assert p1.puntuacion(lista1,10) == 71

def test1SpareAlFinal():
    lista1 = [1,3,2,5,2,5,2,1,5,4,2,3,7,1,0,1,3,4,8,2,1]
    assert p1.puntuacion(lista1,10) == 62

def test2SpareEntreMedias():
    lista1 = [2,4,2,1,3,5,3,6,5,5,9,1,5,3,2,1,0,0,3,2]
    assert p1.puntuacion(lista1,10) == 76

def test2SpareAlFinal():
    lista1 = [1,3,5,3,1,0,2,4,5,4,2,1,3,5,3,1,3,7,9,1,7]
    assert p1.puntuacion(lista1,10) == 79

def testTodoSpare():
    lista1 = [8,2,8,2,8,2,8,2,8,2,8,2,8,2,8,2,8,2,8,2,2]
    assert p1.puntuacion(lista1,10) == 174

def test1StrikeTodo3():
    lista1 = [10,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    assert p1.puntuacion(lista1,10) == 70

def test1StrikeAlfinalConTodo4():
    lista1 = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,10,4,4]
    assert p1.puntuacion(lista1,10) == 90

def test2StrikesSeguidosConTodo3():
    lista1 = [3,3,10,10,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    assert p1.puntuacion(lista1,10) == 87

def testTodoStrikes():
    lista1 = [10,10,10,10,10,10,10,10,10,10,10,10]
    assert p1.puntuacion(lista1,10) == 300

def test2StrikesSeguidosDe2SpareConTodo9():
    lista1 = [10,10,9,1,7,3,9,0,0,9,0,9,0,9,0,9,0,9]
    assert p1.puntuacion(lista1,10) == 139

def test2StrikesConDosSpareAlFinalConTodo1():
    lista1 = [1,1,1,1,1,1,1,1,1,1,1,1,10,10,9,1,5,5,1]
    assert p1.puntuacion(lista1,10) == 87

def test2SpareConCuatroStrikeAlFinalConTodo1():
    lista1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,9,7,3,10,10,10,10]
    assert p1.puntuacion(lista1,10) == 109

##############################################
#   EXCEPCIONES 
##############################################

##########LISTAS
def test3RondasListas():
    lista1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,9,7,3,10,10,10,10]
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.puntuacion(lista1,3)
    assert str(exception.value) == "El número debe ser exactamente 10"

def test14RondasListas():
    lista1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,9,7,3,10,10,10,10]
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.puntuacion(lista1,14)
    assert str(exception.value) == "El número debe ser exactamente 10"

def testBolosNegativosListas():
    lista1 = [1,1,1,1,1,1,-1,1,1,1,1,1,1,9,7,3,10,10,10,10]
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.puntuacion(lista1,14)
    assert str(exception.value) == "No puedes derribar bolos negativos palomo"


def testBolosMayoresQue10():
    lista1 = [1,1,1,50,11,1,1,1,1,1,1,1,1,9,7,3,10,10,10,10]
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.puntuacion(lista1,14)
    assert str(exception.value) == "No puedes derribar bolos negativos palomo"

def testMeterloPorElAgujeroEquivocadoListas():
    lista1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,9,7,3,10,10,"klkwawawa",10]
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.puntuacion(lista1,14)
    assert str(exception.value) == "no estas metiendo numeros"



########################DICCIONARIOS

def test7RondasDic():
    dic1 = {1: [4,3], 2: [4,3], 3:[4,3], 4:[4,3], 5:[4,3], 6:[4,3], 7:[4,3]}
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.dicScore(dic1)
    assert str(exception.value) == "El número debe ser exactamente 10"

def test11RondasDic():
    dic1 = {1: [4,3], 2: [4,3], 3:[4,3], 4:[4,3], 5:[4,3], 6:[4,3], 7:[4,3],8:[4,3],9:[4,3],10:[4,3],11:[4,3]}
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.dicScore(dic1)
    assert str(exception.value) == "El número debe ser exactamente 10"

def testBolosNegativosDic():
    dic1 = {1: [4,3], 2: [4,3], 3:[4,3], 4:[4,3], 5:[4,3], 6:[4,3], 7:[4,3],8:[4,3],9:[4,3],10:[4,3],11:[4,-3]}
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.dicScore(dic1)
    assert str(exception.value) == "No puedes derribar bolos negativos palomo"

def testBolosMayoresQue10Dic():
    dic1 = {1: [4,3], 2: [4,3], 3:[4,3], 4:[4,3], 5:[4,3], 6:[4,3], 7:[11,3],8:[4,19],9:[4,3],10:[4,3],11:[4,3]}
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.dicScore(dic1)
    assert str(exception.value) == "No puedes derribar bolos negativos palomo"

def testMeterloPorElAgujeroEquivocadoDic():
    dic1 = {1: [4,3], 2: [4,3], 3:[4,3], 4:[4,3], 5:[4,3], 6:[4,3], 7:[2,3],8:[4,1],9:[4,3],10:[4,"delo3"],11:[4,3]}
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.dicScore(dic1)
    assert str(exception.value) == "no estas metiendo numeros"

######################STRING

def test7RondasString():
    cadena = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"
    
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.strScore(cadena, 7)
    assert str(exception.value) == "El número debe ser exactamente 10"

def test19RondasString():
    cadena = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"
    
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.strScore(cadena, 19)
    assert str(exception.value) == "El número debe ser exactamente 10"

def testNumeroNegativoString():
    cadena = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1"
    
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.strScore(cadena, 10)
    assert str(exception.value) == "No puedes derribar bolos negativos palomo"

def testNumeroMayorQue10String():
    cadena = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,69"
    
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.strScore(cadena, 10)
    assert str(exception.value) == "No puedes derribar bolos negativos palomo"

def testMeterloPorElAgujeroEquivocadoString():
    cadena = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,<==3"
    
    #p1.puntuacion(lista1,3)
    with pytest.raises(Kata) as exception:
        #raise NumeroMenorQue10Exception.NumeroMenorQue10Exception("El número debe ser exactamente 10")
        #p1.puntuacion(lista1,10)
        p1.strScore(cadena, 10)
    assert str(exception.value) == "no estas metiendo numeros"




###################################################################
#   DICCIONARIOS
###################################################################
def testDiccionarioTodo7():
    dic1 = {1: [4,3], 2: [4,3], 3:[4,3], 4:[4,3], 5:[4,3], 6:[4,3], 7:[4,3], 8:[4,3], 9:[4,3],10:[4,3]}
    assert p1.dicScore(dic1) == 70

def testDiccionario1SpareAlPrincipioConTodo2():
    dic1 = {1: [5,5], 2: [2,2], 3:[2,2], 4:[2,2], 5:[2,2], 6:[2,2], 7:[2,2], 8:[2,2], 9:[2,2],10:[2,2]}
    assert p1.dicScore(dic1) == 48

def testDiccionario2SpareAlPrincipioSeguidosConTodo2():
    dic1 = {1: [5,5], 2: [5,5], 3:[2,2], 4:[2,2], 5:[2,2], 6:[2,2], 7:[2,2], 8:[2,2], 9:[2,2],10:[2,2]}
    assert p1.dicScore(dic1) == 59

def testDiccionario2SpareEntreMediasSeguidosConTodo3():
    dic1 = {1: [3,3], 2: [3,3], 3:[3,3], 4:[6,4], 5:[7,3], 6:[3,3], 7:[3,3], 8:[3,3], 9:[3,3],10:[3,3]}
    assert p1.dicScore(dic1) == 78

def testDiccionario2SpareAlFinalSeguidosConTodo1():
    dic1 = {1: [1,1], 2: [1,1], 3:[1,1], 4:[1,1], 5:[1,1], 6:[1,1], 7:[1,1], 8:[5,5], 9:[3,7],10:[2,8,4]}
    assert p1.dicScore(dic1) == 53

def testDiccionarioTodoSpare():
    dic1 = {1: [5,5], 2: [4,6], 3:[3,7], 4:[1,9], 5:[9,1], 6:[4,6], 7:[5,5], 8:[4,6], 9:[8,2],10:[2,8,7]}
    assert p1.dicScore(dic1) == 147

def testDiccionario1StrikeAlPrincipioConTodo1():
    dic1 = {1: [10], 2: [1,1], 3:[1,1], 4:[1,1], 5:[1,1], 6:[1,1], 7:[1,1], 8:[1,1], 9:[1,1],10:[1,1]}
    assert p1.dicScore(dic1) == 30

def testDiccionario2StrikesAlMedioConTodo3():
    dic1 = {1: [3,3], 2: [3,3], 3:[3,3], 4:[10], 5:[10], 6:[3,3], 7:[3,3], 8:[3,3], 9:[3,3],10:[3,3]}
    assert p1.dicScore(dic1) == 87

def testDiccionario3StrikesAlMedioConTodo3():
    dic1 = {1: [3,3], 2: [3,3], 3:[3,3], 4:[10], 5:[10], 6:[10], 7:[3,3], 8:[3,3], 9:[3,3],10:[3,3]}
    assert p1.dicScore(dic1) == 111

def testDiccionarioTodoStrikes():
    dic1 = {1: [10], 2: [10], 3:[10], 4:[10], 5:[10], 6:[10], 7:[10], 8:[10], 9:[10],10:[10,10,10]}
    assert p1.dicScore(dic1) == 300

def testDiccionarioMitadStrikesMitadSpare():
    dic1 = {1: [10], 2: [10], 3:[10], 4:[10], 5:[10], 6:[7,3], 7:[2,8], 8:[4,6], 9:[5,5],10:[3,7,10]}
    assert p1.dicScore(dic1) == 211
    
##################################
#   STRINGS
##################################
def testStringTodo1():
    cadena = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1"
    assert p1.strScore(cadena,10) == 20

def testStringTodo4():
    cadena = "4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4"
    assert p1.strScore(cadena,10) == 80

def testString1SpareAlPrincipio():
    cadena = "5,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2"
    assert p1.strScore(cadena,10) == 48

def testString2SpareSeguidosAlPrincipio():
    cadena = "5,5,4,6,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2"
    assert p1.strScore(cadena,10) == 58

def testStringTodoSpare():
    cadena = "5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5"
    assert p1.strScore(cadena,10) == 150

def testStringTodoSpare2():
    cadena = "3,7,5,5,8,2,9,1,6,4,6,4,7,3,8,2,9,1,3,7,9"
    assert p1.strScore(cadena,10) == 170

def testString1StrikeConTodo4():
    cadena = "4,4,10,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4"
    assert p1.strScore(cadena,10) == 90

def testString2StrikesSeguidosEnElMedioConTodo2():
    cadena = "2,2,2,2,2,2,10,10,2,2,2,2,2,2,2,2,2,2"
    assert p1.strScore(cadena,10) == 68

def testString5StrikesAlFinalConTodo1():
    cadena = "1,1,1,1,1,1,1,1,1,1,1,1,1,1,10,10,10,10,10"
    assert p1.strScore(cadena,10) == 104

def testStringTodoStrikes():
    cadena = "10,10,10,10,10,10,10,10,10,10,10,10"
    assert p1.strScore(cadena,10) == 300