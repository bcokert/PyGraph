import unittest
import os
from pygraph.raytrace.Raytracer import Raytracer

class TestRaytracer(unittest.TestCase):

    def setUp(self):
        self.raytracer = Raytracer()

    def test_interface(self):
        for func in ('addSphere', 'addPointLight', 'setAmbient', 'setCamera', 'setOutput', 'render'):
            self.assertTrue(hasattr(self.raytracer, func) and callable(getattr(self.raytracer, func)), "Interface requires function: " + func)

    def test_addSphere(self):
        self.fail("Not yet Implemented")

    def test_addPointLight(self):
        self.fail("Not yet Implemented")

    def test_setAmbient(self):
        self.fail("Not yet Implemented")

    def test_setCamera(self):
        self.fail("Not yet Implemented")

    def test_setOutput(self):
        self.fail("Not yet Implemented")

    def test_render(self):
        self.fail("Not yet Implemented")

    def test_integration_renderComplexScene(self):
        self.fail("Not yet Implemented")
