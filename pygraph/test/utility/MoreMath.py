import unittest
import os
from pygraph.utility.MoreMath import solveQuadratic

class TestMoreMath(unittest.TestCase):
    def setUp(self):
        pass

    def test_solveQuadratic(self):
        self.assertEqual(solveQuadratic(3, -2, -8), [2.0, -4.0/3])
        self.assertEqual(solveQuadratic(1, -2, 1), [1.0, 1.0])
        self.assertEqual(solveQuadratic(2, 0, 4), ["NONE", "NONE"])
        self.assertEqual(solveQuadratic(0, 2, -4), ["NONE", 2.0])
    
