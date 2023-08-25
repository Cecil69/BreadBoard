from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(26)
green = LED(5)

time = 2

def redOn():
    red.on()
    sleep(time)
    red.off()

def yellowOn():
    yellow.on()
    sleep(time)
    yellow.off()

def greenOn():
    green.on()
    sleep(time)
    green.off()

while True:
    redOn()
    yellowOn()
    greenOn()