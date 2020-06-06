#!/usr/bin/python3
"""[summary]
"""


def text_indentation(text):
    """[summary]

    Args:
        text ([type]): [description]
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    for x, letter in enumerate(text):
        if letter in ['.', '?', ':']:
            print(text[i:x + 1].strip() + '\n')
            i = x + 1
    print(text[i:].strip(), end='')
