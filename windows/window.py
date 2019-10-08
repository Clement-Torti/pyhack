from utils import log
import curses
'''
Superclass of all windows
'''


class Window:
    def __init__(self, stdscr, keypad):
        self.stdscr = stdscr
        curses.curs_set(0)

    def setAction(self, c):
        log("action {} received by {}".format(c, self), self.stdscr)

    def draw(self):
        log("draw called on {}".format(self), self.stdscr)
