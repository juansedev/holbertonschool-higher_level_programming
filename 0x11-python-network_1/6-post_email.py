#!/usr/bin/python3
""" Script to display an specific Header http"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {}
    values['email'] = email
    req = requests.post(url, values)
    print(req.text)
