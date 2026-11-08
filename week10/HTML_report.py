import sqlite3  # Python 기본 SQLite 모듈
from pathlib import Path  # 파일 경로 처리
from datetime import date

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

stats = stats + (errCount,)

def build_report(day, stats):  # HTML 문자열 생성
    # 통계 다섯 값 + 같은 기간의 오류 건수
    avg_t, min_t, max_t, avg_h, count, errors = stats
    return f"""<!doctype html>
<html lang="ko"><meta charset="utf-8">
<title>{day} 센서 리포트</title>
<h1>{day} 센서 리포트</h1>
<ul>
  <li>평균 온도: {avg_t:.1f} °C</li>
  <li>최저/최고: {min_t:.1f} / {max_t:.1f} °C</li>
  <li>평균 습도: {avg_h:.1f} %</li>
  <li>정상 {count}건 · 오류 {errors}건</li>
</ul></html>"""  # .1f는 소수 한 자리 표시



day = date.today().strftime("%Y-%m-%d")

REPORT_DIR = Path("reports")  # 결과 폴더
REPORT_DIR.mkdir(exist_ok=True)  # 이미 있어도 허용

html = build_report(day, stats)  # stats는 여섯 항목
report_path = REPORT_DIR / f"report_{day}.html"
report_path.write_text(html, encoding="utf-8")  # 저장

print("생성:", report_path.resolve())  # 절대 경로