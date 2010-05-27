# Class to contain information about a tileset
# Contains:
#	The data of the actual tileset
#	The size of the tileset
#	The size of the individual tiles
#	
#	Functions for getting a specific tile (returning a tile structure)
#	
#
#
#

from base import Base
from map import Map
from tile import Tile

class Tileset (Base):
	def __init__(self):
		Base.__init__(self)
		
		self.map = None						# The associated map
		
		self.data =	None			 		# The tileset image
		self.size = (0, 0) 					# In pixels
		self.sizeTiles = (0, 0) 			# In tiles
		
		self.tileSize = (0, 0) 				# In pixels
		
	"""Loads an image to use as a tileset
		Args:
			filename - The path to the image to use.
			size - The size of each tile (in pixels)
			
		Returns:
			True if succesfull, False if not
	"""
	def load(self, filename, size):
		# Try to load the file
		image = self.drawer.LoadImage(filename)
		if not image:
			print("Could not load image at " + filename)
			return False
			
		# Okay, file loaded.
		self.data = image
		
		# Set the tilesize
		self.tilesize = size
	
	"""Get the top and bottom coords for a tile
	
		Args:
			tileCoord - The coordinate of the tile (in tiles)
			
		Returns:
			A list in the form ((topX, topY), (bottomX, bottomY))
	"""
	def _getCoords(self, tileCoord):
		# Do some simple maths to get the coords
		top = (tileCoord[0]*self.tileSize[0], tileCoord[1]*self.tileSize[1])
		bottom = (top[0] + tileSize[0], top[1] + tileSize[1])
		
		# Make sure these values are within the size of the tileset
		if top[0] < 0 or top[1] < 0 or bottom[0] > self.size[0] or bottom[1] > self.size[1]:
			# One of the values is too big
			print ("Warning: The tile coords requested are out of the bounds of the tileset!")
			print ("The coordinates returned are of the tile (0, 0)")
			return ((0, 0), (0, 0))
		else:
			return (top, bottom)
			
	"""Get a tile
		
		Args:
			tileCoord - The coordinate of the tile (in tiles)
			
		Returns:
			A tile structure representing the requested tile
	"""
	def getTile(self, tileCoord):
		tile = Tile()
		tile.tileset = self
		tile.topcoord, tile.bottomcoord = self._getCoords(tileCoord)
		
		return tile
