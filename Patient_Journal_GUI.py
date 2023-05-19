# Form implementation generated from reading ui file 'patientjournal.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 770)
        MainWindow.setStyleSheet("#topPanel { background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0, stop:0 rgba(91, 204, 233, 100), stop:1 rgba(32, 80, 96, 100)); }\n"
"\n"
"#centralwidget { background: rgba(32, 80, 96, 100); }\n"
"\n"
"QLabel { color: white; }\n"
"QLineEdit { border-radius: 3px; }\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topPanel = QtWidgets.QWidget(parent=self.centralwidget)
        self.topPanel.setObjectName("topPanel")
        self.blabla = QtWidgets.QHBoxLayout(self.topPanel)
        self.blabla.setContentsMargins(0, 0, 0, 0)
        self.blabla.setObjectName("blabla")
        self.currentDateTime = QtWidgets.QLabel(parent=self.topPanel)
        self.currentDateTime.setObjectName("currentDateTime")
        self.blabla.addWidget(self.currentDateTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.blabla.addItem(spacerItem)
        self.refreshButton = QtWidgets.QPushButton(parent=self.topPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy)
        self.refreshButton.setMinimumSize(QtCore.QSize(55, 55))
        self.refreshButton.setStyleSheet("#refreshButton\n"
"{\n"
"  color: white;\n"
"  background-color: #27a9e3;\n"
"  border-width: 0px;\n"
"  border-radius: 3px;\n"
"}\n"
"\n"
"#refreshButton:hover { background-color: #66c011; }")
        self.refreshButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arrow-refresh-reload-icon-29.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.refreshButton.setIcon(icon)
        self.refreshButton.setObjectName("refreshButton")
        self.blabla.addWidget(self.refreshButton)
        self.turnoffButton = QtWidgets.QPushButton(parent=self.topPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turnoffButton.sizePolicy().hasHeightForWidth())
        self.turnoffButton.setSizePolicy(sizePolicy)
        self.turnoffButton.setMinimumSize(QtCore.QSize(55, 55))
        self.turnoffButton.setStyleSheet("#turnoffButton\n"
"{\n"
"  color: white;\n"
"  background-color: #27a9e3;\n"
"  border-width: 0px;\n"
"  border-radius: 3px;\n"
"}\n"
"\n"
"#turnoffButton:hover { background-color: #66c011; }")
        self.turnoffButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("av31b71d17623543e4ccf.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.turnoffButton.setIcon(icon1)
        self.turnoffButton.setIconSize(QtCore.QSize(16, 60))
        self.turnoffButton.setObjectName("turnoffButton")
        self.blabla.addWidget(self.turnoffButton)
        self.verticalLayout.addWidget(self.topPanel)
        self.overallFunctions = QtWidgets.QHBoxLayout()
        self.overallFunctions.setContentsMargins(-1, 0, -1, -1)
        self.overallFunctions.setObjectName("overallFunctions")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.overallFunctions.addWidget(self.pushButton_15)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.overallFunctions.addWidget(self.pushButton_14)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setObjectName("pushButton_8")
        self.overallFunctions.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.overallFunctions.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.overallFunctions.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.overallFunctions.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.overallFunctions.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.overallFunctions.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.overallFunctions)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.patientBooking = QtWidgets.QHBoxLayout()
        self.patientBooking.setContentsMargins(-1, 0, -1, -1)
        self.patientBooking.setObjectName("patientBooking")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(254, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.patientBooking.addWidget(self.frame)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labResult = QtWidgets.QPushButton(parent=self.centralwidget)
        self.labResult.setObjectName("labResult")
        self.horizontalLayout_8.addWidget(self.labResult)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_8.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_8.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_8.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_8.addWidget(self.pushButton_9)
        self.patientBooking.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.patientBooking)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.patientLogo = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patientLogo.sizePolicy().hasHeightForWidth())
        self.patientLogo.setSizePolicy(sizePolicy)
        self.patientLogo.setMinimumSize(QtCore.QSize(254, 190))
        self.patientLogo.setText("")
        self.patientLogo.setScaledContents(False)
        self.patientLogo.setObjectName("patientLogo")
        self.horizontalLayout_4.addWidget(self.patientLogo)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout_4.addWidget(self.calendarWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.patientResistent = QtWidgets.QLabel(parent=self.centralwidget)
        self.patientResistent.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        #self.patientResistent.setStyleSheet("#patientResistent { background: rgb(255, 0, 0)}")
        self.patientResistent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.patientResistent.setObjectName("patientResistent")
        self.verticalLayout.addWidget(self.patientResistent)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(218)
        self.horizontalLayout_5.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_6.addWidget(self.listWidget)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.listWidget_3 = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_3.setObjectName("listWidget_3")
        self.horizontalLayout.addWidget(self.listWidget_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.currentDateTime.setText(_translate("MainWindow", "Monday, 05-03-2023  17.53.53."))
        self.pushButton_15.setText(_translate("MainWindow", "Forside"))
        self.pushButton_14.setText(_translate("MainWindow", "Patientsøgning"))
        self.pushButton_8.setText(_translate("MainWindow", "Ret patientoplysninger"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.labResult.setText(_translate("MainWindow", "Lab-svar"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "Ny konsultation"))
        #self.patientResistent.setText(_translate("MainWindow", "OBS - Patient er diagnosticeret med multiresistent bakterieinfektion"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Navn"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "CPR-nummer"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Køn"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Alder"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patientinformation"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Seneste konsultationer"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "DIagnoser"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

# Her starter min kode
        # Connect søg patient funktionen to a function that opens patientsøgningen
        self.pushButton_14.clicked.connect(self.patientsoegning)
        # Connect søg patient funktionen to a function that opens patientsøgningen
        self.pushButton_8.clicked.connect(self.opretpatient)


    # The function. which opens patientsøgning -function
    def patientsoegning(self):
        import subprocess
        subprocess.run(["python", "Patient_Soegning_GUI.py"])


    # The function. which opens patientsøgning -function
    def opretpatient(self):
            import subprocess
            subprocess.run(["python", "personoplysninger.py"])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())