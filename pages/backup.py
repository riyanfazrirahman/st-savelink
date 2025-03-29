import streamlit as st
from utils.backup_manager import backup_database, get_backup_list, delete_backup, get_backup_file_path

st.title("📂 Database Backup Manager")

# Tombol untuk membuat backup baru
if st.button("📌 Create New Backup"):
    timestamp, folder = backup_database()
    st.success(f"✅ Backup berhasil! Disimpan di `{folder}`")
    st.rerun()  # Refresh halaman

# Menampilkan daftar backup yang tersedia
backups = get_backup_list()

if backups:
    st.subheader("📜 Available Backups")
    for folder in backups:
        
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            st.write(f"📅 **{folder}**")  # Menampilkan nama folder backup
        with col2:
            with open(get_backup_file_path(folder, "users_backup.csv"), "rb") as file:
                st.download_button(
                    "⬇ Download Users Backup",
                    file,
                    file_name=f"users_backup_{folder}.csv",
                    mime="text/csv"
                )
        with col3:
            with open(get_backup_file_path(folder, "links_backup.csv"), "rb") as file:
                st.download_button(
                    "⬇ Download Links Backup",
                    file,
                    file_name=f"links_backup_{folder}.csv",
                    mime="text/csv"
                )
        with col4:
            if st.button("❌ Delete", key=f"del_{folder}"):
                if delete_backup(folder):
                    st.warning(f"🗑 Backup `{folder}` telah dihapus!")
                    st.rerun()
                else:
                    st.error(f"❌ Gagal menghapus backup `{folder}`. Pastikan folder ada.")


else:
    st.info("Belum ada backup yang tersedia.")

