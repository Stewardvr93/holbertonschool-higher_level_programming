#!/usr/bin/python3
"""
Modulo say_my_name
first_name : Primer Nombre
last_name : Segundo Nombre
"""


def say_my_name(first_name, last_name=""):
    """
    Imprime una cadena con los dos parametros de entrada.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
