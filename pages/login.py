import streamlit as st
from utils.auth import login, register_user

st.title("🔑 Link Saver - Login/Register")

# Buat tab untuk Login dan Register
tab_login, tab_register = st.tabs(["Login", "Register"])

# **Tab Login**
with tab_login:

    st.subheader("Masukkan username dan password untuk login.")
    username = st.text_input("👤 Username", placeholder="Masukkan username")
    password = st.text_input("🔑 Password", type="password", placeholder="Masukkan password")
    login_button = st.button("🚀 Login", use_container_width=True)

    if login_button:
        if not username or not password:
            st.error("Username dan password harus diisi!")
        else:
            role = login(username, password)
            if role:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = role
                st.success(f"Selamat datang, {username}!")
                st.rerun()
            else:
                st.error("Username atau password salah.")

# **Tab Register**
with tab_register:
    st.subheader("Buat akun baru untuk menggunakan sistem.")
    new_username = st.text_input("👤 Username Baru", placeholder="Masukkan username baru")
    new_password = st.text_input("🔑 Password Baru", type="password", placeholder="Masukkan password")
    confirm_password = st.text_input("🔁 Konfirmasi Password", type="password", placeholder="Masukkan kembali password")
    register_button = st.button("📝 Register", use_container_width=True)

    if register_button:
        if not new_username or not new_password or not confirm_password:
            st.error("Semua kolom harus diisi!")
        elif new_password != confirm_password:
            st.error("Password dan konfirmasi password tidak cocok!")
        else:
            success = register_user(new_username, new_password)
            if success:
                st.success("Registrasi berhasil! Silakan login.")
            else:
                st.error("Username sudah digunakan. Silakan pilih username lain.")
