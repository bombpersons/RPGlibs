# Class to contain information about a layer
# Contains:
#	Layer data (which tiles and where)
#	Height and width of layer
#	Name
#	Whether or not this layer is a colliding layer.

from base import Base

class Layer (Base):
	def __init__(self):
		Base.__init__(self)
		
		self.map = None # The map this layer belongs to
		
		self.data = [] # List of tile numbers
		self.solid = False # True if this layer is impassible
		self.width = 0
		self.height = 0
	
	""" Draw a rectangle of a layer
	"""
	def drawRect(self, top, bottom):
		# First use the camera position to determine what tiles we want
		realTop = [0, 0]
		realTop[0] = self.map.camera.pos[0] + (top[0] - (self.map.drawer.getRes(self.map.drawer.image)[0] / 2))
		realTop[1] = self.map.camera.pos[1] + (top[1] - (self.map.drawer.getRes(self.map.drawer.image)[1] / 2))
		
		realBottom = [0, 0]
		realBottom[0] = self.map.camera.pos[0] + (bottom[0] - (self.map.drawer.getRes(self.map.drawer.image)[0] / 2))
		realBottom[1] = self.map.camera.pos[1] + (bottom[1] - (self.map.drawer.getRes(self.map.drawer.image)[1] / 2))
		
		# Convert these into tile coords
		topPos = (int((realTop[0] / self.map.tilesets[0].tileSize[0])) - 1, int((realTop[1] / self.map.tilesets[0].tileSize[1])) - 1)
		bottomPos = (int((realBottom[0] / self.map.tilesets[0].tileSize[0])) + 1, int((realBottom[1] / self.map.tilesets[0].tileSize[1])) + 1)
		
		#print realTop, realBottom
		
		# Loop through all of the tiles in this rectangle and draw them.
		for y in range(topPos[1], bottomPos[1]):
			for x in range(topPos[0], bottomPos[0]):
				self.drawTile((x, y))
								
	""" Draw a single tile
	"""
	def drawTile(self, pos):
		# Find the tile number to draw.
		n = (((pos[1]) * self.width) + pos[0])
		if n > 0 and n < self.map.size[0] * self.map.size[1]:
			tile = self.data[n]
		else:
			tile = 0
		
		# Figure out where to draw the tile on the screen
		drawX, drawY = self.map.globalToLocal((((n % self.map.size[0])*self.map.tilesets[0].tileSize[0]), (int(n / self.map.size[0])*self.map.tilesets[0].tileSize[1])))

		# Check if the tile is on screen
		if drawX < self.map.drawer.getRes(self.map.drawer.image)[0] and drawX > -1*self.map.tilesets[0].tileSize[0] and drawY < self.map.drawer.getRes(self.map.drawer.image)[1] and drawY > -1*self.map.tilesets[0].tileSize[1]:
		
			# Don't need to draw if tile is 0
			if tile != 0:
				
				# Reduce tile number by one	
				tile -= 1
				
				# Draw the tile
				self.map.tilesets[0].getTile((tile % self.map.tilesets[0].sizeTiles[0], int(tile / self.map.tilesets[0].sizeTiles[0]))).draw((drawX, drawY))
			
			# If the tile is 0, fill it in with black
			else:
				
				#self.map.drawer.clear(rect=(drawX, drawY, self.map.tilesets[0].tileSize[0], self.map.tilesets[0].tileSize[1]))
				
				pass
	
	""" Draw the whole layer
	"""
	def draw(self):
		# This should work but doesn't				
		#self.drawRect((0, 0), self.map.size)
		
		for x in range(self.map.size[0]):
			for y in range(self.map.size[1]):
				self.drawTile((x, y))
			
	""" Check for collision
	"""
	def isColliding(self, pos):
		# First, check if we are a colliding layer, if not there is no point in proceeding
		if self.solid:
			
			# Find what tile this position would be on
			tilePos = (int(pos[0] / self.map.tilesets[0].tileSize[0]), int(pos[1] / self.map.tilesets[0].tileSize[1]))
			
			# Convert this to raw data form
			tilePosNum = (((tilePos[1]) * self.width) + tilePos[0])
			
			# Check if this tile has a value
			if self.data[tilePosNum] != 0:
				return True
		
		# This layer isn't collidable
		return False
		
	def isRectColliding(self, rect):
		if self.solid:
			
			realTop = (rect[0], rect[1])
			realBottom = (rect[0] + rect[2], rect[1] + rect[3])
			
			# Find out if there are any tiles in this rectangle
			topPos = (int((realTop[0] / self.map.tilesets[0].tileSize[0])), int((realTop[1] / self.map.tilesets[0].tileSize[1])))
			bottomPos = (int((realBottom[0] / self.map.tilesets[0].tileSize[0])) + 1, int((realBottom[1] / self.map.tilesets[0].tileSize[1])) + 1)
			
			for y in range(topPos[1], bottomPos[1]):
				for x in range(topPos[0], bottomPos[0]):
					n = (((y) * self.width) + x)
					if self.data[n] != 0:
						return True
					
