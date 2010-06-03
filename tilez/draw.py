# This file can be customized to support different graphics libraries.
# For example sfml or pygame
#
#
#

## PyGame
import pygame
from pygame.locals import *

from base import Base

class DrawerSDL (Base):
	def __init__(self):
		Base.__init__(self)
		
		# Pygame doesn't need to be initialized for what we are doing
		self.image = None
		
		# Variables for tiled to work with, specific to SDL
		self.xCameraMultiplier = 1		# tells the camera which direction is positive on the x axis
		self.yCameraMultiplier = 1		# and also for the y axis
		
	def setResolution(self, width, height):
		self.image = pygame.Surface((width, height), flags=HWSURFACE)
	
	def getRes(self, image):
		return (image.get_width(), image.get_height())
		
	def loadImage(self, filename):
		try:
			image = pygame.image.load(filename)
		except pygame.error, message:
			print ("Cannot load image at: " + filename)
			print ("Are you sure this file is the right format?")
			print ("Are you sure you have permission to access this file?")
			print ("Are you sure the file exists?")
			return None
		
		return image
	
	def blit(self, top, bottom, pos, source):
		if self.image != None:
			self.image.blit(source, (pos[0], pos[1]), area=(top[0], top[1], bottom[0] - top[0], bottom[1] - top[1]))
	
	def clear(self):
		self.image.fill((0, 0, 0))

## Pyglet

#import pyglet
#from base import Base

#class Drawer (Base):
	#def __init__(self):
		#Base.__init__(self)
		
		#self.image = None
		
	#def setResolution(self, width, height):
		#self.image = pyglet.image.create(width, height)
		
	#def loadImage(self, filename):
		#return pyglet.image.load(filename)
		
	#def blit(self, top, bottom, pos, source):
		#subimage = source.get_region(top[0], top[1], top[0] - bottom[0], top[1] - bottom[0])
		#self.image.texture.blit_into(subimage, pos[0], pos[1], 0)
	
	#def clear(self):
		##self.image.clear()
		#pass

from PySFML import sf
from base import Base

class DrawerSFML (Base):
	def __init__(self):
		Base.__init__(self)
		
		# Set initial variables
		self.image = None
	
		# Variables for tiled to work with, specific to SDL
		self.xCameraMultiplier = 1		# tells the camera which direction is positive on the x axis
		self.yCameraMultiplier = 1		# and also for the y axis	
	
	# Set the resolution to draw the map
	def setResolution(self, width, height):
		self.image = sf.Image(width, height, sf.Color(0, 0, 0, 255))
	
	# Get the resolution
	def getRes(self, image):
		return (image.GetWidth(), image.GetHeight())
	
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
		sprite = sf.Sprite(source)
		sprite.SetSubRect(sf.IntRect(top[0], top[1], bottom[0], bottom[1]))
		sprite.SetPosition(pos[0], pos[1])
		
		# draw to our image
		self.image.Draw(sprite)
	
	# clears the image to black	
	def clear(self):
		if self.image != None:
			self.image.Clear(sf.Color(0, 0, 0, 255))
