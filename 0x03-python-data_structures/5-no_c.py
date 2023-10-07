#!/usr/bin/python3
def no_c(my_string):
    tmp = ''
    length = len(my_string)
    for i in range(length):
        if my_string[i] not in 'cC':
            tmp += my_string[i]
    return tmp
