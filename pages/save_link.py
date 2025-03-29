import streamlit as st
from utils.link_manager import save_link
import requests
from bs4 import BeautifulSoup

st.title("🔗 Save Link")

# Check if the user is logged in
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("⚠️ You must log in first to save links!")
    st.stop()  # Stop further execution

url = st.text_input("Enter URL")

def get_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string if soup.title else "No Title"
    except:
        return "Failed to retrieve title"

if st.button("Save"):
    if url:
        title = get_title(url)
        save_link(st.session_state.username, title, url)
        st.success("✅ Link saved successfully!")
    else:
        st.error("❌ Please enter a URL first!")
