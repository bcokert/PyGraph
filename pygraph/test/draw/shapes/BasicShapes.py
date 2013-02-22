import unittest
from pygraph.draw.shapes.BasicShapes import BasicShapes

class TestBasicShapes(unittest.TestCase):

    def setUp(self):
        self.shapes = BasicShapes(100, 100)

    def test_interface(self):
        for func in ('setCanvasSize', 'drawLine'):
            self.assertTrue(hasattr(self.shapes, func) and callable(getattr(self.shapes, func)), "Interface requires function: " + func)

    def test_setCanvasSize(self):
        self.assertEqual(self.shapes.setCanvasSize(300, 400), (300, 400))
        self.assertEqual(self.shapes.setCanvasSize(500), (500, 400))
        self.assertEqual(self.shapes.setCanvasSize(), (500, 400))
        self.assertEqual(self.shapes.setCanvasSize(600, 700), (600, 700))

    def test_drawLine(self):
        self.shapes.setCanvasSize(1000, 1000)
        pixels = self.shapes.drawLine(0, 0, 1000, 1000, (255, 255, 255))
        self.assertTrue(len(pixels) >= 1000)
        self.assertTrue(len(pixels[0]) == 3)
        self.assertTrue(pixels[0][0] == 0 and pixels[0][1] == 0 and pixels[1000][0] == 1000 and pixels[1000][1] == 1000)
