#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
        new_list = []
        div = 0
        for i in range(list_length):
                try:
                        div = my_list_1[i] / my_list_2[i]
                except ZeroDivisionError:
                        print("Division by 0")
                except (TypeError, ValueError):
                        print("Invalid data type ")
                except IndexError:
                        print("Index out the range")
                finally:
                        new_list.append(div)
        return new_list
