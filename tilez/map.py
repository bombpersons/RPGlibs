# Class that contains all the data for a map
# Contains -
#	The tileset data
#	The map's 

from base import Base
from draw import DrawerSDL
from tileset import Tileset
from layer import Layer
from camera import Camera

from xml.sax import ContentHandler, parse

# A sax handler to load xml maps
class MapLoader (ContentHandler):
	def __init__(self):
		ContentHandler.__init__(self)
		
		self.map = Map()
		
		self.dataBuffer = ''
		self.dataEncoding = ''
		
		self.inMap = False
		self.inTileset = False
		self.inLayer = False
		self.inData = False
		self.inProperties = False
		
	# The start of an xml tag
	def startElement(self, name, attrs):
		if name == 'map':
			# We can get some basic info about the map from this tag
			if 'width' in attrs.getNames():
				# Be careful here, attrs.getValue always return a
				# string, so always convert afterwards
				self.map.size[0] = int(attrs.getValue('width'))
			
			if 'height' in attrs.getNames():
				self.map.size[1] = int(attrs.getValue('height'))
			
			# remember that we are in this tag
			self.inMap = True
		
		# Tileset tag
		# Add a new tileset to the map with all the options
		if name == 'tileset' and self.inMap == True:
			# Make a new blank tileset.
			tileset = Tileset()
			
			# Attach the map to the tileset
			tileset.map = self.map
			
			# Fill it with some of the new info in this tag
			if 'tilewidth' in attrs.getNames():
				tileset.tileSize[0] = int(attrs.getValue('tilewidth'))
			if 'tileheight' in attrs.getNames():
				tileset.tileSize[1] = int(attrs.getValue('tileheight'))
			if 'name' in attrs.getNames():
				tileset.name = attrs.getValue('name')
				
			# K, add this tileset to the loaded map
			self.map.tilesets.append(tileset)
			
			# We can add things from nested tags into it later.
			
			self.inTileset = True
			
		# Image Tag
		# We should add this image to the current tileset
		if name == 'image' and self.inTileset:
			# Find the location of the image and load it
			if 'source' in attrs.getNames():
				self.map.tilesets[-1].load(attrs.getValue('source'), self.map.tilesets[-1].tileSize)
			
			# K, done... assuming that image loaded.
			
		# Layer Tag
		if name == 'layer' and self.inMap:
			# Make a new layer
			layer = Layer()
			
			# Attach layer to map
			layer.map = self.map
			
			# Get the name of the layer
			if 'name' in attrs.getNames():
				layer.name = attrs.getValue('name')
			
			# Width and Height
			if 'width' in attrs.getNames():
				layer.width = int(attrs.getValue('width'))
			if 'height' in attrs.getNames():
				layer.height = int(attrs.getValue('height'))
			
			# Add the new layer to the map
			self.map.layers.append(layer)
			
			# We're inside the layer tag now
			self.inLayer = True
		
		# Properties
		if name == 'properties' and self.inLayer:
			self.inProperties = True
		
		if name == 'property' and self.inProperties and self.inLayer:
			# Add this property to the current layer
			if 'name' in attrs.getNames():
				if attrs.getValue('name') == 'Solid':
					if 'value' in attrs.getNames():
						if attrs.getValue('value') == '1':
							self.map.layers[-1].solid = True
		
		# Data Tag
		if name == 'data' and self.inLayer:
			# Find out how the data is encoded
			if 'encoding' in attrs.getNames():
				self.dataEncoding = attrs.getValue('encoding')
			
			# Flush the buffer
			self.dataBuffer = ''
			
			# Inside data, now we can load the layer data
			self.inData = True	
	
	# The characters inbetween tags
	def characters(self, content):
		if self.inData:
		
			# Since this function will not necessarily be called with all of
			# the data (it will feed us chunks), we need to write all the
			# data to a buffer and process the information after we know
			# that the tag is finished.
			
			# The buffer should have been flushed at the start of the tag
			self.dataBuffer += content
	
	# The end of an xml tag
	def endElement(self, name):
		if name == 'map':
			self.inMap = False
		if name == 'tileset':
			self.inTileset = False
		if name == 'layer':
			self.inLayer = False
		if name == 'data':
			# Decode the data in the buffer
			if self.dataEncoding == 'csv':
				for tile in self.dataBuffer.split(','):
					self.map.layers[-1].data.append(int(tile))
			
			self.inData = False
		if name == 'properties':
			self.inProperties = False

