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
        self.lsys.addRule('A', ['B', 'i'])
        self.lsys.addRule('BC', ['AAA', 'kkikiikk'])
        self.lsys.addRule('D', ['a'])
        self.lsys.addRule('D', ['b'])
        self.lsys.addRule('D', ['b'])
        self.lsys.addRule('D', ['c'])
        self.lsys.addRule('D', ['a'])
        self.lsys.addRule('D', ['b'])
        self.lsys.addRule('E', ['i'], 9)
        self.lsys.addRule('E', ['j'])
        self.lsys.addRule('E', ['k'], 3)

        self.assertIn('A', self.lsys.rules)
        self.assertIn('BC', self.lsys.rules)
        self.assertIn('D', self.lsys.rules)
        self.assertIn('E', self.lsys.rules)

        self.assertEqual(self.lsys.rules['A'], [[1, 'B', 'i']])
        self.assertEqual(self.lsys.rules['BC'], [[1, 'AAA', 'kkikiikk']])
        self.assertEqual(self.lsys.rules['D'], [[2, 'a'], [3, 'b'], [1, 'c']])
        self.assertEqual(self.lsys.rules['E'], [[9, 'i'], [1, 'j'], [3, 'k']])

    def test_generate(self):
        self.fail("Not yet Implemented")

    def test_expand(self):
        self.fail("Not yet Implemented")

    def test_setRasterFunction(self):
        self.fail("Not yet Implemented")

    def test_rasterize(self):
        self.fail("Not yet Implemented")
