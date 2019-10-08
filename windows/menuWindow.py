from window import Window
import utils
import curses

'''
The menu window
'''

class Menu(Window):
    def __init__(self, h, w, options, stdscr):
        Window.__init__(self, stdscr, False)
        self.options = options
        self.h = h
        self.w = w
        self.selectedOption = 0
        self.stdscr

        self.draw()

    '''
    option selector methods
    '''
    def incOption(self):
        self.setSelectedOption((self.selectedOption + 1) % len(self.options))

    def decOption(self):
        self.setSelectedOption((self.selectedOption - 1) % len(self.options))

    def setSelectedOption(self, index):
        assert 0 <= index < len(self.options), "invalid option index"
        self.selectedOption = index
        self.draw()


    def setAction(self, c):
        if c == curses.KEY_DOWN:
            self.incOption()
        elif c == curses.KEY_UP:
            self.decOption()
        elif c == 10:
            return self.selectedOption



    def draw(self):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        for i, o in enumerate(self.options):
            x = self.w // 2 - (len(o) // 2)
            y = self.h // 2 - (len(self.options) // 2 - i)
            if self.selectedOption == i:
                self.stdscr.addstr(y, x, o, curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, o)
