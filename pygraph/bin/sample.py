#Write a basic random png
from pygraph.output.pngwriter import PNGWriter
writer = PNGWriter()
list_of_rows_of_pixels = [(255, 0, 0, 0, 255, 0, 0, 0, 255), (0, 0, 0, 127, 127, 127, 255, 255, 255)]
writer.write('./test.png', list_of_rows_of_pixels)
