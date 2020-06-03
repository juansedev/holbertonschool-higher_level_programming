#!/usr/bin/python3
"""
    In this module it implemente a function that returns
    the list of available attributes and methods of an object
"""


def lookup(obj):
    """ This function returns the list of available
    attributes and methods of an object

        Arguments:
        obj {object} -- This is the object to validate its
        attributes and methods

        Returns:
        [list] -- list with all attributes and methods
    """
    return dir(obj)
