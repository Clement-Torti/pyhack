
import sys
sys.path.insert(1, './windows')
sys.path.insert(1, './model')

import curses
from menuWindow import Menu
from scoreWindow import ScoreWindow
from tutorialWindow import TutorialWindow
from gameWindow import GameWindow
import utils
from window import Window
'''
BPI pyhack project
'''



def createWindow(window, stdscr):
    h, w = stdscr.getmaxyx()

    if window == utils.MENU:
        options = ["play", "scores", "tutorials"]
        return Menu(h, w, options, stdscr)
    elif window == utils.GAME:
        return GameWindow(stdscr)
    elif window == utils.SCORES:
        return ScoreWindow(stdscr)
    elif window == utils.TUTORIAL:
        return TutorialWindow(stdscr)


def main(stdscr):
    window = createWindow(utils.MENU, stdscr)

    while 1:
        c = stdscr.getch()
        if c == ord("q"):
            break
        else:
            w = window.setAction(c)
            if w != None:
                stdscr.clear()
                window = createWindow(w, stdscr)

curses.wrapper(main)
