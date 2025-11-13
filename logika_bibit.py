from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from ui_bibit import Ui_FormBibit
from database import DatabaseConnection


class BibitWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormBibit()
        self.ui.setupUi(self)
        self.setWindowTitle("Form Input Bibit")

        # 🔗 Hubungkan ke database
        self.db = DatabaseConnection()
        self.conn = self.db.get_connection()
        self.cursor = self.conn.cursor()

        # Hubungkan tombol-tombol
        self.ui.btnNew.clicked.connect(self.new_data)
        self.ui.btnSave.clicked.connect(self.save_data)
        self.ui.btnView.clicked.connect(self.view_data)
        self.ui.btnBack.clicked.connect(self.close)

        # Saat form dibuka, langsung tampilkan data
        self.view_data()

    def new_data(self):
        """Membersihkan semua input."""
        self.ui.txtKode.clear()
        self.ui.txtNama.clear()
        self.ui.txtSatuan.clear()
        self.ui.txtMasuk.clear()
        self.ui.txtKeluar.clear()
        self.ui.txtStok.clear()
        QMessageBox.information(self, "Info", "Form baru siap diisi.")

    def save_data(self):
        """Simpan data bibit ke database."""
        kode = self.ui.txtKode.text().strip()
        nama = self.ui.txtNama.text().strip()
        satuan = self.ui.txtSatuan.text().strip()
        stok = self.ui.txtStok.text().strip() or 0

        if not kode or not nama or not satuan:
            QMessageBox.warning(self, "Peringatan", "Semua field wajib diisi!")
            return

        try:
            query = """
                INSERT INTO bibit (kd_bibit, nama_bibit, satuan, stok)
                VALUES (%s, %s, %s, %s)
            """
            values = (kode, nama, satuan, stok)
            self.cursor.execute(query, values)
            self.conn.commit()

            QMessageBox.information(self, "Sukses", f"Data bibit '{nama}' berhasil disimpan!")
            self.new_data()
            self.view_data()  # refresh tabel
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data!\n{e}")

    def view_data(self):
        """Ambil dan tampilkan data bibit dari database ke tabel di UI."""
        try:
            self.cursor.execute("SELECT kd_bibit, nama_bibit, satuan, stok FROM bibit")
            results = self.cursor.fetchall()

            # Bersihkan tabel
            self.ui.tableBibit.setRowCount(0)

            if not results:
                return

            # Masukkan data ke tabel UI
            for row_index, row_data in enumerate(results):
                self.ui.tableBibit.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    self.ui.tableBibit.setItem(row_index, col_index, QTableWidgetItem(str(data)))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengambil data!\n{e}")

    def closeEvent(self, event):
        """Tutup koneksi ketika jendela ditutup."""
        self.db.close_connection()
        event.accept()
