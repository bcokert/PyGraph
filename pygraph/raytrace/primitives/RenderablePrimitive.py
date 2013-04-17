from pygraph.raytrace.Raytracer import VectorError
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
        >>> print("This class should be extended by a primitive. See an extending primitive for usage")
    """

    def __init__(self):
        self.diffuse_color = [0.8, 0.8, 0.8]
        self.diffuse_constant = 1.0
        self.specular_color = [1.0, 1.0, 1.0]
        self.specular_constant = 1.0
        self.shininess = 50

    def setDiffuseColor(self, color="NONE"):
        try:
            self._verifyVector(color, v_type="RGB")
        except VectorError, e:
            return self.diffuse_color

        self.diffuse_color = list(color)
        return self.diffuse_color

    def setSpecularColor(self, color="NONE"):
        try:
            self._verifyVector(color, v_type="RGB")
        except VectorError, e:
            return self.specular_color

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
        self._verifyVector(origin)
        self._verifyVector(ray)
        return "NONE"

    def normalAt(self, position):
        self._verifyVector(position)
        return "NONE"

    ### Below are duplicates of the functions for vectors found in Raytracer. Will be removed once a vector class is created ###
    def normalize(self, vector):
        summ = self.vectorLength(vector)
        return [i/summ for i in vector]

    def vectorLength(self, vector):
        summ = 0.0
        for i in vector:
            summ += float(i)*i
        return math.sqrt(summ)

    def crossProduct(self, a, b):
        return [
            float(a[1])*b[2] - a[2]*b[1],
            float(a[2])*b[0] - a[0]*b[2],
            float(a[0])*b[1] - a[1]*b[0]
            ]

    def vectorAdd(self, a, b):
        return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

    def vectorSubtract(self, a, b):
        return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

    def dotProduct(self, a, b):
        summ = 0.0
        for i in range(len(a)):
            summ += float(a[i])*b[i]
        return summ

    def _verifyVector(self, vector, v_type='xyz'):
        if not (type(vector) is list):
            raise VectorError(v_type, len(v_type), vector, msg="Vector is not a list")
        elif len(v_type) != len(vector):
            raise VectorError(v_type, len(v_type), vector)
        elif(v_type == 'xyz'):
            for i in vector:
                if type(i) != float:
                    raise VectorError('float', len(v_type), vector)
            return
        elif(v_type == 'RGB'):
            for i in vector:
                if (type(i) != float or i < 0.0 or i > 1.0):
                    raise VectorError('RGB float', len(v_type), vector)
            return
                    
        elif(v_type == "wh"):
            for i in vector:
                if type(i) != int:
                    raise VectorError('Width Height int', len(v_type), vector)
            return
        raise VectorError(v_type, len(v_type), vector, msg="Unknown Vector Type")
