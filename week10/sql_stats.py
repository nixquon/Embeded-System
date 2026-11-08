import sqlite3  # Python 기본 SQLite 모듈
from pathlib import Path  # 파일 경로 처리

conn = sqlite3.connect("sensors.db")  # DB 연결·생성

start_ts = "2026-11-08T00:00:00+09:00"  # 시작 포함
end_ts   = "2026-11-09T00:00:00+09:00"  # 끝 제외

stats = conn.execute("""
SELECT
    AVG(temperature), -- 평균 온도
    MIN(temperature), -- 최저 온도
    MAX(temperature), -- 최고 온도
    AVG(humidity),    -- 평균 습도
    COUNT(*)          -- 정상 행 수
FROM readings
WHERE status = 'OK'
  AND timestamp >= ?
  AND timestamp < ?
""", (start_ts, end_ts)).fetchone()

errCount = conn.execute("""
SELECT
    COUNT(*)          -- 정상 행 수
FROM readings
WHERE status = 'ERROR'
  AND timestamp >= ?
  AND timestamp < ?
""", (start_ts, end_ts)).fetchone()

for st, value in zip(["avg_t", "min_t", "max_t", "avg_h", "count"], stats):
  print (f"{st} : {value}");
