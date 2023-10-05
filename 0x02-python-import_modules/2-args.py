#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    length = len(arguments)
    if (length == 1):
        print("0 arguments.")
    elif (length == 2):
        print("1 argument:")
        print("{}: {}".format(length,arguments[1]))
    elif (length > 2):
        print("{} arguments:".format(length - 1))
        for i, value in enumerate(arguments):
            if (i == 0):
                continue
            print("{}: {}".format(i, value))
