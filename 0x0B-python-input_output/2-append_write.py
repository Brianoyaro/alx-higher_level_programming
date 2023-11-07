#!/usr/bin/python3
"""module that appends test
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)\
            returns the number of characters added
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
