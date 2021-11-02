from carta import cartas 
from ordenador import ordenador 
from random import randint
from abc import ABCMeta


class truco (metaclass=ABCMeta):
    def jugar():
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
                truco.mostrarmano(ucartas)
                cartajugada=truco.jugarCarta(ucartas)                              
                ucartas=truco.eliminarcarta(ucartas,cartajugada)
                cartaordenador=ordenador.ordenador_jugar(ocartas,cartajugada) 
                ocartas=truco.eliminarcarta(ocartas,cartaordenador)      
                print("Jugaste "+cartas.mostrarcarta(cartajugada)+" y el ordenador jugo "+cartas.mostrarcarta(cartaordenador))
                cartas.mostrarcarta(cartaordenador)
                if cartajugada>cartaordenador:
                    contadoruser+=1
                    print("Ganaste esta mano")
                    print("")
                elif cartaordenador>cartajugada:
                    contadorordenador+=1
                    print("la maquina gana esta mano")
                    print("")
                else:  
                    contadorordenador+=1
                    contadoruser+=1
                    print("Mano empatada")
                    print("")
        return ganador 

    #Muestra las cartas disponibles
    def mostrarmano(ucartas):
        for carta in ucartas:
            cartas.ajugar(carta)

    #Controla que el jugador juegue una carta que tenga    
    def jugarCarta(ucartas): 
        cartajugada = int(input("carta a jugar: ")) 
        while cartajugada not in ucartas:
            if cartajugada not in ucartas:
                cartajugada = int(input("Elige una carta que tengas :"))
        return cartajugada              
            
    #Elimina la carta jugada    
    def eliminarcarta(ucartas,cartajugada):
        if cartajugada==ucartas[0]: 
            ucartas.pop(0)                
            return ucartas
        if cartajugada==ucartas[1]:
            ucartas.pop(1)             
            return ucartas
        if cartajugada==ucartas[2]: 
            ucartas.pop(2)              
            return ucartas