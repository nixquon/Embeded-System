from gpiozero import Button
from signal import pause

button = Button(27,
    bounce_time=0.1
)

count = 0  # 눌림 횟수 카운트

def count_press():    
    global count
    count += 1
    print(f"count={count}")

button.when_pressed = count_press
try:
    pause()
finally:
    button.close()