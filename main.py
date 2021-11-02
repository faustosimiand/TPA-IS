from operator import truediv
from random import randint
import time
import os
from presentaciones import ui 
from carta import cartas #esto tiene mostrar carta y jugarCarta
from ordenador import ordenador #esto tiene ordenador_jugar


ui.inicio()
ucartas=[randint(1,14),randint(1,14),randint(1,14)]
ocartas=[randint(1,14),randint(1,14),randint(1,14)]
contadoruser=0
contadorordenador=0
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
        cartas.mostrarmano(ucartas)
        cartajugada=cartas.jugarCarta(ucartas)
        print("Jugaste: ")
        cartas.mostrarcarta(cartajugada)
        ucartas=cartas.eliminarcarta(ucartas,cartajugada)
        cartaordenador=ordenador.ordenador_jugar(ocartas,cartajugada) #probar con rich comparison
        ocartas=cartas.eliminarcarta(ocartas,cartaordenador)      
        print("el ordenador jugo: ")
        cartas.mostrarcarta(cartaordenador)
        if cartajugada>cartaordenador:
            contadoruser+=1
            print("Ganaste esta mano")
        elif cartaordenador>cartajugada:
            contadorordenador+=1
            print("la maquina gana esta mano")
        else:  
            contadorordenador+=1
            contadoruser+=1
            print("Mano empatada")
ui.mostrarganador(ganador)