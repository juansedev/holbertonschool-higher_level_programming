#!/usr/bin/python3
"""This module defines the square class with init
   method, handle execptions and area method
"""


class Square:
        """This es a class of a square"""
        def __init__(self, size=0):
                """Thie __init__ method initialize a instance with a private
                instace atributte size and validate datatype

                Args:
                        size (int): Value of the size of the square
                """

                self.size = size

        @property
        def size(self):
                """Getter method of atributte size"""

                return self.__size

        @size.setter
        def size(self, size):
                """Settet method of atributte size

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
                """This method compute the value of area of a square

                Returns:  area
                """

                area = self.__size ** 2
                return area

        def my_print(self):
                """This method print a square of hash(#)"""

                if self.__size is 0:
                        print()
                        return

                for i in range(self.__size):
                        for j in range(self.__size):
                                print("{}".format("#"), end="")
                        print()
