from gpiozero import Button

button = Button(27)  # 내부 풀업이 기본값

print("버튼을 누르세요.")
button.wait_for_press() # 입력 대기

print("버튼이 눌렸습니다.")
button.close()
