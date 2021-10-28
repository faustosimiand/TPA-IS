import random
import time
import os
from presentaciones import presentacion
from carta import cartas
from random import randrange

def jugarCarta(ucartas): 
    cartajugada = input("carta a jugar: ") 
    while cartajugada not in ucartas:
        if cartajugada not in ucartas:
            cartajugada = input("Elige una carta que tengas :")
        return cartajugada       
    #eliminar la carta jugada

def ordenador(cartajugada,ocartas):
    cartaordenador:int
    if ocartas(1)>cartajugada:
        cartaordenador=ocartas(1)
    elif ocartas(2)>cartajugada:
        cartaordenador=ocartas(2)
    elif ocartas(3)>cartajugada:
        cartaordenador=ocartas(3)                
    else:
        cartaordenador=random(ocartas)
    return cartaordenador  
    #eliminar la carta jugada


#en el main hay que hacer un random para las 3 cartas y mostrarlas
#asignar dos contadores para user y para pc
#definir ganador (1 si es user, 2 si es pc)
#hacer un while con un boolean 
#hacer un if considerando los contadores para jugar las 3 veces
#llamar a jugar carta pasando como parametro las cartas y mostrar la carta jugada
#llamar a ordenador y pasarle la carta jugada y mostrar la carta jugada
#hacer if con las dos cartas para sumar los contadores y decir quien gana la mano (si son iguales se le suma a los 2)

