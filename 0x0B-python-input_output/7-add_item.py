#!/usr/bin/python3
"""
script that adds all arguments to a Python list, then save them to a file
"""

import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load(filename)
except FileNotFoundError:
    json_list = []

    for arg in argv[1]:
        json_list.append(arg)

        save(json_list, filename)
