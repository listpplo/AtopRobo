# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RoboTeach.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(889, 665)
        self.actionCreate_New_Program = QAction(MainWindow)
        self.actionCreate_New_Program.setObjectName(u"actionCreate_New_Program")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2Page1 = QWidget()
        self.tabWidget_2Page1.setObjectName(u"tabWidget_2Page1")
        self.horizontalLayout_2 = QHBoxLayout(self.tabWidget_2Page1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(self.tabWidget_2Page1)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.frame = QFrame(self.tabWidget_2Page1)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(290, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.groupBox)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10)


        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_2)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.groupBox)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_13)


        self.gridLayout.addWidget(self.frame_9, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(252, 255, 51);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(25, 255, 140);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}")
        self.pushButton_5.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(252, 255, 51);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(25, 255, 140);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}")
        self.pushButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(252, 255, 51);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(25, 255, 140);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}")
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_10 = QPushButton(self.frame_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy2.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy2)
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(252, 255, 51);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(25, 255, 140);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}")
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(252, 255, 51);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(25, 255, 140);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}")
        self.pushButton_4.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.gridLayout_2.addWidget(self.frame_7, 2, 1, 1, 1)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_11)

        self.pushButton_2 = QPushButton(self.frame_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(252, 255, 51);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(25, 255, 140);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}")
        self.pushButton_2.setCheckable(False)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_8 = QPushButton(self.frame_8)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(252, 255, 51);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(25, 255, 140);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}")
        self.pushButton_8.setCheckable(False)

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_8)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy2.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy2)
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(252, 255, 51);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(25, 255, 140);\n"
"	border:2px dashed black;\n"
"	border-radius:20%;\n"
"}")
        self.pushButton_9.setCheckable(False)

        self.verticalLayout_3.addWidget(self.pushButton_9)


        self.gridLayout_2.addWidget(self.frame_8, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.frame)

        self.tabWidget_2.addTab(self.tabWidget_2Page1, "")

        self.horizontalLayout.addWidget(self.tabWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Robo Teaching Window", None))
        self.actionCreate_New_Program.setText(QCoreApplication.translate("MainWindow", u"Create New Program", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Z", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"T", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"LIve Cordinates", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"T :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Z :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"PLC :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Connect To\n"
"Robot", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enable\n"
"Torque Lock", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Disable\n"
"Torque Lock", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Go Home", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Table Editor", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save Location", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Delete Location", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Save Table", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabWidget_2Page1), "")
    # retranslateUi

