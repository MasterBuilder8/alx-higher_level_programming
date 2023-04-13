#!/usr/bin/python3
"""Module to define subclass"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class which inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """instantiation of width and height"""
        self.integer_validator("width", self.__width)
        self.__width = width
        self.integer_validator("height", self.__height)
        self.__height = height

        def area(self):
            """computes the area of the Rectangle instance"""
            return self.__width * self.__height

        def __str__(self):
            """returns the string to print"""
            return "[Rectangle] {}/{}".format(self.__width, self.__height)
