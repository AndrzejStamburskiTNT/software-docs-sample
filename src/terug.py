from gpiozero import LED
from time import sleep

pin0 = LED(17)
pin1 = LED(27)
pin2 = LED(22)
pin3 = LED(23)

mot0 = LED(24)
mot1 = LED(25)
mot2 = LED(8)
mot3 = LED(7)

clockwiseSeq = ["0001", "0011", "0010", "0110", "0100", "1100", "1000", "1001"];
counterClockwiseSeq = ["0001", "1001", "1000", "1100", "0100", "0110", "0010", "0011"];
currentPins = "9999";

def setPins( pins ):
#    print "Set pins to: " + pins;
    global currentPins;
    if len(pins) != 4:
        return "Ivalid parametr. Expected 4 chars string, got: " + setPins
    if (pins[0] == '0') & (currentPins[0] != '0'):
        pin0.off();
        mot0.off();
    if (pins[0] == '1') & (currentPins[0] != '1'):
        pin0.on();
        mot0.on();
    if (pins[1] == '0') & (currentPins[1] != '0'):
        pin1.off();
        mot1.off();
    if (pins[1] == '1') & (currentPins[1] != '1'):
        pin1.on();
        mot1.on();
    if (pins[2] == '0') & (currentPins[2] != '0'):
        pin2.off();
        mot2.off();
    if (pins[2] == '1') & (currentPins[2] != '1'):
        pin2.on();
        mot2.on();
    if (pins[3] == '0') & (currentPins[3] != '0'):
        pin3.off();
        mot3.off();
    if (pins[3] == '1') & (currentPins[3] != '1'):
        pin3.on();
        mot3.on();
    currentPins = pins;
    return;

def rotateClockwise( speed ):
    for pins in clockwiseSeq:
        setPins( pins );
        delay = float(1) / speed;
        sleep( delay );
    return;

def rotateCounterClockwise ( speed ):
    for pins in counterClockwiseSeq:
        setPins( pins );
        sleep(float(1) / speed)
    return

while True:
    rotateClockwise( 1200 );
