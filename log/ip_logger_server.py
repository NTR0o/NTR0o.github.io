import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import sqlite3

# --- CONFIGURATION ---
PORT = 8000
SITE_DIR = r"C:\Users\roo\Desktop\Website"  # Serve the website folder
DB_PATH = r"C:\Users\roo\Desktop\Website\log\ip_log.db"

# Add your IPs to ignore
IGNORE_IPS = [
    "127.0.0.1",       # your own computer
    "192.168.1.1" #pc
   
]

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS connections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT NOT NULL,
        path TEXT,
        method TEXT,
        status_code INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# --- REQUEST HANDLER ---
class LoggingHandler(SimpleHTTPRequestHandler):

    def log_ip(self, status_code):
        ip = self.client_address[0]
        if ip in IGNORE_IPS:
            return

        path = self.path
        method = self.command

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO connections (ip, path, method, status_code)
            VALUES (?, ?, ?, ?)
        ''', (ip, path, method, status_code))
        conn.commit()
        conn.close()

        print(f"[LOGGED] {ip} {method} {path} -> {status_code}")

    def do_GET(self):
        super().do_GET()
        self.log_ip(200 if self.path != "/favicon.ico" else 404)

    def do_POST(self):
        super().do_POST()
        self.log_ip(200)

# --- MAIN ---
if __name__ == "__main__":
    os.chdir(SITE_DIR)  # serve website files
    init_db()
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, LoggingHandler)
    print(f"Server running on port {PORT} and serving {SITE_DIR}")
    httpd.serve_forever()
