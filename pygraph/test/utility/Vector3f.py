import unittest
import os
from pygraph.utility.Vector3f import Vector3f

class TestVector3f(unittest.TestCase):

    def setUp(self):
        self.vector = Vector3f(0.0, 0.0, 0.0)

    def test_interface(self):
        for func in ('normalize', 'cross', '__add__', '__sub__', '__mul__', 'dot', 'length', '__getitem__', 'toList'):
            self.assertTrue(hasattr(self.vector, func) and callable(getattr(self.vector, func)), "Interface requires function: " + func)

    def test_normalize(self):
        v1 = Vector3f(1, 2, 2)
        self.assertEqual(v1.normal, 0)
        v1 = v1.normalize()
        self.assertEqual(v1.toList(), [1.0/3, 2.0/3, 2.0/3])
        self.assertEqual(v1.toList(), [1.0/3, 2.0/3, 2.0/3])
        self.assertEqual(v1.normal, 1)
        self.assertEqual(Vector3f(1, 0, 0).normalize().toList(), [1.0, 0.0, 0.0])
        self.assertEqual(Vector3f(0, 0, 1).normalize().toList(), [0.0, 0.0, 1.0])

    def test_length(self):
        self.assertEqual(Vector3f(1, 2, 2).length(), 3.0)
        self.assertEqual(Vector3f(1, 0, 0).length(), 1.0)
        self.assertEqual(Vector3f(0, 0, 1).length(), 1.0)

    def test_cross(self):
        vector1 = Vector3f(1, 0, 0)
        vector2 = Vector3f(0, 1, 0)
        vector3 = Vector3f(0, 0, 1)
        self.assertEqual(vector1.cross(vector2).toList(), [0.0, 0.0, 1.0])
        self.assertEqual(vector2.cross(vector3).toList(), [1.0, 0.0, 0.0])
        self.assertEqual(vector3.cross(vector1).toList(), [0.0, 1.0, 0.0])

    def test_add(self):
        v1 = Vector3f(1, 2, 3)
        v2 = Vector3f(4, 5, 6)
        sumv = v1 + v2
        print sumv
        self.assertEqual(sumv.toList(), [5.0, 7.0, 9.0])

    def test_sub(self):
        v1 = Vector3f(1, 2, 3)
        v2 = Vector3f(4, 5, 6)
        v3 = Vector3f(1, 0, 1)
        v4 = Vector3f(0, 1, 0)
        dif1 = v1 - v2
        dif2 = v3 - v4
        self.assertEqual(dif1.toList(), [-3.0, -3.0, -3.0])
        self.assertEqual(dif2.toList(), [1.0, -1.0, 1.0])

    def test_mul(self):
        v1 = Vector3f(1, 2, 3)
        v2 = Vector3f(4, 5, 6)

        m1 = v1 * 1
        m2 = v1 * 3
        m3 = v1 * v2
        self.assertEqual(m1.toList(), [1.0, 2.0, 3.0])
        self.assertEqual(m2.toList(), [3.0, 6.0, 9.0])
        self.assertEqual(m3.toList(), [4.0, 10.0, 18.0])

    def test_dot(self):
        v1 = Vector3f(1, 0, 0)
        v2 = Vector3f(0, 1, 0)
        v3 = Vector3f(0, 0, 1)
        v4 = Vector3f(1, 2, 3)
        v5 = Vector3f(4, 5, 6)
        self.assertEqual(v1.dot(v2), 0.0)
        self.assertEqual(v2.dot(v3), 0.0)
        self.assertEqual(v3.dot(v1), 0.0)
        self.assertEqual(v4.dot(v5), 32.0)
        self.assertEqual(v5.dot(v4), 32.0)
