# Class to contain information about a layer
# Contains:
#	Layer data (which tiles and where)
#	Height and width of layer
#	Name
#	Whether or not this layer is a colliding layer.

from base import Base

class Layer (Base):
	def __init__(self):
		Base.__init__(self)
		
		self.map = None # The map this layer belongs to
		
		self.data = [] # List of tile numbers
		self.width = 0
		self.height = 0

	""" Draw the whole layer
	"""
	def draw(self):
		n = 0
		for tile in self.data:
			if tile != 0:
				tile -= 1
				self.map.tilesets[0].getTile((tile % self.map.tilesets[0].sizeTiles[0], int(tile / self.map.tilesets[0].sizeTiles[0]))).draw(((((n % self.map.size[0])*self.map.tilesets[0].tileSize[0]) + (self.map.drawer.getRes(self.map.drawer.image)[0] / 2) + self.map.camera.pos[0]), ((int(n / self.map.size[0])*self.map.tilesets[0].tileSize[1]) + (self.map.drawer.getRes(self.map.drawer.image)[1] / 2) + self.map.camera.pos[1])))
			n += 1
