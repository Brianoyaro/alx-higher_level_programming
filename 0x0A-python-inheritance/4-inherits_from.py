#!/usr/bin/python3
"""inherits_from module
"""


def inherits_from(obj, a_class):
    """checks if obj is an instance or inherited from a_class\
            and returns True if so
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
