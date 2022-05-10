#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        valor = 0
        clave = ""
        for iterador in a_dictionary:
            if a_dictionary[iterador]:
                if a_dictionary[iterador] > valor:
                    valor = a_dictionary[iterador]
                    clave = iterador
        if clave not in a_dictionary:
            return ("None")
        else:
            return (clave)
