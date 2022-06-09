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
