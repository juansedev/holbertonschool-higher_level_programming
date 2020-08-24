#!/usr/bin/python3
""" Script to display an specific Header http"""

import urllib.request
import sys


if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(e.code)
