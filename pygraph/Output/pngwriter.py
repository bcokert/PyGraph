import pygraph.lib.png as png

class PNGWriter:
    """Takes structures of pixels and writes them to a png

    :Interface:
        - 'write': Takes a list of pixels and writes them to the specified file
        - 'mode': Sets the writers color output modes, given a string for the mode

    :Examples:
    >>> from pygraph.output.pngwriter import PNGWriter
    >>> writer = PNGWriter()
    >>> list_of_rows_of_pixels = [(255, 0, 0, 0, 255, 0, 0, 0, 255), (0, 0, 0, 127, 127, 127, 255, 255, 255)]
    >>> writer.write('./test.png', list_of_rows_of_pixels)
    Created image: pictures/test.png

    ..todo::
        - Create the mode method
    """

    def __init__(self):
        pass

    def write(self, out_file, pixels):
        f = open(out_file, 'wb')
        w = png.Writer(len(pixels[0])/3, len(pixels))
        w.write(f, pixels)
        f.close()
        print "Created image: " + out_file
