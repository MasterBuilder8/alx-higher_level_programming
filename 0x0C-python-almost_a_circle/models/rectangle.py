#!/usr/bin/python3
"""Defining the class 'Rectangle'
"""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing a rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """gets the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """gets  the x coordinate of the rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            if type(x) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """get the y coordinate of the rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            if type(y) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """returns the area value of the Rectangle instance"""
            return self.__width * self.__height

        def display(self):
            """Print the rectangle using "#" character"""
            if self.__y > 0:
                print('\n' * self.__y, end="")

            for i in range(self.__height):
                if self.__x > 0:
                    print('' * self.__x, end="")

                print('#' * self.__width)

        def __str__(self):
            """Returns the print() and str() representation of the Rectangle"""
            return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                    self.id, self.x, self.y, self.width, self.height)

        def update(self, *args, **kwargs):
            """Update the class Rectangle"""
            if args:
                self.id = args[0] if args[0] is not None else self.id
                self.width = args[1] if len(args) > 1 else self.width
                self.height = args[2] if len(args) > 2 else self.height
                self.x = args[3] if len(args) > 3 else self.x
                self.y = args[4] if len(args) > 4 else self.y
            else kwargs:
                self.id = kwargs.get("id", self.id)
                self.width = kwargs.get("width", self.width)
                self.height = kwargs.get("height", self.height)
                self.x = kwargs.get("x", self.x)
                self.y = kwargs.get("y", self.y)

        def to_dictionary(self):
            """returns the dictionary representation of a Rectangle"""
            return {
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y,
                    }

