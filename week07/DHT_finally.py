import time
from datetime import datetime
import board
import adafruit_dht

sensor = adafruit_dht.DHT22(
    board.D17, use_pulseio=False
)

def reading(success: int, failure: int, cout: int) -> tuple:
    try:
        t = sensor.temperature
        h = sensor.humidity
        if t is None or h is None:  # 값이 없는지 먼저 검사
            raise ValueError("값 없음")
        if not (-40 <= t <= 80 and 0 <= h <= 100):  # 범위 검사
            raise ValueError("범위 초과")
        success += 1  # 모든 검사를 통과한 경우만 성공 집계
        printing(cout, "정상", t, h)
    except RuntimeError as error:  # 센서 읽기 오류 처리
        failure += 1  # 실패 횟수 증가
        printing(cout, "재시도", error = error)
    except ValueError as error:  # None 또는 범위 검사 실패
        failure += 1
        printing(cout, "제외", error = error)
    finally:
        return success, failure

def printing(cout: int, state: str,
             t: float = None, h: float = None,
             error: str = None):
    now = datetime.now().strftime("%H:%M:%S")
    if (state == "정상"):
        print(f"{cout:02d} {now} | "  # 순번: 01~10 / 시간 %H:%M:%S
            f"{state} | " # 상태 출력
            f"{t:.1f} ℃ | "  # 온도 : *.0℃ 
            f"{h:.1f} %RH")  # 습도 *.0 %RH
    else: 
        print(f"{cout:02d} {now} | "  # 순번: 01~10 / 시간 %H:%M:%S
            f"{state} | " # 상태 출력
            f"{error} | ") # 에러 내용 출력

try:
    success = 0
    failure = 0
    cout = 0
    while(True):
        cout += 1
        success, failure = reading(success, failure, cout)
        time.sleep(2.0)
finally:
    sensor.exit()
