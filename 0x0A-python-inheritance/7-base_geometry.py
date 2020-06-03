#!/usr/bin/python3
""" In this module it create a Class BaseGeometry"""


class BaseGeometry:
    """This a class BaseGeometry"""
    def area(self):
        """Method for compute the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
