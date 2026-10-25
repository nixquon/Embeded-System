import time
from datetime import datetime
import board
import adafruit_dht
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

sensor = adafruit_dht.DHT22(
    board.D17, use_pulseio=False
)

i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(
    128, 64, i2c, addr=0x3C
)

def reading() -> tuple:
    try:
        t = sensor.temperature
        h = sensor.humidity
        if t is None or h is None:  # 값이 없는지 먼저 검사
            raise ValueError("값 없음")
        if not (-40 <= t <= 80 and 0 <= h <= 100):  # 범위 검사
            raise ValueError("범위 초과")
        return t, h, None
    except RuntimeError as error:  # 센서 읽기 오류 처리
        return None, None, error
    except ValueError as error:  # None 또는 범위 검사 실패
        return None, None, error


def oledWriting(temperature, humidity, error = None):
    display.fill(0)

    image = Image.new("1", (display.width, display.height))
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    if (not (error is None)):
        draw.text((0, 0), "Sensor Error", font=font, fill=255)
        draw.text((0, 32), str(error)[:20], font=font, fill=255)

    else:
        draw.text((0, 8), f"{temperature:.1f} C", font=font, fill=255)
        draw.text((0, 32), f"{humidity:.1f} %RH", font=font, fill=255)

    display.image(image)

    display.show()

try:
    while(True):
        temperature, humidity, error = reading() # 온도, 습도, 에러 읽기
        oledWriting(temperature, humidity, error) # OLED에 출력
        time.sleep(2.0)
finally:
    sensor.exit()
    display.fill(0); display.show()