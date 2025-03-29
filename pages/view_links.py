import streamlit as st
from utils.link_manager import get_links, delete_link

st.title("📂 Saved Links")

# Check if the user is logged in
if "username" not in st.session_state:
    st.warning("Please log in first!")
    st.stop()

# Retrieve saved links from the database
links = get_links(st.session_state.username)

if links:
    for title, url, timestamp in links:
        col1, col2 = st.columns([0.8, 0.2])
        
        with col1:
            st.write(f"### [{title}]({url})")
            st.caption(f"Saved on: {timestamp}")

        with col2:
            if st.button("🗑 Delete", key=url):  
                delete_link(st.session_state.username, url)
                st.rerun()  # Refresh the page after deleting the link
else:
    st.write("No links saved yet.")
