import curses
from menu import Menu
from utils import log
'''
BPI pyhack project
'''


def main(stdscr):
    h, w = stdscr.getmaxyx()
    options = ["play", "scores", "tutorials"]
    selectedOption = 0

    menu = Menu(h, w, options, stdscr)

    while 1:
        c = stdscr.getch()
        if c == ord("q"):
            break
        else:
            menu.setAction(c)

curses.wrapper(main)
