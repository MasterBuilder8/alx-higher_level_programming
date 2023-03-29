#!/usr/bin/python3
"""defines a class square"""

class Square:
    """
    class Square defining a square of 'size'

    Attributes: size
    """
    def __init__(self, size=0):
        """
        create first instance of a square

        Args: size
        """
        self.__size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if type(size) != int:
                raise TypeError('size must be an integer')
            elif value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

                def area(self):
                    return self.__size ** 2
