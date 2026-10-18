from gpiozero import LED
from signal import pause
from time import sleep

led = LED(17)

def forBlink():
    try:
        for i in range(5):
            led.on()
            sleep(1.0)
            led.off()
            sleep(1.0)
            print(i + 1)
    finally:
        led.off()
        led.close()


led.blink(on_time = 1.0, off_time = 1.0)

try:
    pause()
finally:
    led.off()
    led.close()

