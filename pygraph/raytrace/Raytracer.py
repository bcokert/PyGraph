from pygraph.render.Renderer import Renderer

class Raytracer:
    """A class that implements a basic ray tracer. Not intended to provide complex functions, but rather to call them.
    
    :Methodss:
        - 'render': Calculates the pixels and outputs them with its own Renderer object
        - 'addSphere': Basic sample function that adds a sphere to the scene
    
    :Examples:
        >>> from pygraph.raytrace.Raytracer import Raytracer
        >>> raytracer = Raytracer()
        >>> raytracer.addSphere([0, 0, 0], 1) # x,y,z radius
        >>> raytracer.addPointLight([1, -2, 1], [255, 255, 255], 2) # [xyz], [RGB], strength (relative)
        >>> raytracer.setAmbient([255, 255, 255], 0.1) # RGB, Alpha
        >>> raytracer.setCamera([0, -2, 0], [0, 1, 0], [0, 0, 1], 35) # [xyz], [forward], [up], fov
        >>> raytracer.setOutput('test.png', 500, 500) # name, width, height
        >>> raytracer.render(3) # max bounces
    """

    def __init__(self):
        pass

    def addSphere(self):
        pass

    def addPointLight(self):
        pass

    def setAmbient(self):
        pass

    def setCamera(self):
        pass

    def setOutput(self):
        pass

    def render(self):
        pass
