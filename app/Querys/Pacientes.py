import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app.config.text import conn

with conn.cursor() as cur:
    cur.execute("SELECT * FROM EMPRESA04.adningreso WHERE AINCONSEC IN (460527,460526,460525,460524)")
    print(cur.fetchall())