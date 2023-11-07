#!/usr/bin/python3
"""module that prints to a file
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)\
            returns the number of characters written
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
