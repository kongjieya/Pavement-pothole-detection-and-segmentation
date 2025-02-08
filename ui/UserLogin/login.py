# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_v2.ui'
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

class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        if not LoginMainWindow.objectName():
            LoginMainWindow.setObjectName(u"LoginMainWindow")
        LoginMainWindow.resize(701, 450)
        self.mainWindow = QWidget(LoginMainWindow)
        self.mainWindow.setObjectName(u"mainWindow")
        self.mainWindow.setStyleSheet(u"QLineEdit{\n"
"	border-radius:5px;\n"
"	border:1px black solid;\n"
"}\n"
"QLineEdit:hover{\n"
"	padding:2px;\n"
"\n"
"}")
        self.logo_name = QLabel(self.mainWindow)
        self.logo_name.setObjectName(u"logo_name")
        self.logo_name.setGeometry(QRect(200, 10, 291, 61))
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
        self.edit_username = QLineEdit(self.mainWindow)
        self.edit_username.setObjectName(u"edit_username")
        self.edit_username.setGeometry(QRect(260, 110, 201, 31))
        self.edit_username.setStyleSheet(u"")
        self.edit_username.setClearButtonEnabled(True)
        self.edit_password = QLineEdit(self.mainWindow)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setGeometry(QRect(260, 170, 201, 31))
        self.edit_password.setStyleSheet(u"")
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.edit_password.setClearButtonEnabled(True)
        self.btn_login = QPushButton(self.mainWindow)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(260, 230, 201, 31))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Arial\";\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.btn_register = QPushButton(self.mainWindow)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(260, 280, 201, 31))
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 11pt \"Arial\";\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        self.close_btn = QPushButton(self.mainWindow)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(650, 20, 30, 30))
        self.close_btn.setStyleSheet(u"border:none")
        icon = QIcon()
        icon.addFile(u":/login_icon/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(30, 30))
        self.min_btn = QPushButton(self.mainWindow)
        self.min_btn.setObjectName(u"min_btn")
        self.min_btn.setGeometry(QRect(610, 20, 30, 30))
        self.min_btn.setStyleSheet(u"border:none")
        icon1 = QIcon()
        icon1.addFile(u":/login_icon/img/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon1)
        self.min_btn.setIconSize(QSize(30, 30))
        self.user_lgo = QPushButton(self.mainWindow)
        self.user_lgo.setObjectName(u"user_lgo")
        self.user_lgo.setGeometry(QRect(220, 113, 21, 31))
        self.user_lgo.setStyleSheet(u"width:30px;\n"
"height:30px;\n"
"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/login_icon/img/\u624b\u673a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_lgo.setIcon(icon2)
        self.user_lgo.setIconSize(QSize(20, 20))
        self.pad_logo = QPushButton(self.mainWindow)
        self.pad_logo.setObjectName(u"pad_logo")
        self.pad_logo.setGeometry(QRect(220, 170, 21, 31))
        self.pad_logo.setStyleSheet(u"width:30px;\n"
"height:30px;\n"
"border:none;")
        icon3 = QIcon()
        icon3.addFile(u":/login_icon/img/\u5bc6\u7801.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pad_logo.setIcon(icon3)
        self.pad_logo.setIconSize(QSize(20, 20))
        LoginMainWindow.setCentralWidget(self.mainWindow)

        self.retranslateUi(LoginMainWindow)

        QMetaObject.connectSlotsByName(LoginMainWindow)
    # setupUi

    def retranslateUi(self, LoginMainWindow):
        LoginMainWindow.setWindowTitle(QCoreApplication.translate("LoginMainWindow", u"\u767b\u5f55", None))
        self.logo_name.setText(QCoreApplication.translate("LoginMainWindow", u"\u7528\u6237\u767b\u5f55", None))
        self.edit_username.setPlaceholderText(QCoreApplication.translate("LoginMainWindow", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7", None))
        self.edit_password.setPlaceholderText(QCoreApplication.translate("LoginMainWindow", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.btn_login.setText(QCoreApplication.translate("LoginMainWindow", u"\u767b\u5f55", None))
        self.btn_register.setText(QCoreApplication.translate("LoginMainWindow", u"\u6ce8\u518c", None))
        self.close_btn.setText("")
        self.min_btn.setText("")
        self.pad_logo.setText("")
    # retranslateUi

