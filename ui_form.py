# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionBibit = QAction(main)
        self.actionBibit.setObjectName(u"actionBibit")
        self.actionKelurahan_Desa = QAction(main)
        self.actionKelurahan_Desa.setObjectName(u"actionKelurahan_Desa")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuMenu_Aplikasi = QMenu(self.menubar)
        self.menuMenu_Aplikasi.setObjectName(u"menuMenu_Aplikasi")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Aplikasi.menuAction())
        self.menuMenu_Aplikasi.addAction(self.actionBibit)
        self.menuMenu_Aplikasi.addAction(self.actionKelurahan_Desa)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionBibit.setText(QCoreApplication.translate("main", u"Bibit", None))
        self.actionKelurahan_Desa.setText(QCoreApplication.translate("main", u"Kelurahan/Desa", None))
        self.menuMenu_Aplikasi.setTitle(QCoreApplication.translate("main", u"Menu Aplikasi", None))
    # retranslateUi

