# Class to contain information for an individual tile
# Contains -
# 	The associated tileset
#	The positions (pixels) of the tile on the tileset

from base import Base
from tileset import Tileset

class Tile (Base):
	def __init__(self):
		Base.__init__(self)
		
		self.tileset = None 			# A blank tileset
		self.topcoord = (0, 0) 			# The top left of the tile
		self.bottomcoord = (0, 0) 		# The bottomm right of the tile
		
	"""Draw the tile to an image.
	   Args:
			pos - The coords to draw at.
		
	   Returns:
			True if succesful.
	"""
	def draw(self, pos):
		# blit the tile to the image
		return self.tileset.map.drawer.blit(self.topcoord, self.bottomcoord, pos, self.tileset.data)
