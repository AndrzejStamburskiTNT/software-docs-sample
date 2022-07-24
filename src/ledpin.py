from gpiozero import LED
from time import sleep

led_yel = LED(17)
led_gro = LED(27)
led_blu = LED(22)
led_red = LED(23)

while True:
    led_red.on()
    sleep(1)
    led_gro.on()
    led_red.off()
    sleep(1)
    led_blu.on()
    led_gro.off()
    sleep(1)
    led_yel.on()
    led_blu.off()
 
    sleep(1)
    led_yel.off()
