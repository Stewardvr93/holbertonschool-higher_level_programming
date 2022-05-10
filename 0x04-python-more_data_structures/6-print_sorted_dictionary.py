#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for iterador in sorted(a_dictionary):
        print("{}: {}".format(iterador, a_dictionary[iterador]))
