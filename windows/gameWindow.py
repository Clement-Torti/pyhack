'''
Game window
'''

import utils
from window import Window

class GameWindow(Window):
	def __init__(self, stdscr):
		Window.__init__(self, stdscr, True)

		self.draw()

	
	def setAction(self, c):
		if c == ord('c'):
			return utils.MENU


	def draw(self):
		self.stdscr.addstr("Game window")