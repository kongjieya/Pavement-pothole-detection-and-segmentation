# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_v7.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 630)
        icon = QIcon()
        icon.addFile(u":/img/icons/kk.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame {\n"
"    border: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setStyleSheet(u"background-color: rgb(83, 91, 99);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_5.setLineWidth(1)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 12, 0)
        self.horizontalSpacer_2 = QSpacerItem(619, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u7ec6\u9ed1"])
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 19px;")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(619, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(11, -1, 3, -1)
        self.min_btn = QPushButton(self.frame_6)
        self.min_btn.setObjectName(u"min_btn")
        self.min_btn.setStyleSheet(u"QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"padding-bottom:5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/img/img/\u6700\u5c0f\u5316.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.min_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.min_btn)

        self.max_btn = QPushButton(self.frame_6)
        self.max_btn.setObjectName(u"max_btn")
        self.max_btn.setStyleSheet(u"QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"padding-bottom:2px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/img/img/\u6700\u5927\u5316.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/img/img/\u8fd8\u539f.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.max_btn.setIcon(icon2)
        self.max_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.max_btn)

        self.close_btn = QPushButton(self.frame_6)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"padding-bottom:5px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/img/img/\u5173\u95ed.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_6.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(14)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(200, 16777215))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy4)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(33, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.label_userAvatar = QLabel(self.frame_8)
        self.label_userAvatar.setObjectName(u"label_userAvatar")
        self.label_userAvatar.setEnabled(True)
        self.label_userAvatar.setMaximumSize(QSize(35, 35))
        self.label_userAvatar.setStyleSheet(u"")
        self.label_userAvatar.setPixmap(QPixmap(u":/img/img/kk.jpg"))
        self.label_userAvatar.setScaledContents(True)
        self.label_userAvatar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_userAvatar)

        self.pushButton_mian_username = QPushButton(self.frame_8)
        self.pushButton_mian_username.setObjectName(u"pushButton_mian_username")
        self.pushButton_mian_username.setMinimumSize(QSize(75, 23))
        self.pushButton_mian_username.setMaximumSize(QSize(160, 23))
        self.pushButton_mian_username.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pushButton_mian_username.setAutoFillBackground(False)
        self.pushButton_mian_username.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border: 0px;\n"
"    font:12px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/img/img/\u5c55\u5f00.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_mian_username.setIcon(icon4)
        self.pushButton_mian_username.setIconSize(QSize(12, 12))
        self.pushButton_mian_username.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_mian_username)

        self.horizontalSpacer_4 = QSpacerItem(32, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"    font:  17px \"\u5fae\u8f6f\u96c5\u9ed1\";  \n"
"\n"
"}\n"
"QPushButton:hover { \n"
"	background:#e6e6e6;\n"
" }\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.index_btn = QPushButton(self.frame_3)
        self.index_btn.setObjectName(u"index_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.index_btn.sizePolicy().hasHeightForWidth())
        self.index_btn.setSizePolicy(sizePolicy6)
        self.index_btn.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setBold(False)
        font1.setItalic(False)
        self.index_btn.setFont(font1)
        self.index_btn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/img/img/\u9996\u9875.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.index_btn.setIcon(icon5)

        self.verticalLayout.addWidget(self.index_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.main_btn = QPushButton(self.frame_3)
        self.main_btn.setObjectName(u"main_btn")
        sizePolicy6.setHeightForWidth(self.main_btn.sizePolicy().hasHeightForWidth())
        self.main_btn.setSizePolicy(sizePolicy6)
        self.main_btn.setMinimumSize(QSize(0, 35))
        icon6 = QIcon()
        icon6.addFile(u":/img/img/YOLO.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.main_btn.setIcon(icon6)
        self.main_btn.setIconSize(QSize(19, 17))

        self.verticalLayout.addWidget(self.main_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.userinfo_btn = QPushButton(self.frame_3)
        self.userinfo_btn.setObjectName(u"userinfo_btn")
        sizePolicy6.setHeightForWidth(self.userinfo_btn.sizePolicy().hasHeightForWidth())
        self.userinfo_btn.setSizePolicy(sizePolicy6)
        self.userinfo_btn.setMinimumSize(QSize(0, 35))
        self.userinfo_btn.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/img/img/\u4e2a\u4eba\u4e2d\u5fc3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.userinfo_btn.setIcon(icon7)
        self.userinfo_btn.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.userinfo_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.exit_btn = QPushButton(self.frame_3)
        self.exit_btn.setObjectName(u"exit_btn")
        sizePolicy6.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy6)
        self.exit_btn.setMinimumSize(QSize(0, 35))
        self.exit_btn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.exit_btn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/img/img/\u9000\u51fa.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_btn.setIcon(icon8)
        self.exit_btn.setIconSize(QSize(14, 14))
        self.exit_btn.setAutoRepeatDelay(300)

        self.verticalLayout.addWidget(self.exit_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(3)
        sizePolicy7.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy7)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(4)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy8)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4.setLineWidth(1)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 210, 582, 123))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(7)
        sizePolicy9.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy9)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_input = QLabel(self.frame_12)
        self.label_input.setObjectName(u"label_input")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_input.sizePolicy().hasHeightForWidth())
        self.label_input.setSizePolicy(sizePolicy10)
        self.label_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1.1px solid gray;\n"
