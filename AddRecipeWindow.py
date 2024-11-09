# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddRecipeWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_AddRecipe(object):
    def setupUi(self, AddRecipe):
        if not AddRecipe.objectName():
            AddRecipe.setObjectName(u"AddRecipe")
        AddRecipe.resize(657, 470)
        icon = QIcon()
        icon.addFile(u":/icons/Asstes/Icons/icons8-add-properties-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AddRecipe.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(AddRecipe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.groupBox = QGroupBox(AddRecipe)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 25, -1, -1)
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(u"tableWidget")
        font1 = QFont()
        font1.setPointSize(12)
        self.tableWidget.setFont(font1)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(0)

        self.verticalLayout.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(AddRecipe)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(200, 0))
        self.groupBox_2.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setKerning(False)
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border:2px dashed black;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(127, 255, 42);\n"
"}")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 25, -1, -1)
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Asstes/Icons/icons8-add-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(60, 60))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/Asstes/Icons/icons8-load-cargo-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(60, 60))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(255, 153, 28);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Asstes/Icons/icons8-delete-all-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(60, 60))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(255, 47, 78);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Asstes/Icons/icons8-exit-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(60, 60))

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(AddRecipe)
        self.pushButton_4.clicked.connect(AddRecipe.close)

        QMetaObject.connectSlotsByName(AddRecipe)
    # setupUi

    def retranslateUi(self, AddRecipe):
        AddRecipe.setWindowTitle(QCoreApplication.translate("AddRecipe", u"Add Recipe Window", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddRecipe", u"File List", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AddRecipe", u"Options", None))
        self.pushButton.setText(QCoreApplication.translate("AddRecipe", u"Add Recipe", None))
        self.pushButton_2.setText(QCoreApplication.translate("AddRecipe", u"Load Recipe", None))
        self.pushButton_3.setText(QCoreApplication.translate("AddRecipe", u"Delete Recipe", None))
        self.pushButton_4.setText(QCoreApplication.translate("AddRecipe", u"Exit", None))
    # retranslateUi

