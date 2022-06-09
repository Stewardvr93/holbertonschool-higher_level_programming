#!/usr/bin/python3
"""Funcion que regresa una lista.
"""


def lookup(obj):
    """Devuelve una lista de atributos y metodos
    que esten disponibles del objeto"""
    return dir(obj)
