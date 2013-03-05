from pygraph.render.Renderer import Renderer
from pygraph.generate.SimpleTurtle import SimpleTurtle
from pygraph.generate.LSystem import LSystem
from datetime import datetime
import cProfile

generation_depth = 30

cProfile.run("renderer = Renderer(1000, 1000)")
cProfile.run("turtle = SimpleTurtle(500, 999, 90, renderer)")
cProfile.run("lsys = LSystem()")

turtle.setAngle(30)
turtle.setRandomAngle(3)

lsys.addRule('D', ['T', 'T', 'T', 'T', 'T', 'BT'])
lsys.addRule('T', ['s', 's', 'p', 'F', 'SS', 'o'])
lsys.addRule('F', ['r', 'r', 'r', 'r', 'r', 'r'])
lsys.addRule('SS', ['p', 'l', 'rr', 'rr', 'rr', 'rr', 'rr', 'S', 'o', 'p', 'r', 'll', 'll', 'll', 'll', 'll', 'S', 'o'])
lsys.addRule('S', ['s', 's'])
lsys.addRule('S', [])
lsys.addRule('BT', ['p', 'l', 'l', 'l', 'l', 'rr', 'BL', 'o', 'p', 'r', 'r', 'r', 'r', 'll', 'BR', 'o', 's', 'T', 'T', 'BT'])
lsys.addRule('BL', ['ll', 's', 'SS', 's', 'SS', 'BL'])
lsys.addRule('BR', ['rr', 's', 'SS', 's', 'SS', 'BR'])

lsys.setRasterFunction('s', turtle.draw)
lsys.setRasterFunction('l', turtle.turnLeft)
lsys.setRasterFunction('r', turtle.turnRight)
lsys.setRasterFunction('ll', turtle.turnLeftRandom)
lsys.setRasterFunction('rr', turtle.turnRightRandom)
lsys.setRasterFunction('p', turtle.push)
lsys.setRasterFunction('o', turtle.pop)

lsys.setRasterFunction('S', lambda : 1)
lsys.setRasterFunction('SS', lambda : 1)
lsys.setRasterFunction('BT', lambda : 1)
lsys.setRasterFunction('S', lambda : 1)
lsys.setRasterFunction('F', lambda : 1)
lsys.setRasterFunction('BR', lambda : 1)
lsys.setRasterFunction('BL', lambda : 1)
lsys.setRasterFunction('T', lambda : 1)
lsys.setRasterFunction('D', lambda : 1)

cProfile.run("gen = lsys.generate(['D'], generation_depth)")
cProfile.run("lsys.rasterize(gen)")
cProfile.run("renderer.render('sample2_depth' + str(generation_depth) + '_output.png')")
