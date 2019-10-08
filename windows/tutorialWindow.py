'''
tutorial window
'''
from window import Window
import utils

class TutorialWindow(Window):
	def __init__(self, stdscr):
		Window.__init__(self, stdscr, False)
		self.draw(self.stdscr)

	def setAction(self, c):
		if c == ord('c'):
			return utils.MENU

	def draw(self, stdscr):
		self.stdscr.addstr("No tutorials available for now. click 'c' to return")

