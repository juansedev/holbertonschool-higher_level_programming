#!/usr/bin/python3
""" Script to display an specific Header http"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    value = req.headers['X-Request-Id']
    print(value)
