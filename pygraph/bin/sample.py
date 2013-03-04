from pygraph.render.Renderer import Renderer
from pygraph.generate.SimpleTurtle import SimpleTurtle
from pygraph.generate.LSystem import LSystem
from datetime import datetime
import cProfile

generation_depth = 6

cProfile.run("renderer = Renderer(1000, 1000)")
cProfile.run("turtle = SimpleTurtle(10, 999, 65, renderer)")
cProfile.run("lsys = LSystem()")

lsys.addRule('X', ['F', 'l', 'p', 'p', 'X', 'o', 'r', 'X', 'o', 'r', 'F', 'p', 'r', 'F', 'X', 'o', 'l', 'X'])
lsys.addRule('F', ['F', 'F'])

lsys.setRasterFunction('F', turtle.draw)
lsys.setRasterFunction('X', lambda : 1)
lsys.setRasterFunction('l', turtle.turnLeft)
lsys.setRasterFunction('r', turtle.turnRight)
lsys.setRasterFunction('p', turtle.push)
lsys.setRasterFunction('o', turtle.pop)

cProfile.run("gen = lsys.generate(['X'], generation_depth)")
cProfile.run("lsys.rasterize(gen)")
cProfile.run("renderer.render('depth' + str(generation_depth) + '_output.png')")
