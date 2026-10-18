from gpiozero import Button, LED
from signal import pause

button = Button(27)
led = LED(17)

button.when_pressed = led.on
button.when_released = led.off

try:
    pause() 
finally:
    led.off()
    button.close()
    led.close()
