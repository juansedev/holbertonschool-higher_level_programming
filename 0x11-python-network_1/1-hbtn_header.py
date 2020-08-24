#!/usr/bin/python3
""" Script to display an specific Header http"""

import urllib.request
import sys


if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        result = response.headers['X-Request-Id']
        print(result)
