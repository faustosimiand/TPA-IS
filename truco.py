from carta import cartas 
from ordenador import ordenador 
import random
from abc import ABCMeta


class truco (metaclass=ABCMeta):
    def jugar():
        listacartas=(1,1,1,1,2,2,2,2,3,3,3,3,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,9,9,9,9,10,10,10,10,11,12,13,14)
        maso=random.sample(listacartas,6)
        ucartas=[maso[0],maso[1],maso[2]]
        ocartas=[maso[3],maso[4],maso[5]]
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
                pos=truco.jugarCarta(ucartas)
                cartajugada=truco.cartaajugar(pos,ucartas)                            
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
        numero=1
        for carta in ucartas:
            print(str(numero)+": "+cartas.mostrarcarta(carta))
            numero=numero+1

    #Controla que el jugador juegue una carta que tenga    
    def jugarCarta(ucartas):
        bool=False 
        cartajugada = int(input("carta a jugar: ")) 
        while bool==False:
            if cartajugada==1:
                bool=True   
                return cartajugada
            if cartajugada==2:
                bool=True   
                return cartajugada  
            if cartajugada==3:
                bool=True   
                return cartajugada
            else:
                cartajugada = int(input("Ingrese 1,2 o 3: "))

                        
            
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
    
    def cartaajugar(cartajugada,ucartas): 
        if cartajugada==1: 
            return ucartas[0]
        if cartajugada==2:                         
            return ucartas[1]
        if cartajugada==3:                           
            return ucartas[2]