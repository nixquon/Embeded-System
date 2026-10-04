from gpiozero import LED
from time import sleep

led = LED(17)

def normalBlink():
    led.blink(on_time = 1.0, off_time = 1.0, n = 5)

def unbalancedBlink():
    led.blink(on_time = 0.2, off_time = 0.8, n = 10)

def warningBlink():
    while True:
        led.blink(on_time = 0.1, off_time = 0.1, n = 3)
        sleep(1.5)

try:
    normalBlink()
    sleep(10)
    unbalancedBlink()
    sleep(10)
    warningBlink()
finally:
    led.off()
    led.close()