import unittest
import os
from pygraph.test.raytrace.primitives.RenderablePrimitive import TestRenderablePrimitive
from pygraph.raytrace.primitives.Sphere import Sphere
from pygraph.utility.Vector3f import Vector3f

class TestSphere(TestRenderablePrimitive):

    def setUp(self):
        self.renderable = Sphere()
        self.renderable2 = Sphere()

    def test_interface(self):
        super(TestSphere, self).test_interface()
        for func in ['setRadius']:
            self.assertTrue(hasattr(self.renderable, func) and callable(getattr(self.renderable, func)), "Interface requires function: " + func)

    def test_intersect(self):
        sphere1 = Sphere(Vector3f(2.0, 0.0, 0.0), 1)
        sphere2 = Sphere(Vector3f(-2.0, 0.0, 0.0), 1)

        self.assertEqual(sphere1.intersect(Vector3f(0, 0, 0), Vector3f(1, 0, 0)), 1.0)
        self.assertEqual(sphere1.intersect(Vector3f(0, 0, 0), Vector3f(0, 1, 0)), "NONE")

        self.assertEqual(sphere2.intersect(Vector3f(0, 0, 0), Vector3f(1, 0, 0)), "NONE")

    def test_normalAt(self):
        sphere1 = Sphere(Vector3f(2.0, 0.0, 0.0), 1)

        self.assertEqual(sphere1.normalAt(Vector3f(1, 0, 0)).toList(), [-1, 0, 0])
        self.assertEqual(sphere1.normalAt(Vector3f(1, 0.1, 0)).toList(), Vector3f(-1, 0.1, 0.0).toList())
        self.assertEqual(sphere1.normalAt(Vector3f(5, 0, 0)).toList(), [3, 0, 0])

    def test_setRadius(self):
        self.assertEqual(self.renderable.setRadius(1.0), 1.0)
        self.assertEqual(self.renderable.setRadius(0.0), 1.0)
        self.assertEqual(self.renderable.setRadius(-1.0), 1.0)
        self.assertEqual(self.renderable.setRadius(1.1), 1.1)
        self.assertEqual(self.renderable.setRadius(0.0005), 0.0005)
        self.assertEqual(self.renderable.setRadius(), 0.0005)
        self.assertEqual(self.renderable.setRadius(1), 1.0)
