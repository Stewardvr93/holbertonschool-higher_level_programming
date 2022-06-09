#!/usr/bin/python3
"""Modulo de add_attribute"""


def add_attribute(obj, atributo, value):
    """Comparamos el obj con dict para
    verificar si sale false es xq no es posible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, atributo, value)
