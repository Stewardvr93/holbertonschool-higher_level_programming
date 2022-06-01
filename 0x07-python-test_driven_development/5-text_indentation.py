#!/usr/bin/python3
"""
Modulo que agrega dos lineas despues
de encontrar ciertos caracter especiales
y imprime la cadena
"""


def text_indentation(text):
    """Imprime el texto sumandole dos saltos de linea despues de
    los char especiales del for y elimina los espacios iniciales y finales
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for limite in ".:?":
        text = (limite + "\n\n").join(
            [espacios.strip(" ") for espacios in text.split(limite)]
        )
    print("{}".format(text), end="")
