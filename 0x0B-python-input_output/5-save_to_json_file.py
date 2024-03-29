#!/usr/bin/python3
"""
Contains the function "json_file"
"""

import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
