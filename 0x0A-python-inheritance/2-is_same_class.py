#!/usr/bin/python3
"""Se compara un objeto con una instacia"""


def is_same_class(obj, a_class):
    """Returna verdadero si el obj es una
    instancia de la clase, si no falso"""
    return type(obj) is a_class
