#!/usr/bin/python3
def uniq_add(my_list=[]):
        add = 0
        index1 = 0
        for i in my_list:
                number = my_list[index1]
                add += number
                index2 = index1 + 1
                for j in range(index2, len(my_list)):
                        if number == j:
                                my_list[index2] = 0
                        index2 += 1
                index1 += 1
        return add
