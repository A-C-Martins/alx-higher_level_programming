#!/usr/bin/python3
'''
Prevents the user from dynamically
creating nes instance attributes
except it is called first_name
'''


class LockedClass:
    '''
    the locked class
    '''
    __slots__ = ['first_name']
