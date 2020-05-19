#!/usr/bin/python3
"""This module  defines the Square class with the __init__ function

"""


class Square:
        """This is a class of a square"""

        def __init__(self, size):
                """The __init__ method initialize a instance with a private
                instace atributte size

                Args:
                        size (int): Value of the size of the square
                """
                self.__size = size
