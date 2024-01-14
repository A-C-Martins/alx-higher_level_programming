#!/usr/bin/python3
import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test(unittest.TestCase):

    def setUp(self):
        '''Initialize every test'''
        Base._Base__nb_objects = 0

    def testBases(self):
        '''The normal id assign'''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_baseId(self):
        '''Integer test'''
        b = Base(7)
        self.assertEqual(b.id, 7)

    def test_baseMinId(self):
        '''Negative integer test'''
        b = Base(-7)
        self.assertEqual(b.id, -7)

    def test_baseDecimalId(self):
        '''Decimal integer test'''
        b = Base(0.000007)
        self.assertEqual(b.id, 0.000007)

    def test_baseIdBoolTrue(self):
        '''Bool true integer test'''
        b = Base(True)
        self.assertEqual(b.id, True)

    def test_baseIdBoolFalse(self):
        '''Bool False Integer test'''
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_baseIdchar(self):
        '''Char test'''
        with self.assertRaises(NameError):
            b = Base(c)

    def test_baseIdString(self):
        '''String Integer test'''
        b = Base('Empa')
        self.assertEqual(b.id, 'Empa')

    def test_baseIdList(self):
        '''List Integer test'''
        b = Base([1, 2])
        self.assertEqual(b.id, [1, 2])

    def test_baseIdList(self):
        '''Tuple Integer test'''
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))

    def test_baseIdDict(self):
        '''Dictionary Integer test'''
        b = Base({'di': 2, 'mono': 1})
        self.assertEqual(b.id, {'di': 2, 'mono': 1})

    def test_baseIdNone(self):
        '''Dictionary Integer test'''
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_baseIdEmptyList(self):
        '''Empty List Integer test'''
        b = Base([])
        self.assertEqual(b.id, [])

    def test_baseIdEmptyList(self):
        '''Tuple Integer test'''
        b = Base(())
        self.assertEqual(b.id, ())

    def test_baseIdEmptyDict(self):
        '''Dictionary Integer test'''
        b = Base({})
        self.assertEqual(b.id, {})

    def test_Dict2JASONString(self):
        '''Jason to String Function'''
        b = Base()
        t_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(type(b.to_json_string(t_dict)), str)

    def test_Dict2JASONStringNone(self):
        '''Jason to String Function'''
        b = Base()
        self.assertEqual(b.to_json_string(None), '[]')

    def testNAN(self):
        '''Test for NaN as argument'''
        b = Base(float('nan'))
        self.assertNotEqual(b.id, float('nan'))


    def testInf(self):
        '''Test for Inf as argument'''
        b = Base(float('inf'))
        self.assertEqual(b.id, float('inf'))

if __name__ == '__main__':
    unittest.main()
