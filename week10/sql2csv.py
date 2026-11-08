import csv
import sqlite3

conn = sqlite3.connect("sensors.db")  # DB 연결·생성

start_ts = "2026-11-08T00:00:00+09:00"  # 시작 포함
end_ts   = "2026-11-09T00:00:00+09:00"  # 끝 제외

rows = conn.execute("""
SELECT timestamp, temperature, humidity
FROM readings
WHERE status = 'OK'   -- 정상 데이터만 선택
  AND timestamp >= ? -- 시작 시각 이상
  AND timestamp < ?  -- 끝 시각 미만
ORDER BY timestamp ASC -- 시간 오름차순
""", (start_ts, end_ts)).fetchall()  # 결과를 리스트로


with open("daily_export.csv", "w",  # 기존 파일 덮어쓰기
          newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([  # 열 이름을 먼저 기록
        "timestamp", "temperature", "humidity"
    ])
    writer.writerows(rows)  # 27쪽 조회 결과 전체 저장
