#!/usr/bin/python3
""" In this module it create a Class Squere that inherits
    from r"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This a class Rectangle"""

    def __init__(self, size):
        """Initialize an instance of Square

        Arguments:
            size: value for __size attribute
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of object Rectangle"""
        string_obj = "[Square] {}/{}".format(self.__size, self.__size)
        return string_obj
