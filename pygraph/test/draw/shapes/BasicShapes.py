import unittest
from pygraph.draw.shapes.BasicShapes import BasicShape

class TestBasicShapes(unittest.TestCase):

    def setUp(self):
        self.shape = BasicShape()

    def test_setShapeType(self):
        self.assertEqual(self.shape.setShapeType('banana'), 'NONE')
        self.assertEqual(self.shape.setShapeType('LINE'), 'LINE')
        self.assertEqual(self.shape.setShapeType('none'), 'LINE')
        self.assertEqual(self.shape.setShapeType('NONE'), 'NONE')
