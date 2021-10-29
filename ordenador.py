from abc import ABCMeta
from random import randint

class ordenador (metaclass=ABCMeta):

    def __init__(self, x=5,y=5):
        self.ft=x
        self.inch=y
    
    def mayor(self, other):
        in1=self.ft*12+self.inch
        in2=other.ft*12+other.inch
        if in1>in2:
            return True
        else:
            return False

    def ordenador_jugar(cartajugada,ocartas):
        c1=ocartas[0] 
        c2=ocartas[1]
        c3=ocartas[2]
        if  ordenador.mayor(c1,cartajugada)==True:
            cartaordenador=ocartas[0]
        elif ordenador.mayor(c2,cartajugada)==True:
            cartaordenador=ocartas[1]
        elif ordenador.mayor(c3,cartajugada)==True:
            cartaordenador=ocartas[2]                
        else:
            cartaordenador=randint(ocartas)
        return cartaordenador  
        #eliminar la carta jugada