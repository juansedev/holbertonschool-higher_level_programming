#!/usr/bin/python3
"""This module defines the square class  with init
   function and handle exceptions
"""


class Square:
        """This is a class of a square"""
        def __init__(self, size=0):
                """The __init__ method initialize a instance with a private
                instace atributte size and validation datatype

                Args:
                        size (int): Value of the size of the square
                """

                if isinstance(size, int):
                        if size < 0:
                                raise ValueError("size must be >= 0")
                        else:
                                self.__size = int(size)
                else:
                        raise TypeError("size must be an integer")
