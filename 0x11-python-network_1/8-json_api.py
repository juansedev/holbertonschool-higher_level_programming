#!/usr/bin/python3
""" Script to display an specific Header http"""

import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    values = {}
    if len(argv) > 1:
        values['q'] = argv[1]
    else:
        values['q'] = {""}
    req = requests.post(url, values)
    if req.json():
        try:
            check = req.json()
        except ValueError:
            print("Not a valid JSON")
        print("[{}] {}".format(check.get('id'),
                               check.get('name')))
    else:
        print("No result")
