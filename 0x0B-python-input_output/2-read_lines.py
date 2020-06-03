#!/usr/bin/python3
"""In this module it create a function that read
    n lines of a file
"""


def read_lines(filename="", nb_lines=0):
    """This  function that reads n lines of a text file
    (UTF8) and prints it to stdout:

    Arguments:
        filename {str} -- This is the file to read(default: {""})
        nb_lines {int} -- This is the number line to read(default: {0})
    """
    with open(filename, mode='r', encoding='utf-8') as my_file:
        f_list = my_file.readlines()
        if nb_lines <= 0 or nb_lines > len(f_list):
            nb_lines = len(f_list)
        i = 0
        for i in range(nb_lines):
            print(f_list[i], end='')
    return i + 1
