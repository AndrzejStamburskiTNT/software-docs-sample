import curses
from threading import Thread
from time import sleep
from enum import Enum
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

State = Enum('State', 'stop voor terug links rechts')

def turnLeft( ):
    rotateCounterClockwise( 1000, motor2 );
    rotateClockwise( 1000, motor1 );
    return;

def turnRight( ):
    rotateCounterClockwise( 1000, motor1 );
    rotateClockwise( 1000, motor2 );
    return;

def goBack( ):
    rotateClockwise( 1000, motor1 );
    rotateClockwise( 1000, motor2 );
    return;

def goAchead( ):
    rotateCounterClockwise( 1000, motor1 );
    rotateCounterClockwise( 1000, motor2 );
    return;

def stop( ):
    return;

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()
RobotState = State.voor
stdscr.addstr(5,10,"Ga Voor        ")
stdscr.refresh()

def handleState():
    while RobotState != State.stop:
        if RobotState is State.voor:
            goAchead();
        if RobotState is State.terug:
            goBack();
        if RobotState is State.links:
            turnLeft();
        if RobotState is State.rechts:
            turnRight();
    return;

def checkKeys():
    key = ''
    global RobotState;
    while key != ord('q'):
        key = stdscr.getch()
        if key == curses.KEY_UP:
            RobotState = State.voor;
            stdscr.addstr(5,10,"Ga Voor        ")
            stdscr.refresh()
        elif key == curses.KEY_DOWN:
            RobotState = State.terug;
            stdscr.addstr(5,10,"Ga Terug       ")
            stdscr.refresh()
        elif key == curses.KEY_LEFT:
            RobotState = State.links;
            stdscr.addstr(5,10,"Ga Links       ")
            stdscr.refresh()
        elif key == curses.KEY_RIGHT:
            RobotState = State.rechts;
            stdscr.addstr(5,10,"Ga Rechts      ")
            stdscr.refresh()
    RobotState = State.stop;
    return;

def setPins( pins, motor ):
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
        sleep(float(1) / speed);
    return;

def rotateCounterClockwise ( speed, motor ):
    for sequence in counterClockwiseSeq:
        setPins( sequence, motor );
        sleep(float(1) / speed)
    return

stateHandler = Thread(target = handleState, args = [])
stateHandler.start()
#stateHandler.join()

checkKeys()

print "State: " + str(RobotState)
print "thread finished...exiting"

curses.endwin()
