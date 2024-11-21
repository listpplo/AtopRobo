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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(969, 686)
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
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(90)

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.tabWidget_2.addTab(self.tabWidget_2Page1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toolBox_19 = QToolBox(self.tab)
        self.toolBox_19.setObjectName(u"toolBox_19")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.toolBox_19.setFont(font)
        self.toolBox_19.setFrameShape(QFrame.Shape.Box)
        self.toolBox_19.setFrameShadow(QFrame.Shadow.Raised)
        self.toolBox_19Page1 = QWidget()
        self.toolBox_19Page1.setObjectName(u"toolBox_19Page1")
        self.verticalLayout_5 = QVBoxLayout(self.toolBox_19Page1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.toolBox_19Page1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(True)
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3.setCheckable(False)
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_22, 2, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_23, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_3)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.spinBox_2, 3, 2, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.spinBox, 2, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.pushButton_17 = QPushButton(self.toolBox_19Page1)
        self.pushButton_17.setObjectName(u"pushButton_17")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton_17.setFont(font2)
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_5.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.toolBox_19Page1)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font2)
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_5.addWidget(self.pushButton_18)

        self.frame_10 = QFrame(self.toolBox_19Page1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_16 = QFrame(self.toolBox_19Page1)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_16)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget_2 = QTableWidget(self.frame_16)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(20)

        self.gridLayout_6.addWidget(self.tableWidget_2, 1, 3, 1, 1)

        self.groupBox_22 = QGroupBox(self.frame_16)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setMinimumSize(QSize(0, 50))
        self.groupBox_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_22)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_27 = QLabel(self.groupBox_22)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_27)

        self.label_28 = QLabel(self.groupBox_22)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_28)

        self.label_30 = QLabel(self.groupBox_22)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_30)

        self.label_29 = QLabel(self.groupBox_22)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_29)

        self.label_32 = QLabel(self.groupBox_22)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_32)

        self.label_31 = QLabel(self.groupBox_22)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_31)

        self.label_33 = QLabel(self.groupBox_22)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_33)

        self.label_34 = QLabel(self.groupBox_22)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_34)


        self.gridLayout_6.addWidget(self.groupBox_22, 2, 3, 1, 1)

        self.groupBox_20 = QGroupBox(self.frame_16)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_25 = QLabel(self.groupBox_20)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(50, 50))
        self.label_25.setPixmap(QPixmap(u":/icons/Asstes/Icons/icons8-height-100.png"))
        self.label_25.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_25)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_20)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.doubleSpinBox)


        self.gridLayout_6.addWidget(self.groupBox_20, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.groupBox_21 = QGroupBox(self.frame_16)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMaximumSize(QSize(130, 100))
        self.groupBox_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_21)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_26 = QLabel(self.groupBox_21)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(50, 50))
        self.label_26.setPixmap(QPixmap(u":/icons/Asstes/Icons/icons8-width-100.png"))
        self.label_26.setScaledContents(True)

        self.verticalLayout_9.addWidget(self.label_26)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_21)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.doubleSpinBox_2)


        self.gridLayout_6.addWidget(self.groupBox_21, 0, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_16)

        icon = QIcon()
        icon.addFile(u":/icons/Asstes/Icons/icons8-a-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolBox_19.addItem(self.toolBox_19Page1, icon, u"Part \"A\" Tray")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font1)
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_4.setCheckable(False)
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.label_24 = QLabel(self.groupBox_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_24, 2, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_35, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_4)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.spinBox_4, 3, 2, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox_4)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.spinBox_3, 2, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.pushButton_19 = QPushButton(self.page)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFont(font2)
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.page)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.pushButton_20)

        self.frame_17 = QFrame(self.page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_17)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tableWidget_3 = QTableWidget(self.frame_17)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(20)

        self.gridLayout_8.addWidget(self.tableWidget_3, 1, 3, 1, 1)

        self.groupBox_23 = QGroupBox(self.frame_17)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMinimumSize(QSize(0, 50))
        self.groupBox_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_23)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_36 = QLabel(self.groupBox_23)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_36)

        self.label_37 = QLabel(self.groupBox_23)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_37)

        self.label_38 = QLabel(self.groupBox_23)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_38)

        self.label_39 = QLabel(self.groupBox_23)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_39)

        self.label_40 = QLabel(self.groupBox_23)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_40)

        self.label_41 = QLabel(self.groupBox_23)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_41)

        self.label_42 = QLabel(self.groupBox_23)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_42)

        self.label_43 = QLabel(self.groupBox_23)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_43)


        self.gridLayout_8.addWidget(self.groupBox_23, 2, 3, 1, 1)

        self.groupBox_24 = QGroupBox(self.frame_17)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_24)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_44 = QLabel(self.groupBox_24)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(50, 50))
        self.label_44.setPixmap(QPixmap(u":/icons/Asstes/Icons/icons8-height-100.png"))
        self.label_44.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_44)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_24)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.doubleSpinBox_3)


        self.gridLayout_8.addWidget(self.groupBox_24, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.groupBox_25 = QGroupBox(self.frame_17)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setMaximumSize(QSize(130, 100))
        self.groupBox_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_25)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_45 = QLabel(self.groupBox_25)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(50, 50))
        self.label_45.setPixmap(QPixmap(u":/icons/Asstes/Icons/icons8-width-100.png"))
        self.label_45.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_45)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_25)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.doubleSpinBox_4)


        self.gridLayout_8.addWidget(self.groupBox_25, 0, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_17)

        icon1 = QIcon()
        icon1.addFile(u":/icons/Asstes/Icons/icons8-b-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolBox_19.addItem(self.page, icon1, u"Part \"B\" Tray")

        self.horizontalLayout_3.addWidget(self.toolBox_19)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget_2)

        self.frame = QFrame(self.centralwidget)
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
        font3 = QFont()
        font3.setPointSize(12)
        self.label_11.setFont(font3)
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


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(1)


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
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Delay", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabWidget_2Page1), QCoreApplication.translate("MainWindow", u"Pick Step", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Part Tray \"A\" Orientation", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Rows", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Columns", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Save Origin", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Reset Location", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Origin Loaction", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Z :", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"T :", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Vertical Height", None))
        self.label_25.setText("")
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Horizontal Width", None))
        self.label_26.setText("")
        self.toolBox_19.setItemText(self.toolBox_19.indexOf(self.toolBox_19Page1), QCoreApplication.translate("MainWindow", u"Part \"A\" Tray", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Part Tray \"B\" Orientation", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Rows", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Columns", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Save Origin", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Reset Location", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Origin Loaction", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Z :", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"T :", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Vertical Height", None))
        self.label_44.setText("")
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"Horizontal Width", None))
        self.label_45.setText("")
        self.toolBox_19.setItemText(self.toolBox_19.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Part \"B\" Tray", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Move Step", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Drop Step", None))
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
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
    # retranslateUi

