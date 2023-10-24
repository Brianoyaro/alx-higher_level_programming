#!/usr/bin/python3

"""module containing Square class. Also defines private instance attribute size"""


class Square:
    """square class with private instance attribute size"""
    def __init__(self, size):
        """
        __init__ function that initialises the class

        Arguments:
            size: An integer representing square size
        """
        self.__size = size
