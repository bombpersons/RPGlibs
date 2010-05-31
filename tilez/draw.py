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
		self.image = sf.Image(width, height, sf.color(0, 0, 0, 255))
		
	# Load an image
	def loadImage(self, filename):
		image = sf.Image()
		image.LoadFromFile(filename)
		
		if image == None:
			# Couldn't load image for some reason...
			print("Error, Could not load image at '" + filename + "'\n")
			print("Do you have permission to access these files? Do they exist?\n")
			return None
		
		return image
	
	# Draw an image onto another (the map image)
	def blit(self, top, bottom, pos, source):
		# make a temperory sprite
		sprite = sf.Sprite()
		sprite.SetSubRect(sf.IntRect(top[0], top[1], bottom[0], bottom[1]))
		sprite.SetPosition(pos[0], pos[1])
		
		# draw to our image
		self.image.Draw(sprite)
	
	# clears the image to black	
	def clear(self):
		if self.image != None:
			self.image.Clear(sf.color(0, 0, 0, 255))
