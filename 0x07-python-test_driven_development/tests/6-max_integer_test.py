#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
from curses.ascii import isdigit
import unittest
max_integer = __import__('6-max_integer').max_integer
hugo = max_integer([1, 2, 3, 4])


class TestMaxInteger(unittest.TestCase):
    """Clase que comprueba errores de max_integer
    """

    def test_Vacio(self):
        """Verificamos si la lista esta vacia"""
        resultado = max_integer()
        self.assertIsNone(resultado)

    def test_negative_number_list(self):
        """Existe la prueba de "lista de un elemento"""
        self.assertEqual(max_integer([-1]), -1)

    def test_min(self):
        """Verificamos si el resultado de la lista es correcto"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_diferent(self):
        """Verificamos que el resultado sea diferente"""
        self.assertNotEqual(max_integer([1, 2, 3, 4]), 5)

    def test_caracter(self):
        """Verificamos la captura del erro por mandar un caracter"""
        with self.assertRaises(TypeError):
            max_integer(([1, "s", 3, 4]), 4)

    def test_None(self):
        """Verificamos si mandamos un none con el type"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_false(self):
        """Verificamos si es falso"""
        self.assertFalse(isdigit(max_integer([1, 2, 3, 4])))

    def test_cadena_igual(self):
        """Verificamos que el resultado sea igual a 0"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_sumita(self):
        """Verificamos que el resultado sea igual a 20"""
        self.assertEqual(max_integer([10 + 10, 20]), 20)

    def test_mul(self):
        """Verificamos que el resultado sea igual a 100"""
        self.assertEqual(max_integer([10 * 10, 20]), 100)

    def test_Tupla(self):
        """Verificamos si mandamos una tupla el resultado debe ser 2"""
        self.assertEqual(max_integer((1, 2)), 2)

    def test_Bool(self):
        """Verificamos si mandamos un True debe generar un TypeError"""
        with self.assertRaises(TypeError):
            max_integer(True, False)

    def test_multilistas(self):
        """Verificamos una lista de listas"""
        self.assertEqual(max_integer([[1, 2, 3], [4, 5, 6, 7]]), [4, 5, 6, 7])

    def test_negativo(self):
        """Verificamos si el numero"""
        self.assertEqual(max_integer([-100, -2, -3, -4]), -2)

    def test_huge_number(self):
        """Comprobamos un numero muy grande"""
        self.assertEqual(max_integer([126, 1e1010]), 1e1010)

    def test_tiny_number(self):
        """Comprobamos con un numero pequeño"""
        self.assertEqual(max_integer([-126, 1e-1010]), 0.0)

    def test_float(self):
        """Comprobamos una lista de enteros y flotantes"""
        self.assertEqual(max_integer([3, 7.9, 5]), 7.9)

    def test_Parametro(self):
        """Verificamos un parametro que no es una lista"""
        with self.assertRaises(TypeError):
            max_integer(90)

if __name__ == '__main__':
    unittest.main()
