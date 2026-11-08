import time
from zoneinfo import ZoneInfo
from datetime import datetime
import board
import adafruit_dht
from pathlib import Path
import csv
import sqlite3  # Python 기본 SQLite 모듈

conn = sqlite3.connect("sensors.db")  # DB 연결·생성

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
        errorMsg = str(error)
    except ValueError as error: # None 또는 범위 검사 실패
        t, h = None, None
        status = "ERROR"
        errorMsg = str(error)
    finally:
        return {"timestamp" : timestamp(),
                "temperature" : t, "humidity" : h,
                "status" : status, "device_id" : "board D17",
                "error_message" : errorMsg}



def timestamp():
    return datetime.now(ZoneInfo("Asia/Seoul")).isoformat(
        timespec="seconds"  # 소수 초를 생략
    )

INSERT_SQL = """
INSERT INTO readings (
    timestamp, temperature, humidity,
    status, device_id, error_message
) VALUES (?, ?, ?, ?, ?, ?)
"""  # 여섯 값을 ? 위치에 바인딩

def insert_record(conn, record):  # 한 건 저장 함수
    try:
        with conn:  # 성공 시 commit, 예외 시 rollback
            conn.execute(INSERT_SQL, (
                record["timestamp"],
                record["temperature"],
                record["humidity"],
                record["status"],
                record["device_id"],
                record["error_message"]
            ))
    except sqlite3.Error as exc:  # DB 오류 처리
        print("DB 저장 실패:", exc)
        raise  # 호출한 쪽에도 오류 전달


try:
    cout = 0
    while(cout < 10):
        cout += 1
        read = reading()
        print(read)
        insert_record(conn, read)
        time.sleep(2.0)
finally:
    sensor.exit()