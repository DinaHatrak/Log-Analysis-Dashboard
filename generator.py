import time
import random
import datetime

responses = [
    '192.168.1.50 - - [{time}] "GET /index.html HTTP/1.1" 200 1024',
    '192.168.1.12 - - [{time}] "POST /api/v1/login HTTP/1.1" 200 432',
    '172.16.0.5 - - [{time}] "GET /secret-path HTTP/1.1" 404 234',
    '192.168.1.99 - - [{time}] "GET /dashboard HTTP/1.1" 500 5021'
]

print("[*] Generating fake live logs into server.log... Press Ctrl+C to stop.")
while True:
    now = datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S +0300')
    log_line = random.choice(responses).format(time=now)
    with open("server.log", "a") as f:
        f.write(log_line + "\n")
    time.sleep(random.uniform(0.5, 2.0))
