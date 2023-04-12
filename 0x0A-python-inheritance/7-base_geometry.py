#!/usr/bin/python3
"""defining an empty class"""



class BaseGeometry:
    """Empty Class"""
    def area(self):
        """Method raise Exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates value

        Raise:
        TypeError
        ValueError
        """
        if type(value) is not int:
            raise TypeError(name + 'must be an integer')
        if value <= 0:
            raise ValueError(name + 'must be greater than 0')
