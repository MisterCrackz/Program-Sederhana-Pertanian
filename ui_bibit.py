# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bibit.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_FormBibit(object):
    def setupUi(self, FormBibit):
        if not FormBibit.objectName():
            FormBibit.setObjectName(u"FormBibit")
        FormBibit.resize(1056, 697)
        self.verticalLayout = QVBoxLayout(FormBibit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupInput = QGroupBox(FormBibit)
        self.groupInput.setObjectName(u"groupInput")
        self.gridLayoutInput = QGridLayout(self.groupInput)
        self.gridLayoutInput.setObjectName(u"gridLayoutInput")
        self.labelKode = QLabel(self.groupInput)
        self.labelKode.setObjectName(u"labelKode")

        self.gridLayoutInput.addWidget(self.labelKode, 0, 0, 1, 1)

        self.txtKode = QLineEdit(self.groupInput)
        self.txtKode.setObjectName(u"txtKode")

        self.gridLayoutInput.addWidget(self.txtKode, 0, 1, 1, 1)

        self.labelNama = QLabel(self.groupInput)
        self.labelNama.setObjectName(u"labelNama")

        self.gridLayoutInput.addWidget(self.labelNama, 1, 0, 1, 1)

        self.txtNama = QLineEdit(self.groupInput)
        self.txtNama.setObjectName(u"txtNama")

        self.gridLayoutInput.addWidget(self.txtNama, 1, 1, 1, 1)

        self.labelSatuan = QLabel(self.groupInput)
        self.labelSatuan.setObjectName(u"labelSatuan")

        self.gridLayoutInput.addWidget(self.labelSatuan, 2, 0, 1, 1)

        self.txtSatuan = QLineEdit(self.groupInput)
        self.txtSatuan.setObjectName(u"txtSatuan")

        self.gridLayoutInput.addWidget(self.txtSatuan, 2, 1, 1, 1)

        self.labelMasuk = QLabel(self.groupInput)
        self.labelMasuk.setObjectName(u"labelMasuk")

        self.gridLayoutInput.addWidget(self.labelMasuk, 3, 0, 1, 1)

        self.txtMasuk = QLineEdit(self.groupInput)
        self.txtMasuk.setObjectName(u"txtMasuk")

        self.gridLayoutInput.addWidget(self.txtMasuk, 3, 1, 1, 1)

        self.labelKeluar = QLabel(self.groupInput)
        self.labelKeluar.setObjectName(u"labelKeluar")

        self.gridLayoutInput.addWidget(self.labelKeluar, 4, 0, 1, 1)

        self.txtKeluar = QLineEdit(self.groupInput)
        self.txtKeluar.setObjectName(u"txtKeluar")

        self.gridLayoutInput.addWidget(self.txtKeluar, 4, 1, 1, 1)

        self.labelStok = QLabel(self.groupInput)
        self.labelStok.setObjectName(u"labelStok")

        self.gridLayoutInput.addWidget(self.labelStok, 5, 0, 1, 1)

        self.txtStok = QLineEdit(self.groupInput)
        self.txtStok.setObjectName(u"txtStok")

        self.gridLayoutInput.addWidget(self.txtStok, 5, 1, 1, 1)

        self.layoutButtonInput = QHBoxLayout()
        self.layoutButtonInput.setObjectName(u"layoutButtonInput")
        self.btnNew = QPushButton(self.groupInput)
        self.btnNew.setObjectName(u"btnNew")

        self.layoutButtonInput.addWidget(self.btnNew)

        self.btnSave = QPushButton(self.groupInput)
        self.btnSave.setObjectName(u"btnSave")

        self.layoutButtonInput.addWidget(self.btnSave)

        self.btnView = QPushButton(self.groupInput)
        self.btnView.setObjectName(u"btnView")

        self.layoutButtonInput.addWidget(self.btnView)

        self.btnBack = QPushButton(self.groupInput)
        self.btnBack.setObjectName(u"btnBack")

        self.layoutButtonInput.addWidget(self.btnBack)


        self.gridLayoutInput.addLayout(self.layoutButtonInput, 6, 0, 1, 2)


        self.verticalLayout.addWidget(self.groupInput)

        self.groupView = QGroupBox(FormBibit)
        self.groupView.setObjectName(u"groupView")
        self.verticalLayoutView = QVBoxLayout(self.groupView)
        self.verticalLayoutView.setObjectName(u"verticalLayoutView")
        self.layoutViewButtons = QHBoxLayout()
        self.layoutViewButtons.setObjectName(u"layoutViewButtons")
        self.txtCari = QLineEdit(self.groupView)
        self.txtCari.setObjectName(u"txtCari")

        self.layoutViewButtons.addWidget(self.txtCari)

        self.btnEdit = QPushButton(self.groupView)
        self.btnEdit.setObjectName(u"btnEdit")

        self.layoutViewButtons.addWidget(self.btnEdit)

        self.btnDel = QPushButton(self.groupView)
        self.btnDel.setObjectName(u"btnDel")

        self.layoutViewButtons.addWidget(self.btnDel)

        self.btnBackView = QPushButton(self.groupView)
        self.btnBackView.setObjectName(u"btnBackView")

        self.layoutViewButtons.addWidget(self.btnBackView)


        self.verticalLayoutView.addLayout(self.layoutViewButtons)

        self.tableBibit = QTableWidget(self.groupView)
        if (self.tableBibit.columnCount() < 6):
            self.tableBibit.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableBibit.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableBibit.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableBibit.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableBibit.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableBibit.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableBibit.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableBibit.setObjectName(u"tableBibit")
        self.tableBibit.setColumnCount(6)
        self.tableBibit.horizontalHeader().setVisible(True)
        self.tableBibit.horizontalHeader().setStretchLastSection(True)

        self.verticalLayoutView.addWidget(self.tableBibit)


        self.verticalLayout.addWidget(self.groupView)


        self.retranslateUi(FormBibit)

        QMetaObject.connectSlotsByName(FormBibit)
    # setupUi

    def retranslateUi(self, FormBibit):
        FormBibit.setWindowTitle(QCoreApplication.translate("FormBibit", u"Form Input Bibit", None))
        self.groupInput.setTitle(QCoreApplication.translate("FormBibit", u"FORM INPUT BIBIT", None))
        self.labelKode.setText(QCoreApplication.translate("FormBibit", u"KODE BIBIT :", None))
        self.labelNama.setText(QCoreApplication.translate("FormBibit", u"NAMA BIBIT :", None))
        self.labelSatuan.setText(QCoreApplication.translate("FormBibit", u"SATUAN :", None))
        self.labelMasuk.setText(QCoreApplication.translate("FormBibit", u"BIBIT MASUK :", None))
        self.labelKeluar.setText(QCoreApplication.translate("FormBibit", u"BIBIT KELUAR :", None))
        self.labelStok.setText(QCoreApplication.translate("FormBibit", u"STOK BIBIT :", None))
        self.btnNew.setText(QCoreApplication.translate("FormBibit", u"NEW", None))
        self.btnSave.setText(QCoreApplication.translate("FormBibit", u"SAVE", None))
        self.btnView.setText(QCoreApplication.translate("FormBibit", u"VIEW", None))
        self.btnBack.setText(QCoreApplication.translate("FormBibit", u"BACK", None))
        self.groupView.setTitle(QCoreApplication.translate("FormBibit", u"VIEW INFORMASI BIBIT", None))
        self.txtCari.setPlaceholderText(QCoreApplication.translate("FormBibit", u"Cari...", None))
        self.btnEdit.setText(QCoreApplication.translate("FormBibit", u"EDIT", None))
        self.btnDel.setText(QCoreApplication.translate("FormBibit", u"DELETE", None))
        self.btnBackView.setText(QCoreApplication.translate("FormBibit", u"BACK", None))
        ___qtablewidgetitem = self.tableBibit.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormBibit", u"Kode", None));
        ___qtablewidgetitem1 = self.tableBibit.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormBibit", u"Nama Bibit", None));
        ___qtablewidgetitem2 = self.tableBibit.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormBibit", u"Satuan", None));
        ___qtablewidgetitem3 = self.tableBibit.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormBibit", u"Masuk", None));
        ___qtablewidgetitem4 = self.tableBibit.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormBibit", u"Keluar", None));
        ___qtablewidgetitem5 = self.tableBibit.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormBibit", u"Stok", None));
    # retranslateUi

