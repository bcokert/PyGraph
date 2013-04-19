import unittest
import os
from pygraph.raytrace.primitives.RenderablePrimitive import RenderablePrimitive
from pygraph.utility.Vector3f import Vector3f

class TestRenderablePrimitive(unittest.TestCase):

    def setUp(self):
        self.renderable = RenderablePrimitive()

    def test_interface(self):
        for func in ('intersect', 'setDiffuseColor', 'setSpecularColor', 'setDiffuseConstant', 'setSpecularConstant', 'setShininess', 'normalAt'):
            self.assertTrue(hasattr(self.renderable, func) and callable(getattr(self.renderable, func)), "Interface requires function: " + func)

    def test_intersect(self):
        self.assertEqual(self.renderable.intersect(Vector3f(1.0, 1.0, 1.0), Vector3f(1.0, 1.0, 1.0)), "NONE")
        self.assertEqual(self.renderable.intersect(Vector3f(1.0, 5.0, 7.0), Vector3f(1.0, 2.0, 5.0)), "NONE")

    def test_setDiffuseColor(self):
        self.assertEqual(self.renderable.setDiffuseColor([1.0, 1.0, 1.0]), [1.0, 1.0, 1.0])
        self.assertEqual(self.renderable.setDiffuseColor([0.0, 1.0, 0.34]), [0.0, 1.0, 0.34])
        self.assertEqual(self.renderable.setDiffuseColor([-1.0, 1.0, 1.0]), [0.0, 1.0, 0.34])
        self.assertEqual(self.renderable.setDiffuseColor([1.0, 1.2, 1.0]), [0.0, 1.0, 0.34])
        self.assertEqual(self.renderable.setDiffuseColor(), [0.0, 1.0, 0.34])

    def test_setSpecularColor(self):
        self.assertEqual(self.renderable.setSpecularColor([1.0, 1.0, 1.0]), [1.0, 1.0, 1.0])
        self.assertEqual(self.renderable.setSpecularColor([0.0, 1.0, 0.34]), [0.0, 1.0, 0.34])
        self.assertEqual(self.renderable.setSpecularColor([-1.0, 1.0, 1.0]), [0.0, 1.0, 0.34])
        self.assertEqual(self.renderable.setSpecularColor([1.0, 1.2, 1.0]), [0.0, 1.0, 0.34])
        self.assertEqual(self.renderable.setSpecularColor(), [0.0, 1.0, 0.34])

    def test_setDiffuseConstant(self):
        self.assertEqual(self.renderable.setDiffuseConstant(1.0), 1.0)
        self.assertEqual(self.renderable.setDiffuseConstant(0.0), 0.0)
        self.assertEqual(self.renderable.setDiffuseConstant(-1.0), 0.0)
        self.assertEqual(self.renderable.setDiffuseConstant(1.1), 0.0)
        self.assertEqual(self.renderable.setDiffuseConstant(1), 0.0)
        self.assertEqual(self.renderable.setDiffuseConstant(), 0.0)

    def test_setSpecularConstant(self):
        self.assertEqual(self.renderable.setSpecularConstant(1.0), 1.0)
        self.assertEqual(self.renderable.setSpecularConstant(0.0), 0.0)
        self.assertEqual(self.renderable.setSpecularConstant(-1.0), 0.0)
        self.assertEqual(self.renderable.setSpecularConstant(1.1), 0.0)
        self.assertEqual(self.renderable.setSpecularConstant(1), 0.0)
        self.assertEqual(self.renderable.setSpecularConstant(), 0.0)

    def test_setShininess(self):
        self.assertEqual(self.renderable.setShininess(1), 1)
        self.assertEqual(self.renderable.setShininess(0.0), 1)
        self.assertEqual(self.renderable.setShininess(-1), 1)
        self.assertEqual(self.renderable.setShininess(11), 11)
        self.assertEqual(self.renderable.setShininess(102), 102)
        self.assertEqual(self.renderable.setShininess(), 102)

    def test_normalAt(self):
        self.assertEqual(self.renderable.normalAt(Vector3f(1.0, 1.0, 1.0)), "NONE")
        self.assertEqual(self.renderable.normalAt(Vector3f(1.0, 5.0, 7.0)), "NONE")
