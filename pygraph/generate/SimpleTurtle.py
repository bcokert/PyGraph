from pygraph.draw.shapes.BasicShapes import BasicShapes
import math

class SimpleTurtle:
    """Implements the drawing functions and stack for a basic turtle. Must be driven externally (eg: by LSystem)
    
    :Functions:
        - 'turnRight': Turns the turtle CW by angle
        - 'turnLeft': Turns the turtle CCW by angle
        - 'draw': Draws a line in the current direction
        - 'push': Pushes the current position and angle onto the stack
        - 'pop': Restores the previous position and angle from the stack
        - 'render': Renders the current session
        - 'reset': Resets the current session
    
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
        self.renderer = renderer
        self.shapes = BasicShapes(renderer.buffer_x, renderer.buffer_y)
        self.stack = []

    def turnRight(self, angle=25.0):
        self.angle -= angle
        while (self.angle < 0.0):
            self.angle += 360.0
        return self.angle

    def turnLeft(self, angle=25.0):
        self.angle += angle
        while (self.angle >= 360.0):
            self.angle -= 360.0
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
