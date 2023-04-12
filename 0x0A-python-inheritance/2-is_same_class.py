#!/usr/bin/python3
"""a function that checks if an object is an instance of, or if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
    """

    if type(obj) == a_class:
        return True
    return False
