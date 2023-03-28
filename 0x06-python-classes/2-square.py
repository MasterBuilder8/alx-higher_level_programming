#!/usr/bin/python3
"""define class square"""

class square:
    """ definea square by size"""

    def __init__(self, size=0):
        """
        the __init__ method initializes the size of a square
        arg: size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
