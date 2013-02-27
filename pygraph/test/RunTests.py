import unittest
runner = unittest.TextTestRunner(verbosity=2)

"""Suite_Draw"""
import pygraph.test.draw.shapes.BasicShapes as TC_BasicShapes
suite_draw = unittest.TestLoader().loadTestsFromModule(TC_BasicShapes)

"""Suite_Render"""
import pygraph.test.render.Renderer as TC_Renderer
suite_render = unittest.TestLoader().loadTestsFromModule(TC_Renderer)

all_tests = unittest.TestSuite([suite_draw, suite_render])
result = runner.run(all_tests)
