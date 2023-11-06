#!/usr/bin/python3
"""Rectangle module
"""
mod = __import__('7-base_geometry').BaseGeometry


class Rectangle(mod):
    """Rectangle class
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """returns area of rectangle
        """
        return self.__width * self.__height
    def __str__(self):
        """returns a printable format string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
