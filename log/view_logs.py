import sqlite3
import os
import time

DB_PATH = r"C:\Users\roo\Desktop\Website\log\ip_log.db"
REFRESH_INTERVAL = 2  # seconds

def view_logs():
    last_ids = set()  # Track already printed IDs

    while True:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT id, ip, method, path, status_code, timestamp FROM connections ORDER BY timestamp ASC')
        rows = c.fetchall()
        conn.close()

        # Print only new rows
        for row in rows:
            if row[0] not in last_ids:
                print(f"ID: {row[0]} | IP: {row[1]} | Method: {row[2]} | Path: {row[3]} | Status: {row[4]} | Time: {row[5]}")
                last_ids.add(row[0])

        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    print("--- Auto-refreshing logs (Ctrl+C to stop) ---\n")
    view_logs()
