#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return (fct(*args))
    except Exception as mensaje:
        print("Exception: {}".format(mensaje), file=sys.stderr)
        return (None)
