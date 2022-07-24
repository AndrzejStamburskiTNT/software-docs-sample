import curses
from threading import Thread
from time import sleep
from enum import Enum

State = Enum('State', 'stop voor terug links rechts')
RobotState = State.stop

def turnLeft( ):
    print "Links...";
    return;

def turnRight( ):
    print "Rechts...";
    return;

def moveDown( ):
    print "Terug...";
    return;

def moveUp( ):
    print "Ga voor...";
    return;

def stop( ):
    print "Stop...";
    return;

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

def handleState():
    if RobotState is State.stop:
        stop();
    if RobotState is State.voor:
        moveUp();
    if RobotState is State.terug:
        moveDown();
    if RobotState is State.links:
        moveLeft();
    if RobotState is State.rechts:
        moveRight();

def checkKeys():
    key = ''
#	global RobotState
    while key != ord('q'):
        key = stdscr.getch()
        stdscr.addch(20,25,key)
        stdscr.refresh()
        if key == curses.KEY_UP:
            RobotState = State.voor;
        elif key == curses.KEY_DOWN:
            RobotState = State.terug;
        elif key == curses.KEY_LEFT:
            RobotState = State.links;
        elif key == curses.KEY_RIGHT:
            RobotState = State.rechts;

#keyMonitor = Thread(target = checkKeys, args = [])
stateHandler = Thread(target = handleState, args = [])
#keyMonitor.start()
stateHandler.start()
#keyMonitor.join()
stateHandler.join()

checkKeys()

print "State: " + str(RobotState)
print "thread finished...exiting"

curses.endwin()
