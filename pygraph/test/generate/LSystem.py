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
        self.lsys.addRule('A', ['i', 'B'])
        self.lsys.addRule('B', ['j', 'C'])
        self.lsys.addRule('C', ['k', 'D'])
        self.lsys.addRule('D', ['l', 'E'])
        self.lsys.addRule('E', ['m', 'A'])
        self.assertEqual(self.lsys.generate(['A'], 4), ['i', 'j', 'k', 'l', 'E'])
        self.assertEqual(self.lsys.generate(['A'], 7), ['i', 'j', 'k', 'l', 'm', 'i', 'j', 'C'])
        self.assertEqual(self.lsys.generate(['A', 'A'], 3), ['i', 'j', 'k', 'D', 'i', 'j', 'k', 'D'])
        self.assertEqual(self.lsys.generate(['A', 'C', 'a', 'E'], 3), ['i', 'j', 'k', 'D', 'k', 'l', 'm', 'A', 'a', 'm', 'i', 'j', 'C'])

        self.lsys.addRule('Q', ['R', 'q', 'Q', 'R'])
        self.lsys.addRule('R', ['S', 't'])
        self.lsys.addRule('S', ['cat'])
        print self.lsys.generate(['Q', 'dog'], 5)
        self.assertEqual(self.lsys.generate(['Q', 'dog'], 5),
                ['cat', 't', 'q', 'cat', 't', 'q', 'cat', 't', 'q', 'S', 't', 'q', 'R', 'q', 'Q', 'R', 'S', 't', 'cat', 't', 'cat', 't', 'cat', 't', 'dog'])

    def test_expand(self):
        self.lsys.addRule('A', ['k', 'i'])
        self.lsys.addRule('E', ['i', 'A'], 3)
        self.assertEqual(self.lsys.expand('E'), ['i', 'A'])
        self.assertEqual(self.lsys.expand('A'), ['k', 'i'])
        self.lsys.addRule('E', ['j'])
        self.lsys.addRule('E', ['k'], 3)
        for i in range(20):
            self.assertIn(self.lsys.expand('E'), [['i', 'A'], ['j'], ['k']], "E did not expand properly")

        self.lsys.addRule('A', ['j'], 999) # 99.9% chance of choosing j, so we're gonna check that at least 90% are j
        count = 0
        for i in range(20):
            expansion = self.lsys.expand('A')
            if (expansion == ['j']):
                count += 1
        self.assertGreater(count, 17, "A did not expand to j often enough (%s/20), given that it has a 99.9%% chance of doing so" % (count))

    def test_setRasterFunction(self):
        self.fail("Not yet Implemented")

    def test_rasterize(self):
        self.fail("Not yet Implemented")
