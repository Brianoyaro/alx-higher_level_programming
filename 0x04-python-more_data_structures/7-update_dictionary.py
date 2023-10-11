#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return None
    else:
        temp = {key: value}
        return a_dictionary.update(temp)
