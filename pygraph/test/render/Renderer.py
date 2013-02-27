import unittest
import os
from pygraph.render.Renderer import Renderer
from pygraph.draw.shapes.BasicShapes import BasicShapes

class TestRenderer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.shapes = BasicShapes(10, 10)
        self.line1 = self.shapes.drawLine(0, 5, 9, 5, (255, 0, 0))
        self.line2 = self.shapes.drawLine(0, 5, 9, 5, (0, 255, 0))
        self.line3 = self.shapes.drawLine(5, 0, 5, 9, (0, 0, 255))

    def setUp(self):
        self.renderer = Renderer(10, 10)

    def test_interface(self):
        for func in ('render', 'clearBuffer', 'setBackgroundColor', 'drawOver', 'drawUnder'):
            self.assertTrue(hasattr(self.renderer, func) and callable(getattr(self.renderer, func)), "Interface requires function: " + func)

    def test_render(self):
        self.renderer.setBackgroundColor(200, 200, 200)
        self.renderer.clearBuffer()
        self.renderer.drawOver(self.line1)
        self.renderer.drawUnder(self.line2, 3, 3)

        render = self.renderer.render()
        self.assertIs(type(render), list)
        self.assertEqual(render[5], [255, 0, 0]*10, "The red line was not rendered properly")
        self.assertEqual(render[8], [200, 200, 200]*3 + [0, 255, 0]*7, "The green line was not rendered properly")
        for row in [0, 1, 2, 3, 4, 6, 7, 9]:
            self.assertEqual(render[row], [200, 200, 200]*10, "Row " + str(row) + " did not render background properly")

        self.renderer.render('./test.png')
        self.assertTrue(os.path.exists('./test.png'), "The file wasn't created upon rendering")
        try:
            os.remove('./test.png')
        except OSError:
            fail("Could not clean up the created test file")

    def test_clearBuffer(self):
        self.renderer.setBackgroundColor(10, 20, 30)
        self.renderer.clearBuffer()
        for i, row in enumerate(self.renderer.pixels):
            self.assertEqual(row[0:30], [10, 20, 30]*10, "Row " + str(i) + " was not cleared")

    def test_setBackgroundColor(self):
        self.assertEqual(self.renderer.setBackgroundColor(200, 200, 200), [200, 200, 200])
        self.assertEqual(self.renderer.setBackgroundColor(256, 255, 255), [200, 200, 200])
        self.assertEqual(self.renderer.setBackgroundColor(), [200, 200, 200])
        self.assertEqual(self.renderer.setBackgroundColor(200, 100), [200, 200, 200])
        self.assertEqual(self.renderer.setBackgroundColor(200, 100, 50), [200, 100, 50])

    def test_drawOver(self):
        self.renderer.drawOver(self.line1)
        self.assertEqual(self.renderer.pixels[5], [255, 0, 0]*10)

        self.renderer.drawOver(self.line1, 3, 2)
        self.assertEqual(self.renderer.pixels[7][9:30], [255, 0, 0]*7)

        self.renderer.drawOver(self.line2, 2, 0)
        self.assertEqual(self.renderer.pixels[5], [255, 0, 0]*2 + [0, 255, 0]*8)

    def test_drawUnder(self):
        self.renderer.drawUnder(self.line1)
        self.assertEqual(self.renderer.pixels[5], [255, 0, 0]*10)

        self.renderer.drawUnder(self.line1, 3, 2)
        self.assertEqual(self.renderer.pixels[7][9:30], [255, 0, 0]*7)

        self.renderer.drawUnder(self.line2, 2, 0)
        self.assertEqual(self.renderer.pixels[5], [255, 0, 0]*10)

    def test_integration_drawOrder(self):
        self.renderer.drawOver(self.line1, 0, -2)
        self.renderer.setBackgroundColor(100, 100, 100)
        self.renderer.clearBuffer()
        self.renderer.drawOver(self.line1)
        self.renderer.drawUnder(self.line2, 1, 3)
        self.renderer.drawOver(self.line3)
        self.renderer.drawUnder(self.line3, 2)
        render = self.renderer.render()

        self.renderer.render('./integration_drawOrder.png')
        self.assertTrue(os.path.exists('./integration_drawOrder.png'), "The file wasn't created upon rendering")

        self.assertIs(type(render), list)
        for row in [0, 1, 2, 3, 4, 6, 7, 9]:
            self.assertEqual(render[row], [100, 100, 100]*5 + [0, 0, 255] + [100, 100, 100] + [0, 0, 255] + [100, 100, 100]*2,
                    "Background did not render properly on row: " + str(row))
        self.assertEqual(render[5], [255, 0, 0]*5 + [0, 0, 255] + [255, 0, 0]*4, "Redline did not render properly")
        self.assertEqual(render[8], [100, 100, 100] + [0, 255, 0]*4 + [0, 0, 255] + [0, 255, 0]*4, "GreenLine did not render properly")
