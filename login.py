# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 723)
        MainWindow.setStyleSheet("#centralWidget { background: rgba(32, 80, 20, 100); }\n"
"\n"
"#topPanel { background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0, stop:0 rgba(91, 204, 233, 100), stop:1 rgba(32, 80, 96, 100)); }\n"
"\n"
"#loginForm\n"
"{\n"
"  background: rgba(0, 0, 0, 80);\n"
"  border-radius: 8px;\n"
"}\n"
"QLabel { color: white; }\n"
"QLineEdit { border-radius: 3px; }\n"
"\n"
"QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #27a9e3;\n"
"  border-width: 0px;\n"
"  border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover { background-color: #66c011; }\n"
"\n"
"")
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topPanel = QtWidgets.QWidget(parent=self.centralWidget)
        self.topPanel.setObjectName("topPanel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topPanel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currentDateTime = QtWidgets.QLabel(parent=self.topPanel)
        self.currentDateTime.setObjectName("currentDateTime")
        self.horizontalLayout.addWidget(self.currentDateTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.shutdownButton = QtWidgets.QPushButton(parent=self.topPanel)
        self.shutdownButton.setMinimumSize(QtCore.QSize(55, 55))
        self.shutdownButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("arrow-refresh-reload-icon-29.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.shutdownButton.setIcon(icon)
        self.shutdownButton.setIconSize(QtCore.QSize(30, 30))
        self.shutdownButton.setObjectName("shutdownButton")
        self.horizontalLayout.addWidget(self.shutdownButton)
        self.restartButton = QtWidgets.QPushButton(parent=self.topPanel)
        self.restartButton.setMinimumSize(QtCore.QSize(55, 55))
        self.restartButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("av31b71d17623543e4ccf.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.restartButton.setIcon(icon1)
        self.restartButton.setIconSize(QtCore.QSize(50, 50))
        self.restartButton.setObjectName("restartButton")
        self.horizontalLayout.addWidget(self.restartButton)
        self.verticalLayout.addWidget(self.topPanel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(parent=self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(150, 150))
        self.logo.setStyleSheet("border: 1px solid;")
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setOpenExternalLinks(False)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loginForm = QtWidgets.QWidget(parent=self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginForm.sizePolicy().hasHeightForWidth())
        self.loginForm.setSizePolicy(sizePolicy)
        self.loginForm.setMinimumSize(QtCore.QSize(350, 200))
        self.loginForm.setStyleSheet("#loginForm { border: 1px solid; }\n"
"")
        self.loginForm.setObjectName("loginForm")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loginForm)
        self.verticalLayout_2.setContentsMargins(35, 35, 35, 35)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.loginForm)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.loginForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(182, 25))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.loginForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.loginForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(182, 25))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.loginButton = QtWidgets.QPushButton(parent=self.loginForm)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 25))
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        self.horizontalLayout_4.addWidget(self.loginForm)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 24))
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
        self.currentDateTime.setText(_translate("MainWindow", "Monday, 05-03-2023 - 17.52.50."))
        self.label.setText(_translate("MainWindow", "Brugernavn:"))
        self.label_2.setText(_translate("MainWindow", "Adgangskode:"))
        self.loginButton.setText(_translate("MainWindow", "Login"))

# Her starter min kode
        # Connect the login button to a function that checks the username and password
        self.loginButton.clicked.connect(self.handleLogin)

    def handleLogin(self):
        us = self.lineEdit.text()
        pw = self.lineEdit_2.text()
        f = open("Loginbrugernavne.txt", "r")
        # Flag sørger for at funktionen kun kører en gang, og ikke kører for hvert log-in
        flag = False  # set the flag to False initially
        for line in f.readlines():
            us, pw = line.strip().split("|")
            # Check if the username and password are correct
            if self.lineEdit.text() == us and self.lineEdit_2.text() == pw:
                # If the login is successful, launch a new Python file
                subprocess.run(["python", "patientjournal.py"])
                flag = True  # set the flag to True after executing the code inside the if statement
        if not flag:
            #If the login fails, show an error message
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Incorrect username or password.")
            msgBox.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
