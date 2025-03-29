import os
import sqlite3
import pandas as pd
from datetime import datetime

BACKUP_DIR = "backup"

def backup_database():
    """Backup database ke folder 'backup/{timestamp}' dalam format CSV."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(BACKUP_DIR, timestamp)

    os.makedirs(backup_folder, exist_ok=True)
    conn = sqlite3.connect("database.db")

    # Backup tabel users
    users_df = pd.read_sql_query("SELECT * FROM users", conn)
    users_backup_path = os.path.join(backup_folder, "users_backup.csv")
    users_df.to_csv(users_backup_path, index=False)

    # Backup tabel links
    links_df = pd.read_sql_query("SELECT * FROM links", conn)
    links_backup_path = os.path.join(backup_folder, "links_backup.csv")
    links_df.to_csv(links_backup_path, index=False)

    conn.close()
    return timestamp, backup_folder  # Return info untuk notifikasi di Streamlit

def get_backup_list():
    """Mengembalikan daftar folder backup berdasarkan timestamp."""
    if not os.path.exists(BACKUP_DIR):
        return []
    
    return sorted(
        [folder for folder in os.listdir(BACKUP_DIR) if os.path.isdir(os.path.join(BACKUP_DIR, folder))],
        reverse=True
    )

def get_backup_file_path(folder, filename):
    """Mengembalikan path lengkap dari file backup tertentu."""
    return os.path.join(BACKUP_DIR, folder, filename)

def delete_backup(folder):
    """Menghapus folder backup tertentu."""
    folder_path = os.path.join(BACKUP_DIR, folder)
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            os.remove(os.path.join(folder_path, file))
        os.rmdir(folder_path)
        return True
    return False