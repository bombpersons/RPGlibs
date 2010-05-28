# Class that contains all the data for a map
# Contains -
#	The tileset data
#	The map's 

from base import Base
from draw import Drawer
from tileset import Tileset

from xml.sax import handler

class Map (Base):
	def __init__(self):
		Base.__init__(self)
		
		# Define some variables
		self.tilesets = []					# Tilesets the map can use
		self.drawer = Drawer()				# Interface to graphics
		
		self.layers = [[]]					# The map data (tiles)
		self.size = (0, 0)					# The maps dimensions
	
	"""Loads a map and associated data (tilesets etc..)
	   Args:
			filename - The path to the map.
	   
	   Returns:
			True if succesfull
	"""
	def load(self, filename):
		pass
	
	"""Clears and Updates the maps image
	   Args:
			None
	   Returns:
			True if succesfull
	"""
	def update(self):
		for layer in self.layers:
			n = 0
			for tile in layer:
				self.tilesets[0].getTile(tile % self.tilesets[0].sizeTiles[0], int(tile / self.tilesets[0].sizeTiles[0])).draw(n % self.size[0], int(n / self.size[0])
				n += 1
		
		#No Problems
		return True

# A sax handler to load xml maps
class MapLoader(handler):
	# Set the map to load into
	def __init__(self, map):
		handler.__init__(self)
		
		self.map = map
		
		self.inMap = False
		self.inTileset = False
		
	# The start of an xml tag
	def startElement(self, name, attrs):
		if name == 'map':
			# We can get some basic info about the map from this tag
			if 'width' in attrs.getNames():
				self.map.size[0] = attrs.getValue('width')
			
			if 'height' in attrs.getNames():
				self.map.size[1] = attrs.getValue('height')
			
			# remember that we are in this tag
			self.inMap = True
		
		# Tileset tag
		# Add a new tileset to the map with all the options
		if name == 'tileset' and self.inMap == True:
			# Make a new blank tileset.
			tileset = Tileset()
			
			# Fill it with some of the new info in this tag
			if 'tilewidth' in attrs.getNames():
				tileset.tileSize[0] = attrs.getValue('tilewidth')
			if 'tileheight' in attrs.getNames():
				tileset.tileSize[1] = attrs.getValue('tileheight')
			if 'name' in attrs.getNames():
				tileset.name = attrs.getValue('name')
				
			# K, add this tileset to the loaded map
			# We can add things from nested tags into it later.
			
			self.inTileset = True
			
		# Image Tag
		# We should add this image to the current tileset
		if name == 'image' and self.inTileset:
			# Find the location of the image and load it
			if 'source' in attrs.getNames():
				self.tileset[-1].data = self.drawer.loadImage(attr.getValue('source'))
			
			# K, done... assuming that image loaded.
			
			
	# The end of an xml tag
	def endElement(self, name, attrs):
		if name == 'map':
			self.inMap = False
		if name == 'tileset':
			self.inTileset = False
