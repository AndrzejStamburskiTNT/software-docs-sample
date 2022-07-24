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
        sleep(float(1) / speed)
    return

while True:
    rotateCounterClockwise( 1200, motor1 );
    rotateClockwise( 1200, motor2 );
