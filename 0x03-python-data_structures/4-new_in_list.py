#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = [x for x in my_list]
    if (idx < 0):
        return copy
    length = len(my_list)
    if (idx >= length):
        return copy
    else:
        for i in range(length):
            if (i == idx):
                copy[i] = element
                return copy
