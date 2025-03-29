import streamlit as st
from config.database import init_db

# Konfigurasi aplikasi
st.set_page_config(page_title="Link Saver App", page_icon="🔗", layout="wide")

# Inisialisasi database
init_db()

# Inisialisasi session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = None
    st.rerun()

# Fungsi logout
def logout():
    st.session_state.logged_in = False
    st.session_state.role = None
    st.session_state.username = None
    st.rerun()

# Definisi halaman
save_link_page = st.Page("pages/save_link.py", title="Save Link", icon="🔗", default=True)
view_links_page = st.Page("pages/view_links.py", title="View Links", icon="📂")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
login_page = st.Page("pages/login.py", title="Log in", icon=":material/login:")

# Logika navigasi
if st.session_state.logged_in:
    username_display = f"Hallo, 👤 {st.session_state.username}"
    if st.session_state.role == "admin":
        pg = st.navigation({
            username_display: [logout_page],
            "Menu": [
                save_link_page, 
                view_links_page
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