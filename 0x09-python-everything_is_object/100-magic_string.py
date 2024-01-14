#!/usr/bin/python3
def magic_string(lst=[]):
    lst.insert(len(lst) - 1, 'Holberton')
    return ', '.join(lst)
