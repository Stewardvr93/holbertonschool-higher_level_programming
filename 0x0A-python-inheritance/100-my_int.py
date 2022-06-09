#!/usr/bin/python3
"""Clase MyInt que hereda de int"""


class MyInt(int):
    """Define la clase"""

    def __eq__(self, value):
        """Igualidad"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Desigualdad"""
        return super().__eq__(value)
