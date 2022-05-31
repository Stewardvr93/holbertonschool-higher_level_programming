#!/usr/bin/python3
"""
Modulo para dividir una matrix
Divide cada elemento de una matrix
de números por un número
"""


def matrix_divided(matrix, div):
    """
    Función que divide todos los elementos de una matriz
    """
    nuevo = []
    error = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    if len(matrix) > 0:
        tamaño = len(matrix[0])
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        elif div == 0:
            raise ZeroDivisionError("division by zero")
        for iterador in matrix:
            filas = []
            if len(iterador) != tamaño:
                raise TypeError(error2)
            for iterador2 in iterador:
                if isinstance(iterador2, (int, float)):
                    filas.append(round(iterador2 / div, 2))
                else:
                    raise TypeError(error)
            nuevo.append(filas)
    return nuevo
