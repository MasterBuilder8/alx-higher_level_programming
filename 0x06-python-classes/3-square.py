#!/usr/bin/python3

"""defines a class square"""

class Square:
    """
    intializing the size

    Attribute: size
    """
    def __init__(self, size=0):
        """
        creating the size instation with options

        Args: size

        Raises:
        TypeError: If 'size' is not an 'int'
        ValueError: If 'size' is less than '0'
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        elif size < 0:
            raise ValueError('size must be >= 0')

        def area(self):
            """returns the current square area"""

            return self.__size ** 2
