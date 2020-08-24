#!/usr/bin/python3
""" Script to display an specific Header http"""

import urllib.request


if __name__ == "__main__":

    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
            print("Body response:")
            print("\t- type: {}".format(type(response.read().decode('utf-8'))))
            print("\t- content: {}".format(response.read().decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
