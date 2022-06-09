#!/usr/bin/python3
"""Modulo BaseGeometry que contiene
un metodo area"""


class BaseGeometry():
    """Clase BaseGeometry"""

    def area(self):
        """Genera una excepcion"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validamos el valor en el metodo publico"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
