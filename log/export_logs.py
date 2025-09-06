import sqlite3
import os
from datetime import datetime

# Paths
DB_PATH = r"C:\Users\roo\Desktop\Website\log\ip_log.db"
OUTPUT_FILE = r"C:\Users\roo\Desktop\Website\log\ip_logs.txt"

def export_logs():
    if not os.path.exists(DB_PATH):
        print(f"Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, ip, method, path, status_code, timestamp FROM connections ORDER BY timestamp ASC')
    rows = c.fetchall()
    conn.close()

    # Write to text file
    with open(OUTPUT_FILE, 'w') as f:
        f.write(f"IP LOG EXPORT - {datetime.now()}\n")
        f.write("="*50 + "\n\n")
        for row in rows:
            f.write(f"ID: {row[0]} | IP: {row[1]} | Method: {row[2]} | Path: {row[3]} | Status: {row[4]} | Time: {row[5]}\n")

    print(f"Exported {len(rows)} log entries to {OUTPUT_FILE}")

if __name__ == "__main__":
    export_logs()
