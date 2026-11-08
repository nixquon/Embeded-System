import time
from zoneinfo import ZoneInfo
from datetime import datetime
import board
import adafruit_dht
from pathlib import Path
import csv

CSV_PATH = Path("environment.csv")
new_file = not CSV_PATH.exists()  # 새 파일 여부

sensor = adafruit_dht.DHT22(
    board.D17, use_pulseio=False
)

def reading() -> dict:
    try:
        t = sensor.temperature
        h = sensor.humidity
        status = "OK"
        errorMsg = ""
        if t is None or h is None:
            raise ValueError("missing Value")
        if not (-40 <= t <= 80 and 0 <= h <= 100):
            raise ValueError("range out")
    except RuntimeError as error: # 센서 읽기 오류 처리
        t, h = None, None
        status = "ERROR"
        errorMsg = error
    except ValueError as error: # None 또는 범위 검사 실패
        t, h = None, None
        status = "ERROR"
        errorMsg = error
    finally:
        return {"timestamp" : timestamp(),
                "temperature" : t, "humidity" : h,
                "status" : status, "device_id" : "board D17",
                "error_message" : errorMsg}



def timestamp():
    return datetime.now(ZoneInfo("Asia/Seoul")).isoformat(
        timespec="seconds"  # 소수 초를 생략
    )

def append_csv(record):  # 레코드 한 건을 추가
    with CSV_PATH.open(
        "a", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        if new_file:  # 파일이 없었던 경우에만 헤더 작성
            writer.writerow([
                "timestamp", "temperature",
                "humidity", "status",
                "device_id", "error_message"
            ])
        writer.writerow([  # 헤더와 동일한 열 순서
            record["timestamp"],
            record["temperature"],  # None은 빈 칸
            record["humidity"],
            record["status"],  # 정상 OK / 오류 ERROR
            record["device_id"],
            record["error_message"]
        ])
        file.flush()  # Python 버퍼를 OS에 전달

try:
    cout = 0
    while(cout < 10):
        cout += 1
        read = reading()
        print(read)
        append_csv(read)
        time.sleep(2.0)
finally:
    sensor.exit()