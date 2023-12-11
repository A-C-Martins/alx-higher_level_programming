#!/usr/bin/python3

def no_c(my_string):
    #new_string = my_string.replace("c", "")
    for str in my_string:
        if str == "c" or "C":
            new_string = my_string.replace("c", "")
            modi = new_string.replace("C", "")
    return modi
