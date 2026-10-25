import time
from datetime import datetime
import board
import adafruit_dht

sensor = adafruit_dht.DHT22(board.D17, use_pulseio=False)

for count in range(1, 11):  # 총 10회
    temperature = sensor.temperature
    humidity = sensor.humidity

    now = datetime.now().strftime("%H:%M:%S")

    print(f"{count:02d} {now} | "  # 순번: 01~10 / 시간 %H:%M:%S
          f"{temperature:.1f} ℃ | "  # 온도 : *.0℃ 
          f"{humidity:.1f} %RH")  # 습도 *.0 %RH
    time.sleep(2.0)  # 2초 대기

sensor.exit()
