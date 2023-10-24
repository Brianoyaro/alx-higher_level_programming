#!/usr/bin/python3


"""Square class"""



class Square:
    """
    Square class

    Arguments:
    size: private instance attribute representing square size
    """
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
