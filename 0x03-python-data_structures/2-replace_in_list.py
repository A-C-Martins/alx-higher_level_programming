#!/usr/bin/python3
""" Write a function that replaces an element of a list at a specific position (like in c). """

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(range(len(my_list) - 1)):
        return my_list
    
    for i in (range(len(my_list) - 1)):
        if idx == i:
            my_list[i] = element
    
    return my_list
