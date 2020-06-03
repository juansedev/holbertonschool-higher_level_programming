#!/usr/bin/python3
"""In this module, it creates a function to validate the instance class"""


def is_kind_of_class(obj, a_class):
    """ This function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from, the
    specified class ; otherwise False

    Arguments:
        obj -- Object to validate class
        a_class -- name of the class for compare
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
