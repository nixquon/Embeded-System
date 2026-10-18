from gpiozero import DigitalInputDevice
from time import sleep

gpio22 = DigitalInputDevice(22)

try:
    while True:
        print(gpio22.value)

        sleep(0.1)
finally:
    gpio22.close()