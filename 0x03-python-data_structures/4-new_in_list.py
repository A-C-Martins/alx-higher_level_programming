#!/usr/bin/python3
""" Write a function that replaces an element in a 
list at a specific position without modifying the
original list (like in c) """

def new_in_list(my_list, idx, element):
    new_list = []
    
    if idx < 0:
        return my_list
    if idx > len(range(len(my_list) - 1)):
        return my_list
    new_list = my_list[:]
    for i in (range(len(new_list) - 1)):
        if idx == i:
            new_list[i] = element
            return new_list
