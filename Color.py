# Cambia el color para glVertex
def color(r, g, b):
    self.r = r * 255
    self.g = g * 255
    self.b = b * 255
	return bytes ([r, g, b])