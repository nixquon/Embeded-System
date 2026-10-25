import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont # pillow 라이브러리

i2c = busio.I2C(board.SCL, board.SDA) # 클록·데이터 핀 설정

display = adafruit_ssd1306.SSD1306_I2C( # OLED 객체 생성
    128, 64, i2c, addr=0x3C # 가로·세로 픽셀 수, 버스, 주소
)

display.fill(0)  # 이전 화면의 픽셀을 버퍼에서 지움

image = Image.new("1", (display.width, display.height)) # 이미지 버퍼 생성, 단색 모드
draw = ImageDraw.Draw(image)

# 기본 폰트 로드
font = ImageFont.load_default()

draw.text((0, 0), "Embedded System", font=font, fill=255)
draw.text((0, 16), "I2C OLED", font=font, fill=255)
draw.text((0, 32), "Hello!", font=font, fill=255)

display.image(image)

display.show()  # 세 줄을 그린 버퍼를 한 번에 전송