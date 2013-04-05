import unittest
import os
from pygraph.raytrace.Raytracer import Raytracer

class TestRaytracer(unittest.TestCase):

    def setUp(self):
        self.raytracer = Raytracer()

    def test_interface(self):
        for func in ('addSphere', 'addPointLight', 'setAmbient', 'setCamera', 'setOutput', 'render', 'normalize', 'crossProduct', 'vectorAdd', 'dotProduct', 'findCollision', 'calculateColor'):
            self.assertTrue(hasattr(self.raytracer, func) and callable(getattr(self.raytracer, func)), "Interface requires function: " + func)

    def test_addSphere(self):
        self.raytracer.addSphere([0.0,0.0,0.0], 2)
        self.raytracer.addSphere([1.0,1.0,1.0], 4)
        self.assertEqual(self.raytracer.spheres, [[[0.0, 0.0, 0.0], 2.0], [[1.0, 1.0, 1.0], 4.0]])

    def test_addPointLight(self):
        self.raytracer.addPointLight([0.0,0.0,0.0], [100, 100, 100], 2)
        self.raytracer.addPointLight([1.0,1.0,1.0], [200, 200, 200], 6)
        self.assertEqual(self.raytracer.point_lights, [[[0.0,0.0,0.0], [100, 100, 100], 2.0], [[1.0,1.0,1.0], [200, 200, 200], 6.0]])

    def test_setAmbient(self):
        self.assertEqual(self.raytracer.ambient, [0,0,0])
        self.raytracer.setAmbient([100, 100, 100])
        self.assertEqual(self.raytracer.ambient, [100, 100, 100])

    def test_setOutput(self):
        self.raytracer.setOutput('test.png', [700, 800])
        self.assertEqual(self.raytracer.output_file, 'test.png')
        self.assertEqual(self.raytracer.output_size, [700, 800])
        self.assertEqual(self.raytracer.renderer.buffer_x, 700)
        self.assertEqual(self.raytracer.renderer.buffer_y, 800)

    def test_normalize(self):
        self.assertEqual(self.raytracer.normalize([1, 2, 2]), [1.0/3, 2.0/3, 2.0/3])
        self.assertEqual(self.raytracer.normalize([1, 0, 0]), [1.0, 0.0, 0.0])
        self.assertEqual(self.raytracer.normalize([0, 0, 1]), [0.0, 0.0, 1.0])

    def test_crossProduct(self):
        self.assertEqual(self.raytracer.crossProduct([1, 0, 0], [0, 1, 0]), [0.0, 0.0, 1.0])
        self.assertEqual(self.raytracer.crossProduct([0, 1, 0], [0, 0, 1]), [1.0, 0.0, 0.0])
        self.assertEqual(self.raytracer.crossProduct([0, 0, 1], [1, 0, 0]), [0.0, 1.0, 0.0])

    def test_setCamera(self):
        self.assertEqual(self.raytracer.camera, [])
        self.raytracer.setCamera([0.0, -2.0, 0.0], [0.0, 4.0, 0.0], [0.0, 0.0, 2.0], 70)
        self.assertEqual(self.raytracer.camera, [[0.0, -2.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0], 70])

    def test_vectorAdd(self):
        self.assertEqual(self.raytracer.vectorAdd([1,2,3], [4,5,6]), [5, 7, 9])

    def test_vectorSubtract(self):
        self.assertEqual(self.raytracer.vectorSubtract([1,2,3], [4,5,6]), [-3, -3, -3])
        self.assertEqual(self.raytracer.vectorSubtract([1,0,1], [0,1,0]), [1, -1, 1])

    def test_dotProduct(self):
        self.assertEqual(self.raytracer.dotProduct([1, 0, 0], [0, 1, 0]), 0.0)
        self.assertEqual(self.raytracer.dotProduct([0, 1, 0], [0, 0, 1]), 0.0)
        self.assertEqual(self.raytracer.dotProduct([0, 0, 1], [1, 0, 0]), 0.0)
        self.assertEqual(self.raytracer.dotProduct([1, 2, 3], [4, 5, 6]), 32.0)

    def test_calculateColor(self):
        self.fail("Cannot test yet")

    def test_render(self):
        self.raytracer.setOutput('test_render_output.png', [500, 500])
        self.raytracer.addSphere([0.0, 1.0, 0.0], 0.25)
        self.raytracer.addPointLight([1.0,-1.0,1.0], [255, 255, 255], 1)
        self.raytracer.setCamera([0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], 70)
        self.raytracer.render()
        self.assertTrue(os.path.exists('./test_render_output.png'), "The file wasn't created upon rendering")

    def test_findCollision(self):
        self.raytracer.addSphere([2.0, 0.0, 0.0], 1)
        self.raytracer.setCamera([0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0], 70)
        self.assertEqual(self.raytracer.findCollision([1.0, 0.0, 0.0]), [1.0, [[2.0, 0.0, 0.0], 1]])

    def test_integration_renderComplexScene(self):
        self.raytracer.setOutput('test_integration_renderComplexScene.png', [800, 800])
        self.raytracer.addSphere([0.0, 1.0, 0.0], 0.5)
        self.raytracer.addSphere([-1.0, 1.0, 0.0], 0.4)
        self.raytracer.addSphere([0.0, -1.0, 0.7], 0.1)
        self.raytracer.addPointLight([1.0,-4.0,1.0], [255, 255, 255], 2)
        self.raytracer.setCamera([0.0, -3.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], 70)
        self.raytracer.render()
        self.assertTrue(os.path.exists('./test_integration_renderComplexScene.png'), "The file wasn't created upon rendering")
