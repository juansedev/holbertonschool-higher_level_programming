#!/usr/bin/python3
"""[summary]
"""


def print_square(size):
    """[summary]

    Args:
        size ([type]): [description]
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end='')
        print()
