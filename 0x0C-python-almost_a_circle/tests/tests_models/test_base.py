#!/usr/bin/python3
""" This is a Unittest module """


import unittest
from models.base import Base



class TestBase(unittest.TestCase):
    """ Test Cases for Base Class """

    def setUp(self):
        """This method set up initial state for all test methods"""
        Base._Base__nb_objects = 0
        #print("setUp")

    def tearDown(self):
        """This method to perform cleanup after each test method completes"""
        #print("tearDown")

    def test_id_single(self):
        """ Test for set id function """
        b0 = Base(1)
        self.assertEqual(b0.id, 1)

    def test_id_none(self):
        """ Test for set id function """
        b0 = Base(None)
        self.assertEqual(b0.id, 1)

    def test_id_multiple(self):
        """ Test for set id function """
        b0 = Base()
        b1 = Base()
        self.assertEqual(b0.id, 1)
        self.assertEqual(b1.id, 2)



    def test_id_error(self):
        """ Test for set id function """
        self.assertEqual("Juan", Base("Juan").id)
        self.assertEqual(2.5, Base(2.5).id)
        self.assertEqual([1, 2], Base([1, 2]).id)
        self.assertEqual({'1': 2}, Base({'1': 2}).id)
        self.assertEqual(True, Base(True).id)