# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MappingWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_MappingWindow(object):
    def setupUi(self, MappingWindow):
        if not MappingWindow.objectName():
            MappingWindow.setObjectName(u"MappingWindow")
        MappingWindow.resize(473, 556)
        MappingWindow.setStyleSheet(u"QFrame{\n"
"	border:2px dashed black;\n"
"	background:transparent;\n"
"	border-radius:20%;\n"
"}")
        self.verticalLayout = QVBoxLayout(MappingWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(MappingWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(64, 255, 150);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/Asstes/Icons/icons8-add-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(255, 156, 34);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Asstes/Icons/icons8-cross-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(64, 255, 150);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Asstes/Icons/icons8-save-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(155, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Asstes/Icons/icons8-export-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.frame)

        self.tableWidget = QTableWidget(MappingWindow)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(MappingWindow)
        self.pushButton_5.clicked.connect(MappingWindow.close)

        QMetaObject.connectSlotsByName(MappingWindow)
    # setupUi

    def retranslateUi(self, MappingWindow):
        MappingWindow.setWindowTitle(QCoreApplication.translate("MappingWindow", u"Mapping Window", None))
        self.pushButton.setText(QCoreApplication.translate("MappingWindow", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("MappingWindow", u"Delete", None))
        self.pushButton_4.setText(QCoreApplication.translate("MappingWindow", u"Save", None))
        self.pushButton_5.setText(QCoreApplication.translate("MappingWindow", u"Exit", None))
    # retranslateUi

