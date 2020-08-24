#!/usr/bin/python3
# Script to display an specific Header http

from urllib import request
from sys import argv


if __name__ == "__main__":

    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        result = response.headers['X-Request-Id']
        print(result)
