#!/usr/bin/python3
"""in ths module it create a method to fill a pascal trangule"""


def pascal_triangle(n):
    """function def pascal_triangle(n): that returns a list of
    lists of integers representing the Pascal’s triangle of n:

    Args:
        n (int): n is a value for create a Pascal Trangule
    """

    if n:
        if n is 1:
            return [[1]]
        if n is 2:
            return [[1], [1, 1]]
        if n > 2:
            pascal = [[1], [1, 1]]
            j = 3
            while j <= n:
                new = []
                last = pascal[-1]
                last_len = len(last)
                i = 0
                while i < last_len + 1:
                    if i is last_len:
                        break
                    if i is 0:
                        new.append(1)
                        i += 1
                    else:
                        value = last[i] + last[i - 1]
                        new.append(value)
                        i += 1
                new.append(1)
                j += 1
                pascal.append(new)
            return pascal
