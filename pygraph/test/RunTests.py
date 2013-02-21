import unittest
runner = unittest.TextTestRunner(verbosity=2)

"""Suite_Draw"""
import pygraph.test.draw.shapes.BasicShapes as TC_BasicShapes
suite_draw = unittest.TestLoader().loadTestsFromModule(TC_BasicShapes)
result = runner.run(suite_draw)
