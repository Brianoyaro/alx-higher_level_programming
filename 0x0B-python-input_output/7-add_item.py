#!/usr/bin/python3
"""module that adds all arguments to a Python list\
        then save them to a file
"""
to_json = __import__('5-save_to_json_file').save_to_json_file
from_json = __import__('6-load_from_json_file').load_from_json_file
import sys


filename = "add_item.json"
args = sys.argv
value = ''
for i, val in  enumerate(args):
    if i != 0:
        value += val
to_json(list(value), filename)

