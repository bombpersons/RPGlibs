from map import Map
from PySFML import sf

if __name__ == "__main__":
	# Make a window
	window = sf.RenderWindow(sf.VideoMode(800, 600, 32), "Tilez Test")
	
	# Load a map
	map = Map()
	map.load("test/data/house")
	
	# Start the main loop
	running = True
	while running:
		event = sf.Event()
		while window.GetEvent(event):
			if event.Type == sf.Event.Closed:
				running = False
		
		# Draw the map
		map.update()
				
		# Clear screen
		window.Clear()
		
		# Draw the map to the screen
		if map.drawer.image != None:
			window.Draw(map.drawer.image)
		
		# Display the window
		window.Display()
