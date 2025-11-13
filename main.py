# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_main
from logika_bibit import BibitWindow  # pakai file logika_bibit.py

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_main()
        self.ui.setupUi(self)

        # Aksi menu Bibit di menu utama
        self.ui.actionBibit.triggered.connect(self.open_bibit_window)

    def open_bibit_window(self):
        self.bibit_window = BibitWindow()  # buka form bibit
        self.bibit_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
