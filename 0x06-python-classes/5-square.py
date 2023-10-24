#!/usr/bin/python3


"""
module containing Square class
"""


class Square:
    """
    A Square class

    Attributes:
        size: private instance attribute of the square created
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise ValueError("size must be >= 0")
        elif size < 0:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise ValueError("size must be >= 0")
        elif value < 0:
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    """
    public instance returning square's current area
    """
    def area(self):
        return (self.__size) ** 2

    """
    public instance that  prints in stdout the square with the character #
    """
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print(self.__size * '#')
