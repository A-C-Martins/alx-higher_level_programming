#!/usr/bin/python3
"""
 Module that contains the Square Class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Class Square
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Print a string format
        '''
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''getter size
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter size
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Args and kwargs
        '''
        lst = ['id', 'size', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, lst[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        '''Convert in a dictionary format
        '''
        dic_s = {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.width}
        return dic_s
