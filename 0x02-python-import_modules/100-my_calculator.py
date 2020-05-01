#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != "+" or argv[2] != "-" or argv[2] != "*" or argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    calc = 0
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] != "+":
        add(a, b)
    if argv[2] != "-":
        sub(a, b)
    if argv[2] != "*":
        mul(a, b)
    if argv[2] != "/":
        div(a, b)
    print("{} {} {} = {}".format(a, argv[2], b, calc))
