from gpiozero import Button
from signal import pause
button = Button(27, bounce_time=0.1,
    hold_time=2.0
)
def pressed():
    print("짧게 누름")
def held():
    print("2초 이상 누름")

button.when_pressed = pressed # 누르기 시작
button.when_held = held 
try:
    pause()
finally:
    button.close()
