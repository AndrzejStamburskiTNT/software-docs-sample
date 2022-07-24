import curses
from gpiozero import LED
from time import sleep

mot10 = LED(17)
mot11 = LED(27)
mot12 = LED(22)
mot13 = LED(23)
motor1 = [mot10, mot11, mot12, mot13]

mot20 = LED(24)
mot21 = LED(25)
mot22 = LED(8)
mot23 = LED(7)
motor2 = [mot20, mot21, mot22, mot23]

clockwiseSeq = ["0001", "0011", "0010", "0110", "0100", "1100", "1000", "1001"];
counterClockwiseSeq = ["0001", "1001", "1000", "1100", "0100", "0110", "0010", "0011"];

def setPins( pins, motor ):
#    print "Setting pins to: " + pins;
    if len(pins) != 4:
        return "Ivalid parametr. Expected 4 chars string, got: " + setPins
    i = 0;
    for newstate in pins:
        if (newstate == '0'):
            motor[i].off();
        if (newstate == '1'):
            motor[i].on();
        i = i + 1;
    return;

def rotateClockwise( speed, motor ):
    for sequence in clockwiseSeq:
        setPins( sequence, motor );
        sleep( float(1) / speed );
    return;

def rotateCounterClockwise ( speed, motor ):
    for sequence in counterClockwiseSeq:
        setPins( sequence, motor );
        sleep( float(1) / speed )
    return

def turnLeft( ):
    stdscr.addstr(3, 15, "Links")
    rotateCounterClockwise( 600, motor2 );
    rotateClockwise( 600, motor1 );
    return;

def turnRight( ):
    stdscr.addstr(3, 25, "Rechts")
    rotateCounterClockwise( 600, motor1 );
    rotateClockwise( 600, motor2 );
    return;

def moveDown( ):
    stdscr.addstr(4, 20, "Terug")
    rotateClockwise( 300, motor2 );
    rotateClockwise( 300, motor1 );
    return;

def moveUp( ):
    stdscr.addstr(2, 20, "Ga voor")
    rotateCounterClockwise( 300, motor2 );
    rotateCounterClockwise( 300, motor1 );
    return;

def stop( ):
    setPins( "0000", motor1 )
    setPins( "0000", motor2 )
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
