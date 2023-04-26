#!/usr/bin/python3
"""writing a function that returns the addition of two ints/floats"""


def add_integer(a, b=98):
    """function that takes two ints/floats


    Args: a, b

    Raises: TypeError if items are not int/float

    Retuns: sum of a + b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if isinstance(a, float):
        a = int(a)
        if isinstance(b, float):
            b = int(b)

            return a + b
