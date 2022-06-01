#!/usr/bin/python3
"""
Modulo para imprimir un cuadrado
con el caracter #
Size es el tamaño de cada lado
"""


def print_square(size):
    """
    Funcion que imprime un cuadrado con size osea el argumento.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not float and size < 0:
        raise TypeError("size must be an integer")
    for filas in range(0, size):
        for columnas in range(0, size):
            print("#", end="")
        print("")
