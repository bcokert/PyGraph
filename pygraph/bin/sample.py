from pygraph.render.Renderer import Renderer
from pygraph.generate.SimpleTurtle import SimpleTurtle
from pygraph.generate.LSystem import LSystem
from datetime import datetime

time = datetime.now()
print "Start: " + str(datetime.now() - time); time = datetime.now()
renderer = Renderer(1000, 1000)
print "Create Renderer: " + str(datetime.now() - time); time = datetime.now()
turtle = SimpleTurtle(500, 999, 95, renderer)
print "Create Turtle: " + str(datetime.now() - time); time = datetime.now()
lsys = LSystem()
print "Create LSystem: " + str(datetime.now() - time); time = datetime.now()

lsys.addRule('X', ['F', 'l', 'p', 'p', 'X', 'o', 'r', 'X', 'o', 'r', 'F', 'p', 'r', 'F', 'X', 'o', 'l', 'X'])
lsys.addRule('F', ['F', 'F'])
print "Create Rules: " + str(datetime.now() - time); time = datetime.now()

lsys.setRasterFunction('F', turtle.draw)
lsys.setRasterFunction('X', lambda : 1)
lsys.setRasterFunction('l', turtle.turnLeft)
lsys.setRasterFunction('r', turtle.turnRight)
lsys.setRasterFunction('p', turtle.push)
lsys.setRasterFunction('o', turtle.pop)
print "Set Raster Functions: " + str(datetime.now() - time); time = datetime.now()

gen = lsys.generate(['X'], 7)
print "Generate production: " + str(datetime.now() - time); time = datetime.now()
lsys.rasterize(gen)
print "Rasterize production: " + str(datetime.now() - time); time = datetime.now()
renderer.render('sample_output.png')
print "Render: " + str(datetime.now() - time); time = datetime.now()
