import unittest

from carros_utils import filtrar_carros


class FiltrarCarrosTests(unittest.TestCase):
    def test_filtra_por_texto_e_ordena_por_preco(self):
        carros = [
            type('Carro', (), {'modelo': 'Civic', 'localizacao': 'Lisboa', 'valor': 80, 'classificacao': '5'})(),
            type('Carro', (), {'modelo': 'Focus', 'localizacao': 'Porto', 'valor': 50, 'classificacao': '4'})(),
            type('Carro', (), {'modelo': 'Golf', 'localizacao': 'Lisboa', 'valor': 60, 'classificacao': '5'})(),
        ]

        resultado = filtrar_carros(carros, 'lisboa', 'preco')

        self.assertEqual([carro.modelo for carro in resultado], ['Golf', 'Civic'])


if __name__ == '__main__':
    unittest.main()
