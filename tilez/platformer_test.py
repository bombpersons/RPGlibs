from map import Map, loadMap
import pygame
from pygame.locals import *

class Game:
	def __init__(self, map=None):
		self.map = map

class Character:
	def __init__(self, map=None, filename=''):
		self.pos = [0, 0] # Position of the character
		self.speed = 5 # How fast the character moves
		self.image = None # The sprite for the player
		
		self.map = map # Map this character is on
		
		self.gravity = 2
		
		if filename != '':
			self.load(filename)
	
	def load(self, filename):
		self.image = pygame.image.load(filename)
	
	def moveForward(self):
		self.pos[0] += self.speed
	
	def moveBackward(self):
		self.pos[0] -= self.speed
	
	def fall(self):
		if not self.map.isRectColliding((self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())):
			self.pos[1] += self.gravity
		else:
			self.pos[1] -= self.gravity
		
	def draw(self, dest): # Dest is the image to draw to (eg the screen)
		dest.blit(self.image, self.map.globalToLocal(self.pos))
		
class Player (Character):
	def __init__(self, **kwargs):
		Character.__init__(self, **kwargs)
		
	def input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			self.moveForward()
		if keys[pygame.K_LEFT]:
			self.moveBackward()
		
		self.fall()
		
		self.map.camera.pos = self.pos


if __name__ == "__main__":
	# Init pygame
	pygame.init()
	screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
	
	# Load a map
	map = loadMap("test/data/ice")
	map.setResolution(1366, 768)
	
	# Make a character
	player = Player(map=map, filename='character.png')
	player.pos = [0, -20]
	
	running = True
	n = 0
	oldtime = 0
	timeTaken = 0
	while running:
		oldtime = pygame.time.get_ticks()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		player.input()
				
		screen.fill((0, 0, 0))
		map.update()
		screen.blit(map.drawer.image, (0, 0))
		player.draw(screen)
		pygame.display.update()
		
		timeTaken = pygame.time.get_ticks() - oldtime
		print 1000 / timeTaken
