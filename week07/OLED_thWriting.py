import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)

display = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

temperature = 25.4  # 화면 배치를 시험할 가상 온도
humidity = 61.2  # 화면 배치를 시험할 가상 습도

display.fill(0)

image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)

# 기본 폰트 로드
font = ImageFont.load_default()

draw.text((0, 0), "Temperature", font=font, fill=255)
draw.text((0, 16), f"{temperature:.1f} C", font=font, fill=255)
draw.text((0, 34), "Humidity", font=font, fill=255)
draw.text((0, 50), f"{humidity:.1f} %RH", font=font, fill=255)

display.image(image)

display.show()  # 세 줄을 그린 버퍼를 한 번에 전송
