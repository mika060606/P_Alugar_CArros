import unittest

from carros_utils import filtrar_carros


class FiltrarCarrosTests(unittest.TestCase):
    def test_filtra_por_texto_e_ordena_por_preco(self):
        carros = [
            type('Carro', (), {'modelo': 'Civic', 'localizacao': 'Lisboa', 'valor': 80, 'classificacao': '5', 'ano': 2021})(),
            type('Carro', (), {'modelo': 'Focus', 'localizacao': 'Porto', 'valor': 50, 'classificacao': '4', 'ano': 2020})(),
            type('Carro', (), {'modelo': 'Golf', 'localizacao': 'Lisboa', 'valor': 60, 'classificacao': '5', 'ano': 2022})(),
        ]

        resultado = filtrar_carros(carros, 'lisboa', 'preco')

        self.assertEqual([carro.modelo for carro in resultado], ['Golf', 'Civic'])

    def test_filtra_por_preco_ano_modelo_localidade_e_classificacao(self):
        carros = [
            type('Carro', (), {'modelo': 'Civic', 'localizacao': 'Lisboa', 'valor': 80, 'classificacao': '5', 'ano': 2021})(),
            type('Carro', (), {'modelo': 'Focus', 'localizacao': 'Porto', 'valor': 50, 'classificacao': '4', 'ano': 2020})(),
            type('Carro', (), {'modelo': 'Golf', 'localizacao': 'Lisboa', 'valor': 60, 'classificacao': '5', 'ano': 2022})(),
        ]

        resultado = filtrar_carros(
            carros,
            '',
            '',
            {
                'min_preco': '60',
                'max_preco': '90',
                'ano': '2021',
                'modelo': 'civic',
                'localidade': 'lisboa',
                'classificacao': '5',
            },
        )

        self.assertEqual([carro.modelo for carro in resultado], ['Civic'])


if __name__ == '__main__':
    unittest.main()
