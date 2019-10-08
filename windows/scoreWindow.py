'''
score window
'''

from window import Window
from score import Score
import utils

class ScoreWindow(Window):
	def __init__(self, stdscr):
		Window.__init__(self, stdscr, False)
		# read scores
		self.scores = [Score("cltorti", 1, "33"), Score("tortic", 5, "2"),]

		# draw billboard
		self.draw()


	def setAction(self, c):
		if c == ord('c'):
			return utils.MENU

	def draw(self):
		for i, s in enumerate(self.scores):
			self.stdscr.addstr(i, 0, str(s))

		self.stdscr.addstr(len(self.scores), 0, "click 'c' to return to menu")



