import streamlit as st
from config.database import init_db

# Application configuration
st.set_page_config(page_title="Link Saver App", page_icon="🔗", layout="wide")

# Initialize the database
init_db()

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = None
    st.rerun()
    st.toast("Welcome to the Link Saver App!")

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = None
    st.rerun()
    st.toast("You have logged out successfully!")

# Define pages
save_link_page = st.Page("pages/save_link.py", title="Save Link", icon="🔗", default=True)
view_links_page = st.Page("pages/view_links.py", title="View Links", icon="📂")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
login_page = st.Page("pages/login.py", title="Log in", icon=":material/login:")
backup_to_csv_page = st.Page("pages/backup.py", title="Backup to CSV", icon=":material/backup:")

# Navigation logic
if st.session_state.logged_in:
    username_display = f"Hello, 👤 {st.session_state.username}"
    if st.session_state.role == "admin":
        pg = st.navigation({
            username_display: [logout_page],
            "Menu": [
                save_link_page, 
                view_links_page,
                backup_to_csv_page,
            ],
        })
    else:
        pg = st.navigation({
            username_display: [logout_page],
            "Menu": [
                save_link_page,
                view_links_page
            ],
        })
else:
    pg = st.navigation([
        login_page, 
        save_link_page
    ])

pg.run()
