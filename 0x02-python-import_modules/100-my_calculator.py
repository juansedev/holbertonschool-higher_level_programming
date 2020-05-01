#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] != "+" and sys.argv[2] != "-" and sys.argv[2] != "*" and sys.argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        calc = add(a, b)
    if sys.argv[2] == "-":
        calc = sub(a, b)
    if sys.argv[2] == "*":
        calc = mul(a, b)
    if sys.argv[2] == "/":
        calc = div(a, b)
    print("{} {} {} = {}".format(a, sys.argv[2], b, calc))
