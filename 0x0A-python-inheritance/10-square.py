#!/usr/bin/python3
"""Modulo Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Clase Square que hereda de la la clase
    Rectangle"""

    def __init__(self, size):
        """Genera una instancia"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
