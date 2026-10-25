from gpiozero import Button
from signal import pause

button = Button(27)

def pressed():
    print("PRESSED")
def released():
    print("RELEASED")

#이벤트 등록 
button.when_pressed = pressed
button.when_released = released

try:
    pause()
finally:
    button.close()
