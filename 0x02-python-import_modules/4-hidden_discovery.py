#!/usr/bin/python3
import hidden_4
for arg in dir(hidden_4):
    if arg[0] != '_':
        print(arg)
