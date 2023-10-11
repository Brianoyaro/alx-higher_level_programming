#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ls = []
    for key,val in a_dictionary.items():
        if val == value:
            ls.append(key)
    for i in range(len(ls)):
        a_dictionary.pop(ls[i])
    return a_dictionary
