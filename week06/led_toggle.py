from gpiozero import Button, LED
from signal import pause

button = Button(27)
led = LED(17)

def toggle_led():
    led.toggle()
    state = "ON" if led.is_lit else "OFF"
    print(f"LED={state}")

button.when_pressed = toggle_led

try:
    pause() 
finally:
    led.off()
    button.close()
    led.close()
