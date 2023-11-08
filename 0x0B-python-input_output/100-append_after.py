#!/usr/bin/python3
"""module performing search for a string and updates consecutive line
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text after each line containing a specific string
    """
    temp = ''
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if search_string in line:
                temp += line + new_string
            else:
                temp += line

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(temp)
