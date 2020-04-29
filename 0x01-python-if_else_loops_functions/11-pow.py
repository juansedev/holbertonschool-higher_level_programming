#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        result = 1
    elif b < 0:
        result = 1
        for i in range(b, 0):
            result /= a
    else:
        result = 1
        for i in range(b):
            result *= a
    return result
