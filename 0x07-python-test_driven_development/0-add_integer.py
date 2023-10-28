#!/usr/bin/python3
'''Integer addition module
'''
def add_integer(a, b=98):
    """ function that adds two numbers

    Args:
        a: first parameter
        b(optional): second parameter

    Return:
        a + b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
