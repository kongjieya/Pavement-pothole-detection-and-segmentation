# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AICS.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import AICS_rc

class Ui_AIMainWindow(object):
    def setupUi(self, AIMainWindow):
        if not AIMainWindow.objectName():
            AIMainWindow.setObjectName(u"AIMainWindow")
        AIMainWindow.resize(842, 572)
        AIMainWindow.setStyleSheet(u"")
        self.centralWidget = QWidget(AIMainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setStyleSheet(u"border: 0px;")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget_out = QListWidget(self.centralWidget)
        self.listWidget_out.setObjectName(u"listWidget_out")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_out.sizePolicy().hasHeightForWidth())
        self.listWidget_out.setSizePolicy(sizePolicy)
        self.listWidget_out.setStyleSheet(u"QListWidget{\n"
"background-color: rgb(255, 255, 255); \n"
"color:rgb(51,51,51); \n"
"border: 0px solid  rgb(247, 247, 247);\n"
"outline:0px;}\n"
"QListWidget::Item{\n"
"background-color:rgb(255, 255, 255);}\n"
"QListWidget::Item:hover{\n"
"background-color: rgb(255, 255, 255); }\n"
"QListWidget::item:selected{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:black;\n"
"    border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"QListWidget::item:selected:!active{\n"
"border: 1px solid  rgb(255, 255, 255); \n"
"background-color: rgb(255, 255, 255); \n"
"color:rgb(51,51,51); } ")
        self.listWidget_out.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget_out.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_out.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget_out.setFlow(QListView.TopToBottom)
        self.listWidget_out.setProperty("isWrapping", False)
        self.listWidget_out.setWordWrap(False)

        self.gridLayout.addWidget(self.listWidget_out, 0, 0, 1, 2)

        self.widget = QWidget(self.centralWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(0, 108))
        self.widget.setMaximumSize(QSize(16777215, 131))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(129, 16, 112, 23)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_input = QTextEdit(self.widget)
        self.textEdit_input.setObjectName(u"textEdit_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(8)
        sizePolicy2.setHeightForWidth(self.textEdit_input.sizePolicy().hasHeightForWidth())
        self.textEdit_input.setSizePolicy(sizePolicy2)
        self.textEdit_input.setMinimumSize(QSize(591, 51))
        self.textEdit_input.setMaximumSize(QSize(599, 51))
        self.textEdit_input.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"        border-top-left-radius: 10px;\n"
"        border-top-right-radius: 10px;")

        self.verticalLayout.addWidget(self.textEdit_input)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(26)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(599, 39))
        self.frame.setMaximumSize(QSize(599, 39))
        self.frame.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"        border-bottom-left-radius: 10px;\n"
"        border-bottom-right-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(547, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_Submit = QPushButton(self.frame)
        self.pushButton_Submit.setObjectName(u"pushButton_Submit")
        self.pushButton_Submit.setMinimumSize(QSize(25, 21))
        self.pushButton_Submit.setMaximumSize(QSize(25, 21))
        self.pushButton_Submit.setStyleSheet(u"border: 0px;")
        icon = QIcon()
        icon.addFile(u":/img/img/up-b-\u5411\u4e0a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Submit.setIcon(icon)
        self.pushButton_Submit.setIconSize(QSize(21, 21))

        self.horizontalLayout_2.addWidget(self.pushButton_Submit)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)

        AIMainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(AIMainWindow)

        QMetaObject.connectSlotsByName(AIMainWindow)
    # setupUi

    def retranslateUi(self, AIMainWindow):
        AIMainWindow.setWindowTitle(QCoreApplication.translate("AIMainWindow", u"MainWindow", None))
        self.textEdit_input.setHtml(QCoreApplication.translate("AIMainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_Submit.setText("")
    # retranslateUi

