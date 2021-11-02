from presentaciones import ui 
from truco import truco

ui.inicio()
ganador=truco.jugar()
ui.mostrarganador(ganador)