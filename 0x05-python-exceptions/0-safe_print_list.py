#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    contador = 0
    for iterador in range(0, x):
        try:
            print("{:d}".format(my_list[iterador]), end="")
            contador = contador + 1
        except:
            pass
    print()
    return(contador)
