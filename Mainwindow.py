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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 751)
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
        self.label_2 = QLabel(self.tabWidget_4Page1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 130, 49, 16))
        icon9 = QIcon()
        icon9.addFile(u":/icons/Asstes/Icons/icons8-home-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_4.addTab(self.tabWidget_4Page1, icon9, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 130, 49, 16))
        icon10 = QIcon()
        icon10.addFile(u":/icons/Asstes/Icons/icons8-graphs-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_4.addTab(self.tab, icon10, "")

        self.verticalLayout_2.addWidget(self.tabWidget_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamilies([u"System"])
        self.pushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 60))
        self.pushButton_2.setFont(font)

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
        font1 = QFont()
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tableWidget.rowCount() < 14):
            self.tableWidget.setRowCount(14)
        font2 = QFont()
        font2.setPointSize(9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem21)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMinimumSize(QSize(275, 306))
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	border:1px solid black;\n"
"}")
        self.tableWidget.setRowCount(14)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout.addWidget(self.tableWidget)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.tableWidget_2 = QTableWidget(self.frame_2)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem31)
        if (self.tableWidget_2.rowCount() < 14):
            self.tableWidget_2.setRowCount(14)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font2);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem43)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy2.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy2)
        self.tableWidget_2.setMinimumSize(QSize(275, 306))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	border:1px solid black;\n"
"}")
        self.tableWidget_2.setRowCount(14)
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

        self.tabWidget_4.setCurrentIndex(1)


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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tabWidget_4Page1), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Graph", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Graphs", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PLC Status", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Robo Status", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Program Parameter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bin A", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"11", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bin B", None))
        ___qtablewidgetitem22 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem23 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem25 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem26 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem27 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem28 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem29 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem30 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem31 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem32 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem33 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem34 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem35 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem36 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem37 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem38 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem39 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem40 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem41 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem42 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem43 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"11", None));
        self.menuTeach.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTeach_2.setTitle(QCoreApplication.translate("MainWindow", u"Teach", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuAbout_Help.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

