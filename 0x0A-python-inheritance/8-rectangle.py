#!/usr/bin/python3
"""Module to define a subclass"""

BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherites from BaseGeometry class
    
    Attributes:
    width and height
    """
def __init__(self, width, height):
    """instantiation of width and height"""
    self.integer_validator("width", self.__width)
    self.integer_validator("height", self.__height)
    self.__width = width
    self.__height = height
