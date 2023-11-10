#!/usr/bin/python3
"""base module
"""
import json


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

    @staticmethod        
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)
