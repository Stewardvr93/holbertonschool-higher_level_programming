#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    multi = 0
    divi = 0
    for iterador in my_list:
        multi = multi + (iterador[0] * iterador[1])
        divi = divi + (iterador[1])
    return (multi / divi)
