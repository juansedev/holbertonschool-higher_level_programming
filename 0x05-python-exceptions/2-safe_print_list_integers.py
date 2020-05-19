#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        j = 0
        for i in my_list:
                try:
                        if j == x:
                                break
                        print("{:d}".format(i), end="")
                        j += 1
                except:
                        continue
        print()
        return j
