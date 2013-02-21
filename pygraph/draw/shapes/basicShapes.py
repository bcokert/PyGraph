BASIC_SHAPES = ('NONE', 'LINE')

class BasicShape:
    def __init__(self):
        self.shape_type = "NONE"

    def render(self):
        pass

    def setShapeType(self, new_type):
        if any(new_type in types for types in BASIC_SHAPES):
            self.shape_type = new_type
        return self.shape_type
