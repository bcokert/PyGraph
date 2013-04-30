import math
from pygraph.raytrace.primitives.RenderablePrimitive import RenderablePrimitive
from pygraph.utility.Vector3f import Vector3f
from pygraph.utility.MoreMath import solveQuadratic

class Sphere(RenderablePrimitive):
    """A class that represents perfect spheres
    
    :Methods:
        - 'intersect': Returns the distance from the given origin along the given ray that the closest collision occurs with the sphere
        - 'normalAt': Returns the normal of the sphere at the given point. May be garbage if the point is not a collision point.
        - 'setRadius': Sets the radius of the sphere
        - 'setOrigin': Sets the center of the sphere
    
    :Examples:
        >>> from pygraph.raytrace.primitives.Sphere import Sphere
        >>> from pygraph.utility.Vector3f import Vector3f
        >>> sphere = Sphere()
        >>> sphere.setRadius(2.0)
        >>> sphere.setOrigin(Vector3f(3, 0, 0))
        >>> intersect = sphere.intersect(Vector3f(0,0,0), Vector3f(1, 0, 0)) # Does intersect
        >>> sphere.normalAt(intersect) # A Vector3f
    """

    def __init__(self, origin="NONE", radius=1.0):
        super(Sphere, self).__init__(origin=origin)

        self.setRadius(radius)

    def intersect(self, origin, ray):
        origin_sub_sphere = origin - self.origin
        b = 2 * origin_sub_sphere.dot(ray)
        c = origin_sub_sphere.dot(origin_sub_sphere) - self.radius*self.radius

        intersect = "NONE"
        for col in solveQuadratic(1, b, c):
            if (col != "NONE" and col > 0.0):
                if (intersect == "NONE" or col < intersect):
                    intersect = col
        return intersect

    def normalAt(self, position):
        return (position - self.origin) * (1/self.radius)

    def setRadius(self, radius="NONE"):
        if (type(radius) in [int, float] and radius > 0.0):
            self.radius = float(radius)
        return self.radius
