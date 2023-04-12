#!/usr/bin/python3
"""creating a function"""

def lookup(obj):
    """function that returns the list of available attributes and methods of an object

    Returns: a list of object
    """
    list = dir(obj)
    return list
