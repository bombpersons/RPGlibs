import pyglet
from map import Map, loadMap
from draw import DrawerPyGlet

if __name__ == "__main__":
	window = pyglet.window.Window()
	
	label = pyglet.text.Label('Hello')
	
	map = Map(drawer=DrawerPyGlet())
	map = loadMap('test/data/house', map=map)
	
	@window.event
	def on_draw():
		window.clear()
		map.update()
		label.draw()
	
	pyglet.app.run()
