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

    def to_json(self, attrs=None):
        s_dict = self.__dict__

        if type(attrs) is list and all([type(i) is str for i in attrs]):
            new_dict = {}
            for name in attrs:
                if name in s_dict:
                    new_dict[name] = s_dict[name]

        return self.__dict__