# The map class

class Map (Base):
	def __init__(self, drawer=DrawerSDL()):
		Base.__init__(self)
		
		# Define some variables
		self.tilesets = []					# Tilesets the map can use
		self.drawer = drawer				# Interface to graphics (Default is SDL)
		
		self.camera = Camera()				# The camera to use as the position of the viewer
		
		self.layers = []					# The map data (tiles)
		self.size = [0, 0]					# The maps dimensions
		
		self.setResolution(800, 600)		# Default resolution
	
	""" Change the resolution to draw the map
	"""	
	def setResolution(self, width, height):
		return self.drawer.setResolution(width, height)
		
	"""Loads a map and associated data (tilesets etc..)
	   Args:
			filename - The path to the map.
	   
	   Returns:
			True if succesfull
	"""
	## TO DO:
	## FIX THIS FUNCTION (Currently, the map is erased when the function exits)
	def load(self, filename):
		# Parse the file with our custom handler
		loader = MapLoader()
		parse(filename, loader)
		
		self = loader.map
		
		# Print out the details of the map
		print ("Loaded map!")
		print ("Map Size", self.size)
		for layer in self.layers:
			print ("Layer " + layer.name + " data")
			print (layer.data)
		
	"""Clears and Updates the maps image
	   Args:
			None
	   Returns:
			True if succesfull
	"""
	def update(self):
		# First check if the camera has moved
		# If the camera hasn't moved then there is no point in redrawing
		# the whole map again.
		if self.camera.pos !=  self.camera.oldpos:
			
			# Even if the camera has changed positions, we still don't
			# need to redraw the whole map. We can blit the part of the
			# image that won't change and save some cpu cycles and
			# hopefully increase the FPS.
			
			# Calculate the amount the camera moved.
			diff = (self.camera.oldpos[0] - self.camera.pos[0], self.camera.oldpos[1] - self.camera.pos[1])
			
			# If this is more than the whole screen size, then we might
			# as well redraw the whole screen.
			if (diff[0] > self.drawer.getRes(self.drawer.image)[0] and diff[1] > self.drawer.getRes(self.drawer.image)[1]) or (diff[0] < -1*self.drawer.getRes(self.drawer.image)[0] and diff[1] < -1*self.drawer.getRes(self.drawer.image)[1]):
				
				# Clear the screen
				self.drawer.clear()
				
				# Draw each layer in order
				for layer in self.layers:
					layer.draw()
			
			# If not, move the screen accordingly and only update the
			# bit we need to.
			else:
				# Blit the the part of the screen that hasn't changed
				self.drawer.blit((0, 0), self.drawer.getRes(self.drawer.image), diff, self.drawer.image)
				
				# Update the part of the screen that is new.
				for layer in self.layers:
					if diff[0] > 0:
						layer.drawRect((0, 0), (diff[0], self.drawer.getRes(self.drawer.image)[1]))
					elif diff[0] < 0:
						layer.drawRect((self.drawer.getRes(self.drawer.image)[0] + diff[0], 0), self.drawer.getRes(self.drawer.image))
					
					if diff[1] > 0:
						layer.drawRect((0, 0), 	(self.drawer.getRes(self.drawer.image)[0], diff[1]))
					elif diff[1] < 0:
						layer.drawRect((0, self.drawer.getRes(self.drawer.image)[1] + diff[1]), self.drawer.getRes(self.drawer.image))
			
			# Update the camera
			self.camera.oldpos = (self.camera.pos[0], self.camera.pos[1])
		
		#No Problems
		return True
		
	"""Checks for collision
	"""
	def isColliding(self, pos):
		for layer in self.layers:
			if layer.isColliding(pos):
				return True
		
# A map factory
def loadMap(filename, map=Map()):
	# Parse the file with our custom handler
	loader = MapLoader()
	loader.map = map
	parse(filename, loader)
	
	return loader.map
