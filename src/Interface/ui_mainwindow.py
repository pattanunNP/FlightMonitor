# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 642)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("..\Image\shuttle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("border:0;\n"
"background-color:none;")
        MainWindow.setAnimated(True)
        self.drop_shadow_layout = QtWidgets.QWidget(MainWindow)
        self.drop_shadow_layout.setStyleSheet("background-color:none;")
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.drop_shadow_layout)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.drop_shadow = QtWidgets.QFrame(self.drop_shadow_layout)
        self.drop_shadow.setAutoFillBackground(False)
        self.drop_shadow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0149254 rgba(0, 0, 0, 255), stop:0.0248756 rgba(0, 11, 24, 255), stop:1 rgba(0, 73, 141, 255));\n"
"border-radius:10px;")
        self.drop_shadow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drop_shadow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow.setObjectName("drop_shadow")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.drop_shadow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fram = QtWidgets.QFrame(self.frame)
        self.fram.setEnabled(True)
        self.fram.setStyleSheet("background-color:none;")
        self.fram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fram.setObjectName("fram")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.fram)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 921, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Title_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.Title_3.setContentsMargins(10, 10, 10, 10)
        self.Title_3.setObjectName("Title_3")
        self.Name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Name.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 75 20pt \"Roboto\";")
        self.Name.setObjectName("Name")
        self.Title_3.addWidget(self.Name)
        self.SelectComPort = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.SelectComPort.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 69, 111, 255), stop:1 rgba(255, 83, 255, 255));\n"
"padding:5px 5px 5px 5px;\n"
"color:white;\n"
"position: absolute;\n"
"top: 0;\n"
"left: 0;\n"
"width: 100%;\n"
"font: 75 8pt \"Roboto\";")
        self.SelectComPort.setObjectName("SelectComPort")
        self.SelectComPort.addItem("")
        self.SelectComPort.addItem("")
        self.SelectComPort.addItem("")
        self.SelectComPort.addItem("")
        self.SelectComPort.addItem("")
        self.SelectComPort.addItem("")
        self.Title_3.addWidget(self.SelectComPort)
        self.Button = QtWidgets.QHBoxLayout()
        self.Button.setObjectName("Button")
        self.Connect = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Connect.setStyleSheet("QPushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 153, 208, 255), stop:1 rgba(144, 255, 248, 255));\n"
"padding:5px 5px 5px 5px;\n"
"color:white;\n"
"font: 75 8pt \"Roboto\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 153, 208, 255), stop:1 rgba(144, 255, 248, 255));\n"
"padding:5px 5px 5px 5px;\n"
"color:black;\n"
"font: 75 8pt \"Roboto\";\n"
"}")
        self.Connect.setObjectName("Connect")
        self.Button.addWidget(self.Connect)
        self.Title_3.addLayout(self.Button)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.Title_3.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.Title_3.addWidget(self.label_5)
        self.Content = QtWidgets.QFrame(self.fram)
        self.Content.setGeometry(QtCore.QRect(30, 120, 841, 451))
        self.Content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Content)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -40, 961, 611))
        self.stackedWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.stackedWidget.setStyleSheet("color:white;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.page.setObjectName("page")
        self.Temp = QtWidgets.QFrame(self.page)
        self.Temp.setGeometry(QtCore.QRect(20, 110, 250, 250))
        self.Temp.setMaximumSize(QtCore.QSize(250, 250))
        self.Temp.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.Temp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Temp.setObjectName("Temp")
        self.label_2 = QtWidgets.QLabel(self.Temp)
        self.label_2.setGeometry(QtCore.QRect(90, 20, 71, 61))
        self.label_2.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 15pt \"Roboto\";\n"
"border:0px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Temp)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 231, 81))
        self.label_3.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Temp)
        self.label_4.setGeometry(QtCore.QRect(80, 170, 91, 31))
        self.label_4.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_4.setObjectName("label_4")
        self.Humid = QtWidgets.QFrame(self.page)
        self.Humid.setGeometry(QtCore.QRect(300, 110, 250, 250))
        self.Humid.setMaximumSize(QtCore.QSize(250, 250))
        self.Humid.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Humid.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.Humid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Humid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Humid.setObjectName("Humid")
        self.label_8 = QtWidgets.QLabel(self.Humid)
        self.label_8.setGeometry(QtCore.QRect(80, 20, 81, 61))
        self.label_8.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 15pt \"Roboto\";\n"
"border:0px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.Humid)
        self.label_9.setGeometry(QtCore.QRect(40, 80, 231, 81))
        self.label_9.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Humid)
        self.label_10.setGeometry(QtCore.QRect(70, 170, 111, 31))
        self.label_10.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_10.setObjectName("label_10")
        self.Pressure = QtWidgets.QFrame(self.page)
        self.Pressure.setGeometry(QtCore.QRect(580, 110, 250, 250))
        self.Pressure.setMaximumSize(QtCore.QSize(250, 250))
        self.Pressure.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.Pressure.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pressure.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pressure.setObjectName("Pressure")
        self.label_11 = QtWidgets.QLabel(self.Pressure)
        self.label_11.setGeometry(QtCore.QRect(60, 20, 141, 61))
        self.label_11.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 15pt \"Roboto\";\n"
