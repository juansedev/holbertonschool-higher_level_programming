#!/usr/bin/touch3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """


    def empty_list(self):
        """Empty list case"""
        self.assertEqual(max_integer([]), None)

    def not_a_list(self):
        """ Not a number list cases"""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(('a', 'b', 'c')), 'c')

    def number_list(self):
        """Number list cases"""
        self.assertEqual(max_integer([-3, -1, -2]), -1)
        self.assertEqual(max_integer([8 , 4, 5, 2]), 8)
        self.assertEqual(max_integer([-1 , 4, -3, 2]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
