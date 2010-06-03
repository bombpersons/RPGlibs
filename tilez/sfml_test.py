from map import loadMap, Map
from draw import DrawerSFML
from camera import Camera
from PySFML import sf

if __name__ == "__main__":
	# Make a window
	window = sf.RenderWindow(sf.VideoMode(800, 600, 32), "Tilez Test")
	
	# Load a map
	map = Map()
	map.drawer = DrawerSFML()
	map = loadMap("test/data/house", map=map)
	map.drawer.image = window
	
	map.camera = Camera()
	
	# Get input
	input = window.GetInput()
	
	# Start the main loop
	running = True
	n = 0
	
	while running:
		event = sf.Event()
		while window.GetEvent(event):
			if event.Type == sf.Event.Closed:
				running = False
		
		# Move map
		if input.IsKeyDown(sf.Key.Left):
			map.camera.pos[0] -= 5
		if input.IsKeyDown(sf.Key.Right):
			map.camera.pos[0] += 5
		if input.IsKeyDown(sf.Key.Up):
			map.camera.pos[1] -= 5
		if input.IsKeyDown(sf.Key.Down):
			map.camera.pos[1] += 5
		
		if map.isColliding(map.camera.pos):
			print "Colliding!"
		
		# Clear screen
		window.Clear()
				
		# Draw the map
		map.update()
		
		#print n
		n += 1
		
		# Display the window
		window.Display()
