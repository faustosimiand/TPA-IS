from abc import ABCMeta

class ordenador (metaclass=ABCMeta): 
    def ordenador_jugar(ocartas,cartajugada):  
        i=0
        max=len(ocartas)
        supera=False
        while i<max:            
            if  ocartas[i]>cartajugada:
                cartaordenador=ocartas[i]
                supera=True 
                return cartaordenador                                      
            if ocartas[i]==cartajugada:
                cartaordenador=ocartas[i]
                supera=True 
                return cartaordenador 
            i+=1           
        if supera==False:
            cartaordenador=ocartas[0]
            return cartaordenador