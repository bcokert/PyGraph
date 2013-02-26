#Write a basic line
from pygraph.output.pngwriter import PNGWriter
from pygraph.draw.shapes.BasicShapes import BasicShapes
writer = PNGWriter()
shapes = BasicShapes(400, 400)

line1 = shapes.drawLine(11, 11, 211, 371, (255, 0, 0))
line2 = shapes.drawLine(100, 30, 100, 266, (0, 255, 0))
line3 = shapes.drawLine(200, 20, 200, 321, (0, 0, 255))
pixels = [[255 for x in range(3*400)] for y in range(400)]

in_pixels = [line1, line2, line3]

for input_source in in_pixels:
    for y in range(400):
        validx = filter(lambda pix: pix[1] == y, input_source)
        for x in range(400):
            validy = filter(lambda pix: pix[0] == x, validx)
            if (len(validy) > 0):
                pixels[y][3*x] = validy[0][2][0]
                pixels[y][3*x + 1] = validy[0][2][1]
                pixels[y][3*x + 2] = validy[0][2][2]

writer.write('./test.png', pixels)
