#!/usr/bin/python3
"""module writing object to a text file ini Json convention
"""
import json


def save_to_json_file(my_obj, filename):
    """module writing object to a text file ini Json convention
    """
    with open(filename, "w", encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
