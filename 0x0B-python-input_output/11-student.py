#!/usr/bin/python3
"""Student to JSON module
"""


class Student:
    """student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple data structure\
                for JSON serialization of an object
        """
        if attrs is None:
            return self.__dict__

        else:
            val = {}
            for i in attrs:
                for key, value in self.__dict__.items():
                    if key == i:
                        val[i] = value
                        break
            return val

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance:
        """
        for key in json:
            self.__dict__[key] = json[key]
