#!/usr/bin/python3
"""defining a funnction"""


def is_kind_of_class(obj, a_class):
    """function to check if an object is an instance of  a class"""

    if type(obj) == a_class:
        return True
    return False
