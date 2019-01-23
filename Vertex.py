# Cambiar el color de un punto del ViewPort
def glVertex(self, x, y, color):
    x = ((((x + 1)/2) * (self.width)) + self.x)
    y = ((((y + 1)/2) * (self.height)) + self.y)
	self.framebuffer[x][y] = color