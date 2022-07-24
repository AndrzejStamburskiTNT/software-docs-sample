import curses

def turnLeft( ):
    stdscr.addstr(3, 15, "Links")
    return;

def turnRight( ):
    stdscr.addstr(3, 25, "Rechts")
    return;

def moveDown( ):
    stdscr.addstr(4, 20, "Terug")
    return;

def moveUp( ):
    stdscr.addstr(2, 20, "Ga voor")
    return;

def stop( ):
    print "Stop...";
    return;

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP:
        moveUp()
    elif key == curses.KEY_DOWN:
        moveDown()
    elif key == curses.KEY_LEFT:
        turnLeft()
    elif key == curses.KEY_RIGHT:
        turnRight()

curses.endwin()
