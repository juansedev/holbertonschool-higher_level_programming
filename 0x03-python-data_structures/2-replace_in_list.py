#!/bin/usr/python3
def replace_in_list(my_list, idx, element):
        index = 0
        lenght = len(my_list)
        if idx < 0 or idx > lenght - 1:
                return my_list
        for i in range(lenght):
                if index == idx:
                        my_list[index] = element
                        return my_list
                index += 1
