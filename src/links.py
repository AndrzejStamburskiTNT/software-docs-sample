from gpiozero import LED
from time import sleep

mot10 = LED(17)
mot11 = LED(27)
motor1 = [mot10, mot11]

mot20 = LED(23)
mot21 = LED(24)
motor2 = [mot20, mot21]

clockwiseSeq = ["10", "10", "10", "10", "10", "10", "10", "00"];
counterClockwiseSeq = ["01", "01", "01", "01", "01", "01", "01", "01"];

def setPins( pins, motor ):
#    print "Setting pins to: " + pins;
    if len(pins) != 2:
        return "Ivalid parametr. Expected 2 chars string, got: " + setPins
    i = 0;
    for newstate in pins:
        if (newstate == '0'):
            motor[i].off();
        if (newstate == '1'):
            motor[i].on();
        i = i + 1;
    return;

def rotateClockwise( speed, motor ):
    if (speed < 2000):
        setPins( "01", motor)
    for i in range(1, speed):
        setPins( "00", motor );
    return;

def rotateCounterClockwise ( speed, motor ):
    for sequence in counterClockwiseSeq:
        setPins( sequence, motor );
    return

for x in range(1, 10):
    print ("speed: " + str(x))
    for n in range(1, 2000):
        rotateCounterClockwise( x, motor2 );
        rotateClockwise( x, motor1 );
