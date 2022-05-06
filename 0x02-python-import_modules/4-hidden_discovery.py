#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arreglo = dir()
    for iterador in range(0, len(arreglo)):
        if arreglo[iterador][0:2] != "__":
            print("{}".format(arreglo[iterador]))