"")
        self.label_input.setLineWidth(1)
        self.label_input.setScaledContents(False)

        self.horizontalLayout_10.addWidget(self.label_input)

        self.label_out = QLabel(self.frame_12)
        self.label_out.setObjectName(u"label_out")
        sizePolicy10.setHeightForWidth(self.label_out.sizePolicy().hasHeightForWidth())
        self.label_out.setSizePolicy(sizePolicy10)
        self.label_out.setStyleSheet(u"border: 1.1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label_out.setLineWidth(1)

        self.horizontalLayout_10.addWidget(self.label_out)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy4.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy4)
        self.frame_13.setMaximumSize(QSize(16777215, 63))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 6)
        self.groupBox = QGroupBox(self.frame_13)
        self.groupBox.setObjectName(u"groupBox")
        font3 = QFont()
        font3.setFamilies([u"\u534e\u6587\u6977\u4f53"])
        font3.setBold(False)
        font3.setItalic(False)
        self.groupBox.setFont(font3)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 1.1px solid gray;\n"
"	font: 16px\n"
"    }")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 16))
        self.progressBar.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Nirmala UI\";\n"
"color: #ffaaff; \n"
"text-align:center; \n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius: 8px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background:rgb(207, 230, 255);\n"
"border-radius: 7px;\n"
"}")
        self.progressBar.setValue(24)

        self.horizontalLayout_11.addWidget(self.progressBar)


        self.horizontalLayout_9.addWidget(self.groupBox)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(4)
        sizePolicy11.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy11)
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.groupBox_3 = QGroupBox(self.frame_14)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font3)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    border: 1.1px solid gray;\n"
"    font: 16px\n"
"    }")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 9, 9, 0)
        self.tableWidget = QTableWidget(self.groupBox_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy12)
        self.tableWidget.setMinimumSize(QSize(0, 121))
        self.tableWidget.setMaximumSize(QSize(16777215, 121))
        self.tableWidget.setFont(font3)
        self.tableWidget.setStyleSheet(u"font: 14px")

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.horizontalLayout_8.addWidget(self.groupBox_3)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setMaximumSize(QSize(16777215, 63))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_openimg = QPushButton(self.frame_11)
        self.pushButton_openimg.setObjectName(u"pushButton_openimg")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy13.setHorizontalStretch(5)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.pushButton_openimg.sizePolicy().hasHeightForWidth())
        self.pushButton_openimg.setSizePolicy(sizePolicy13)
        self.pushButton_openimg.setMaximumSize(QSize(121, 30))
        icon9 = QIcon()
        icon9.addFile(u":/img/img/\u6587\u4ef6.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_openimg.setIcon(icon9)
        self.pushButton_openimg.setAutoRepeatDelay(301)
        self.pushButton_openimg.setAutoRepeatInterval(100)

        self.gridLayout_2.addWidget(self.pushButton_openimg, 0, 0, 1, 1)

        self.pushButton_sht = QPushButton(self.frame_11)
        self.pushButton_sht.setObjectName(u"pushButton_sht")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(5)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.pushButton_sht.sizePolicy().hasHeightForWidth())
        self.pushButton_sht.setSizePolicy(sizePolicy14)
        self.pushButton_sht.setMaximumSize(QSize(101, 30))
        icon10 = QIcon()
        icon10.addFile(u":/img/img/\u6444\u50cf\u5934.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_sht.setIcon(icon10)

        self.gridLayout_2.addWidget(self.pushButton_sht, 0, 1, 1, 1)

        self.pushButton_start_stop = QPushButton(self.frame_11)
        self.pushButton_start_stop.setObjectName(u"pushButton_start_stop")
        sizePolicy12.setHeightForWidth(self.pushButton_start_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_start_stop.setSizePolicy(sizePolicy12)
        self.pushButton_start_stop.setMaximumSize(QSize(101, 30))
        icon11 = QIcon()
        icon11.addFile(u":/img/img/\u8fd0\u884c.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/img/img/\u6682\u505c.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_start_stop.setIcon(icon11)
        self.pushButton_start_stop.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_start_stop, 0, 2, 1, 1)

        self.pushButton_exit = QPushButton(self.frame_11)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy15.setHorizontalStretch(5)
        sizePolicy15.setVerticalStretch(2)
        sizePolicy15.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy15)
        self.pushButton_exit.setMaximumSize(QSize(101, 30))
        icon12 = QIcon()
        icon12.addFile(u":/img/img/\u7ed3\u675f.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_exit.setIcon(icon12)

        self.gridLayout_2.addWidget(self.pushButton_exit, 0, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.gridLayout.addWidget(self.frame_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.frame_15 = QFrame(self.page_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 801, 591))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(0, 0, 801, 591))
        self.frame_17.setStyleSheet(u"QLineEdit{\n"
"border-radius:5px;\n"
"background:#FFFFFF;\n"
"border:1px solid;\n"
"border-color: rgb(104, 164, 253);\n"
"font:  13px;  \n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(104, 164, 253);\n"
"     \n"
"    font: 18px \"Arial Black\";\n"
"    border-radius:10px;\n"
"    \n"
"}\n"
"QPushButton:hover { \n"
"   \n"
"	background-color: rgb(89, 142, 217);  \n"
" }\n"
"\n"
"")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.tabWidget = QTabWidget(self.frame_17)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 9, 801, 561))
        self.tabWidget.setStyleSheet(u"QTabWidget:pane\n"
"{\n"
"	top:10px;\n"
"    border: none;  \n"
"}\n"
"\n"
"QTabBar:tab\n"
"{ \n"
"	background:transparent;\n"
"	border-bottom: 2px solid rgb(240, 240, 240);\n"
"	font-family:\"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size:14px;\n"
"	padding-left:5px;\n"
"	padding-right:5px;\n"
"	min-width: 85px;\n"
"	min-height:30px;		\n"
"}\n"
" \n"
"QTabBar:tab:selected\n"
"{\n"
"	border-bottom: 2px solid rgb(166, 216, 125);\n"
"	color: rgb(166, 216, 125);\n"
"	font-size:15px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QTabBar:tab:hover\n"
"{\n"
"   \n"
"	color: rgb(166, 216, 125);\n"
"\n"
"}")
        self.tab_mainui_PersonalInfo = QWidget()
        self.tab_mainui_PersonalInfo.setObjectName(u"tab_mainui_PersonalInfo")
        self.handleClose_btn = QPushButton(self.tab_mainui_PersonalInfo)
        self.handleClose_btn.setObjectName(u"handleClose_btn")
        self.handleClose_btn.setGeometry(QRect(650, 370, 101, 31))
        self.handleClose_btn.setStyleSheet(u"")
        self.label_avatar = QLabel(self.tab_mainui_PersonalInfo)
        self.label_avatar.setObjectName(u"label_avatar")
        self.label_avatar.setGeometry(QRect(340, 40, 140, 140))
        self.label_avatar.setStyleSheet(u"")
        self.label_avatar.setPixmap(QPixmap(u":/img/img/kk.jpg"))
        self.label_avatar.setScaledContents(True)
        self.label_avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_25 = QLabel(self.tab_mainui_PersonalInfo)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(190, 220, 111, 51))
        self.label_25.setStyleSheet(u"font:  13px; ")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_24 = QLabel(self.tab_mainui_PersonalInfo)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(190, 360, 111, 51))
        self.label_24.setStyleSheet(u"font:  13px; ")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_createTime = QLineEdit(self.tab_mainui_PersonalInfo)
        self.lineEdit_createTime.setObjectName(u"lineEdit_createTime")
        self.lineEdit_createTime.setGeometry(QRect(300, 370, 221, 31))
        self.handleSubmit_btn = QPushButton(self.tab_mainui_PersonalInfo)
        self.handleSubmit_btn.setObjectName(u"handleSubmit_btn")
        self.handleSubmit_btn.setGeometry(QRect(540, 370, 91, 31))
        self.handleSubmit_btn.setStyleSheet(u"")
        self.lineEdit_phone = QLineEdit(self.tab_mainui_PersonalInfo)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setGeometry(QRect(300, 300, 221, 31))
        self.lineEdit_phone.setStyleSheet(u"")
        self.lineEdit_name = QLineEdit(self.tab_mainui_PersonalInfo)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(300, 230, 221, 31))
        self.lineEdit_name.setDragEnabled(False)
        self.lineEdit_name.setReadOnly(False)
        self.lineEdit_name.setClearButtonEnabled(False)
        self.label_26 = QLabel(self.tab_mainui_PersonalInfo)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(190, 290, 111, 51))
        self.label_26.setStyleSheet(u"font:  13px; ")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.tab_mainui_PersonalInfo, "")
        self.tab_mainui_SecurityCenter = QWidget()
        self.tab_mainui_SecurityCenter.setObjectName(u"tab_mainui_SecurityCenter")
        self.label_27 = QLabel(self.tab_mainui_SecurityCenter)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(210, 160, 111, 51))
        self.label_27.setStyleSheet(u"font:  13px; ")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_28 = QLabel(self.tab_mainui_SecurityCenter)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(210, 300, 111, 51))
        self.label_28.setStyleSheet(u"font:  13px; ")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_check_password = QLineEdit(self.tab_mainui_SecurityCenter)
        self.lineEdit_check_password.setObjectName(u"lineEdit_check_password")
        self.lineEdit_check_password.setGeometry(QRect(320, 310, 221, 31))
        self.lineEdit_check_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_check_password.setClearButtonEnabled(True)
        self.handleSubmit_btn_password = QPushButton(self.tab_mainui_SecurityCenter)
        self.handleSubmit_btn_password.setObjectName(u"handleSubmit_btn_password")
        self.handleSubmit_btn_password.setGeometry(QRect(320, 380, 221, 31))
        self.handleSubmit_btn_password.setStyleSheet(u"")
        self.lineEdit_new_password = QLineEdit(self.tab_mainui_SecurityCenter)
        self.lineEdit_new_password.setObjectName(u"lineEdit_new_password")
        self.lineEdit_new_password.setGeometry(QRect(320, 240, 221, 31))
        self.lineEdit_new_password.setStyleSheet(u"")
        self.lineEdit_new_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_new_password.setClearButtonEnabled(True)
        self.lineEdit_old_password = QLineEdit(self.tab_mainui_SecurityCenter)
        self.lineEdit_old_password.setObjectName(u"lineEdit_old_password")
        self.lineEdit_old_password.setGeometry(QRect(320, 170, 221, 31))
        self.lineEdit_old_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_old_password.setDragEnabled(False)
        self.lineEdit_old_password.setReadOnly(False)
        self.lineEdit_old_password.setClearButtonEnabled(True)
        self.label_34 = QLabel(self.tab_mainui_SecurityCenter)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(210, 230, 111, 51))
        self.label_34.setStyleSheet(u"font:  13px; ")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.tab_mainui_SecurityCenter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 90, 81, 42))
        font4 = QFont()
        font4.setFamilies([u"\u534e\u6587\u5f69\u4e91"])
        font4.setBold(True)
        font4.setItalic(False)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"font-size: 19px;")
        self.tabWidget.addTab(self.tab_mainui_SecurityCenter, "")
        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout_4.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6df1\u5ea6\u5b66\u4e60\u68c0\u6d4b\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8eYOLO\u7684\u8def\u9762\u5751\u6d1e\u68c0\u6d4b\u4e0e\u5206\u5272\u7cfb\u7edf", None))
        self.min_btn.setText("")
        self.max_btn.setText("")
        self.close_btn.setText("")
        self.label_userAvatar.setText("")
        self.pushButton_mian_username.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5\u7528\u6237", None))
        self.index_btn.setText(QCoreApplication.translate("MainWindow", u"  \u9996\u9875     ", None))
        self.main_btn.setText(QCoreApplication.translate("MainWindow", u" \u68c0\u6d4b\u7a0b\u5e8f", None))
        self.userinfo_btn.setText(QCoreApplication.translate("MainWindow", u" \u4e2a\u4eba\u4e2d\u5fc3", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u" \u9000\u51fa\u7cfb\u7edf", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\u57fa\u4e8eYOLO\u7684\u8def\u9762\u5751\u6d1e\u68c0\u6d4b\u4e0e\u5206\u5272\u7cfb\u7edf", None))
        self.label_input.setText("")
        self.label_out.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u8fdb\u5ea6", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u68c0\u6d4b\u8fdb\u5ea6\uff1a%p%", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c\u4e0e\u4f4d\u7f6e\u4fe1\u606f", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u522b", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807\u4f4d\u7f6e", None));
        self.pushButton_openimg.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247/\u89c6\u9891\u68c0\u6d4b", None))
        self.pushButton_sht.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u68c0\u6d4b", None))
        self.pushButton_start_stop.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb/\u6682\u505c", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.handleClose_btn.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.label_avatar.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u6635\u79f0\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c\u65f6\u95f4\uff1a", None))
        self.lineEdit_createTime.setPlaceholderText("")
        self.handleSubmit_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.lineEdit_phone.setText("")
        self.lineEdit_phone.setPlaceholderText("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a\u53f7\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mainui_PersonalInfo), QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u65e7\u5bc6\u7801\uff1a", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u5bc6\u7801\uff1a", None))
        self.lineEdit_check_password.setPlaceholderText("")
        self.handleSubmit_btn_password.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a\u4fee\u6539", None))
        self.lineEdit_new_password.setText("")
        self.lineEdit_new_password.setPlaceholderText("")
        self.lineEdit_old_password.setText("")
        self.lineEdit_old_password.setPlaceholderText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5bc6\u7801\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\u4fee\u6539", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mainui_SecurityCenter), QCoreApplication.translate("MainWindow", u"\u5b89\u5168\u4e2d\u5fc3", None))
    # retranslateUi

