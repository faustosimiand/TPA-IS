from abc import ABCMeta


class cartas (metaclass=ABCMeta):  
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
        