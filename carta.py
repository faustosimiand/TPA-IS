from abc import ABCMeta


class cartas (metaclass=ABCMeta):

        def ajugar(carta):
            if carta == 1:
                print("pulse 1 para jugar 4 de palos")
            elif carta == 2:
                print("pulse 2 para jugar 5 de palos")
            elif carta == 3:
                print("pulse 3 para jugar 6 de palos")
            elif carta == 4:
                print("pulse 4 para jugar 7 de palos")
            elif carta == 5:
                print("pulse 5 para jugar 10 de palos")
            elif carta == 6:
                print("pulse 6 para jugar 11 de palos")
            elif carta == 7:
                print("pulse 7 para jugar 12 de palos")
            elif carta == 8:
                print("pulse 8 para jugar 1 de palos")
            elif carta == 9:
                print("pulse 9 para jugar 2 de palos")
            elif carta == 10:
                print("pulse 10 para jugar 3 de palos")
            elif carta == 11:
                print("pulse 11 para jugar 7 de oro")
            elif carta == 12:
                print("pulse 12 para jugar 7 de espada")
            elif carta == 13:
                print("pulse 13 para jugar 1 de basto")
            elif carta == 14:
                print("pulse 14 para jugar 1 de espada")
        
     

        def mostrarcarta(carta):
            if carta == 1:
                return "4 de palos"
            elif carta == 2:
                return "5 de palos"
            elif carta == 3:
                return "6 de palos"
            elif carta == 4:
                return "7 de palos"
            elif carta == 5:
                return "10 de palos"
            elif carta == 6:
                return "11 de palos"
            elif carta == 7:
                return "12 de palos"
            elif carta == 8:
                return "1 de palos"
            elif carta == 9:
                return "2 de palos"
            elif carta == 10:
                return "3 de palos"
            elif carta == 11:
                return "7 de oro"
            elif carta == 12:
                return "7 de espada"
            elif carta == 13:
                return "1 de basto"
            elif carta == 14:
                return "1 de espada"
        