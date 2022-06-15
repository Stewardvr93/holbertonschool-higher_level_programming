#!/usr/bin/python3
"""Modulo que define la clase rectangulo"""
from models.base import Base


class Rectangle(Base):
    """Define metodos de Rectangle que heredan
    de base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returna el valor ancho de la instancia"""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el valor y lo valida"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returna el valor largo de la instancia"""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el valor y lo valida"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returna el valor x de la instancia"""
        return self.__x

    @x.setter
    def x(self, value):
        """Establece el valor y lo valida"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returna el valor y de la instancia"""
        return self.__y

    @y.setter
    def y(self, value):
        """Establece el valor y lo valida"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calcula el area del rectangulo instanciado"""
        return (self.__width * self.__height)

    def display(self):
        """Imprime una representancion de un rectangulo
        con el caracter #"""
        print('\n' * self.y, end="")
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Imprime la descripcion de un rectangulo"""
        mensajito = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        return mensajito

    def update(self, *args, **kwargs):
        """Actualiza los atributos de la instancia"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returna un diccionario de rectangle"""
        diccionarito = {"id": self.id, "width": self.width,
                        "height": self.height, "x": self.x, "y": self.y}
        return diccionarito