"border:0px;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.Pressure)
        self.label_12.setGeometry(QtCore.QRect(30, 80, 231, 81))
        self.label_12.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Pressure)
        self.label_13.setGeometry(QtCore.QRect(80, 170, 101, 31))
        self.label_13.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_13.setObjectName("label_13")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Heigh = QtWidgets.QFrame(self.page_2)
        self.Heigh.setGeometry(QtCore.QRect(300, 110, 250, 250))
        self.Heigh.setMaximumSize(QtCore.QSize(250, 250))
        self.Heigh.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.Heigh.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Heigh.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Heigh.setObjectName("Heigh")
        self.label_14 = QtWidgets.QLabel(self.Heigh)
        self.label_14.setGeometry(QtCore.QRect(90, 20, 81, 61))
        self.label_14.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 15pt \"Roboto\";\n"
"border:0px;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.Heigh)
        self.label_15.setGeometry(QtCore.QRect(50, 80, 161, 81))
        self.label_15.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Heigh)
        self.label_16.setGeometry(QtCore.QRect(80, 180, 91, 21))
        self.label_16.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.Velocity = QtWidgets.QFrame(self.page_2)
        self.Velocity.setGeometry(QtCore.QRect(21, 110, 250, 250))
        self.Velocity.setMaximumSize(QtCore.QSize(250, 250))
        self.Velocity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Velocity.setAutoFillBackground(False)
        self.Velocity.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.Velocity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Velocity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Velocity.setObjectName("Velocity")
        self.label_17 = QtWidgets.QLabel(self.Velocity)
        self.label_17.setGeometry(QtCore.QRect(70, 20, 151, 61))
        self.label_17.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 15pt \"Roboto\";\n"
"border:0px;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.Velocity)
        self.label_18.setGeometry(QtCore.QRect(30, 80, 231, 81))
        self.label_18.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.Velocity)
        self.label_19.setGeometry(QtCore.QRect(100, 170, 61, 31))
        self.label_19.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.Altitude = QtWidgets.QFrame(self.page_2)
        self.Altitude.setGeometry(QtCore.QRect(581, 110, 250, 250))
        self.Altitude.setMaximumSize(QtCore.QSize(250, 250))
        self.Altitude.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.Altitude.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Altitude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Altitude.setObjectName("Altitude")
        self.label_20 = QtWidgets.QLabel(self.Altitude)
        self.label_20.setGeometry(QtCore.QRect(60, 20, 141, 61))
        self.label_20.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 15pt \"Roboto\";\n"
"border:0px;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Altitude)
        self.label_21.setGeometry(QtCore.QRect(50, 80, 231, 81))
        self.label_21.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.Altitude)
        self.label_22.setGeometry(QtCore.QRect(50, 170, 151, 41))
        self.label_22.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.NO2 = QtWidgets.QFrame(self.page_3)
        self.NO2.setGeometry(QtCore.QRect(20, 110, 250, 250))
        self.NO2.setMaximumSize(QtCore.QSize(250, 250))
        self.NO2.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.NO2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NO2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NO2.setObjectName("NO2")
        self.label_39 = QtWidgets.QLabel(self.NO2)
        self.label_39.setGeometry(QtCore.QRect(80, 20, 81, 61))
        self.label_39.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 25pt \"Roboto\";\n"
"border:0px;")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.NO2)
        self.label_40.setGeometry(QtCore.QRect(90, 80, 81, 81))
        self.label_40.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.NO2)
        self.label_41.setGeometry(QtCore.QRect(90, 170, 61, 31))
        self.label_41.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_41.setObjectName("label_41")
        self.NH3 = QtWidgets.QFrame(self.page_3)
        self.NH3.setGeometry(QtCore.QRect(299, 110, 250, 250))
        self.NH3.setMaximumSize(QtCore.QSize(250, 250))
        self.NH3.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.NH3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NH3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NH3.setObjectName("NH3")
        self.label_42 = QtWidgets.QLabel(self.NH3)
        self.label_42.setGeometry(QtCore.QRect(80, 20, 80, 60))
        self.label_42.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 25pt \"Roboto\";\n"
