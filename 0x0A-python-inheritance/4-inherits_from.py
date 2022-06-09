#!/usr/bin/python3
"""Verifica si el obj es una instancia de una
clase que heredo de a_class"""


def inherits_from(obj, a_class):
    """Verifica si obj es o no una instancia
    que heredo de a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
