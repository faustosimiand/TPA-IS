from presentaciones import ui 
from truco import truco

ui.inicio()
print("")
ganador=truco.jugar()
print("")
ui.mostrarganador(ganador)