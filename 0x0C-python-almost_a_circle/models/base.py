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

    @staticmethod
    def from_json_string(json_string):
        """eturns the list of the JSON string representation json_string
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        dummy = cls(1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        dummy = cls(1, 2, 3)
        if dummy.width == dummy.height:
            filename = 'Square.json'
        else:
            filename = 'Rectangle.json'
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_objs))
