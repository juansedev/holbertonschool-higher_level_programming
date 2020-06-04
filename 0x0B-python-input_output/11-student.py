#!/usr/bin/python3
"""in this module it implement a class student"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Constructor method

        Arguments:
            first_name {str} -- [description]
            last_name {str} -- [description]
            age {str} -- [description]
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
