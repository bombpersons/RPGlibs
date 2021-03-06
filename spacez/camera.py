#       camera.py
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

from base import Base

class Camera (Base):
	def __init__(self):
		Base.__init__(self)
		
		self.pos = [0, 0]			# Where the center of the camera is pointing
		self.oldpos = [9999, 9999]	# Where we were pointing at last frame (used to optimise map drawing)
