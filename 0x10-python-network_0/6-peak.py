#!/usr/bin/python3
""" Function to find a peak """

def find_peak(list_of_integers):
    """ Method doc"""
    if not list_of_integers:
        return None
    else:
        return max(list_of_integers)
