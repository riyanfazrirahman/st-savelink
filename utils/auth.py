import streamlit as st
import sqlite3
import bcrypt

def login(username, password):
    """Memeriksa login user dan memverifikasi password."""
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    
    c.execute("SELECT password, role FROM users WHERE username=?", (username,))
    user = c.fetchone()
    
    conn.close()

    if user and bcrypt.checkpw(password.encode(), user[0].encode()):  
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = user[1]
        return user[1]  # Role pengguna
    else:
        return None


def register_user(username, password):
    """Mendaftarkan user baru dengan password terenkripsi."""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    
    try:
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, "user"))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username sudah ada
    finally:
        conn.close()


