from abc import ABCMeta

class cartas (metaclass=ABCMeta):
    def mostrarcarta(carta):
        if carta == 1:
            print("4 de palos")
        elif carta == 2:
            print("5 de palos")
        elif carta == 3:
            print("6 de palos")
        elif carta == 4:
            print("7 de palos")
        elif carta == 5:
            print("10 de palos")
        elif carta == 6:
            print("11 de palos")
        elif carta == 7:
            print("12 de palos")
        elif carta == 8:
            print("1 de palos")
        elif carta == 9:
            print("2 de palos")
        elif carta == 10:
            print("3 de palos")
        elif carta == 11:
            print("7 de oro")
        elif carta == 12:
            print("7 de espada")
        elif carta == 13:
            print("1 de basto")
        elif carta == 14:
            print("1 de espada")