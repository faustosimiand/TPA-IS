import unittest
from ordenador import ordenador
from truco import truco
from carta import cartas

class TestOperaciones(unittest.TestCase):  
    #probamos si el ordenador devuelve la carta para ganar 
    def test_ordenador(self): 
        esperado=14
        cartausuario=4
        cartasordenador=[1,14,1]
        actual=ordenador.ordenador_jugar(cartasordenador,cartausuario)
        self.assertEqual(actual,esperado)
    
    #probamos el eliminar carta
    def test_eliminarCarta(self):
        carta=4
        cartas=[3,2,4]
        esperado=[3,2]
        actual=truco.eliminarcarta(cartas,carta)
        self.assertEqual(actual,esperado)

    #probamos si el metodo para jugar juega la carta indicada por el usuario
    def test_cartaajugar(self):
        cartas=[1,2,14]
        cartajugada=3
        esperado=14
        actual=truco.cartaajugar(cartajugada,cartas)
        self.assertEqual(actual,esperado)

    #probamos si el metodo muestra la carta que le pasamos
    def test_mostrarCarta(self):
        carta=14
        esperado="1 de espada"
        actual=cartas.mostrarcarta(carta)
        self.assertEqual(actual,esperado)
        
if __name__ == '__main__':
    unittest.main()