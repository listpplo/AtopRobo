# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutUs.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import assets_rc

class Ui_AbouUs(object):
    def setupUi(self, AbouUs):
        if not AbouUs.objectName():
            AbouUs.setObjectName(u"AbouUs")
        AbouUs.resize(606, 514)
        icon = QIcon()
        icon.addFile(u":/Logo/Asstes/Logos/Nordic logo_290x113.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AbouUs.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(AbouUs)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(AbouUs)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/Logo/Asstes/Logos/Nordic Logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(AbouUs)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(AbouUs)

        QMetaObject.connectSlotsByName(AbouUs)
    # setupUi

    def retranslateUi(self, AbouUs):
        AbouUs.setWindowTitle(QCoreApplication.translate("AbouUs", u"About Us", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("AbouUs", u"We are a design house which is involved in Product Design, Process design and Process Automation", None))
        self.label_3.setText(QCoreApplication.translate("AbouUs", u"Contact: Mr Sandip-9015422003 Email id: sandip@nordictechdesign.com", None))
        self.label_4.setText(QCoreApplication.translate("AbouUs", u"Sec-82, Gurgaon", None))
        self.label_5.setText(QCoreApplication.translate("AbouUs", u"Govt Recognised Startup", None))
    # retranslateUi

