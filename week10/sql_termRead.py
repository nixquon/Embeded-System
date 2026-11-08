import sqlite3  # Python 기본 SQLite 모듈

conn = sqlite3.connect("sensors.db")  # DB 연결·생성

start_ts = "2026-11-08T22:27:00+09:00"  # 시작 포함
end_ts   = "2026-11-08T22:28:00+09:00"  # 끝 제외

rows = conn.execute("""
SELECT timestamp, temperature, humidity
FROM readings
WHERE status = 'OK'   -- 정상 데이터만 선택
  AND timestamp >= ? -- 시작 시각 이상
  AND timestamp < ?  -- 끝 시각 미만
ORDER BY timestamp ASC -- 시간 오름차순
""", (start_ts, end_ts)).fetchall()  # 결과를 리스트로

for r in rows:
    print(r)