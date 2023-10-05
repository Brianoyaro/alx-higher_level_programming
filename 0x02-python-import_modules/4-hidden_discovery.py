#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    ls = dir(hidden_4)
    for i in ls:
        if i[0] != '_' and i[1] != '_':
            print(i)
