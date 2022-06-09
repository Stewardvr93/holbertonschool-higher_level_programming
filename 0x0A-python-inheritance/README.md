![](https://pythondiario.com/wp-content/uploads/2016/10/fig108_01_0.jpg)

# 0x0A. Python - Inheritance

------------

## General

- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

------------

## List of poinst.

|  Point | What is done at this point? | level |
| ------------ | ------------ | ------------ |
| 0-lookup.py | Write a function that returns the list of available attributes and methods of an object: | Mandatory |
| 1-my_list.py | Write a class MyList that inherits from list: | Mandatory  |
| 2-is_same_class.py | Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False. | Mandatory  |
| 3-is_kind_of_class.py | Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False. | Mandatory  |
| 4-inherits_from.py | Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False. | Mandatory  |
| 5-base_geometry.py | Write an empty class BaseGeometry. | Mandatory  |
| 6-base_geometry.py | Write a class BaseGeometry (based on 5-base_geometry.py). | Mandatory  |
| 7-base_geometry.py | Write a class BaseGeometry (based on 6-base_geometry.py). | Mandatory  |
| 8-rectangle.py | Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). | Mandatory  |
| 9-rectangle.py | Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py) | Mandatory  |
| 10-square.py | Write a class Square that inherits from Rectangle (9-rectangle.py): |  Mandatory |
| 11-square.py | Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py). |  Mandatory |
| 100-my_int.py | Write a class MyInt that inherits from int: | Advanced |
| 101-add_attribute.py | Write a function that adds a new attribute to an object if it’s possible: | Advanced |

------------

## List of repository files:

|  Point | own comments.  | level |
| ------------ | ------------ | ------------ |
| 0-lookup.py | El método dir() intenta devolver una lista de atributos válidos del objeto. | Mandatory |
| 1-my_list.py | La función sorted() ordena los elementos de un iterable dado en un orden específico (ascendente o descendente) y lo devuelve como una lista. | Mandatory  |
| 2-is_same_class.py | Comparo si el typo de obj es a_class | Mandatory  |
| 3-is_kind_of_class.py | La función isinstance() comprueba si el objeto (primer argumento) es una instancia o subclase de la clase classinfo (segundo argumento). | Mandatory  |
| 4-inherits_from.py | Usamos type y isinstance para verificar. | Mandatory  |
| 5-base_geometry.py | pass hace magia | Mandatory  |
| 6-base_geometry.py | con Exeption retornamos el mensaje | Mandatory  |
| 7-base_geometry.py | Solo generamos otro metodo con validaciones de enteros. | Mandatory  |
| 8-rectangle.py | con super usamos metodos y esas cosas de otra clase | Mandatory  |
| 9-rectangle.py | Se genera un nuevo metodo area y se imprime en el str | Mandatory  |
| 10-square.py | Se genera una nueva clase llamada square y usamos super para heredar metodos de rectangle |  Mandatory |
| 11-square.py | Se imprime el mensaje requerido en el str |  Mandatory |
| 100-my_int.py | El método de tipo de objeto __eq__ compara la igualdad de dos objetos comparando su id, que es su dirección de memoria. y El método de tipo de objeto predeterminado __ne__ llamará al método __eq__ y negará su resultado, por lo que la operación __ne__ debe considerarse equivalente a !( x == y) |  Advanced |
| 101-add_attribute.py | El método hasattr() devuelve verdadero si un objeto tiene el atributo nombrado dado y falso si no lo tiene. La función setattr() establece el valor del atributo de un objeto. | Advanced |

------------

# Documentation:

### Links:

- https://docs.python.org/3/tutorial/classes.html#inheritance
- https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
- https://hub.packtpub.com/inheritance-python/
- https://www.youtube.com/watch?v=d8kCdLCi6Lk
- https://www.programiz.com/python-programming/methods/built-in/dir
- https://www.programiz.com/python-programming/methods/built-in/isinstance
- https://www.programiz.com/python-programming/methods/built-in/sorted
- https://www.programiz.com/python-programming/methods/built-in/super
- https://twiserandom.com/python/__eq__-__ne__-__lt__-__gt__-__ge__-__le__-in-python-a-tutorial/index.html#_ne
- https://www.programiz.com/python-programming/methods/built-in/hasattr
- https://www.programiz.com/python-programming/methods/built-in/setattr

------------

# Author


## Juan Sebastian Avendaño Gonzalez:
- Git: https://github.com/AvendanoisPepe
- Twitter: https://twitter.com/Sebastian_Aven
- Linkedin: https://www.linkedin.com/in/juan-sebastian-avenda%C3%B1o-gonz%C3%A1lez-8b1185200/


------------


![](https://scontent.fbog4-1.fna.fbcdn.net/v/t39.30808-6/271153206_3074657909465585_6907762404450913633_n.jpg?_nc_cat=105&_nc_rgb565=1&ccb=1-5&_nc_sid=730e14&_nc_ohc=Wm9imN7mxqAAX_DgRTy&_nc_ht=scontent.fbog4-1.fna&oh=00_AT9bMuywrpnZKR3yaTAPu-lqwQ0uJpFTGIYQPM2wabvWlg&oe=61EB1180)