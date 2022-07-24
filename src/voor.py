import time, sys, os
import RPi.GPIO as GPIO

from enum import Enum

def goBack( ):
    stop();
    rotateClockwise( 1000, motor1 );
    rotateClockwise( 1000, motor2 );
    return;

def goAhead( ):
    stop();
    rotateCounterClockwise( 1000, motor1 );
    rotateCounterClockwise( 1000, motor2 );
    return;

def stop( ):
    stopMotor( motor1 );
    stopMotor( motor2 );
    pulseMotor1[0].stop();
    pulseMotor1[1].stop();
    pulseMotor2[0].stop();
    pulseMotor2[1].stop();
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

def rotateClockwise( speed, motor ):
    setPins( "01", motor );
    #do something with speed
    return;

def rotateCounterClockwise ( speed, motor ):
    setPins( "10", motor );
    #do something with speed
    return

def stopMotor ( motor ):
    setPins( "00", motor );
    return;

mot10 = 12
mot11 = 13
motor1 = [mot10, mot11]

mot20 = 18
mot21 = 19
motor2 = [mot20, mot21]

#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(motor1[0], GPIO.OUT)
GPIO.setup(motor1[1], GPIO.OUT)
GPIO.setup(motor2[0], GPIO.OUT)
GPIO.setup(motor2[1], GPIO.OUT)

pulseMotor1 = []
pulseMotor1.append(GPIO.PWM(mot10, 1000));
pulseMotor1.append(GPIO.PWM(mot11, 1000));

pulseMotor2 = []
pulseMotor2.append(GPIO.PWM(mot20, 1000));
pulseMotor2.append(GPIO.PWM(mot21, 1000));

def gaVoor():
    setPins("00", motor1);
    pulseMotor1[0].start(50);
    setPins("00", motor2);
    pulseMotor2[0].start(50);
    return;

def Main():
    gaVoor();
    time.sleep(5);
    stop()
    return;

Main()
GPIO.cleanup()
