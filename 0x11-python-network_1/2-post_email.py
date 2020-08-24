#!/usr/bin/python3
""" Script to display an specific Header http"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {}
    values['email'] = email
    url_values = urllib.parse.urlencode(values)
    url_values = url_values.encode('ascii')
    with urllib.request.urlopen(url, url_values) as response:
        print(response.read().decode('utf-8'))
