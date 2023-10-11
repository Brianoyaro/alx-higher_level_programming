#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not a_dictionary:
        return None
    return a_dictionary.update({key:value})
