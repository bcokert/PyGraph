import math

class RenderablePrimitive:
    """A class that baseclasses renderable objects, like spheres or quads. Provides the main interface, and the property setters/getters
    
    :Methods:
        - 'intersect': Returns the distance along the given ray from the given origin that the closest collision with this object occurs. Baseclass cannot collide
        - 'setDiffuseColor': Sets the float RGB color for diffuse light, and returns it
        - 'setSpecularColor': Sets the float RGB color for specular light, and returns it
        - 'setDiffuseConstant': Sets the float scale for diffuse light, and returns it
        - 'setSpecularConstant': Sets the float scale for specular light, and returns it
        - 'setShininess': Sets the int power factor for phong shininess. Usually between 1 and 200
        - 'normalAt': Returns the normal to the primitive at a particular point. May be garbage if the given point is not an intersection
    
    :Examples:
        >>> "This class should be extended by a primitive. See an extending primitive for usage"
    """

    def __init__(self):
        self.diffuse_color = [0.8, 0.8, 0.8]
        self.diffuse_constant = 1.0
        self.specular_color = [1.0, 1.0, 1.0]
        self.specular_constant = 1.0
        self.shininess = 50

    def setDiffuseColor(self, color="NONE"):
        if (self._isColor(color)):
            self.diffuse_color = list(color)
        return self.diffuse_color

    def setSpecularColor(self, color="NONE"):
        if (self._isColor(color)):
            self.specular_color = list(color)
        return self.specular_color

    def setDiffuseConstant(self, factor="NONE"):
        if (type(factor) == float and factor >= 0.0 and factor <= 1.0):
            self.diffuse_constant = factor
        return self.diffuse_constant

    def setSpecularConstant(self, factor="NONE"):
        if (type(factor) == float and factor >= 0.0 and factor <= 1.0):
            self.specular_constant = factor
        return self.specular_constant

    def setShininess(self, power="NONE"):
        if (type(power) == int and power > 0 and power < 1000):
            self.shininess = power
        return self.shininess

    def intersect(self, origin, ray):
        return "NONE"

    def normalAt(self, position):
        return "NONE"

    def _isColor(self, color):
        if (type(color) == list and len(color) == 3):
            for col in color:
                if (type(col) != float or col < 0.0 or col > 1.0):
                    return False
            return True
        return False
