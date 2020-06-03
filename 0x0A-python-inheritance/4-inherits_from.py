#!/usr/bin/python3
"""In this module, it creates a function to validate the instance class
    is a a class that inherited
"""


def inherits_from(obj, a_class):
    """ This function that returns True if the object is an instance of,
    or if the object is only  an instance of a class that inherited from the
    specified class ; otherwise False

    Arguments:
        obj -- Object to validate class
        a_class -- name of the class for compare
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
