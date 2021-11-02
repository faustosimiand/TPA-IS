from abc import ABCMeta


class ui (metaclass=ABCMeta):

    def inicio(): #muestra la primer pantalla
        print("---------------------------------------")
        print("-                                     -")       
        print("-           JUEGO DE TRUCO            -")        
        print("-                                     -")         
        input("-------PULSA ENTER PARA INGRESAR-------")

    
    def mostrarganador(ganador):
        if ganador==1:
            print("---------------------------------------")
            print("-                                     -")        
            print("-             HAS GANADO              -")        
            print("-                                     -")                     
            print("---------------------------------------")
        elif ganador==2:
            print("---------------------------------------")
            print("-                                     -")        
            print("-       TE GANO LA MAQUINA XD         -")        
            print("-                                     -")                     
            print("---------------------------------------")