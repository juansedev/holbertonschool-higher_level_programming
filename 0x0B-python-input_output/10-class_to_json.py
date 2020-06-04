#!/usr/bin/python3
"""Write a function that returns the dictionary description with simple data
    structure(list, dictionary, string, integer and boolean) for JSON
    serialization of an object:
"""


def class_to_json(obj):
    """Returns the dictionary of object

    Arguments:
        obj {[type]} -- object to convert
    """
    return obj.__dict__
