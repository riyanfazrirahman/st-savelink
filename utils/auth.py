import streamlit as st
import sqlite3
import bcrypt

DATABASE = "database.db"

def connect_db():
    """Create a connection to the SQLite database."""
    return sqlite3.connect(DATABASE)

def login(username, password):
    """Verify user login credentials and check password."""
    conn = connect_db()
    c = conn.cursor()
    
    c.execute("SELECT password, role FROM users WHERE username=?", (username,))
    user = c.fetchone()
    
    conn.close()

    if user and bcrypt.checkpw(password.encode(), user[0].encode()):  
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = user[1]
        return user[1]  # Return user role
    return None

def register_user(username, password):
    """Register a new user with an encrypted password."""
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    conn = connect_db()
    c = conn.cursor()
    
    try:
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, "user"))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username already exists
    finally:
        conn.close()
