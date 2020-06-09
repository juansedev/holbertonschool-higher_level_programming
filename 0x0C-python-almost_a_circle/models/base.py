#!/usr/bin/python3
""" Module for a Class Base"""


class Base:
    """This is a Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is a method initializer

        Args:
            id (int, optional): value to set id of the object.
            Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            if id <= Base.__nb_objects:
                Base.__nb_objects += 1
                self.id = Base.__nb_objects
            else:
                self.id = id
