#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key,value in a_dictionary.items():
        buf = value * 2
        new.update({key : buf})
    return new
