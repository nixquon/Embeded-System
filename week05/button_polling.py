from gpiozero import Button
from time import sleep

button = Button(27, pull_up = None)

try:
    while True:
        if button.is_pressed:
            print("PRESSED")
        else:
            print("RELEASED")

        sleep(0.1)
finally:
    button.close()