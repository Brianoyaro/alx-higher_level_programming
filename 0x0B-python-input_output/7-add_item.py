#!/usr/bin/python3
"""module that adds all arguments to a Python list\
        then save them to a file
"""
import sys
import os
to_json = __import__('5-save_to_json_file').save_to_json_file
from_json = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
if os.path.exists(filename):
    val = from_json(filename)
    val += sys.argv[1:]
    to_json(list(val), filename)

else:
    to_json(sys.argv[1:], filename)
