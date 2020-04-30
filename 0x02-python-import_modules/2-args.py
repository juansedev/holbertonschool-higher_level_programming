#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 arguments.")
    print("1:", format(sys.argv[1]))
else:
    i = 1
    print("{} arguments:".format(len(sys.argv) - 1))
    for arg in sys.argv:
        if i < len(sys.argv):
            print("{}: {}".format(i, sys.argv[i]))
        i += 1
