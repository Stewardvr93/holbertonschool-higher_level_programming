#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square():
    """Inicializando la funcion inicial.
    """

    def __init__(self, size=0):
        """controlamos las exepciones
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returnamos el valor de la operacion"""
        self.area = self.__size ** 2
        return (self.area)
