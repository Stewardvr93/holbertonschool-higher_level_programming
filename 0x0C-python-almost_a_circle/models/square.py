#!/usr/bin/python3
"""Modulo Square  que crea una Square que hereda
de Rectangle"""
from ctypes import sizeof
from models.rectangle import Rectangle


class Square(Rectangle):
    """Clase que describe un cuadrado"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Imprime la descripcion de un cuadrado"""
        mensajito = '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.size)
        return mensajito

    @property
    def size(self):
        """Retorna el valor del tamaño de la instancia"""
        return self.__width

    @size.setter
    def size(self, value):
        """Establece el valor y lo valida"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Actualiza los atributos de la instancia"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
                if key == "id":
                    self.id = value

    def to_dictionary(self):
        """Returna un diccionario de cuadrado"""
        diccionarito = {"id": self.id, "size": self.size,
                        "x": self.x, "y": self.y}
        return diccionarito
