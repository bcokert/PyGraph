import unittest
import os
from time import time
from pygraph.raytrace.Raytracer import Raytracer
from pygraph.utility.Vector3f import Vector3f

class TestRaytracer(unittest.TestCase):

    def setUp(self):
        self.raytracer = Raytracer()
        self.v1 = Vector3f(0.0,0.0,0.0)
        self.v2 = Vector3f(1.0,1.0,1.0)
        self.v3 = Vector3f(2.0,2.0,2.0)
        self.rv1 = Vector3f(1, 0, 0)
        self.rv2 = Vector3f(0, 1, 0)
        self.rv3 = Vector3f(0, 0, 1)

    def test_interface(self):
        for func in ('addSphere', 'addPointLight', 'setAmbient', 'setCamera', 'setOutput', 'render', 'findCollision', 'calculateColor'):
            self.assertTrue(hasattr(self.raytracer, func) and callable(getattr(self.raytracer, func)), "Interface requires function: " + func)

    def test_addSphere(self):
        self.raytracer.addSphere(self.v1, 2)
        self.raytracer.addSphere(self.v2, 4)
        v1s = (self.raytracer.spheres[0][0].toList(), self.raytracer.spheres[0][1])
        v2s = (self.raytracer.spheres[1][0].toList(), self.raytracer.spheres[1][1])
        self.assertEqual(v1s, (self.v1.toList(), 2.0))
        self.assertEqual(v2s, (self.v2.toList(), 4.0))

    def test_addPointLight(self):
        self.raytracer.addPointLight(self.v1, [.4, .4, .4], 2)
        self.raytracer.addPointLight(self.v2, [.8, .8, .8], 6)
        l1 = self.raytracer.point_lights[0]
        l2 = self.raytracer.point_lights[1]
        self.assertEqual((l1[0].toList(), l1[1], l1[2]), (self.v1.toList(), [.4, .4, .4], 2.0))
        self.assertEqual((l2[0].toList(), l2[1], l2[2]), (self.v2.toList(), [.8, .8, .8], 6.0))

    def test_setAmbient(self):
        self.assertEqual(self.raytracer.ambient, [0.0, 0.0, 0.0])
        self.raytracer.setAmbient([.2, .2, .2])
        self.assertEqual(self.raytracer.ambient, [.2, .2, .2])

    def test_setOutput(self):
        self.raytracer.setOutput('test.png', [700, 800])
        self.assertEqual(self.raytracer.output_file, 'test.png')
        self.assertEqual(self.raytracer.output_size, [700, 800])
        self.assertEqual(self.raytracer.renderer.buffer_x, 700)
        self.assertEqual(self.raytracer.renderer.buffer_y, 800)

    def test_setCamera(self):
        self.assertEqual(self.raytracer.camera, [])
        self.raytracer.setCamera(self.v1, self.rv1 * 3, self.rv2 * 5, 70)
        self.assertEqual(self.raytracer.camera[0].toList(), self.v1.toList())
        self.assertEqual(self.raytracer.camera[1].toList(), self.rv1.toList())
        self.assertEqual(self.raytracer.camera[2].toList(), self.rv2.toList())
        self.assertEqual(self.raytracer.camera[3].toList(), self.rv3.toList())
        self.assertEqual(self.raytracer.camera[4], 70.0)

    def test_render(self):
        self.raytracer.setOutput('test_render_output.png', [100, 100])
        self.raytracer.setAmbient([0.2, 0.2, 0.2])
        self.raytracer.addSphere(Vector3f(0, 1, 0), 0.25)
        self.raytracer.addPointLight(Vector3f(1.0,-1.0,1.0), [1.0, 1.0, 1.0], 1)
        self.raytracer.setCamera(Vector3f(0.0, 0.0, 0.0), Vector3f(0.0, 1.0, 0.0), Vector3f(0.0, 0.0, 1.0), 70)
        start = time()
        self.raytracer.render()
        end = time()
        self.assertTrue(os.path.exists('./test_render_output.png'), "The file wasn't created upon rendering")
        print "Rendered a 100 * 100 image with 1 sphere and 1 light in {} seconds".format(end - start)

    def test_findCollision(self):
        sphere = Vector3f(2.0, 0.0, 0.0)
        self.raytracer.addSphere(sphere, 1)
        self.raytracer.setCamera(Vector3f(0.0, 0.0, 0.0), Vector3f(1.0, 0.0, 0.0), Vector3f(0.0, 0.0, 1.0), 70)
        col = self.raytracer.findCollision(Vector3f(1.0, 0.0, 0.0))
        self.assertEqual((col[0], col[1][0].toList(), col[1][1]), (1.0, sphere.toList(), 1))

    def test_integration_renderComplexScene(self):
        self.raytracer.setOutput('test_integration_renderComplexScene.png', [300, 300])
        self.raytracer.setAmbient([0.2, 0.2, 0.2])
        self.raytracer.addSphere(Vector3f(0.0, 1.0, 0.0), 0.5)
        self.raytracer.addSphere(Vector3f(-1.0, 1.0, 0.0), 0.4)
        self.raytracer.addSphere(Vector3f(0.0, -1.0, 0.7), 0.1)
        self.raytracer.addPointLight(Vector3f(1.0,-4.0,1.0), [1.0, 1.0, 1.0], 2)
        self.raytracer.setCamera(Vector3f(0.0, -6.0, 0.0), Vector3f(0.0, 1.0, 0.0), Vector3f(0.0, 0.0, 1.0), 70)
        start = time()
        self.raytracer.render()
        end = time()
        self.assertTrue(os.path.exists('./test_integration_renderComplexScene.png'), "The file wasn't created upon rendering")
        print "Rendered a 300 * 300 image with 3 spheres and 1 light in {} seconds".format(end - start)
