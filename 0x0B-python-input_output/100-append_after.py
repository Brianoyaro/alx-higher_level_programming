#!/usr/bin/python3
"""module performing search for a string and updates consecutive line
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a specific string
    """
    with open(filename, encoding='utf-8') as f:
        ls=[]
        for line in f:
            ls.append(line)

    string = ''
    for i, line in enumerate(ls):
        if search_string in line:
            string += line
            string += new_string
            string += new_string
        else:
            string += line
 
    with open(filename, "w", encoding="utf-8") as f:
        f.write(string)
