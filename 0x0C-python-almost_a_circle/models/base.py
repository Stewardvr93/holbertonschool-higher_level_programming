#!/usr/bin/python3
"""Clase base que servira para todo el proyecto"""
import json
import csv


class Base():
    """La idea es evitar duplicidad de
    datos en las clases futuras"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Inicializacion de atributos del objeto base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Obtenemos la forma de un Objeto JSON
        en forma de cadena"""
        if not list_dictionaries or list_dictionaries == [None]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Crea un archivo .json con una cadena de
        bibliotecas"""
        lista = []
        if list_objs is not None and len(list_objs) > 0:
            for objeto in list_objs:
                lista.append(objeto.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as myfile:
            myfile.write(Base.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """Devuelve la lista de la representación de cadena JSON"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returna una instancia con todos los
        atributos establecidos"""
        if cls.__name__ == 'Rectangle':
            ficti = cls(1, 1)
        elif cls.__name__ == 'Square':
            ficti = cls(1)
        ficti.update(**dictionary)
        return ficti

    @classmethod
    def load_from_file(cls):
        """Leemos el archivo a crear y recorremos
        el contenido para usar el metodo create"""
        try:
            with open(cls.__name__ + ".json", "r") as myfile:
                leer = myfile.read()
                lista_dicci = cls.from_json_string(leer)
                listas = []
                for lis in lista_dicci:
                    listas.append(cls.create(**lis))
                return listas
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Creamos un archivo .csv y le agregamos
        su contenido"""
        linea = []
        with open(cls.__name__ + ".csv", "w") as myfile:
            if list_objs is None or len(list_objs) <= 0:
                myfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    linea = ["id", "width", "height", "x", "y"]
                if cls.__name__ == 'Square':
                    linea = ["id", "size", "x", "y"]
            var = csv.DictWriter(myfile, fieldnames=linea)
            for iterador2 in list_objs:
                var.writerow(iterador2.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Lee la funcion save"""
        try:
            with open(cls.__name__ + ".csv", "r") as myfile:
                if cls.__name__ == 'Rectangle':
                    linea = ["id", "width", "height", "x", "y"]
                if cls.__name__ == 'Square':
                    linea = ["id", "size", "x", "y"]
                readeer = csv.DictReader(myfile, fieldnames=linea)
                dcts = [dict([clave, int(valor)]
                        for clave, valor in ltera.items())
                        for ltera in readeer]
                return [cls.create(**dicci) for dicci in dcts]
        except Exception:
            return []
