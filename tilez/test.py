from map import loadMap
from PySFML import sf

if __name__ == "__main__":
	# Make a window
	window = sf.RenderWindow(sf.VideoMode(800, 600, 32), "Tilez Test")
	
	# Load a map
	map = loadMap("test/data/ice")
	
	map.drawer.image = window
	
	# Start the main loop
	running = True
	while running:
		event = sf.Event()
		while window.GetEvent(event):
			if event.Type == sf.Event.Closed:
				running = False
		
		# Clear screen
		window.Clear()
				
		# Draw the map
		map.update()
				
		# Display the window
		window.Display()
