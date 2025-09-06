import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ip_log.db")

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute('DELETE FROM connections')
c.execute('DELETE FROM sqlite_sequence WHERE name="connections"')  # reset autoincrement
conn.commit()
conn.close()

print("All logs cleared.")
