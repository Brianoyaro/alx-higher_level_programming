#!/usr/bin/python3
"""is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance or inherited from a_class\
            and returns True if so
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
