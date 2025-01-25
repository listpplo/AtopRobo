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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBox, QVBoxLayout, QWidget)
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
        self.toolBox_19Page1.setGeometry(QRect(0, 0, 627, 555))
        self.verticalLayout_5 = QVBoxLayout(self.toolBox_19Page1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_16 = QFrame(self.toolBox_19Page1)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget_2 = QTableWidget(self.frame_16)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.tableWidget_2.setFont(font1)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_4.addWidget(self.tableWidget_2)

        self.frame_10 = QFrame(self.frame_16)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMaximumSize(QSize(291, 16777215))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.spinBox = QSpinBox(self.frame_11)
        self.spinBox.setObjectName(u"spinBox")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.spinBox.setFont(font3)
        self.spinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(200)
        self.spinBox.setValue(0)

        self.horizontalLayout_8.addWidget(self.spinBox)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.comboBox = QComboBox(self.frame_13)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"Rockwell"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.comboBox.setFont(font4)

        self.horizontalLayout_12.addWidget(self.comboBox)


        self.verticalLayout_7.addWidget(self.frame_13)

        self.pushButton_3 = QPushButton(self.frame_12)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))

        self.verticalLayout_7.addWidget(self.pushButton_3)

        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_16.addWidget(self.label_19)

        self.lineEdit_2 = QLineEdit(self.frame_21)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setReadOnly(False)

        self.horizontalLayout_16.addWidget(self.lineEdit_2)


        self.verticalLayout_7.addWidget(self.frame_21)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.verticalLayout_6.addWidget(self.frame_12)


        self.horizontalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_5.addWidget(self.frame_16)

        icon = QIcon()
        icon.addFile(u":/icons/Asstes/Icons/icons8-a-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolBox_19.addItem(self.toolBox_19Page1, icon, u"Part \"A\" Tray")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 379, 322))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_17 = QFrame(self.page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget_3 = QTableWidget(self.frame_17)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setFont(font1)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_5.addWidget(self.tableWidget_3)

        self.frame_14 = QFrame(self.frame_17)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMaximumSize(QSize(329, 16777215))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_15)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.spinBox_2 = QSpinBox(self.frame_15)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setFont(font3)
        self.spinBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(200)
        self.spinBox_2.setValue(0)

        self.horizontalLayout_13.addWidget(self.spinBox_2)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_18)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_14.addWidget(self.label_17)

        self.comboBox_3 = QComboBox(self.frame_19)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 30))
        self.comboBox_3.setFont(font3)

        self.horizontalLayout_14.addWidget(self.comboBox_3)


        self.verticalLayout_9.addWidget(self.frame_19)

        self.pushButton_11 = QPushButton(self.frame_18)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 50))

        self.verticalLayout_9.addWidget(self.pushButton_11)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_15.addWidget(self.label_18)

        self.lineEdit = QLineEdit(self.frame_20)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setReadOnly(False)

        self.horizontalLayout_15.addWidget(self.lineEdit)


        self.verticalLayout_9.addWidget(self.frame_20)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.verticalLayout_8.addWidget(self.frame_18)


        self.horizontalLayout_5.addWidget(self.frame_14)


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

        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_7.setCheckable(False)

        self.verticalLayout_2.addWidget(self.pushButton_7)


        self.gridLayout_2.addWidget(self.frame_7, 2, 1, 1, 1)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        font5 = QFont()
        font5.setPointSize(12)
        self.label_11.setFont(font5)
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

        self.tabWidget_2.setCurrentIndex(2)


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
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Z", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"T", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Teaching Parameter", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Number Of Location", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Select Location :", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add Location", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Current Play Location :", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.toolBox_19.setItemText(self.toolBox_19.indexOf(self.toolBox_19Page1), QCoreApplication.translate("MainWindow", u"Part \"A\" Tray", None))
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Z", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"T", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Teaching Parameter", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Number Of Location", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Select Location :", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Add Location", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Current Play Location :", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
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
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Play A", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Play B", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Table Editor", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save Location", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Delete Location", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
    # retranslateUi

