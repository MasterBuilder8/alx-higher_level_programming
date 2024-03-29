#!/usr/bin/python3
"""
This  module  contains the "Square" class
"""


from module.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the class Square"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                    elif a == 1:
                        self.size = arg
                    elif a == 2:
                        self.x = arg
                    elif a == 3:
                        self.y = arg
                    a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                    elif k == "size":
                        self.size = v
                    elif k == "x":
                        self.x = v
                    elif k = "y":
                        self.y = v


    def __str__(self):
        """Return the print() and str () representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y,
                }
