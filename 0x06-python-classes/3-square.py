#!/usr/bin/python3


"""
Module containing Square Class
"""


class Square:
    """
    
    A square class

    Attributes:
        size: private instance attribute representing square size
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
    public instance method returning current square's area
    """
    def area(self):
        return (self.__size) ** 2
