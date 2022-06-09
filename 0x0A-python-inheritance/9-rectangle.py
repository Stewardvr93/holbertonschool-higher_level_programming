#!/usr/bin/python3
"""Modulo Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clase Rectangle que hereda de la la clase
    BaseGeometry"""

    def __init__(self, width, height):
        """Genera una instancia de un rectangulo"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula el area de la instancia del rectangulo"""
        return self.__width * self.__height

    def __str__(self):
        """Returna el mensaje requerido"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
