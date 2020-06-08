#!/usr/bin/python3
"""In this module it creare a class Base"""


class Base:
    """ This is a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a initializer method

        Args:
            id (int, optional): Value to set id attribute. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            if id is Base.__nb_objects:
                Base.__nb_objects += 1
                self.id = Base.__nb_objects
            else:
                self.id = id
