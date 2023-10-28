#!/usr/bin/python3
"""
    module that prints a square with the character #.
"""
def print_square(size):
    """
    function that prints a square #-ed

    Args:
        size: size of square

    Return:
        #-ed [size] square
    """
    if (not isinstance(size, int)) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    else:
        for i in range(size):
            print('#' * size)
