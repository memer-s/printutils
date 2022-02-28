import curses
import time

# init
stdscr = curses.initscr()
stdscr.keypad(True)
curses.noecho()
curses.cbreak()

string = ""

while True:
	stdscr.addstr(0,0,string)
	c = stdscr.getch()
	if(c==ord('q')):
		break
	string += chr(c)

time.sleep(1)

# TERMINATE
curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()