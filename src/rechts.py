import RPi.GPIO as GPIO # import GPIO librery

from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1B = 16 # set GPIO-03 as Input 2 of the controller IC
Motor1E = 12 # set GPIO-04 as Enable pin 1 of the controller IC

Motor2B = 03
Motor2E = 04

GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

pwm1=GPIO.PWM(Motor1E,100) # configuring Enable pin means GPIO-04 for PWM
pwm2=GPIO.PWM(Motor2E,100) # configuring Enable pin means GPIO-04 for PWM
pwm1.start(100) # starting it with 50% dutycycle
pwm2.start(100) # starting it with 50% dutycycle

print "GO 100 percent"
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(2)

for speed in ([70, 90, 50, 30, 20, 20, 20, 10, 10, 10]):
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
    print ("GO " + str(speed) + " percent")
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    sleep(1)

print "Now stop"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
pwm1.stop() # stop PWM from GPIO output it is necessary
pwm2.stop() # stop PWM from GPIO output it is necessary
GPIO.cleanup()
