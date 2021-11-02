from abc import ABCMeta

class ordenador (metaclass=ABCMeta): 
    def ordenador_jugar(ocartas,cartajugada):  
        i=0
        while i<=len(ocartas):
            if  ocartas[i]>=cartajugada:
                cartaordenador=ocartas[i]
                return cartaordenador                        
            elif ocartas[i]==cartajugada:
                cartaordenador=ocartas[i]
                return cartaordenador
            else:
                cartaordenador=ocartas[0]
                return cartaordenador  