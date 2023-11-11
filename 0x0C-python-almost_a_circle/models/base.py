#!/usr/bin/python3
"""base module
"""
import json
import os


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
        """writes the JSON string representation of list_objs to a file
        """
        to_dict_list = []
        # change list instancces in list_objs to json serializable
        for val in list_objs:
            to_dict_list.append(val.to_dictionary())

        # filename as a class attribute else use '{}.json.format(cls.__name__)
        filename = cls.filename_json

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(to_dict_list))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = cls.filename_json
        if os.path.isfile(filename):
            with open(filename, mode='r', encoding='utf-8') as f:
                temp = f.read()
            # list_of_instances = json.loads(temp)
            list_of_instances = cls.from_json_string(temp)
            final_list = []
            for val in list_of_instances:
                dummy = cls.create(**val)
                final_list.append(dummy)
            return final_list
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv
        """
        filename = cls.filename_csv
        list_dict = []
        # save every instance of list_objs to json serializable
        for val in list_objs:
            value = val.to_dictionary()
            list_dict.append(value)
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(list_dict))

    @classmethod
    def load_from_file_csv(cls):
        """deserialises csv file data
        """
        # filename ca also be found using 'cls.__name__
        filename = cls.filename_csv
        if os.path.isfile(filename):
            with open(filename, mode='r', encoding='utf-8') as f:
                temp = f.read()

            start_list = json.loads(temp)
            final_list = []
            for val in start_list:
                dummy = cls.create(**val)
                final_list.append(dummy)
            return final_list
        else:
            return []
