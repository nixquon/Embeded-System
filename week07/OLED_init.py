import board
import busio # I2C 버스 인터페이스
import adafruit_ssd1306  # OLED 드라이버

i2c = busio.I2C(board.SCL, board.SDA) # 클록·데이터 핀 설정

display = adafruit_ssd1306.SSD1306_I2C( # OLED 객체 생성
    128, 64, i2c, addr=0x3C # 가로·세로 픽셀 수, 버스, 주소
)
display.fill(0) # 메모리의 모든 픽셀을 0으로 지움
display.show() # 버퍼 내용을 실제 OLED로 전송
