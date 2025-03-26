# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PLCSettings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OffsetSettings(object):
    def setupUi(self, OffsetSettings):
        if not OffsetSettings.objectName():
            OffsetSettings.setObjectName(u"OffsetSettings")
        OffsetSettings.resize(302, 214)
        self.verticalLayout = QVBoxLayout(OffsetSettings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(OffsetSettings)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setAutoFillBackground(False)
        self.doubleSpinBox_2.setWrapping(True)
        self.doubleSpinBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox_2.setDecimals(3)
        self.doubleSpinBox_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox_2, 2, 1, 1, 1)

        self.GT01Live = QLabel(self.frame)
        self.GT01Live.setObjectName(u"GT01Live")
        self.GT01Live.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.GT01Live, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.doubleSpinBox.setAccelerated(True)
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setSingleStep(0.000000000000000)
        self.doubleSpinBox.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)

        self.GT02Live = QLabel(self.frame)
        self.GT02Live.setObjectName(u"GT02Live")
        self.GT02Live.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.GT02Live, 3, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(OffsetSettings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.pushButton_2 = QPushButton(OffsetSettings)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(OffsetSettings)
        self.pushButton_3.clicked.connect(OffsetSettings.close)

        QMetaObject.connectSlotsByName(OffsetSettings)
    # setupUi

    def retranslateUi(self, OffsetSettings):
        OffsetSettings.setWindowTitle(QCoreApplication.translate("OffsetSettings", u"Form", None))
        self.doubleSpinBox_2.setSuffix(QCoreApplication.translate("OffsetSettings", u" mm", None))
        self.GT01Live.setText(QCoreApplication.translate("OffsetSettings", u"----", None))
        self.label_2.setText(QCoreApplication.translate("OffsetSettings", u"GT-02 Offset", None))
        self.label.setText(QCoreApplication.translate("OffsetSettings", u"GT-01 Offset", None))
        self.doubleSpinBox.setSuffix(QCoreApplication.translate("OffsetSettings", u" mm", None))
        self.GT02Live.setText(QCoreApplication.translate("OffsetSettings", u"----", None))
        self.label_3.setText(QCoreApplication.translate("OffsetSettings", u"Live value :", None))
        self.label_4.setText(QCoreApplication.translate("OffsetSettings", u"Live value :", None))
        self.pushButton.setText(QCoreApplication.translate("OffsetSettings", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("OffsetSettings", u"Cancle", None))
        self.pushButton_2.setText(QCoreApplication.translate("OffsetSettings", u"Reset Counter", None))
    # retranslateUi

