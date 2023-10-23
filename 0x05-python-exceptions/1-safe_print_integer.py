#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for i in value:
            pass
        return False
    except TypeError:
        print("{:d}".format(value))
        return True
