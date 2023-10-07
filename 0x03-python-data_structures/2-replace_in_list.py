#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0):
        return my_list
    length = len(my_list)
    if (idx >= length):
        return my_list
    else:
        for i in range(length):
            if (i == idx):
                my_list[i] = element
                return my_list
