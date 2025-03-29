import sqlite3
from datetime import datetime

def save_link(username, title, url):
    """Save a link to the database with the associated username and timestamp."""
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO links (username, title, url, timestamp) VALUES (?, ?, ?, ?)",
              (username, title, url, timestamp))
    conn.commit()
    conn.close()

def get_links(username):
    """Retrieve all saved links for a specific user."""
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT title, url, timestamp FROM links WHERE username=?", (username,))
    links = c.fetchall()
    conn.close()
    return links

def delete_link(username, url):
    """Delete a saved link based on the username and URL."""
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DELETE FROM links WHERE username=? AND url=?", (username, url))
    conn.commit()
    conn.close()