"border:0px;")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.NH3)
        self.label_43.setGeometry(QtCore.QRect(90, 80, 81, 81))
        self.label_43.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.NH3)
        self.label_44.setGeometry(QtCore.QRect(90, 180, 91, 21))
        self.label_44.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_44.setObjectName("label_44")
        self.CO = QtWidgets.QFrame(self.page_3)
        self.CO.setGeometry(QtCore.QRect(580, 110, 250, 250))
        self.CO.setMaximumSize(QtCore.QSize(250, 250))
        self.CO.setStyleSheet("QFrame{\n"
"border:5px solid rgb(62, 240, 175);\n"
"border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"border:5px solid rgb(154, 134, 255);\n"
"border-radius:125px;\n"
"}")
        self.CO.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CO.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CO.setObjectName("CO")
        self.label_45 = QtWidgets.QLabel(self.CO)
        self.label_45.setGeometry(QtCore.QRect(90, 20, 61, 61))
        self.label_45.setStyleSheet("color:rgb(255, 85, 127);\n"
"font: 75 25pt \"Roboto\";\n"
"border:0px;")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.CO)
        self.label_46.setGeometry(QtCore.QRect(80, 80, 231, 81))
        self.label_46.setStyleSheet("font: 75 30pt \"Roboto\";\n"
"color:white;\n"
"border:0;")
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.CO)
        self.label_47.setGeometry(QtCore.QRect(100, 180, 51, 31))
        self.label_47.setStyleSheet("border:0px;\n"
"color:rgb(255, 255, 255);\n"
"font: 75 15pt \"Roboto\";")
        self.label_47.setObjectName("label_47")
        self.Info_3 = QtWidgets.QFrame(self.page_3)
        self.Info_3.setGeometry(QtCore.QRect(20, 30, 810, 71))
        self.Info_3.setStyleSheet("")
        self.Info_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info_3.setObjectName("Info_3")
        self.stackedWidget.addWidget(self.page_3)
        self.widget = QtWidgets.QWidget(self.fram)
        self.widget.setGeometry(QtCore.QRect(669, 80, 221, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, -61, 141, 141))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("..\Image\back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("..\Image\forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.fram)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.drop_shadow)
        MainWindow.setCentralWidget(self.drop_shadow_layout)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FLIGHT MONITOR 1.0.0"))
        self.Name.setText(_translate("MainWindow", "FLIGHT MONITOR 1.0.0"))
        self.SelectComPort.setItemText(0, _translate("MainWindow", "COM5"))
        self.SelectComPort.setItemText(1, _translate("MainWindow", "COM6"))
        self.SelectComPort.setItemText(2, _translate("MainWindow", "COM7"))
        self.SelectComPort.setItemText(3, _translate("MainWindow", "COM8"))
        self.SelectComPort.setItemText(4, _translate("MainWindow", "COM11"))
        self.SelectComPort.setItemText(5, _translate("MainWindow", "COM13"))
        self.Connect.setText(_translate("MainWindow", "CONNECT"))
        self.label.setText(_translate("MainWindow", "RSSI :"))
        self.label_5.setText(_translate("MainWindow", "-45dB"))
        self.label_2.setText(_translate("MainWindow", "TEMP"))
        self.label_3.setText(_translate("MainWindow", "20.00 C°"))
        self.label_4.setText(_translate("MainWindow", "DHT21"))
        self.label_8.setText(_translate("MainWindow", "HUMID"))
        self.label_9.setText(_translate("MainWindow", "20.00 %"))
        self.label_10.setText(_translate("MainWindow", "BMP280"))
        self.label_11.setText(_translate("MainWindow", "PRESSURE"))
        self.label_12.setText(_translate("MainWindow", "920 hPa"))
        self.label_13.setText(_translate("MainWindow", "BMP280"))
        self.label_14.setText(_translate("MainWindow", "HEIGH"))
        self.label_15.setText(_translate("MainWindow", "100 m"))
        self.label_16.setText(_translate("MainWindow", "Ground"))
        self.label_17.setText(_translate("MainWindow", "VELOCITY"))
        self.label_18.setText(_translate("MainWindow", "20.00"))
        self.label_19.setText(_translate("MainWindow", "m/s"))
        self.label_20.setText(_translate("MainWindow", "ALTITUDE"))
        self.label_21.setText(_translate("MainWindow", "349 m"))
        self.label_22.setText(_translate("MainWindow", "Sea Level"))
        self.label_39.setText(_translate("MainWindow", "NO2"))
        self.label_40.setText(_translate("MainWindow", "10"))
        self.label_41.setText(_translate("MainWindow", "PPM"))
        self.label_42.setText(_translate("MainWindow", "NH3"))
        self.label_43.setText(_translate("MainWindow", "10"))
        self.label_44.setText(_translate("MainWindow", "PPM"))
        self.label_45.setText(_translate("MainWindow", "CO"))
        self.label_46.setText(_translate("MainWindow", "300"))
        self.label_47.setText(_translate("MainWindow", "PPM"))
        self.pushButton_2.setText(_translate("MainWindow", "Back"))
        self.pushButton.setText(_translate("MainWindow", "Next"))


