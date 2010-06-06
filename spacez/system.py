#       system.py
#       
#       Copyright 2010 gnome <gnome@Archy>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

# The class for a solar system. Handles drawing the screen and updating
# planet orbits etc..

from base import Base
from camera import Camera
from draw import DrawerSDL

class System (Base):
	def __init__(self, *args, **kwargs):
		Base.__init__(self, *args, **kwargs)
		
		self.drawer = DrawerSDL()
		self.camera = Camera()
		
		self.objects = [] # Things in the system (eg, planets, stations)
	
	""" Change the resolution to draw the map
	"""	
	def setResolution(self, width, height):
		return self.drawer.setResolution(width, height)
