#!/usr/bin/python3
"""Module defining a rectangle
"""


class Rectangle:
    """defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """initialises an object

            Arguments:
                width (optional): first argument
                height (optional): second argument
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """returns with from private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width attribute with value if\
            it is an integer greater than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns height which is a private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute with value\
            if it is an integer greater than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    
    def area(self):
        """returns arrea of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
