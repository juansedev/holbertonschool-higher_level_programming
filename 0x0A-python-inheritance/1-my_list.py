#!/usr/bin/python3
"""
    In this module it create the class MyList
"""


class MyList(list):
    """This is the class MyList that inherits from list

    Arguments:
        list {[type]} -- This is the base Class
    """
    def print_sorted(self):
        """
            Function that prints the list, but sorted (ascending sort)
        """
        list_sorted = sorted(self)
        print(list_sorted)
