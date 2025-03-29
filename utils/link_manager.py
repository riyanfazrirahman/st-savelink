import sqlite3
from datetime import datetime

def save_link(username, title, url):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO links (username, title, url, timestamp) VALUES (?, ?, ?, ?)",
              (username, title, url, timestamp))
    conn.commit()
    conn.close()

def get_links(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT title, url, timestamp FROM links WHERE username=?", (username,))
    links = c.fetchall()
    conn.close()
    return links
