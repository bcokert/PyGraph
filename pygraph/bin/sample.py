#Write a basic line
from pygraph.output.pngwriter import PNGWriter
from pygraph.draw.shapes.BasicShapes import BasicShapes
writer = PNGWriter()
shapes = BasicShapes(300, 300)

line = shapes.drawLine(11, 11, 211, 371, (255, 0, 0))
pixels = []

for y in range(

for pixel in line:
    for col in line[2]:
        pixels[line[0]][line[1]].append(col)
list_of_rows_of_pixels = [(255, 0, 0, 0, 255, 0, 0, 0, 255), (0, 0, 0, 127, 127, 127, 255, 255, 255)]
writer.write('./test.png', list_of_rows_of_pixels)
