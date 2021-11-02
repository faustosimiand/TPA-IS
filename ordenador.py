from abc import ABCMeta

class ordenador (metaclass=ABCMeta): 
    def ordenador_jugar(ocartas,cartajugada):  
        i=0
        while i<=len(ocartas):
            if  ocartas[i]>cartajugada:
                cartaordenador=ocartas[i]                        
            elif ocartas[i]==cartajugada:
                cartaordenador=ocartas[i]
            else:
                cartaordenador=ocartas[0]
        return cartaordenador  