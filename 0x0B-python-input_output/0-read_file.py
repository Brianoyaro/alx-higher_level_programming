#!/usr/bin/python3
"""module that reads text
"""


def read_file(filename=""):
    """prints contents of file filename
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
