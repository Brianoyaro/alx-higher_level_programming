#!/usr/bin/python3


"""
module containing Square class
"""


class Square:
    """
    A Square class

    Attributes:
        size: private instance attribute of the square created
        position: private instance attribute of the square created
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise ValueError("size must be >= 0")
        elif size < 0:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
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
                if self.position[1] > 0:
                    print(" " * self.__position[1], end='')
                else:
                    print(" " * self.__position[0], end='')
                print(self.__size * '#')
