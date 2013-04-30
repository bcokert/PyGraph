from pygraph.render.Renderer import Renderer
from pygraph.utility.Vector3f import Vector3f
from math import tan, radians, sqrt

class Raytracer:
    """A class that implements a basic ray tracer. Not intended to provide complex functions, but rather to call them.
    
    :Methods:
        - 'render': Calculates the pixels and outputs them with its own Renderer object
        - 'addSphere': Basic sample function that adds a sphere to the scene
    
    :Examples:
        >>> from pygraph.raytrace.Raytracer import Raytracer
        >>> raytracer.render()
    """

    def __init__(self):
        self.primitives = []
        self.point_lights = []
        self.ambient = [0.0,0.0,0.0]
        self.pixels = []

        self.output_width = 100
        self.output_height = 100
        self.output_file = "default_output.png"

        self.minimum_distance_from_camera = 0.01
        self.renderer = 'NONE'
        
        self.camera_origin = "NONE"
        self.camera_forward = "NONE"
        self.camera_up = "NONE"
        self.camera_right = "NONE"
        self.screen_horizonal = "NONE"
        self.screen_vertical = "NONE"

    def addPrimitive(self, primitive):
        self.primitives.append(primitive)

    def addPointLight(self, origin, color, strength):
        self.point_lights.append([origin.duplicate(), color, strength])

    def setAmbient(self, color):
        self.ambient = list(color)

    def setCamera(self, origin, forward, up, field_of_view):
        self.camera_origin = origin.duplicate()
        self.camera_forward = forward.normalize()
        self.camera_up = up.normalize()
        self.camera_right = forward.cross(up).normalize()

        self.screen_halfwidth = tan(radians(field_of_view/2.0))
        self.screen_halfheight = tan(radians((self.output_height/self.output_width) * field_of_view/2.0))

    def setOutput(self, out_file, out_width, out_height):
        self.output_file = out_file
        self.output_width = out_width
        self.output_height = out_height

        self.renderer = Renderer(self.output_width, self.output_height)
        self.renderer.setBackgroundColor(R=80, G=80, B=80)

    def render(self):
        """Calculates each pixel by shooting rays through them from a camera

        :Explaination:
            For each pixel:
                pixel_color = color from rays collisions
                ray = point on camera plane - camera
                point on camera plane = center of plane + distance right + distance up
                center of plane = camera + forward
                distance right = du * right vector
                distance up = dv * up vector
                du = % along right vector = ((x - pixel_width/2) / pixel_width) * screen_halfwidth
                du factored = (2x - pixel_width) * screen_halfwidth / 2*pixel_width
                We can calculate the part outside the brackets outside of the for loop
                And do a similar thing for height
            So:
                du = (2x - pixel_width) * width_shortcut
                dv = (2y - pixel_height) * height_shortcut
                We need to flip dv to match the fact that y increases as we go down (technical issue, not really geometric)
        """
        width_shortcut = self.screen_halfwidth / (2 * self.output_width)
        height_shortcut = self.screen_halfheight / (2 * self.output_height)
        center_of_camera_plane = self.camera_origin + self.camera_forward

        for y in range(self.output_height):
            for x in range(self.output_width):
                du = (2*x - self.output_width) * width_shortcut
                dv = -(2*y - self.output_height) * height_shortcut

                point_on_camera_plane = center_of_camera_plane + self.camera_right * du + self.camera_up * dv
                ray = (point_on_camera_plane - self.camera_origin).normalize()

                collision, collided_object = self.findClosestCollision(self.camera_origin, ray)
                if (collision != 'NONE' and collision > self.minimum_distance_from_camera):
                    self.renderer.drawOver([[x, y, [int(255*i) for i in self.calculateColor(self.camera_origin, ray, collision, collided_object)]]])

        self.renderer.render(file_name=self.output_file)

    def findClosestCollision(self, origin, ray):
        collision, collision_object = 'NONE', 'NONE'
        for primitive in self.primitives:
            intersect = primitive.intersect(origin, ray)
            if (intersect != "NONE" and intersect < collision):
                collision, collision_object = intersect, primitive
        return [collision, collision_object]

    def calculateColor(self, origin, ray, dist, primitive):
        p_collision = origin + ray * dist
        v_normal = primitive.normalAt(p_collision)

        amb_diff = [primitive.diffuse_color[0] * self.ambient[0], primitive.diffuse_color[1] * self.ambient[1], primitive.diffuse_color[2] * self.ambient[2]]
        color_local = list(amb_diff)

        for light in self.point_lights:
            v_light = (light[0] - p_collision).normalize()
            v_reflected = (v_normal * 2 * v_normal.dot(v_light) - v_light).normalize()
            c_light = [(float(light[2]) * i) for i in light[1]]
            attenuation = 1.0/(light[0] - p_collision).length()

            i_diffuse = max(0.0, v_normal.dot(v_light))
            i_specular = max(0.0, v_reflected.dot(v_light)) ** primitive.shininess

            c_diffuse = [primitive.diffuse_constant * i_diffuse * i for i in primitive.diffuse_color]
            c_specular = [primitive.diffuse_constant * i_specular * i for i in primitive.specular_color]

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
