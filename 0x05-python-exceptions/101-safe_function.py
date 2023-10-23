#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        val = fct(*args)
        return val
    except Exception as es:
        print("Exception:", es, file=sys.stderr)
        return None
