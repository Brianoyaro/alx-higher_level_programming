#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
        try:
            size + 0
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
    def area(self):
        return (self.__size) ** 2
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        try:
            value + 0
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
