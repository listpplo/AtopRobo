# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
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
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 616)
        MainWindow.setDocumentMode(False)
        self.actionAdd_Recipe = QAction(MainWindow)
        self.actionAdd_Recipe.setObjectName(u"actionAdd_Recipe")
        icon = QIcon()
        icon.addFile(u":/icons/Asstes/Icons/icons8-add-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAdd_Recipe.setIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Asstes/Icons/icons8-export-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setMenuRole(QAction.MenuRole.QuitRole)
        self.actionExit.setPriority(QAction.Priority.HighPriority)
        self.actionTeach_Robo = QAction(MainWindow)
        self.actionTeach_Robo.setObjectName(u"actionTeach_Robo")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Asstes/Icons/icons8-robot-30.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionTeach_Robo.setIcon(icon2)
        self.actionMapping = QAction(MainWindow)
        self.actionMapping.setObjectName(u"actionMapping")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Asstes/Icons/icons8-mapping-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionMapping.setIcon(icon3)
        self.actionPLC_Settings = QAction(MainWindow)
        self.actionPLC_Settings.setObjectName(u"actionPLC_Settings")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Asstes/Icons/icons8-plc-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPLC_Settings.setIcon(icon4)
        self.actionRobo_Settings = QAction(MainWindow)
        self.actionRobo_Settings.setObjectName(u"actionRobo_Settings")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Asstes/Icons/icons8-robot-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRobo_Settings.setIcon(icon5)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Asstes/Icons/icons8-help-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionHelp.setIcon(icon6)
        self.actionInformation = QAction(MainWindow)
        self.actionInformation.setObjectName(u"actionInformation")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Asstes/Icons/icons8-information-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionInformation.setIcon(icon7)
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Asstes/Icons/icons8-logout-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionLogout.setIcon(icon8)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border:2px dashed black;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget_4 = QTabWidget(self.frame)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy1)
        self.tabWidget_4.setStyleSheet(u"QLabel{\n"
"	border:none;\n"
"}")
        self.tabWidget_4.setIconSize(QSize(30, 30))
        self.tabWidget_4Page1 = QWidget()
        self.tabWidget_4Page1.setObjectName(u"tabWidget_4Page1")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidget_4Page1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.tabWidget_4Page1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        font1 = QFont()
        font1.setBold(True)
        self.groupBox_6.setFont(font1)
        self.groupBox_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.groupBox_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_2)


        self.gridLayout_2.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFont(font1)
        self.groupBox_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)


        self.gridLayout_2.addWidget(self.groupBox_9, 1, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setFont(font1)
        self.groupBox_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.groupBox_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)


        self.gridLayout_2.addWidget(self.groupBox_10, 0, 2, 1, 1)

        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setFont(font1)
        self.groupBox_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.groupBox_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_11)


        self.gridLayout_2.addWidget(self.groupBox_8, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tabWidget_4Page1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_7 = QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font1)
        self.groupBox_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_7.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_10)


        self.gridLayout.addWidget(self.groupBox_7, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font1)
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_4.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_8)


        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_9)


        self.gridLayout.addWidget(self.groupBox_5, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        icon9 = QIcon()
        icon9.addFile(u":/icons/Asstes/Icons/icons8-home-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_4.addTab(self.tabWidget_4Page1, icon9, "")

        self.verticalLayout_2.addWidget(self.tabWidget_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setFamilies([u"OCR A"])
        font2.setPointSize(16)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color:black;\n"
"	border:3px dashed black;\n"
"	background-color: rgb(255, 7, 19);\n"
"}")
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(50, 50))
        self.pushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QSize(0, 60))
        font3 = QFont()
        font3.setFamilies([u"OCR A"])
        font3.setPointSize(14)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	color:black;\n"
"	border:3px dashed black;\n"
"	background-color: rgb(255, 7, 19);\n"
"}")
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border:2px dashed black;\n"
"}\n"
"\n"
"QLabel{\n"
"	border:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(18)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(True)
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setKerning(True)
        self.tableWidget.setFont(font6)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	border:1px solid black;\n"
"}")
        self.tableWidget.setGridStyle(Qt.PenStyle.DashDotDotLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setPointSize(13)
        font7.setBold(True)
        font7.setUnderline(True)
        self.label_5.setFont(font7)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.tableWidget_2 = QTableWidget(self.frame_2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy2.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy2)
        self.tableWidget_2.setMinimumSize(QSize(0, 0))
        self.tableWidget_2.setFont(font6)
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	border:1px solid black;\n"
"}")
        self.tableWidget_2.setGridStyle(Qt.PenStyle.DashDotDotLine)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout.addWidget(self.tableWidget_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuTeach = QMenu(self.menubar)
        self.menuTeach.setObjectName(u"menuTeach")
        self.menuTeach_2 = QMenu(self.menubar)
        self.menuTeach_2.setObjectName(u"menuTeach_2")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuAbout_Help = QMenu(self.menubar)
        self.menuAbout_Help.setObjectName(u"menuAbout_Help")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuTeach.menuAction())
        self.menubar.addAction(self.menuTeach_2.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout_Help.menuAction())
        self.menuTeach.addAction(self.actionAdd_Recipe)
        self.menuTeach.addAction(self.actionMapping)
        self.menuTeach.addSeparator()
        self.menuTeach.addAction(self.actionLogout)
        self.menuTeach.addSeparator()
        self.menuTeach.addAction(self.actionExit)
        self.menuTeach_2.addAction(self.actionTeach_Robo)
        self.menuSettings.addAction(self.actionPLC_Settings)
        self.menuSettings.addAction(self.actionRobo_Settings)
        self.menuAbout_Help.addAction(self.actionHelp)
        self.menuAbout_Help.addAction(self.actionInformation)

        self.retranslateUi(MainWindow)

        self.tabWidget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Testing Machine", None))
        self.actionAdd_Recipe.setText(QCoreApplication.translate("MainWindow", u"Add Recipe", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionTeach_Robo.setText(QCoreApplication.translate("MainWindow", u"Teach Robo", None))
        self.actionMapping.setText(QCoreApplication.translate("MainWindow", u"Mapping", None))
        self.actionPLC_Settings.setText(QCoreApplication.translate("MainWindow", u"PLC Settings", None))
        self.actionRobo_Settings.setText(QCoreApplication.translate("MainWindow", u"Robo Settings", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionInformation.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Current Part Parameter", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"LVDT 1 Value", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Part Status", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"LVDT 2 Value", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Difference", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Cycle Parameter", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"NG Part", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Type \"A\"", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Type \"B\"", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tabWidget_4Page1), QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PLC Status", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Robo Status", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Robo Parameter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bin A", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bin B", None))
        self.menuTeach.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTeach_2.setTitle(QCoreApplication.translate("MainWindow", u"Teach", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuAbout_Help.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

