import unittest
from pygraph.generate.LSystem import LSystem

class TestLSystem(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        self.lsys = LSystem()

    def test_interface(self):
        for func in ('addRule', 'generate', 'expand', 'setRasterFunction', 'rasterize'):
            self.assertTrue(hasattr(self.lsys, func) and callable(getattr(self.lsys, func)), "Interface requires function: " + func)

    def test_addRule(self):
        self.fail("Not yet Implemented")

    def test_generate(self):
        self.fail("Not yet Implemented")

    def test_expand(self):
        self.fail("Not yet Implemented")

    def test_setRasterFunction(self):
        self.fail("Not yet Implemented")

    def test_rasterize(self):
        self.fail("Not yet Implemented")
