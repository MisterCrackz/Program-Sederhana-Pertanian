import mysql.connector
from mysql.connector import Error
import sys
sys.stdout.reconfigure(encoding='utf-8')

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        try:
            # Ganti konfigurasi sesuai setting XAMPP/phpMyAdmin kamu
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",         # default user di XAMPP
                password="",         # kosong kalau tidak pakai password
                database="pertanian" # nama database kamu
            )

            if self.connection.is_connected():
                print("✅ Koneksi ke database pertanian berhasil!")

        except Error as e:
            print(f"❌ Gagal konek ke database: {e}")

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("🔌 Koneksi database ditutup.")
