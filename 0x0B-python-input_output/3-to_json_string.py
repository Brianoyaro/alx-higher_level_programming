#!/usr/bin/python3
"""to JSON module
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of my_obj
    """
    value = json.dumps(my_obj)
    return value
