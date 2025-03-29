import streamlit as st
from utils.auth import login, register_user

st.title("🔑 Link Saver - Login/Register")

# Create tabs for Login and Register
tab_login, tab_register = st.tabs(["Login", "Register"])

# **Login Tab**
with tab_login:

    st.subheader("Enter your username and password to log in.")
    username = st.text_input("👤 Username", placeholder="Enter your username")
    password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
    login_button = st.button("🚀 Login", use_container_width=True)

    if login_button:
        if not username or not password:
            st.error("Username and password are required!")
        else:
            role = login(username, password)
            if role:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = role
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Incorrect username or password.")

# **Register Tab**
with tab_register:
    st.subheader("Create a new account to use the system.")
    new_username = st.text_input("👤 New Username", placeholder="Enter a new username")
    new_password = st.text_input("🔑 New Password", type="password", placeholder="Enter a password")
    confirm_password = st.text_input("🔁 Confirm Password", type="password", placeholder="Re-enter your password")
    register_button = st.button("📝 Register", use_container_width=True)

    if register_button:
        if not new_username or not new_password or not confirm_password:
            st.error("All fields are required!")
        elif new_password != confirm_password:
            st.error("Password and confirmation do not match!")
        else:
            success = register_user(new_username, new_password)
            if success:
                st.success("Registration successful! Please log in.")
            else:
                st.error("Username already taken. Please choose another one.")
