#import NumeroMenorQue10Exception
#p2=NumeroMenorQue10Exception.NumeroMenorQue10Exception(Exception)
class Kata(Exception):
    #def __init__(self, mensaje="El número introducido debe ser exactamente 10"):
        #self.mensaje = mensaje
        #super().__init__(mensaje)
   
    def puntuacion(self,bolosTirados,rondas):
        #rondas
        score =0
        indice =0
        for numero in bolosTirados:
            if not isinstance(numero, int):
                raise Kata("no estas metiendo numeros")
            if numero <0 or numero>10:
                raise Kata("No puedes derribar bolos negativos palomo")
            



        if rondas != 10:
            raise Kata("El número debe ser exactamente 10")
        
        for i in range(rondas):
            
            if (bolosTirados[indice] == 10) :
                score+=10 + bolosTirados[indice+1] + bolosTirados[indice+2]
                indice+=1
            elif bolosTirados[indice] + bolosTirados[indice+1] ==10:
                #como es un spare, tienes que sumarle el primer juego de la siguiente ronda
                score+=10 + bolosTirados[indice+2]
                indice+=2
                print("ronda",i, "score",score,"indice",indice)
            else:
                score += (bolosTirados[indice] + bolosTirados[indice+1])
            #print("celda", indice ,"valor", self.tirada(indice), "celda+1", indice+1,"valor+1",self.tirada(indice+1))
                indice+=2
                print("ronda",i, "score",score,"indice",indice)
        return score

    def dicScore(self,bolosTiradosDic):
        clave =1
        score =0
        indice=0
        #print(all(value < 0 for value in list(bolosTiradosDic.values())))
        for i in bolosTiradosDic:
            for elemento in bolosTiradosDic[i]:
                if not isinstance(elemento, int):
                     raise Kata("no estas metiendo numeros")
                if elemento<0 or elemento>10:
                    raise Kata("No puedes derribar bolos negativos palomo")

        if len(bolosTiradosDic) != 10:
            raise Kata("El número debe ser exactamente 10")

        for key in sorted(bolosTiradosDic.keys()):
            print("KEY", key)
            #STRIKE
            if bolosTiradosDic[key][0] == 10:
                #1 strike seguido de una ronda normal key!=10 and
                if  key != len(bolosTiradosDic) and   (len(bolosTiradosDic[key+1]) >=2):
                    score+= 10 + bolosTiradosDic[key+1][0] + bolosTiradosDic[key+1][1]
                    print("1 stk -> normal","puntuacion", score,"key", key ,"1celda",bolosTiradosDic[key+1][0],"2celda", bolosTiradosDic[key+1][1])
                    clave+=1
                #1 strike seguido de otro strike
                else:
                    if key == len(bolosTiradosDic):
                        score+= 10 + bolosTiradosDic[key][1] + bolosTiradosDic[key][2]
                        clave+=1
                    else:
                        score+= 10 + bolosTiradosDic[key+1][0] + bolosTiradosDic[key+2][0]
                        print("else","puntuacion", score,"key", key ,"1celda",bolosTiradosDic[key+1][0])
                        clave+=1
            #SPARE
            elif bolosTiradosDic[key][0] + bolosTiradosDic[key][1] ==10:
                #print("key", key, "tamaño", len(bolosTiradosDic))
                if key == len(bolosTiradosDic):
                    #print("2key", key)
                    score += 10 + bolosTiradosDic[key][2]
                    clave+=1
                else:
                    score += 10 + bolosTiradosDic[key+1][0]
                    clave+=1
            #NORMAL
            else:
                score += sum(valor for valor in bolosTiradosDic[clave])
                print("puntuacion", score,"key", key ,"1celda",bolosTiradosDic[key][0],"2celda", bolosTiradosDic[key][1])
                clave+=1

        return score 

    def strScore(self,cadenaDeBolosTirados,rondas):


        if rondas != 10:
            raise Kata("El número debe ser exactamente 10")
        

        score=0
        indice =0
        lista_de_bolos = cadenaDeBolosTirados.split(",")
        try:
            lista_de_enteros = [int(numero) for numero in lista_de_bolos]
            for num in lista_de_enteros:
                if num <0 or num>10:
                    raise Kata("No puedes derribar bolos negativos palomo")

            for i in range(rondas):
                if lista_de_enteros[indice] ==10:
                    score+= 10 + lista_de_enteros[indice+1] + lista_de_enteros[indice+2]
                    indice+=1
                elif lista_de_enteros[indice] + lista_de_enteros[indice+1]==10:
                    score+= 10 + lista_de_enteros[indice+2]
                    print("inidce", indice)
                    indice+=2
                else:
                    score+= lista_de_enteros[indice] + lista_de_enteros[indice+1]
                    indice+=2
            return score
        except ValueError:
           raise Kata("no estas metiendo numeros") 