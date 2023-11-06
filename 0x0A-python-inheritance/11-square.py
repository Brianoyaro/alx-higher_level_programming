#!/usr/bin/python3
"""square module
"""
mod = __import__('9-rectangle').Rectangle


class Square(mod):
    """square class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of square
        """
        return self.__size ** 2

    def __str__(self):
        """returns a nicely printable string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
