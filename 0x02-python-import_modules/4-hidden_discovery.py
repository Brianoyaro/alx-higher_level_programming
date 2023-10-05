#!/usr/bin/python3
import hidden_4
if __name__ == "__main_":
    names = dir(hidden_4)
    snames = sorted(name for name in names if not name.startswith("__"))
    for name in snames:
        print(name)
