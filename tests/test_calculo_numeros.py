import unittest
from unittest.mock import patch
from src.exceptions import ingrese_numero, NumeroDebeSerPositivo

class TestCalculoNumeros(unittest.TestCase):
    # Casos válidos
    @patch('builtins.input', return_value='1')
    def test_valido_1(self, mock_input):
        self.assertEqual(ingrese_numero(), 1)

    @patch('builtins.input', return_value='42')
    def test_valido_2(self, mock_input):
        self.assertEqual(ingrese_numero(), 42)

    @patch('builtins.input', return_value='999')
    def test_valido_3(self, mock_input):
        self.assertEqual(ingrese_numero(), 999)

    @patch('builtins.input', return_value='123456')
    def test_valido_4(self, mock_input):
        self.assertEqual(ingrese_numero(), 123456)

    @patch('builtins.input', return_value='5')
    def test_valido_5(self, mock_input):
        self.assertEqual(ingrese_numero(), 5)

    # Casos negativos
    @patch('builtins.input', return_value='-1')
    def test_negativo_1(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-42')
    def test_negativo_2(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-100')
    def test_negativo_3(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-999')
    def test_negativo_4(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-123456')
    def test_negativo_5(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    # Casos no numéricos
    @patch('builtins.input', return_value='abc')
    def test_no_numerico_1(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='12abc')
    def test_no_numerico_2(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='!')
    def test_no_numerico_3(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value=' ')
    def test_no_numerico_4(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='')
    def test_no_numerico_5(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()