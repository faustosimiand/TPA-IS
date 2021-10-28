from abc import ABCMeta


class ui (metaclass=ABCMeta):

    def inicio(): #muestra la primer pantalla
        print("--------------------------------------")
        print("-                                    -")
        print("-                                    -")
        print("-                                    -")
        print("-          JUEGO DE TRUCO            -")        
        print("-                                    -")
        print("-                                    -")
        print("-                                    -")
        print("--------------------------------------")
        input("       PULSA ENTER PARA INGRESAR      ")

    
    def mostrarganador(ganador):
        if ganador==1:
            print("Has ganado")
        elif ganador==2:
            print("Te ha ganado la maquina :(")