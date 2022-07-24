import curses
import time, sys, os
import RPi.GPIO as GPIO

from threading import Thread
from enum import Enum

def Measure():
	start = 0
	stop = 0
	realstart = 0
	realstart = time.time()
	GPIO.output(TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)
	start = time.time()
	while GPIO.input(ECHO)==0:
		start = time.time()
		Dif = time.time() - realstart
		if Dif > 0.2:
			#print("Ultrasonic Sensor Timed out, Restarting.")
			time.sleep(0.4)
			return 0;
	while GPIO.input(ECHO)==1:
		stop = time.time()
	elapsed = stop-start
	distance = (elapsed * 36000)/2

	return distance

def showDistance():
    Distance = Measure()
    stdscr.addstr(7,10, "Distance: " + str(Distance))
    stdscr.refresh()
    return;

def monitorDistance():
	while RobotState != State.quit:
		showDistance();
		time.sleep(0.1);
	return;

def turnLeft( ):
    rotateCounterClockwise( 8, motor1 );
    rotateCounterClockwise( 8, motor2 );
    return;

def turnRight( ):
    rotateClockwise( 8, motor2 );
    rotateClockwise( 8, motor1 );
    return;

def goBack( ):
    rotateClockwise( 1000, motor2 );
    rotateCounterClockwise( 1000, motor1 );
    return;

def goAhead( ):
    rotateCounterClockwise( 1000, motor2 );
    rotateClockwise( 1000, motor1 );
    return;

def stop( ):
    stopMotor( motor1 );
    stopMotor( motor2 );
    return;

def handleState():
    while RobotState != State.quit:
		if RobotState is State.voor:
			goAhead();
		if RobotState is State.terug:
			goBack();
		if RobotState is State.links:
			turnLeft();
		if RobotState is State.rechts:
			turnRight();
		if RobotState is State.stop:
			stop();
			time.sleep(0.1)
    return;

def setPins( pins, motor ):
	if len(pins) != 2:
		return "Ivalid parametr. Expected 2 chars string, got: " + setPins
	i = 0;
	for newstate in pins:
		if (newstate == '0'):
			GPIO.output(motor[i], False)
		if (newstate == '1'):
			GPIO.output(motor[i], True)
		i = i + 1;
	return;

def rotate( speed, motor, clockwise ):
	if clockwise:
		sequence = "01"
	else:
		sequence = "10";
	if speed >= 10:
		setPins( sequence, motor )
		time.sleep(0.1)
	else:
		setPins( sequence, motor )
		for i in range(0, 10):
			if i > speed:
				setPins( "00", motor)
			time.sleep(0.001)
	return;

def rotateClockwise( speed, motor ):
	rotate( speed, motor, True );
	return;

def rotateCounterClockwise ( speed, motor ):
	rotate( speed, motor, False );
	return;

def stopMotor ( motor ):
	setPins( "00", motor );
	return;

def checkKeys():
	key = ''
	global RobotState;
	while key != ord('q'):
		time.sleep(0.1)
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
		elif key == ord(' '):
			RobotState = State.stop;
			stdscr.addstr(5,10,"Stop           ")
			stdscr.refresh()
	RobotState = State.quit;
	return;

mot10 = 12
mot11 = 13
motor1 = [mot10, mot11]

mot20 = 18
mot21 = 19
motor2 = [mot20, mot21]

ECHO    = 21
TRIGGER = 20

State = Enum('State', 'stop voor terug links rechts quit')
RobotState = State.stop

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.addstr(5,10,"Stop           ")
stdscr.refresh()

#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO, GPIO.OUT)
GPIO.setup(motor1[0], GPIO.OUT)
GPIO.setup(motor1[1], GPIO.OUT)
GPIO.setup(motor2[0], GPIO.OUT)
GPIO.setup(motor2[1], GPIO.OUT)

GPIO.output(ECHO, False)
GPIO.setup(ECHO,GPIO.IN)

def Main():
	stateHandler = Thread(target = handleState, args = [])
	stateHandler.start()
	#stateHandler.join()
	distanceMonitor = Thread(target = monitorDistance, args = [])
	distanceMonitor.start()

	checkKeys()

	print "State: " + str(RobotState)
	print "thread finished...exiting"

	curses.endwin()

Main()
GPIO.cleanup()
