#!/usr/bin/python
'''
Rectangle tests
'''
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

class TestRectangle(unittest.TestCase):
    '''
    Rectangle test module
    '''
    def setUp(self):
        Base._Base__nb_objects = 0

    def testIdRectangle(self):
        '''Test of Id in Rectangle'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def testIdRectangle2(self):
        '''Test of Id in Rectangle'''
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 1)

    def testIdRectangle3(self):
        '''Test of Id in Rectangle'''
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def testErrHeight(self):
        '''Test of an error in the parameter of rectangle'''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, '2')

    def testErrWidth(self):
        '''Test of an error in the parameter of rectangle'''
        with self.assertRaises(TypeError):
            r1 = Rectangle('10', 2)

    def testErrHeigth_Minus(self):
        '''Test of an error in the parameter of rectangle'''
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def testErrWidth_Minus(self):
        '''Test of an error in the parameter of rectangle'''
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)

    def testErrX(self):
        '''Test of an error in the parameter of rectangle'''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 'is', 2)

    def testErrY(self):
        '''Test of an error in the parameter of rectangle'''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 2, 'is')

    def testErrX_val(self):
        '''Test of an error in the parameter of rectangle'''
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -2, 2)

    def testArea(self):
        '''Test of area function'''
        r1 = Rectangle(3, 5, 2, 6, 1)
        self.assertEqual(r1.area(), 15)

    def testInherit(self):
        '''Test of subclass rectangle in fron Parent base class'''
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_Str_(self):
        '''Test str function'''
        r1 = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(str(r1), '[Rectangle] (2) 2/2 - 2/2')

    def test_Str_3(self):
        '''Test str function'''
        r1 = Rectangle(2, 2, 1)
        self.assertEqual(str(r1), '[Rectangle] (1) 1/0 - 2/2')

    def test_update(self):
        '''Test update'''
        r1 = Rectangle(2, 2, 2, 2, 2)
        r1.update(20, 5, 6, 3, 2)
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 2)

    def test_Dictionary_type(self):
        '''Test dictionary'''
        r1 = Rectangle(3, 5)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def testDictionary(self):
        r1 = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r1.to_dictionary(), {
            'width': 2, 'height': 2, 'x': 2, 'y': 2, 'id': 2})

    def UpdateVarKwargs(self):
        '''Update kwargs'''
        r1 = Rectangle(5, 5, 5, 5)
        r1.update(x=2, height=2, y=3, width=4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.heigth, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)


if __name__ == '__main__':
    unittest.main()
