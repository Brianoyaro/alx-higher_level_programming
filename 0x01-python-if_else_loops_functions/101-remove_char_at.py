#!/usr/bin/python3
def remove_char_at(str, n):
    n = str[:n] + str[n + 1:]
    return n
