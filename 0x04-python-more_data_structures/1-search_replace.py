#!/usr/bin/python3
def search_replace(my_list, search, replace):
        new_list = [None] * len(my_list)
        for i in my_list:
                if i == search:
                        i = replace
        return new_list
