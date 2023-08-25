import gpiozero
import time

led_red = LED(17)
led_green = LED(27)
led_blue = LED(22)

while True:
    led_red.on()
    time.sleep(2)
    led_red.off()
    led_green.on()
    time.sleep(2)
    led_green.off()
    led_blue.on()
    time.sleep(2)
    led_blue.off()
