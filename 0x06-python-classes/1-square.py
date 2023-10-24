#!/usr/bin/python3

"""module containing Square class. Also defines private instance attribute size"""


class Square:
    """square class with private instance attribbute size"""
    def __init__(self, size):
        """__init__ function that initialises the class"""
        self.__size = size
