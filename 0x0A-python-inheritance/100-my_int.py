#!/usr/bin/python3
"""[summary]
"""


class MyInt(int):
    """This a class MyInt that inherits from int"""

    def __eq__(self, other):
        """ Override of the operator == in this method """
        return False

    def __ne__(self, other):
        """Override  of the operator != in this method"""
        return True
