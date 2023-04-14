#!/usr/bin/python3
"""
Contains the function "load_from_json_file"
"""


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)