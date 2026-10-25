import board
import adafruit_dht

sensor = adafruit_dht.DHT22(
    board.D17, use_pulseio=False
)

success = 0
failure = 0

try:
    t = sensor.temperature
    h = sensor.humidity
    if t is None or h is None:  # 값이 없는지 먼저 검사
        raise ValueError("값 없음")
    if not (-40 <= t <= 80 and 0 <= h <= 100):  # 범위 검사
        raise ValueError("범위 초과")
    success += 1  # 모든 검사를 통과시 성공 집계
    print(f"정상 | {t:.1f} ℃ | {h:.1f} %RH")  # 정상 값 출력
except RuntimeError as error:  # 센서 읽기 오류 처리
    failure += 1  # 실패 횟수 증가
    print(f"재시도 | {error}")  # 에러 메시지 출력
except ValueError as error:  # None 또는 범위 검사 실패
    failure += 1
    print(f"제외 | {error}")  # 정상 값으로 사용하지 않음

sensor.exit()