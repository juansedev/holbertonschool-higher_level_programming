#!/usr/bin/python3
"""[summary]
"""


def matrix_divided(matrix, div):
        """[summary]

        Arguments:
            matrix {[type]} -- [description]
            div {[type]} -- [description]
        """

        message1 = "matrix must be a matrix (list of lists) of integers/floats"
        message2 = "Each row of the matrix must have the same size"
        if not type(matrix) is list or len(matrix) is 0:
                raise TypeError(message1)
        for element in matrix:
                if type(element) is not list:
                        raise TypeError(message1)
                if len(matrix[0]) is not len(element):
                        raise TypeError(message2)
                for j in element:
                        if type(j) is not int and type(j) is not float:
                                raise TypeError(message1)

        if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
        if div is 0:
                raise ZeroDivisionError("division by zero")

        return[[round(j / div, 2) for j in i] for i in matrix]
