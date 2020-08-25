#!/usr/bin/python3
""" Script to display an specific Header http"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    code = r.status_code
    if code < 400:
        print(r.text)
    else:
        print("Error code:", code)
