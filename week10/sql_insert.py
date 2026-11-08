import sqlite3  # Python 기본 SQLite 모듈

conn = sqlite3.connect("sensors.db")  # DB 연결·생성

INSERT_SQL = """
INSERT INTO readings (
    timestamp, temperature, humidity,
    status, device_id, error_message
) VALUES (?, ?, ?, ?, ?, ?)
"""  # 여섯 값을 ? 위치에 바인딩

record = {'timestamp': '2026-11-08T21:45:15+09:00', 'temperature': 24.3, 'humidity': 59.4, 'status': 'OK', 'device_id': 'board D17', 'error_message': ''}

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

insert_record(conn, record)
