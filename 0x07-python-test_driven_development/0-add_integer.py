#!/usr/bin/python3
"""
Module 0-add_integer.py:
Add two integers
"""


def add_integer(a, b=98):
        """This function add two integers

        Arguments:
            a {int} -- First value of the add

        Keyword Arguments:
            b {int} -- First value of the add (default: {98})

        Returns:
            [int] -- Result to compute a + b
        """
        if type(a) is not int and type(a) is not float:
                raise TypeError("a must be an integer")
        if type(b) is not int and type(b) is not float:
                raise TypeError("b must be an integer")
        return int(a) + int(b)
