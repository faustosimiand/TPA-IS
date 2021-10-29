from operator import truediv
from random import randint
import time
import os
from presentaciones import ui 
from carta import cartas #esto tiene mostrar carta y jugarCarta
from ordenador import ordenador #esto tiene ordenador_jugar


ui.inicio()
ucartas=[10,randint(1,14),randint(1,14)]
ocartas=[3,10,randint(1,14)]
cartas.ajugar(ucartas[0])
cartas.ajugar(ucartas[1])
cartas.ajugar(ucartas[2])
contadoruser=1
contadorordenador=1
ganador=0 #1 si es user,2 si es ordenador
jugando=True
while jugando==True:
    if contadoruser==2:
        jugando=False
        ganador=1
    elif contadorordenador==2:
        jugando=False
        ganador=2
    else:
        cartajugada=cartas.jugarCarta(ucartas) 
        cartas.mostrarcarta(cartajugada)
        cartaordenador=ordenador.ordenador_jugar(cartajugada,ocartas) #probar con rich comparison
        if cartajugada>cartaordenador:
            contadoruser+=1
            print("Ganaste esta mano")
        elif cartaordenador>cartajugada:
            contadorordenador+=1
            print("la maquina gana esta mano")
        else:  
            contadorordenador+=1
            contadoruser+=1
            print("Empate")
ui.mostrarganador(ganador)





#hacer un if considerando los contadores para jugar las 3 veces
#llamar a jugar carta pasando como parametro las cartas y mostrar la carta jugada
#llamar a ordenador y pasarle la carta jugada y mostrar la carta jugada
#hacer if con las dos cartas para sumar los contadores y decir quien gana la mano (si son iguales se le suma a los 2)

