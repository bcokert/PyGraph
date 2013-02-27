from pygraph.output.PNGWriter import PNGWriter

class Renderer:
    """A class designed to take the output of drawing methods and write them to png's
    
    :Methods:
        - 'render': Writes the current buffer out to file
        - 'clearBuffer': Refreshes the buffer to the background color
        - 'setBackgroundColor': Sets the background color of the buffer, or returns it
        - 'drawOver': Adds the given pixels to the buffer, drawing over non-background pixels
        - 'drawUnder': Adds the given pixels to the buffer, drawing under non-background pixels
    
    :Examples:
        >>> from pygraph.render.Renderer import Renderer
        >>> from pygraph.draw.shapes.BasicShapes import BasicShapes
        >>> renderer = Renderer(400, 400) # Output Buffer Size
        >>> shapes = BasicShapes(400, 400) # Draw Canvas Size
        >>> line1 = shapes.drawLine(10, 10, 300, 300, (255, 0 , 0)) # A shape == A list of pixels
        >>> line2 = shapes.drawLine(20, 20, 20, 350, (0, 0, 255)) # Another shape
        >>> renderer.setBackgroundColor(255, 255, 255) # The default color is white (if no color is received by a shape, then the background color is used)
        >>> renderer.clearBuffer() # Reset buffer for a new image
        >>> renderer.drawOver(line1) # Put the line in the buffer
        >>> renderer.drawOver(line2) # Put the second line in the buffer, covering any pixels shared by other items in the buffer
        >>> renderer.render('./test.png') # Output current buffer to a file
    """

    def __init__(self, buffer_x, buffer_y):
        self.writer = PNGWriter()
        self.background_color = [255, 255, 255]
        self.pixels = [sum([self.background_color for x in range(buffer_x)], []) for y in range(buffer_y)]
        self.buffer_x = buffer_x
        self.buffer_y = buffer_y

    def render(self, file_name='NONE'):
        if (file_name != 'NONE'):
            try:
                self.writer.write(file_name, self.pixels)
            except OSError:
                return self.pixels
        else:
            return self.pixels

    def clearBuffer(self):
        self.pixels = [sum([self.background_color for x in range(self.buffer_x)], []) for y in range(self.buffer_y)]

    def setBackgroundColor(self, R=256, G=256, B=256):
        if (R <= 255 and G <= 255 and B <= 255 and R >= 0 and G >= 0 and B >= 0):
            self.background_color = [R, G, B]
        return self.background_color

    def drawOver(self, pixels, x_orig = 0, y_orig = 0):
        for y in range(self.buffer_y):
            validx = filter(lambda pix: pix[1] == y - y_orig, pixels)
            for x in range(self.buffer_x):
                validy = filter(lambda pix: pix[0] == x - x_orig, validx)
                if (len(validy) > 0):
                    self.pixels[y][3*x:3*x+3] = validy[0][2]

    def drawUnder(self, pixels, x_orig = 0, y_orig = 0):
        for y in range(self.buffer_y):
            validx = filter(lambda pix: pix[1] == y - y_orig, pixels)
            for x in range(self.buffer_x):
                validy = filter(lambda pix: pix[0] == x - x_orig, validx)
                if (len(validy) > 0 and self.pixels[y][3*x:3*x+3] == self.background_color):
                    self.pixels[y][3*x:3*x+3] = validy[0][2]
