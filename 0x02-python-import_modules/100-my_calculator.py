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
    num1 = int(argv[1])
    num2 = int(argv[3])
    print("{} {} {} = {}".format(num1, argv[2], num2, calc))
