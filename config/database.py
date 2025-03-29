import sqlite3
import bcrypt

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY, 
                    password TEXT, 
                    role TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS links (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    username TEXT, 
                    title TEXT, 
                    url TEXT, 
                    timestamp TEXT)''')
    
    # Cek apakah akun admin sudah ada
    c.execute("SELECT COUNT(*) FROM users WHERE username='admin'")
    if c.fetchone()[0] == 0:
        # Buat password admin terenkripsi
        admin_password = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()).decode()
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                  ("admin", admin_password, "admin"))
        print("✅ Akun admin berhasil dibuat!")

    conn.commit()
    conn.close()
