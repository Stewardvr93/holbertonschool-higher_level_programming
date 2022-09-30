#!/usr/bin/python3
"""script that add all arguments to a python list and save it in a file"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    lista = load_from_json_file("add_item.json")
except Exception:
    lista = []

argc = len(sys.argv)

if argc > 1:
    for iterador in range(1, argc):
        lista.append(sys.argv[iterador])
save_to_json_file(lista, "add_item.json")
