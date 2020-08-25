#!/usr/bin/python3
""" Script to display an specific Header http"""

import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    token = argv[2]

    req = requests.get('https://api.github.com/user', auth=(user, token))
    print(req.json().get("id"))
