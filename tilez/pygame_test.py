from map import Map, loadMap
import pygame
from pygame.locals import *

if __name__ == "__main__":
	# Init pygame
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	
	# Load a map
	map = loadMap("test/data/house")
	print map.layers[1].solid
	
	running = True
	n = 0
	oldtime = 0
	timeTaken = 0
	while running:
		oldtime = pygame.time.get_ticks()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			map.camera.pos[1] -= 5
		if keys[pygame.K_DOWN]:
			map.camera.pos[1] += 5
		if keys[pygame.K_LEFT]:
			map.camera.pos[0] -= 5
		if keys[pygame.K_RIGHT]:
			map.camera.pos[0] += 5
		
		if map.isColliding(map.camera.pos):
			pass
				
		screen.fill((0, 0, 0))
		map.update()
		screen.blit(map.drawer.image, (0, 0))
		pygame.display.flip()
		
		timeTaken = pygame.time.get_ticks() - oldtime
		print 1000 / timeTaken
