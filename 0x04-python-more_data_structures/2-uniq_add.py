#!/usr/bin/python3
def uniq_add(my_list=[]):
    sinLosColados = []
    for iterador in my_list:
        if iterador not in sinLosColados:
            sinLosColados.append(iterador)
    return (sum(sinLosColados))
