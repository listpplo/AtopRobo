# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)
import assets_rc

class Ui_PasswordWindow(object):
    def setupUi(self, PasswordWindow):
        if not PasswordWindow.objectName():
            PasswordWindow.setObjectName(u"PasswordWindow")
        PasswordWindow.resize(309, 238)
        self.horizontalLayout = QHBoxLayout(PasswordWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_4 = QTabWidget(PasswordWindow)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4Page1 = QWidget()
        self.tabWidget_4Page1.setObjectName(u"tabWidget_4Page1")
        self.verticalLayout_2 = QVBoxLayout(self.tabWidget_4Page1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.tabWidget_4Page1)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame{\n"
"	border:2px dashed black;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.checkBox, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon = QIcon()
        icon.addFile(u":/icons/Asstes/Icons/icons8-change-password-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border:2px dashed black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(151, 255, 32);\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Asstes/Icons/icons8-circled-right-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(255, 0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Asstes/Icons/icons8-cross-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.tabWidget_4.addTab(self.tabWidget_4Page1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_5, 5, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	border:none;\n"
"}\n"
"QPushButton{\n"
"	border:2px dashed black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(151, 255, 32);\n"
"}")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Asstes/Icons/icons8-change-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(255, 255, 32);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Asstes/Icons/icons8-go-back-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.tabWidget_4.addTab(self.tab, "")

        self.horizontalLayout.addWidget(self.tabWidget_4)

        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.tabWidget_4)
        QWidget.setTabOrder(self.tabWidget_4, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)

        self.retranslateUi(PasswordWindow)

        self.tabWidget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PasswordWindow)
    # setupUi

    def retranslateUi(self, PasswordWindow):
        PasswordWindow.setWindowTitle(QCoreApplication.translate("PasswordWindow", u"Password Window", None))
        self.label_2.setText(QCoreApplication.translate("PasswordWindow", u"Id :", None))
        self.label_3.setText(QCoreApplication.translate("PasswordWindow", u"Password :", None))
        self.checkBox.setText(QCoreApplication.translate("PasswordWindow", u"Show Password", None))
        self.pushButton_3.setText(QCoreApplication.translate("PasswordWindow", u"Change Password", None))
        self.pushButton.setText(QCoreApplication.translate("PasswordWindow", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("PasswordWindow", u"Cancle", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tabWidget_4Page1), QCoreApplication.translate("PasswordWindow", u"Login Page", None))
        self.label_5.setText(QCoreApplication.translate("PasswordWindow", u"Repete Password :", None))
        self.label.setText(QCoreApplication.translate("PasswordWindow", u"Old Password :", None))
        self.label_4.setText(QCoreApplication.translate("PasswordWindow", u"New Password :", None))
        self.pushButton_4.setText(QCoreApplication.translate("PasswordWindow", u"Change", None))
        self.pushButton_5.setText(QCoreApplication.translate("PasswordWindow", u"Go Back", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab), QCoreApplication.translate("PasswordWindow", u"Change Password", None))
    # retranslateUi

