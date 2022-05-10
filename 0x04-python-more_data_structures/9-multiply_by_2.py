#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nuevoDi = {}
    for iterador in a_dictionary:
        nuevoDi[iterador] = a_dictionary[iterador] * 2
    return (nuevoDi)
