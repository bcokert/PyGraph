from pygraph.render.Renderer import Renderer
from pygraph.generate.SimpleTurtle import SimpleTurtle
from pygraph.generate.LSystem import LSystem
from datetime import datetime
import cProfile

generation_depth = 2

cProfile.run("renderer = Renderer(1000, 1000)")
cProfile.run("turtle = SimpleTurtle(500, 500, 60, renderer)")
cProfile.run("lsys = LSystem()")

turtle.setAngle(60)
turtle.setRandomAngle(3)

lsys.addRule('D', ['S', 'r', 'r', 'S', 'r', 'r', 'S'])
lsys.addRule('S', ['S', 'l', 'S', 'r', 'r', 'S', 'l', 'S'])

lsys.setRasterFunction('s', turtle.draw)
lsys.setRasterFunction('l', turtle.turnLeft)
lsys.setRasterFunction('r', turtle.turnRight)
lsys.setRasterFunction('ll', turtle.turnLeftRandom)
lsys.setRasterFunction('rr', turtle.turnRightRandom)
lsys.setRasterFunction('p', turtle.push)
lsys.setRasterFunction('o', turtle.pop)

lsys.setRasterFunction('S', turtle.draw)
lsys.setRasterFunction('D', lambda : 1)

cProfile.run("gen = lsys.generate(['D'], generation_depth)")
cProfile.run("lsys.rasterize(gen)")
cProfile.run("renderer.render('kochtriangle' + str(generation_depth) + '_output.png')")
