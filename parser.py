import re
import sqlite3
import time
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "logs.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS server_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            timestamp TEXT,
            method TEXT,
            url TEXT,
            status INTEGER,
            size INTEGER
        )
    ''')
    conn.commit()
    conn.close()

LOG_PATTERN = r'(?P<ip>\S+) \S+ \S+ \[(?P<date>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'

def parse_and_save_line(line):
    match = re.match(LOG_PATTERN, line)
    if match:
        data = match.groupdict()
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO server_logs (ip, timestamp, method, url, status, size)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data['ip'], data['date'], data['method'], data['url'], int(data['status']), int(data['size'])))
        conn.commit()
        conn.close()

def watch_log_file(file_path):
    init_db()
    print(f"[*] Monitoring log file: {file_path}")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")
            
    with open(file_path, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            parse_and_save_line(line)

if __name__ == "__main__":
    watch_log_file("../server.log")
