#!/usr/bin/python3
"""In this module, it creates a function to validate the object class"""


def is_same_class(obj, a_class):
    """ This function that returns True if the object is exactly an
        instance of the specified class ; otherwise False.

    Arguments:
        obj -- Object to validate class
        a_class -- name of the class for compare
    """
    if type(obj) is a_class:
        return True
    else:
        return False
