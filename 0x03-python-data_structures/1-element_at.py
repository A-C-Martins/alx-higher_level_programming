#!/usr/bin/python3
""" Write a function that retrieves an element from a list like in c """

def element_at(my_list, idx):
    if idx < 0:
        return 'None'
    if idx > len(range(len(my_list) - 1)):
        return 'None'
    for i in (range(len(my_list) - 1)):
        if idx == i:
            x = my_list.pop(i)
    return x
