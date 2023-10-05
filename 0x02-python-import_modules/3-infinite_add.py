#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    summ = 0
    for i, value in enumerate(args):
        if (i == 0):
            continue
        summ += int(value)
    print(summ)
