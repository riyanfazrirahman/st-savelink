import streamlit as st
from utils.link_manager import get_links

st.title("📂 Daftar Link")

links = get_links(st.session_state.username)

if links:
    for title, url, timestamp in links:
        st.write(f"### [{title}]({url})")
        st.caption(f"Disimpan pada: {timestamp}")
else:
    st.write("Belum ada link yang disimpan.")
