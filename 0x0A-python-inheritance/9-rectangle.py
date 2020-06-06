#!/usr/bin/python3
""" In this module it create a Class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This a class Rectangle"""

    def __init__(self, width, height):
        """Initialize an instance of Rectangle

        Arguments:
            width: value for __width attribute
            height: value for __height attribute
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This method return value of area"""
        return self.__height * self.__width

    def __str__(self):
        """Return string representation of object Rectangle"""
        string_obj = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string_obj
