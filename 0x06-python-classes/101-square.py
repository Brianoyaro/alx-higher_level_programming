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
        if isinstance(position, tuple) and isinstance(position[0], int) and isinstance(position[1], int) and position[0] >= 0 or position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and (len(value) == 2) and isinstance(value[0], int) and isinstance(value[1], int) and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
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
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print((" " * self.__position[0]) + ("#" * self.__size))
    def __str__(self):
        val = ""
        if self.__size == 0:
            return val
        val += "{}".format('\n' * self.position[1])
        val += "{}".format('\n'.join([" " * self.__position[0] + "#" * self.size] * self.__size))
        return val
