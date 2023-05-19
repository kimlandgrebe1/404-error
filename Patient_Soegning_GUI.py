# Form implementation generated from reading ui file 'patientsoegning.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(142, 217, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalFrame = QtWidgets.QFrame(parent=Form)
        self.horizontalFrame.setStyleSheet("background-color: rgb(123, 138, 126);")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(parent=self.horizontalFrame)
        self.label.setStyleSheet("font: 13pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setStyleSheet("background-color: rgb(123, 138, 126);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setStyleSheet("background-color: rgb(123, 138, 126);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Indtast CPR-Nummer"))
        self.pushButton.setText(_translate("Form", "Slå op"))

#Her starter min kode
        # Connect søg patient funktionen to function that opens patientsøgningen
        self.pushButton.clicked.connect(self.patientsoegning)

    def patientsoegning(self):
        import subprocess
        import mysql.connector
        from mysql.connector import errorcode
        db = mysql.connector.connect(user='root',
                                     password='lillemand123',
                                     host='127.0.0.1',
                                     database='mydb')
        try:
            conn = db
            cursor = conn.cursor()
            query = "SELECT CPR FROM Patient"
            cursor.execute(query)
            result_CPR = cursor.fetchall()
            CPRs = [CPR[0].replace("'", "") for CPR in result_CPR]  # looper gennem brugernavnene, fjerner "'" og gemmer dem i usernames variablen
            print(CPRs)
        except Exception as e:
            print(e)

        try:
            conn = db
            cursor = conn.cursor()
            query = "SELECT Multiresistent_status FROM Patient"
            cursor.execute(query)
            result_Multiresistent = cursor.fetchall()
            Multiresistent_final = [str(Multi[0]) for Multi in result_Multiresistent]  # looper gennem brugernavnene, fjerner "'" og gemmer dem i usernames variablen
            print(Multiresistent_final)
        except Exception as e:
            print(e)

        entered_CPR = self.lineEdit.text()
        print(Multiresistent_final)
        print(entered_CPR)

        if any(cpr == entered_CPR and mult == '0' for cpr, mult in zip(CPRs, Multiresistent_final)): #zip() metoden laver tuples af CPRs og Multiresistent_final, hvor der så kan sammenlignes CPR og MR_status
            subprocess.run(["python", "Patient_Journal_GUI.py"])

        elif any(cpr == entered_CPR and mult == '1' for cpr, mult in zip(CPRs, Multiresistent_final)):
            subprocess.run(["python", "patientAlert.py"])

        else:
            # If the login fails, show an error message
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Incorrect CPR-nummer")
            msgBox.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
