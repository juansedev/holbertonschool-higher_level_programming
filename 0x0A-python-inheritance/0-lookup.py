#!/usr/bin/python3
"""
    In this module it implemente a function that returns
    the list of available attributes and methods of an object
"""


def lookup(obj):
    """
        Returns: list with all attributes and methods
    """
    return dir(obj)
