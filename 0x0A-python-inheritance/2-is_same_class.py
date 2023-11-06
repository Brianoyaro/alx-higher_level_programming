#!/usr/bin/python3
"""is_same_class module
"""


def is_same_class(obj, a_class):
    """checks if obj is an insatnce of a_class and \
            returns True if so
    """
    if type(obj) == a_class:
        return True
    else:
        return False
