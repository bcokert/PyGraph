import math
from pygraph.raytrace.primitives.RenderablePrimitive import RenderablePrimitive
from pygraph.utility.Vector3f import Vector3f

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

    def __init__(self):
        super(Sphere, self).__init__()
        self.radius = 1.0
        self.origin = Vector3f(0, 0, 0)

    def intersect(self, origin, ray):
        return "NONE"

    def normalAt(self, position):
        return "NONE"
