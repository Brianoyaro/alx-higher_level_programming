#!/usr/bin/python3
"""base module
"""


class Base:
    """base class for entire package
    """
    __nb_objects = 0
    """__nb_objects: private class attribute
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
