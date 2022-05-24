![](https://res.cloudinary.com/practicaldev/image/fetch/s--JjLMNggV--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/ghzlcv0gkpzitutuohd3.png)

# 0x05. Python - Exceptions

------------

## General
- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

------------

## List of poinst.

|  Point | What is done at this point? | level |
| ------------ | ------------ | ------------ |
| 0-safe_print_list.py | Write a function that prints x elements of a list. | Mandatory |
| 1-safe_print_integer.py  | Write a function that prints an integer with "{:d}".format(). | Mandatory |
| 2-safe_print_list_integers.py | Write a function that prints the first x elements of a list and only integers. | Mandatory |
| 3-safe_print_division.py | Write a function that divides 2 integers and prints the result. | Mandatory |
| 4-list_division.py | Write a function that divides element by element 2 lists. | Mandatory |
| 5-raise_exception.py | Write a function that raises a type exception. | Mandatory |
| 6-raise_exception_msg.py | Write a function that raises a name exception with a message. | Mandatory |
| 100-safe_print_integer_err.py | Write a function that prints an integer. | Advanced |
| 101-safe_function.py | Write a function that executes a function safely. | Advanced |

------------

## List of repository files:

|  Point | own comments.  | level |
| ------------ | ------------ | ------------ |
| 0-safe_print_list.py | Recorremos la lista en la cual imprimimos su contenido y ponemos como exepcion pass para que no de error de compilacion. | Mandatory |
| 1-safe_print_integer.py | Simplemente usamos try donde ponemos true y expect donde ponemos false | Mandatory |
| 2-safe_print_list_integers.py | En este caso manejamos los casos de error que creemos que tendra el cod | Mandatory |
| 3-safe_print_division.py | En try hacemos la operacion, el except ponemos none si sale error, y en finally imprimimos | Mandatory |
| 4-list_division.py | Recorremos un ciclo en el cual dividimos la posicion de la lista 1 con la posicion de la lista 2 y generamos execpiones correspondientes con su mensaje | Mandatory |
| 5-raise_exception.py | Con raise lanzamos exepciones o errores | Mandatory |
| 6-raise_exception_msg.py | Usamos raise para forzar un error, en este caso NameError | Mandatory |
| 100-safe_print_integer_err.py | Redirijimos la salida del error a sys.stdeer | Advanced |
| 101-safe_function.py | Returnamos el puntero a la funcion si funciona, de resto none | Advanced |

------------

# Documentation:
### Links:

- https://docs.python.org/es/3.8/tutorial/errors.html
- https://www.programiz.com/python-programming/exception-handling
- https://www.geeksforgeeks.org/python-raise-keyword/
- https://www.youtube.com/watch?v=uqDZuHf2C8U
- https://www.tutorialspoint.com/python/python_exceptions.htm
- https://www.youtube.com/watch?v=sNTowPB4YHI
------------

# Author


## Juan Sebastian Avendaño Gonzalez:
- Git: https://github.com/AvendanoisPepe
- Twitter: https://twitter.com/Sebastian_Aven
- Linkedin: https://www.linkedin.com/in/juan-sebastian-avenda%C3%B1o-gonz%C3%A1lez-8b1185200/

------------


![](https://scontent.fbog4-1.fna.fbcdn.net/v/t39.30808-6/271153206_3074657909465585_6907762404450913633_n.jpg?_nc_cat=105&_nc_rgb565=1&ccb=1-5&_nc_sid=730e14&_nc_ohc=Wm9imN7mxqAAX_DgRTy&_nc_ht=scontent.fbog4-1.fna&oh=00_AT9bMuywrpnZKR3yaTAPu-lqwQ0uJpFTGIYQPM2wabvWlg&oe=61EB1180)