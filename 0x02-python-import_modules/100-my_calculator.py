#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    if (len(args) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    symbols = ['+', '-', '*', '/']
    if (args[2] not in symbols):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(args[1])
        b = int(args[3])
        if (args[2] == '+'):
            c = add(a, b)
            print("{} + {} = {}".format(a, b, c))
        if (args[2] == '-'):
            c = sub(a, b)
            print("{} - {} = {}".format(a, b, c))
        if (args[2] == '*'):
            c = mul(a, b)
            print("{} * {} = {}".format(a, b, c))
        if (args[2] == '/'):
            c = div(a, b)
            print("{} / {} = {}".format(a, b, c))
