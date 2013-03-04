from pygraph.render.Renderer import Renderer
from pygraph.generate.SimpleTurtle import SimpleTurtle
from pygraph.generate.LSystem import LSystem
from datetime import datetime
import cProfile

generation_depth = 40

cProfile.run("renderer = Renderer(1000, 1000)")
cProfile.run("turtle = SimpleTurtle(500, 999, 90, renderer)")
cProfile.run("lsys = LSystem()")

lsys.addRule('D', ['T', 'T', 'T', 'T', 'T', 'BT'])
lsys.addRule('T', ['s', 's', 'p', 'F', 'SS', 'o'])
lsys.addRule('F', ['r', 'r', 'r', 'r', 'r', 'r'])
lsys.addRule('SS', ['p', 'l', 'S', 'o'])
lsys.addRule('SS', ['p', 'r', 'S', 'o'])
lsys.addRule('SS', ['p', 'l', 'S', 'o', 'p', 'r', 'S', 'o'])
lsys.addRule('SS', [])
lsys.addRule('S', ['s'])
lsys.addRule('BT', ['p', 'l', 'l', 'l', 'l', 'B', 'o', 'p', 'r', 'r', 'r', 'r', 'B', 'o', 's', 'T', 'T', 'BT'])
lsys.addRule('B', ['s', 'SS', 'B'])

lsys.setRasterFunction('s', turtle.draw)
lsys.setRasterFunction('l', turtle.turnLeft)
lsys.setRasterFunction('r', turtle.turnRight)
lsys.setRasterFunction('p', turtle.push)
lsys.setRasterFunction('o', turtle.pop)

lsys.setRasterFunction('S', lambda : 1)
lsys.setRasterFunction('SS', lambda : 1)
lsys.setRasterFunction('BT', lambda : 1)
lsys.setRasterFunction('S', lambda : 1)
lsys.setRasterFunction('F', lambda : 1)
lsys.setRasterFunction('B', lambda : 1)
lsys.setRasterFunction('T', lambda : 1)

cProfile.run("gen = lsys.generate(['D'], generation_depth)")
cProfile.run("lsys.rasterize(gen)")
cProfile.run("renderer.render('sample2_depth' + str(generation_depth) + '_output.png')")
