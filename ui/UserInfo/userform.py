# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userform.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)
import user_info_rc

class Ui_personForm(object):
    def setupUi(self, personForm):
        if not personForm.objectName():
            personForm.setObjectName(u"personForm")
        personForm.resize(171, 221)
        personForm.setStyleSheet(u"background-color: white;\n"
"\n"
"")
        self.pushButton_userform_userinfo = QPushButton(personForm)
        self.pushButton_userform_userinfo.setObjectName(u"pushButton_userform_userinfo")
        self.pushButton_userform_userinfo.setGeometry(QRect(0, 60, 171, 41))
        self.pushButton_userform_userinfo.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background:rgb(246,246,247);\n"
"\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font:10px;\n"
"	border: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/img/img/\u7528\u6237\u8bbe\u7f6e.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_userform_userinfo.setIcon(icon)
        self.pushButton_userform_userinfo.setIconSize(QSize(14, 14))
        self.pushButton_userform_AIFirstAid = QPushButton(personForm)
        self.pushButton_userform_AIFirstAid.setObjectName(u"pushButton_userform_AIFirstAid")
        self.pushButton_userform_AIFirstAid.setGeometry(QRect(0, 100, 171, 41))
        self.pushButton_userform_AIFirstAid.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background:rgb(246,246,247);\n"
"\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font:10px;\n"
"	border: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/img/img/\u5ba2\u670d.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_userform_AIFirstAid.setIcon(icon1)
        self.pushButton_userform_AIFirstAid.setIconSize(QSize(14, 14))
        self.pushButton_userform_Feedback = QPushButton(personForm)
        self.pushButton_userform_Feedback.setObjectName(u"pushButton_userform_Feedback")
        self.pushButton_userform_Feedback.setGeometry(QRect(0, 140, 171, 41))
        self.pushButton_userform_Feedback.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background:rgb(246,246,247);\n"
"\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font:10px;\n"
"	border: 0px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/img/img/\u7f16\u8f913.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_userform_Feedback.setIcon(icon2)
        self.pushButton_userform_Feedback.setIconSize(QSize(14, 14))
        self.pushButton_userform_logout = QPushButton(personForm)
        self.pushButton_userform_logout.setObjectName(u"pushButton_userform_logout")
        self.pushButton_userform_logout.setGeometry(QRect(0, 180, 171, 41))
        self.pushButton_userform_logout.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background:rgb(246,246,247);\n"
"\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font:10px;\n"
"	border: 0px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/img/img/\u9000\u51fa3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_userform_logout.setIcon(icon3)
        self.pushButton_userform_logout.setIconSize(QSize(14, 14))
        self.label_line1 = QLabel(personForm)
        self.label_line1.setObjectName(u"label_line1")
        self.label_line1.setGeometry(QRect(0, 60, 221, 1))
        self.label_line1.setStyleSheet(u"\n"
"\n"
"QLabel#label_line1\n"
"{\n"
"	border:1px solid rgb(238,238,238); \n"
"	border-color: rgb(238, 238, 238);\n"
"}")
        self.label_line1_2 = QLabel(personForm)
        self.label_line1_2.setObjectName(u"label_line1_2")
        self.label_line1_2.setGeometry(QRect(0, 180, 221, 1))
        self.label_line1_2.setStyleSheet(u"QLabel\n"
"{\n"
"	border:1px solid rgb(238,238,238); \n"
"	border-color: rgb(238, 238, 238);\n"
"}")
        self.frame = QFrame(personForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 171, 60))
        self.frame.setStyleSheet(u"background-color: white;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_userform_name = QLabel(self.frame)
        self.label_userform_name.setObjectName(u"label_userform_name")
        self.label_userform_name.setGeometry(QRect(0, 20, 171, 31))
        self.label_userform_name.setStyleSheet(u"font-size:12px")
        self.label_userform_name.setAlignment(Qt.AlignCenter)

        self.retranslateUi(personForm)

        QMetaObject.connectSlotsByName(personForm)
    # setupUi

    def retranslateUi(self, personForm):
        personForm.setWindowTitle(QCoreApplication.translate("personForm", u"Form", None))
        self.pushButton_userform_userinfo.setText(QCoreApplication.translate("personForm", u" \u4e2a\u4eba\u4e2d\u5fc3", None))
        self.pushButton_userform_AIFirstAid.setText(QCoreApplication.translate("personForm", u" AI \u5ba2\u670d ", None))
        self.pushButton_userform_Feedback.setText(QCoreApplication.translate("personForm", u" \u610f\u89c1\u53cd\u9988", None))
        self.pushButton_userform_logout.setText(QCoreApplication.translate("personForm", u" \u9000\u51fa\u767b\u5f55", None))
        self.label_line1.setText("")
        self.label_line1_2.setText("")
        self.label_userform_name.setText(QCoreApplication.translate("personForm", u"\u672a\u77e5", None))
    # retranslateUi

