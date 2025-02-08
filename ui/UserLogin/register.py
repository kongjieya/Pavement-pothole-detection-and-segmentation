# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_v2.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import login_rc

class Ui_registerWindow(object):
    def setupUi(self, registerWindow):
        if not registerWindow.objectName():
            registerWindow.setObjectName(u"registerWindow")
        registerWindow.resize(701, 450)
        self.mainWindow = QWidget(registerWindow)
        self.mainWindow.setObjectName(u"mainWindow")
        self.mainWindow.setStyleSheet(u"QLineEdit{\n"
"	border-radius:5px;\n"
"	border:1px black solid;\n"
"}\n"
"QLineEdit:hover{\n"
"	padding:2px;\n"
"\n"
"}")
        self.register_username = QLineEdit(self.mainWindow)
        self.register_username.setObjectName(u"register_username")
        self.register_username.setGeometry(QRect(230, 224, 201, 31))
        self.register_username.setStyleSheet(u"")
        self.register_username.setClearButtonEnabled(True)
        self.register_password = QLineEdit(self.mainWindow)
        self.register_password.setObjectName(u"register_password")
        self.register_password.setGeometry(QRect(230, 274, 201, 31))
        self.register_password.setStyleSheet(u"")
        self.register_password.setEchoMode(QLineEdit.Password)
        self.register_password.setClearButtonEnabled(True)
        self.register_btn = QPushButton(self.mainWindow)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(230, 380, 201, 31))
        self.register_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Arial\";\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.again_password = QLineEdit(self.mainWindow)
        self.again_password.setObjectName(u"again_password")
        self.again_password.setGeometry(QRect(230, 324, 201, 31))
        self.again_password.setStyleSheet(u"")
        self.again_password.setEchoMode(QLineEdit.Password)
        self.again_password.setClearButtonEnabled(True)
        self.logo1 = QPushButton(self.mainWindow)
        self.logo1.setObjectName(u"logo1")
        self.logo1.setGeometry(QRect(190, 230, 21, 21))
        self.logo1.setStyleSheet(u"width:30px;\n"
"height:30px;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u":/login_icon/img/\u624b\u673a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo1.setIcon(icon)
        self.logo1.setIconSize(QSize(20, 19))
        self.logo2 = QPushButton(self.mainWindow)
        self.logo2.setObjectName(u"logo2")
        self.logo2.setGeometry(QRect(190, 280, 21, 21))
        self.logo2.setStyleSheet(u"width:30px;\n"
"height:30px;\n"
"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/login_icon/img/\u5bc6\u7801.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo2.setIcon(icon1)
        self.logo2.setIconSize(QSize(20, 20))
        self.logo3 = QPushButton(self.mainWindow)
        self.logo3.setObjectName(u"logo3")
        self.logo3.setGeometry(QRect(190, 324, 21, 21))
        self.logo3.setStyleSheet(u"width:30px;\n"
"height:30px;\n"
"border:none;")
        self.logo3.setIcon(icon1)
        self.logo3.setIconSize(QSize(20, 21))
        self.close_btn = QPushButton(self.mainWindow)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(650, 20, 30, 30))
        self.close_btn.setStyleSheet(u"border:none")
        icon2 = QIcon()
        icon2.addFile(u":/login_icon/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(30, 30))
        self.min_btn = QPushButton(self.mainWindow)
        self.min_btn.setObjectName(u"min_btn")
        self.min_btn.setGeometry(QRect(610, 20, 30, 30))
        self.min_btn.setStyleSheet(u"border:none")
        icon3 = QIcon()
        icon3.addFile(u":/login_icon/img/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon3)
        self.min_btn.setIconSize(QSize(30, 30))
        self.back_btn = QPushButton(self.mainWindow)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(20, 20, 30, 30))
        self.back_btn.setStyleSheet(u"border:none")
        icon4 = QIcon()
        icon4.addFile(u":/login_icon/img/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon4)
        self.back_btn.setIconSize(QSize(30, 30))
        self.logo_name = QLabel(self.mainWindow)
        self.logo_name.setObjectName(u"logo_name")
        self.logo_name.setGeometry(QRect(190, 20, 291, 41))
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.logo_name.setPalette(palette)
        self.logo_name.setStyleSheet(u"font: 20px \"Bauhaus 93\";")
        self.logo_name.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.mainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 280, 191, 21))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:9px;\n"
"")
        self.label_register_avatar = QLabel(self.mainWindow)
        self.label_register_avatar.setObjectName(u"label_register_avatar")
        self.label_register_avatar.setGeometry(QRect(300, 90, 61, 61))
        self.label_register_avatar.setPixmap(QPixmap(u":/login_icon/img/\u5934\u50cf\u52a0\u53f7.png"))
        self.label_register_avatar.setScaledContents(True)
        self.label_register_avatar.setAlignment(Qt.AlignCenter)
        self.register_nickname = QLineEdit(self.mainWindow)
        self.register_nickname.setObjectName(u"register_nickname")
        self.register_nickname.setGeometry(QRect(230, 170, 201, 31))
        self.register_nickname.setStyleSheet(u"")
        self.register_nickname.setClearButtonEnabled(True)
        self.logo1_2 = QPushButton(self.mainWindow)
        self.logo1_2.setObjectName(u"logo1_2")
        self.logo1_2.setGeometry(QRect(190, 170, 21, 31))
        self.logo1_2.setStyleSheet(u"width:30px;\n"
"height:30px;\n"
"border:none;")
        icon5 = QIcon()
        icon5.addFile(u":/login_icon/img/\u6635\u79f0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo1_2.setIcon(icon5)
        self.logo1_2.setIconSize(QSize(20, 19))
        registerWindow.setCentralWidget(self.mainWindow)

        self.retranslateUi(registerWindow)

        QMetaObject.connectSlotsByName(registerWindow)
    # setupUi

    def retranslateUi(self, registerWindow):
        registerWindow.setWindowTitle(QCoreApplication.translate("registerWindow", u"\u6ce8\u518c", None))
        self.register_username.setPlaceholderText(QCoreApplication.translate("registerWindow", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7", None))
        self.register_password.setPlaceholderText(QCoreApplication.translate("registerWindow", u"\u5bc6\u7801", None))
        self.register_btn.setText(QCoreApplication.translate("registerWindow", u"\u6ce8\u518c", None))
        self.again_password.setText("")
        self.again_password.setPlaceholderText(QCoreApplication.translate("registerWindow", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.logo1.setText("")
        self.logo2.setText("")
        self.logo3.setText("")
        self.close_btn.setText("")
        self.min_btn.setText("")
        self.back_btn.setText("")
        self.logo_name.setText(QCoreApplication.translate("registerWindow", u"\u7528\u6237\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("registerWindow", u" \u5bc6\u7801\u8981\u5305\u542b\u7279\u6b8a\u7b26\u53f7\u3001\u82f1\u6587\u5b57\u6bcd\u548c\u6570\u5b57", None))
        self.label_register_avatar.setText("")
        self.register_nickname.setPlaceholderText(QCoreApplication.translate("registerWindow", u"\u8bf7\u8f93\u5165\u6635\u79f0", None))
        self.logo1_2.setText("")
    # retranslateUi

