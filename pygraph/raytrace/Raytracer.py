from pygraph.render.Renderer import Renderer
from pygraph.utility.Vector3f import Vector3f
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
        >>> raytracer.render()
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
        self.spheres.append([origin.duplicate(), float(radius)])

    def addPointLight(self, origin, color, strength):
        self.point_lights.append([origin.duplicate(), color, strength])

    def setAmbient(self, color):
        self.ambient = list(color)

    def setCamera(self, origin, forward, up, fov):
        self.camera = [origin.duplicate(), forward.normalize(), up.normalize(), forward.cross(up).normalize(), fov]

    def setOutput(self, out_file, out_size):
        self.output_file = out_file
        self.output_size = out_size
        self.renderer = Renderer(self.output_size[0], self.output_size[1])
        self.renderer.setBackgroundColor(R=80, G=80, B=80)

    def render(self):
        screenx = (math.tan(math.radians(self.camera[4]/2))) # The half width of the screen plane
        screeny = (math.tan(math.radians((self.output_size[1]/self.output_size[0]) * self.camera[4]/2))) # The half height of the screen plane
        plane = self.camera[0] + self.camera[1] # The point at the center of the screen plane

        for y in range(self.output_size[1]):
            for x in range(self.output_size[0]):
                ray = plane.duplicate()
                u = (x - float(self.output_size[0])/2)/self.output_size[0] # parameter of width of the screen plane
                v = -(y - float(self.output_size[1])/2)/self.output_size[1] # parameter of height of the screen plane
                du = u*screenx # position along the right vector
                dv = v*screeny # position along the up vector

                ray = ray + self.camera[3] * du # add the right vector
                ray = ray + self.camera[2] * dv # add the up vector
                ray = ray - self.camera[0] # Ray == point on screen - Camera
                ray = ray.normalize()

                collision, collided_object = self.findCollision(ray)

                # Verify that collision is within the clipping plane, and then color it
                if (collision != 'NONE' and collision > self.clipping_distance):
                    self.renderer.drawOver([[x, y, [int(255*i) for i in self.calculateColor(self.camera[0], ray, collision, collided_object)]]])

        self.renderer.render(file_name=self.output_file)

    def findCollision(self, ray):
        collision = 'NONE'
        collision_sphere = 'NONE'
        for sphere in self.spheres:
            cam_sub_sphere = self.camera[0] - sphere[0] # cam-sph
            b = 2 * cam_sub_sphere.dot(ray) # 2(cam-sph).ray
            c = cam_sub_sphere.dot(cam_sub_sphere) - sphere[1]*sphere[1] # (cam-sph).(cam-sph) - radius^2
            # Intersections at cam[0] + t*ray, where t is at^2 + bt + c

            desc = b*b - 4*c
            if (desc < 0.0):
                continue
            sqrt_desc = math.sqrt(desc)
            col1 = (-b + sqrt_desc)/2
            col2 = (-b - sqrt_desc)/2

            # The smallest positive root is where the ray intersects
            intersect = col2
            if (col1 < col2):
                intersect = col1

            if (intersect < 0.0):
                continue

            if (collision == 'NONE'):
                collision = intersect
                collision_sphere = sphere
            elif (intersect < collision):
                collision = intersect
                collision_sphere = sphere

        return [collision, collision_sphere]

    def calculateColor(self, origin, ray, dist, collided_object):
        p_collision = origin + ray * dist
        p_sphere = collided_object[0]
        k_ambient = 1.0
        k_specular = 1.0
        k_diffuse = 0.8
        k_shine = 100
        m_diffuse = [1.0, 0.0, 0.0]
        m_specular = [1.0, 1.0, 1.0]
        v_normal = (p_collision - p_sphere) * (1/collided_object[1])

        c_ambient = [k_ambient * i for i in m_diffuse]
        amb_diff = [c_ambient[0] * self.ambient[0], c_ambient[1] * self.ambient[1], c_ambient[2] * self.ambient[2]]
        color_local = list(amb_diff)

        for light in self.point_lights:
            v_light = (light[0] - p_collision).normalize()
            v_reflected = (v_normal * 2 * v_normal.dot(v_light) - v_light).normalize()
            c_light = [(float(light[2]) * i) for i in light[1]]
            attenuation = 1.0/(light[0] - p_collision).length()

            i_diffuse = max(0.0, v_normal.dot(v_light))
            i_specular = max(0.0, v_reflected.dot(v_light)) ** k_shine

            c_diffuse = [k_diffuse * i_diffuse * i for i in m_diffuse]
            c_specular = [k_specular * i_specular * i for i in m_specular]

            spec_diff = [attenuation * (i[0] + i[1]) for i in zip(c_diffuse, c_specular)]
            spec_diff = [i[0] * i[1] for i in zip(c_light, spec_diff)] # Light color * Material Color(with shading)

            color_local = [i[0] + i[1] for i in zip(color_local, spec_diff)] # add the color created by this light to the current color

        # Here we could recursively fire another ray, if we add a recursion number to calculateColor
        color_reflected = [0.0, 0.0, 0.0]
        color_refracted = [0.0, 0.0, 0.0]

        color = color_local # + color_reflected + color_refracted

        # We might have a value greater than 1 for a component. We need to divide by the maximum to lower intensity whilst retaining the color
        max_color = max(color[0], color[1], color[2])
        if (max_color > 1.0):
            color = [i/max_color for i in color]
        return color
