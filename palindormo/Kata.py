import os

class Kata:

        
    def esPalindromo(self,cadena):
        #cadena = cadena.decode("utf-8")
        #print("cadena", cadena )
        if cadena == ''.join(reversed(cadena)):
            return True
        else:
            return False
        
    def esVocal(self,cadena):
        contador=0
        total =0
        #posible refactor, lower y quitas las mayusculas
        vocales = "aeiouAEIOU"
        #cadena = cadena.decode("utf-8")
        #print("cadenavoc",cadena)
        #if cadena in "aeiouAEIOU":
        for vocal in cadena:
        
            if vocal in vocales:
                #print("cadena", cadena, "vocal",vocal)
            #print("cadena vocal")
                contador += 1
     #   total += contador
        #print(contador)
        return contador

    def startsWithA(self,cadena):
        #cadena1 = cadena.decode("utf8")
        if cadena.startswith("a") or cadena.startswith("A"):
            return True
        else:
            return False
    
    def palabrasConVocalesImpares(self,cadena):
        #cadena1 = cadena.decode("utf8")
        vocales = "aeiouAEIOU"
        contador = 0
        for vocal in cadena:
            if vocal in vocales:
                contador+=1
        if contador % 2 ==1:
            return cadena
        else:
            return False
    
    def palabrasQueTenganTamañoMayorQue7(self,cadena):
        #cadena1 = cadena.decode("utf8")
        if len(cadena) >=7:
            return cadena
        else:
            return False

    def deletarVocalesDeUnaCadena(self,cadena):
        #cadena1 = cadena.decode("utf8")
        cadenaConsonantes = ""
        for vocal in cadena:
            if vocal not in "aeiouAEIOU":
                cadenaConsonantes+=vocal
        return cadenaConsonantes
        
    def annadirZDespuesDeUnaA(self,cadena):
        #cadena1 = cadena.decode("utf8")
        
        caracter_a_insertar = "z"
        #for letter in cadena1:
            #print("vocal", letter)
            #if letter in "aA":
                #print("ltter if", letter)
                
        cadena_nueva = cadena.lower().replace("a" ,"a"  +  caracter_a_insertar)
                
        print(cadena_nueva)
               
        return cadena_nueva
    
    def annadirXTresPosicionesMasDeUnaJ(self,cadena):
        #cadena1 = cadena.decode("utf8")
        
        caracter_a_insertar = "x"
        
        # Encontrar la posición de la primera aparición de "a" (mayúscula o minúscula)
        indice_a = cadena.lower().find("j")

        # Calcular la posición donde se insertará el carácter "z"
        posicion_insercion = indice_a + 3

        # Insertar el carácter "z" en la posición determinada
        cadena_nueva = cadena[:posicion_insercion] + caracter_a_insertar + cadena[posicion_insercion:]
        
        #cadena_nueva = cadena1.lower().replace("j" ,"j"   +  caracter_a_insertar)
        print(cadena_nueva)

        return cadena_nueva
    
    def contar_a_en_una_linea(self,fichero):
        data = fichero.read()
        
        total_aS = 0
        for line in data:
            if line in "a":
                total_aS+=1
        return total_aS
    
    def entero_a_romano(self,numero):
        #numero1 = numero.decode("utf8")
        #intNumero = int(numero1)
        valores = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        resultado = ''

        for valor, simbolo in valores.items():
            while numero >= valor:
                resultado += simbolo
                numero -= valor

        return resultado


