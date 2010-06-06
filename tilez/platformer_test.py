from map import Map, loadMap
import pygame
from pygame.locals import *

class Game:
	def __init__(self, map=None):
		self.map = map

class Character:
	def __init__(self, map=None, filename=''):
		self.pos = [0, 0] # Position of the character
		self.speed = 0 # How fast the character moves
		self.max_speed = 6
		self.acc = 3.0
		self.decell = 0.5
		self.image = None # The sprite for the player
		
		self.map = map # Map this character is on
		
		self.gravity = 2
		
		if filename != '':
			self.load(filename)
	
	def load(self, filename):
		self.image = pygame.image.load(filename)
	
	def moveForward(self):
		if self.map.isRectColliding((self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())) and self.speed < self.max_speed:
			self.speed += self.acc		
	
	def moveBackward(self):
		if self.map.isRectColliding((self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())) and self.speed > -1*self.max_speed:
			self.speed -= self.acc	
	
	def jump(self):
		if self.map.isRectColliding((self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())):
			self.pos[1] -= 100
	
	def fall(self):
		self.pos[0] += self.speed
		
		if not self.map.isRectColliding((self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())):
			self.pos[1] += self.gravity
		
		if self.map.isRectColliding((self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height() - 1)):
			self.pos[0] -= self.speed
			self.speed = 0
			
		if self.map.isRectColliding((self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())):	
			if self.speed < 0:
				self.speed += self.decell
			elif self.speed > 0:
				self.speed -= self.decell
		else:
			if self.speed < 0:
				self.speed += (self.decell / 4)
			elif self.speed > 0:
				self.speed -= (self.decell / 4)
		
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
		if keys[pygame.K_SPACE]:
			self.jump()
		
		self.fall()
		
		self.map.camera.pos = self.pos


if __name__ == "__main__":
	# Init pygame
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	
	# Load a map
	map = loadMap("test/data/ice")
	map.setResolution(800, 600)
	
	# Make a character
	player = Player(map=map, filename='character.png')
	player.pos = [100, 0]
	
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
