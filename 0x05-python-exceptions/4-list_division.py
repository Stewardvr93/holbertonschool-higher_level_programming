#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divino = []
    añadir = 0
    for iterador in range(0, list_length):
        try:
            añadir = my_list_1[iterador] / my_list_2[iterador]
        except IndexError:
            print("out of range")
            añadir = 0
        except ZeroDivisionError:
            print("division by 0")
            añadir = 0
        except TypeError:
            print("wrong type")
            añadir = 0
        finally:
            divino.append(añadir)
    return (divino)
