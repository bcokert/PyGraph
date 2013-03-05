from pygraph.draw.shapes.BasicShapes import BasicShapes
import math
import random

class SimpleTurtle:
    """Implements the drawing functions and stack for a basic turtle. Must be driven externally (eg: by LSystem)
    
    :Functions:
        - 'turnRight': Turns the turtle CW by angle
        - 'turnLeft': Turns the turtle CCW by angle
        - 'turnRightRandom': Turns the turtle CW by a random number in [0, random_angle)
        - 'turnLeftRandom': Turns the turtle CCW by a random number in [0, random_angle)
        - 'draw': Draws a line in the current direction
        - 'push': Pushes the current position and angle onto the stack
        - 'pop': Restores the previous position and angle from the stack
        - 'render': Renders the current session
        - 'reset': Resets the current session
        - 'setAngle': Sets the value of angle for turnLeft and turnRight
        - 'setRandomAngle': Sets the value of random_angle for turnLeftRandom and turnRightRandom
    
    :Examples:
    >>> from pygraph.generate.SimpleTurtle import SimpleTurtle
    >>> turtle = SimpleTurtle(128,0, 90) # x, y, up
    >>> turtle.draw()
    >>> turtle.push()
    >>> turtle.turnLeft(30)
    >>> turtle.draw()
    >>> turtle.pop()
    >>> turtle.turnRight(30)
    >>> turtle.draw()
    >>> turtle.render('./test.png')
    """

    def __init__(self, xpos, ypos, angle, renderer):
        self.x = xpos
        self.y = ypos
        self.angle = float(angle)
        self.turn_angle = 30.0
        self.random_angle = 5.0
        self.renderer = renderer
        self.shapes = BasicShapes(renderer.buffer_x, renderer.buffer_y)
        self.stack = []

    def turnRight(self):
        self.angle -= self.turn_angle
        self.angle %= 360
        return self.angle

    def turnLeft(self):
        self.angle += self.turn_angle
        self.angle %= 360
        return self.angle

    def turnRightRandom(self):
        self.angle -= random.random()*self.random_angle
        self.angle %= 360
        return self.angle

    def turnLeftRandom(self):
        self.angle += random.random()*self.random_angle
        self.angle %= 360
        return self.angle

    def push(self):
        self.stack.append([self.x, self.y, self.angle])

    def pop(self):
        self.x, self.y, self.angle = self.stack.pop()

    def reset(self, xpos, ypos, angle):
        self.x = xpos
        self.y = ypos
        self.angle = float(angle)

    def draw(self, distance=5):
        newx = int(round(float(self.x) + math.cos(math.radians(self.angle)) * float(distance)))
        newy = int(round(float(self.y) - math.sin(math.radians(self.angle)) * float(distance)))
        self.renderer.drawOver(self.shapes.drawLine(self.x, self.y, newx, newy, [0,0,0]))
        self.x = newx
        self.y = newy

    def setAngle(self, angle):
        self.turn_angle = float(angle % 360)
        return self.turn_angle

    def setRandomAngle(self, angle):
        self.random_angle = float(angle % 360)
        return self.random_angle
