#!/usr/bin/python3
'''
Module for test the Square
'''

import unittest
from models.base import Base
from models.square import Square

class Test_Square(unittest.TestCase):
    '''
    Unittest class
    '''
    def setUp(self):
        '''SetUp function'''
        Base._Base__nb_objects = 0

    def test_Str_(self):
        '''Test that print the square'''
        sq = Square(3, id=40)
        self.assertEqual(str(sq), '[Square] (40) 0/0 - 3')

    def testArea(self):
        '''Test Area'''
        sq = Square(7, id=1)
        self.assertEqual(str(sq.area()), '49')

    def testWidth(self):
        '''Test width'''
        sq = Square(7)
        self.assertEqual(7, sq.width)

    def testSize(self):
        '''Test Size'''
        siz = Square(7)
        self.assertEqual(siz.size, 7)

    def testSizeErrVal(self):
        '''Test Errors values'''
        with self.assertRaises(ValueError):
            siz = Square(0)

    def testSizeErrType(self):
        '''Test Errors of typing'''
        with self.assertRaises(TypeError):
            siz = Square()

    def testZero(self):
        '''Test Value Error'''
        with self.assertRaises(ValueError):
            siz = Square(0)

    def testSizeEmpty(self):
        '''Test of empty'''
        with self.assertRaises(TypeError):
            siz = Square()

    def testXvalue(self):
        '''X value test'''
        siz1 = Square(3, 2, 1)
        self.assertEqual(siz1.x, 2)

    def testXvalue2(self):
        '''X value test'''
        siz1 = Square(5, 6)
        self.assertEqual(siz1.x, 6)

    def testXvalue4(self):
        '''X value test'''
        siz1 = Square(5, 6, 2, 4)
        self.assertEqual(siz1.x, 6)

    def testYvalue(self):
        '''Y value test'''
        siz1 = Square(3, 2, 1)
        self.assertEqual(siz1.y, 1)

    def testYalue2(self):
        '''Y value test'''
        siz1 = Square(5, 6)
        self.assertEqual(siz1.y, 0)

    def testYvalue4(self):
        '''identity value test'''
        siz1 = Square(5, 6, 2, 4)
        self.assertEqual(siz1.y, 2)

    def test_identity1(self):
        '''identity value test'''
        siz_i = Square(4, 5)
        self.assertEqual(siz_i.id, 1)

    def test_identity2(self):
        '''identity value test'''
        siz_i2 = Square(4, 0, 0, 5)
        self.assertEqual(siz_i2.id, 5)

    def testUpdate(self):
        '''Update value test'''
        siz = Square(3, 3, 3, 3)
        siz.update(4, 4, 4, 4)
        self.assertEqual(siz.id, 4)
        self.assertEqual(siz.size, 4)
        self.assertEqual(siz.x, 4)
        self.assertEqual(siz.y, 4)

    def testStr(self):
        '''String value test'''
        with self.assertRaises(TypeError):
            siz = Square('cedore')

    def testLst(self):
        '''List test'''
        with self.assertRaises(TypeError):
            siz = Square({'a': 1, 'b': 2})

    def testTup(self):
        '''Tuple test'''
        with self.assertRaises(TypeError):
            siz = Square((2, ))
