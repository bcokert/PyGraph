import unittest
import importlib
import time
import sys
import traceback
import os
import types
import re
import math
all_tests = []

def addTest(module):
    mod = importlib.import_module(module)
    all_tests.append(unittest.TestLoader().loadTestsFromModule(mod))

#####################################################################################
"""Suite_Draw"""
#addTest('pygraph.test.draw.shapes.BasicShapes')

"""Suite_Vector"""
addTest('pygraph.test.utility.Vector3f')

"""Suite_Render"""
addTest('pygraph.test.render.Renderer')

"""Suite_LSystem"""
#addTest('pygraph.test.generate.LSystem')

"""Suite_SimpleTurtle"""
#addTest('pygraph.test.generate.SimpleTurtle')

"""Suite_RenderablePrimitive"""
addTest('pygraph.test.raytrace.primitives.RenderablePrimitive')

"""Suite_Raytracer"""
#addTest('pygraph.test.raytrace.Raytracer')

#####################################################################################

class customResults(unittest.TestResult):
    separator1 = '=' * 70 
    separator2 = '-' * 70
    
    def __init__(self, stream):
        unittest.TestResult.__init__(self)
        self.stream = stream

    def getDescription(self, test):
        regexp = re.search('([^\.]+)\'>', str(test.__class__))
        return regexp.group(1) + ': '+ test._testMethodName

    def printErrors(self):
        self.stream.writeln()
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            self.stream.writeln("%s %s: %s %s" % ('='*10, flavour,self.getDescription(test), '='*(60-len(self.getDescription(test)))))

            #regexp = re.search('.+\n.+(line \d+.+)\n\s*(.+)\n(.+)', err)
            #self.stream.writeln("%s\n%s: %s\n" % (regexp.group(3), regexp.group(1), regexp.group(2)))
            self.stream.writeln(err)

    def startTest(self, test):
        unittest.TestResult.startTest(self, test)
        self.stream.write(self.getDescription(test))
        self.stream.write(" ... ") 

    def addSuccess(self, test):
        unittest.TestResult.addSuccess(self, test)
        self.stream.writeln("pass")
        
    def addError(self, test, err):
        unittest.TestResult.addError(self, test, err)
        self.stream.writeln("ERROR")
        
    def addFailure(self, test, err):
        unittest.TestResult.addFailure(self, test, err)
        self.stream.writeln("FAIL")

class testRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return customResults(self.stream)

 
runner = testRunner(verbosity=2)
result = runner.run(unittest.TestSuite(all_tests))
