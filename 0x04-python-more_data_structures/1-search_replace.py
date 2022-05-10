#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        lista = my_list.copy()
        acumulador = 0
        for iterador in my_list:
            if iterador == search:
                lista[acumulador] = replace
            acumulador += 1
    else:
        lista = my_list
    return lista
