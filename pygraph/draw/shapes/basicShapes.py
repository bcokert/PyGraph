class BasicShapes:
    """A class providing methods for drawing basic 2d shapes

    :Methods:
        - 'drawLine': Returns the pixel list for a line
        - 'setCanvasSize': Given 2 integers, sets the width and height of the plane to draw on
    :Examples:
        >>> from pygraph.draw.shapes.BasicShapes import BasicShapes
        >>> drawer = BasicShapes(600, 600)
        >>> pixels = drawer.drawLine(0, 0, 44, 32, (200, 50, 50))
    """

    def __init__(self, canvas_width, canvas_height):
        self.CANVAS_WIDTH = canvas_width
        self.CANVAS_HEIGHT = canvas_height

    def drawLine(self, x0, y0, x1, y1, RGB):
        pixels = []

        steep = abs(y1 - y0) > abs(x1 - x0)
        plot = lambda x,y: pixels.append((x, y, RGB))

        if (steep): #swap x0/y0 and x1/y1
            x0, y0 = y0, x0; x1, y1 = y1, x1
            plot = lambda y,x: pixels.append((x, y, RGB))

        if (x0 > x1): #swap x0/x1 and y0/y1
            x0, x1 = x1, x0; y0, y1 = y1, y0

        dx, dy = x1 - x0, abs(y1 - y0)
        err = dx/2
        ystep = 1
        if (y0 >= y1):
            ystep = -1
        y = y0

        for x in range(x0, x1 + 1):
            plot(x, y)
            err = err - dy
            if (err < 0):
                y = y + ystep
                err = err + dx

        return pixels
                

    def setCanvasSize(self, width=0, height=0):
        if (width > 0):
            self.CANVAS_WIDTH = width
        if (height > 0):
            self.CANVAS_HEIGHT = height
        return (self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
