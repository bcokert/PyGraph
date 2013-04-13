from pygraph.render.Renderer import Renderer
import math

class Raytracer:
    """A class that implements a basic ray tracer. Not intended to provide complex functions, but rather to call them.
    
    :Methodss:
        - 'render': Calculates the pixels and outputs them with its own Renderer object
        - 'addSphere': Basic sample function that adds a sphere to the scene
    
    :Examples:
        >>> from pygraph.raytrace.Raytracer import Raytracer
        >>> raytracer = Raytracer()
        >>> raytracer.addSphere([0, 0, 0], 1) # x,y,z radius
        >>> raytracer.addPointLight([1, -2, 1], [1.0, 1.0, 1.0], 2) # [xyz], [RGB], strength (relative)
        >>> raytracer.setAmbient([1.0, 1.0, 1.0], 0.1) # RGB, Alpha
        >>> raytracer.setCamera([0, -2, 0], [0, 1, 0], [0, 0, 1], 35) # [xyz], [forward], [up], fov
        >>> raytracer.setOutput('test.png', [500, 500]) # name, width, height
        >>> raytracer.render(3) # max bounces
    """

    def __init__(self):
        self.spheres = []
        self.point_lights = []
        self.ambient = [0.0,0.0,0.0]
        self.camera = []
        self.output_size = []
        self.output_file = ''
        self.pixels = []
        self.clipping_distance = 0.01
        self.renderer = 'NONE'

    def addSphere(self, origin, radius):
        self._verifyVector(origin)
        self.spheres.append([origin, radius])

    def addPointLight(self, origin, color, strength):
        self._verifyVector(origin)
        self._verifyVector(color, v_type='RGB')
        self.point_lights.append([origin, color, strength])

    def setAmbient(self, color):
        self._verifyVector(color, v_type='RGB')
        self.ambient = list(color)

    def setCamera(self, origin, forward, up, fov):
        self._verifyVector(origin)
        self._verifyVector(forward)
        self._verifyVector(up)
        self.camera = [origin, self.normalize(forward), self.normalize(up), self.normalize(self.crossProduct(forward, up)), fov]

    def setOutput(self, out_file, out_size):
        self.output_file = out_file
        self._verifyVector(out_size, v_type='wh')
        self.output_size = out_size
        self.renderer = Renderer(self.output_size[0], self.output_size[1])
        self.renderer.setBackgroundColor(R='0', G='0', B='0')

    def render(self):
        swid = self.output_size[0]/2
        shei = self.output_size[1]/2
        dist = [(swid/math.tan(self.camera[4]/2)) * i for i in self.camera[1]]

        for y in range(self.output_size[1]):
            for x in range(self.output_size[0]):
                ray = self.camera[0] # pos
                ray = self.vectorAdd(ray, [(x - swid)*i for i in self.camera[3]]) # camera + right
                ray = self.vectorAdd(ray, [(y - shei)*i for i in self.camera[2]]) # camera + right + up
                ray = self.vectorAdd(ray, dist) # ray from camera point to pixel
                ray = self.normalize(ray)

                collision, collided_object = self.findCollision(ray)

                # Verify that collision is within the clipping plane, and then color it
                if (collision != 'NONE' and collision > self.clipping_distance):
                    self.renderer.drawOver([[x, y, [int(255*i) for i in self.calculateColor(self.camera[0], ray, collision, collided_object)]]])

        self.renderer.render(file_name=self.output_file)

    def findCollision(self, ray):
        collision = 'NONE'
        a = self.dotProduct(ray, ray) # ray.ray
        for sphere in self.spheres:
            cam_sub_sphere = self.vectorSubtract(self.camera[0], sphere[0]) # cam-sph
            b = 2 * self.dotProduct(cam_sub_sphere, ray) # 2(cam-sph).ray
            c = self.dotProduct(cam_sub_sphere, cam_sub_sphere) - sphere[1]*sphere[1] # (cam-sph).(cam-sph) - radius^2
            # Intersections at cam[0] + t*ray, where t is at^2 + bt + c

            desc = b*b - 4*a*c
            if (desc < 0.0):
                continue
            sqrt_desc = math.sqrt(desc)
            col1 = (-b + sqrt_desc)/(2 * a)
            col2 = (-b - sqrt_desc)/(2 * a)

            # The smallest positive root is where the ray intersects
            intersect = col2
            if (col1 < col2):
                intersect = col1

            if (intersect < 0.0):
                continue

            if (collision == 'NONE'):
                collision = intersect
            elif (intersect < collision):
                collision = intersect

        return [collision, sphere]

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

    def calculateColor(self, origin, ray, dist, collided_object):
        self._verifyVector(ray)

        p_collision = self.vectorAdd(origin, [dist*i for i in ray])
        p_sphere = collided_object[0]
        k_ambient = 1.0
        k_specular = 1.0
        k_diffuse = 0.8
        k_shine = 50
        m_diffuse = [1, 0.0, 0.0]
        m_specular = [1.0, 1.0, 1.0]
        v_normal = self.normalize(self.vectorSubtract([2*i for i in p_collision], p_sphere))

        c_ambient = [k_ambient * i for i in self.ambient]

        color_local = list(c_ambient) # Ambient

        for light in self.point_lights:
            v_light = self.normalize(self.vectorSubtract(light[0], p_collision))
            v_reflected = self.normalize(self.vectorSubtract(v_light, [2*self.dotProduct(v_normal, v_light) * i for i in v_normal]))
            c_light = [(float(light[2]) * i) for i in light[1]]
            attenuation = 1.0/self.vectorLength(self.vectorSubtract(light[0], p_collision))

            i_diffuse = max(0.0, self.dotProduct(v_normal, v_light))
            i_specular = max(0.0, self.dotProduct(v_reflected, v_light)) ** k_shine

            c_diffuse = [k_diffuse * i_diffuse * i for i in m_diffuse]
            c_specular = [k_specular * i_specular * i for i in m_specular]

            spec_diff = [attenuation * i for i in self.vectorAdd(c_diffuse, c_specular)]
            spec_diff = [c_light[0] * spec_diff[0], c_light[1] * spec_diff[1], c_light[2] * spec_diff[2]] # Light color * Material Color(with shading)

            color_local = self.vectorAdd(color_local, spec_diff) # add the color created by this light to the current color

        # Here we could recursively fire another ray, if we add a recursion number to calculateColor
        color_reflected = [0.0, 0.0, 0.0]
        color_refracted = [0.0, 0.0, 0.0]

        color = self.vectorAdd(color_local, self.vectorAdd(color_reflected, color_refracted))

        # We might have a value greater than 1 for a component. We need to divide by the maximum to lower intensity whilst retaining the color
        max_color = max(color[0], color[1], color[2])
        if (max_color > 1.0):
            color = [i/max_color for i in color]
        return color

    def _verifyVector(self, vector, v_type='xyz'):
        if not (type(vector) is list):
            raise VectorError(v_type, len(v_type), vector, msg="Vector is not a list")
        elif len(v_type) != len(vector):
            raise VectorError(v_type, len(v_type), vector)
        elif(v_type == 'xyz'):
            for i in vector:
                if type(i) != float:
                    raise VectorError('float', len(v_type), vector)
                else:
                    return
        elif(v_type == 'RGB'):
            for i in vector:
                if (type(i) != float or i < 0.0 or i > 1.0):
                    raise VectorError('RGB float', len(v_type), vector)
                else:
                    return
        elif(v_type == "wh"):
            for i in vector:
                if type(i) != int:
                    raise VectorError('Width Height int', len(v_type), vector)
                else:
                    return
        raise VectorError(v_type, len(v_type), vector, msg="Unknown Vector Type")

class VectorError(Exception):
    """ Raised when a function expected a vector (of some kind), but received something else"""
    def __init__(self, expected_type, expected_size, bad_vector, msg=''):
        self.vector_type = expected_type
        self.vector_size = expected_size
        self.bad_vector = bad_vector
        self.msg = msg

    def __str__(self):
        if (self.msg != ''):
            return "Error with vector '{0}' with expected type '{1}' and size '{2}': {3}".format(str(self.bad_vector), self.vector_type, self.vector_size, self.msg)
        return "Expected vector type '{0}' with dimension '{1}', but received '{2}'".format(self.vector_type, self.vector_size, str(self.bad_vector))
