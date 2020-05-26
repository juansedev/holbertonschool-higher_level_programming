#!/usr/bin/python3
"""This mnodule define a Rectangule class
"""


class Rectangle:
    """This is a rectangule class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This __init__ method initialize an instance with a private
        instance attributte width and height.

        Keyword Arguments:
            width {int} -- Input value of width (default: {0})
            height {int} -- Input value of height (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Height attribute getter method"""
        return self.__height

    @property
    def width(self):
        """Width attribute getter method"""
        return self.__width

    @height.setter
    def height(self, height):
        """height attribute setter method

        Arguments:
            height {int} -- Input value of height
        """
        if isinstance(height, int) is True:
            if height < 0:
                raise ValueError("width must be >= 0")
            else:
                    self.__height = height
        else:
            raise TypeError("width must be an integer")

    @width.setter
    def width(self, width):
        """Width attribute setter method

        Arguments:
            width {int} -- Input value of height
        """
        if isinstance(width, int) is True:
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                    self.__width = width
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """This method computes the value of the rectangle's area

        Returns:
            [int] -- Value of the compute of area
        """
        return self.__height * self.__width

    def perimeter(self):
        """This method computes the value of the rectangle's perimeter

        Returns:
            [int] -- Value of the compute of perimeter
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns string representation of a Rectangle"""
        if self.__width is 0 or self.__height is 0:
            return ""
        str_object = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str_object += str(self.print_symbol)
            if i < self.__height - 1:
                str_object += "\n"
        return str_object

    def __repr__(self):
        """return a string representation of the rectangle to be able to recreate
        a new instance by
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print message when delete an instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """This method validate which is the biggest rectangle
            and return the biggest
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
