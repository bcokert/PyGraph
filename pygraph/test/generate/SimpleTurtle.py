import unittest
from pygraph.generate.SimpleTurtle import SimpleTurtle
from pygraph.render.Renderer import Renderer
import math

class TestSimpleTurtle(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        self.renderer = Renderer(20, 20)
        self.turtle = SimpleTurtle(10, 19, 90, self.renderer)

    def test_interface(self):
        for func in ('turnRight', 'turnLeft', 'push', 'pop', 'reset', 'draw', 'setAngle', 'setRandomAngle', 'turnLeftRandom', 'turnRightRandom'):
            self.assertTrue(hasattr(self.turtle, func) and callable(getattr(self.turtle, func)), "Interface requires function: " + func)

    def test_turnRight(self):
        self.assertEqual(self.turtle.turnRight(), 60)
        self.assertEqual(self.turtle.turnRight(), 30)

    def test_turnLeft(self):
        self.assertEqual(self.turtle.turnLeft(), 120)
        self.assertEqual(self.turtle.turnLeft(), 150)
    
    def test_draw(self):
        self.turtle.draw(10)
        for i in range(10, 20):
            self.assertEqual(self.renderer.pixels[i], [255, 255, 255]*10 +  [0, 0, 0] + [255, 255, 255]*9)

    def test_push(self):
        self.turtle.push()
        self.turtle.draw(10)
        self.assertEqual([self.turtle.x, self.turtle.y], [10, 9])

    def test_pop(self):
        self.turtle.push()
        self.turtle.draw(10)
        self.turtle.pop()
        self.assertEqual([self.turtle.x, self.turtle.y], [10, 19])

    def test_reset(self):
        self.turtle.draw(10)
        self.turtle.reset(10, 10, 35)
        self.assertEqual([self.turtle.x, self.turtle.y, self.turtle.angle], [10, 10, 35.0])
        for i in range(10, 20): # the render was not touched, just the turtle
            self.assertEqual(self.renderer.pixels[i], [255, 255, 255]*10 +  [0, 0, 0] + [255, 255, 255]*9)

    def test_setAngle(self):
        self.turtle.setAngle(66)
        self.assertEqual(self.turtle.turn_angle, 66.0)
        self.turtle.setAngle(366)
        self.assertEqual(self.turtle.turn_angle, 6.0)
        self.turtle.setAngle(-6)
        self.assertEqual(self.turtle.turn_angle, 354.0)

    def test_setRandomAngle(self):
        self.turtle.setRandomAngle(66)
        self.assertEqual(self.turtle.random_angle, 66.0)
        self.turtle.setRandomAngle(366)
        self.assertEqual(self.turtle.random_angle, 6.0)
        self.turtle.setRandomAngle(-6)
        self.assertEqual(self.turtle.random_angle, 354.0)

    def test_integration_turtleDrawing(self):
        self.turtle.reset(1,1,0)
        self.turtle.setAngle(90)
        self.turtle.draw(10)
        self.turtle.turnRight()
        self.turtle.draw(10)
        self.turtle.turnRight()
        self.turtle.draw(10)
        self.turtle.turnRight()
        self.turtle.draw(10)
        self.turtle.reset(3,3,315)
        self.turtle.push()
        self.turtle.draw(3.0/math.cos(math.radians(45)))
        self.turtle.pop()
        self.turtle.setAngle(45)
        self.turtle.turnLeft()
        self.turtle.draw(3)
        self.renderer.render('./integration_turtleDrawing.png')

        for i in [2, 7, 8, 9, 10]:
            self.assertEqual(self.renderer.pixels[i], [255, 255, 255] +  [0, 0, 0] + [255, 255, 255]*9 + [0, 0, 0] + [255, 255, 255]*8)

        self.assertEqual(self.renderer.pixels[3], [255, 255, 255] +  [0, 0, 0] + [255, 255, 255] + [0,0,0]*4 + [255, 255, 255]*4 + [0,0,0] + [255, 255, 255]*8)
        self.assertEqual(self.renderer.pixels[4], [255, 255, 255] +  [0, 0, 0] + [255, 255, 255]*2 + [0,0,0] + [255, 255, 255]*6 + [0,0,0] + [255, 255, 255]*8)
        self.assertEqual(self.renderer.pixels[5], [255, 255, 255] +  [0, 0, 0] + [255, 255, 255]*3 + [0,0,0] + [255, 255, 255]*5 + [0,0,0] + [255, 255, 255]*8)
        self.assertEqual(self.renderer.pixels[6], [255, 255, 255] +  [0, 0, 0] + [255, 255, 255]*4 + [0,0,0] + [255, 255, 255]*4 + [0,0,0] + [255, 255, 255]*8)

        self.assertEqual(self.renderer.pixels[1], [255, 255, 255] +  [0, 0, 0]*11 + [255, 255, 255]*8)
        self.assertEqual(self.renderer.pixels[11], [255, 255, 255] +  [0, 0, 0]*11 + [255, 255, 255]*8)
