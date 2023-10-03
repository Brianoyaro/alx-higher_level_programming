#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if n in range(97, 123):
            n -= 32
        v = chr(n)
        print("{}".format(v), end='')
    print()
