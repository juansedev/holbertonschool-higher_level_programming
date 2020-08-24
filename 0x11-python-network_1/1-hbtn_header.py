#!/usr/bin/python3
# Script to display an specific Header http

from urllib import request
from sys import argv


if argv[1]:
    url = argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        print(response.info()['X-Request-Id'])
