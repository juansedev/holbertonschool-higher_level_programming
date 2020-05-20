#!/usr/bin/python3
"""This module defines the square class with init
   method, handle execptions and area method
"""


class Square:
        """This es a class of a square"""
        def __init__(self, size = 0):
                """Thie __init__ method initialize a instance with a private
                instace atributte size and validate datatype

                Args:
                        size (int): Value of the size of the square
                """

                if type(size) == int:
                        if size < 0:
                                raise ValueError("size must be >= 0")
                        else:
                                self.__size = size
                else:
                        raise TypeError("size must be an integer")

        def area(self):
                """This method compute the value of area of a square"""

                self.area = (self.__size**2)
                return self.area
