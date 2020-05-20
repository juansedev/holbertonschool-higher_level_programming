#!/usr/bin/python3
"""This module defines the square class with init
   method, handle execptions and area method
"""


class Square:
    """This es a class of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Thie __init__ method initialize a instance with a private
        instace atributte size and validate datatype

        Args:
                size (int): Value of the size of the square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method of atributte position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Settet method of atributte value

        Args:
                value (tuple): Value of the size of the square
        """
        if type(value[0]) == int and type(value[1]) == int \
                and len(value) is 2 and type(value) == tuple:
                self.__position = value
        else:
                raise TypeError("""position must be a tuple of 2
                        positive integers""")

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
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * self.position[0], "#" * self.__size))
