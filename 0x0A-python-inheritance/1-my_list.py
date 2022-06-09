#!/usr/bin/python3
"""MyList hereda una lista"""


class MyList(list):
    """MyList hereda una lista"""

    def print_sorted(self):
        """Imprime la lista ordenadamente"""
        print(sorted(self))
