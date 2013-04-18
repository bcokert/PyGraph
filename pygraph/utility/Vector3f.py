import math

class Vector3f:
    """A class that implements vectors, with helpful overrides and functions
    
    :Methods:
        - '+': Returns the vector v1 + v2
        - '-': Returns the vector v1 - v2
        - '*': Returns the vector v1[0] * v2[0], v1[1] * v2[1], v1[2] * v2[2]. If given a number, scales the vector
        - 'dot': Returns the dot product of the vector and the argument vector
        - 'cross': Returns the cross product of the vector and the argument vector
        - 'length': Returns the length of the vector
        - 'normalize': Normalizes the vector
    
    :Examples:
        >>> from pygraph.utility.Vector3f import *
        >>> v1 = Vector3f(1.0, 1.0, 1.0)
        >>> v2 = Vector3f(2.0, 2.0, -1.0)
        >>> v1 + v2
        >>> v1 - v2
        >>> v1 * v2
        >>> v1 * 5 #[5.0, 5.0, 5.0]
        >>> v1 * 3.2
        >>> v1.dot(v2)
        >>> v1.cross(v2)
        >>> v1[0] #1.0
        >>> v1[0:2] == [1.0, 1.0, 1.0] #true
        >>> v1.normalize()
        >>> v1.length() == 1.0 #true
    """

    def __init__(self, x, y, z, normal=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.normal = normal

    def normalize(self):
        if (self.normal == 1):
            return self
        ll = self.length()
        return Vector3f(self.x/ll, self.y/ll, self.z/ll, normal=1)

    def length(self):
        if (self.normal == 1):
            return 1.0

        summ = float(self.x) ** 2 + float(self.y) ** 2 + float(self.z) ** 2
        return math.sqrt(summ)

    def cross(self, v2):
        x = float(self[1])*v2[2] - self[2]*v2[1]
        y = float(self[2])*v2[0] - self[0]*v2[2]
        z = float(self[0])*v2[1] - self[1]*v2[0]
        return Vector3f(x, y, z)

    def __add__(self, v2):
        return Vector3f(self[0] + v2[0], self[1] + v2[1], self[2] + v2[2])

    def __sub__(self, v2):
        return Vector3f(self[0] - v2[0], self[1] - v2[1], self[2] - v2[2])

    def __mul__(self, v2):
        if (type(v2) == int or type(v2) == float):
            return Vector3f(float(self.x) * v2, float(self.y) * v2, float(self.z) * v2)
        return Vector3f(self[0] * v2[0], self[1] * v2[1], self[2] * v2[2])

    def dot(self, v2):
        return self[0]*v2[0] + self[1]*v2[1] + self[2]*v2[2]

    def __getitem__(self, i):
        if (i==0):
            return self.x
        if (i==1):
            return self.y
        if (i==2):
            return self.z

    def toList(self):
        return [self.x, self.y, self.z]
