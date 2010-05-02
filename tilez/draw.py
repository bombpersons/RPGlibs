# This file can be customized to support different graphics libraries.
# For example sfml or pygame
#
#
#


# SFML

from PySFML import sf
from base import Base

class Drawer (Base):
	def __init__(self):
		Base.__init__(self)
		
		# Set initial variables
		self.image = None
	
	# Set the resolution to draw the map
	def setResolution(self, width, height):
		self.image = sf.Image(width, height, sf.color(0, 0, 0, 255)
		
	# Load an image
	def loadImage(self, fileimage):
		image = sf.Image()
		image.LoadFromFile(filename)
		
		return image
	
	def blit(self, top, bottom, source):
		pass
		
	def clear(self):
		pass
