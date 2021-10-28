from abc import ABCMeta
from random import randint

class ordenador (metaclass=ABCMeta):
    def ordenador_jugar(cartajugada,ocartas): 
        if ocartas[0]>cartajugada:
            cartaordenador=ocartas[0]
        elif ocartas[1]>cartajugada:
            cartaordenador=ocartas[1]
        elif ocartas[2]>cartajugada:
            cartaordenador=ocartas[2]                
        else:
            cartaordenador=randint(ocartas)
        return cartaordenador  
        #eliminar la carta jugada