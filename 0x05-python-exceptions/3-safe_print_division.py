#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        dividemeEsta = a / b
    except(ZeroDivisionError):
        dividemeEsta = None
    finally:
        print("Inside result: {}".format(dividemeEsta))
    return (dividemeEsta)
