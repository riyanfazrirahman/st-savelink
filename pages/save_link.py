import streamlit as st
from utils.link_manager import save_link
import requests
from bs4 import BeautifulSoup

st.title("🔗 Simpan Link")

# Cek apakah user sudah login
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ Anda harus login terlebih dahulu untuk menyimpan link!")
    st.stop()  # Menghentikan eksekusi kode selanjutnya

url = st.text_input("Masukkan URL")

def get_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string if soup.title else "No Title"
    except:
        return "Gagal mengambil title"

if st.button("Simpan"):
    if url:
        title = get_title(url)
        save_link(st.session_state.username, title, url)
        st.success("✅ Link berhasil disimpan!")
    else:
        st.error("❌ Masukkan URL terlebih dahulu!")
