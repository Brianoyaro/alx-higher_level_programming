#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ln1 = len(tuple_a)
    ln2 = len(tuple_b)
    if (ln1 == 0):
        a = 0
        b = 0
    elif (ln1 == 1):
        a = tuple_a[0]
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]
    if (ln2 == 0):
        c = 0
        d = 0
    elif (ln2 == 1):
        c = tuple_b[0]
        d = 0
    else:
        c = tuple_b[0]
        d = tuple_b[1]
    return (a + c, b + d)
