# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_position_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 381)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(144, 339, 80, 25))
        self.saveButton.setObjectName("saveButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 18, 327, 315))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.firstNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.lblFirstName = QtWidgets.QLabel(self.layoutWidget)
        self.lblFirstName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFirstName.setObjectName("lblFirstName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblFirstName)
        self.lastNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lblLastName = QtWidgets.QLabel(self.layoutWidget)
        self.lblLastName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLastName.setObjectName("lblLastName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblLastName)
        self.currentSalaryLabel = QtWidgets.QLabel(self.layoutWidget)
        self.currentSalaryLabel.setObjectName("currentSalaryLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentSalaryLabel)
        self.lblCurrentSalary = QtWidgets.QLabel(self.layoutWidget)
        self.lblCurrentSalary.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentSalary.setObjectName("lblCurrentSalary")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lblCurrentSalary)
        self.currentPositionLabel = QtWidgets.QLabel(self.layoutWidget)
        self.currentPositionLabel.setObjectName("currentPositionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.currentPositionLabel)
        self.newPositionLabel = QtWidgets.QLabel(self.layoutWidget)
        self.newPositionLabel.setObjectName("newPositionLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.newPositionLabel)
        self.lineEditNewPosition = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditNewPosition.setPlaceholderText("")
        self.lineEditNewPosition.setObjectName("lineEditNewPosition")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditNewPosition)
        self.lblCurrentPosition = QtWidgets.QLabel(self.layoutWidget)
        self.lblCurrentPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentPosition.setObjectName("lblCurrentPosition")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lblCurrentPosition)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.saveButton.setText(_translate("Dialog", "Save"))
        self.firstNameLabel.setText(_translate("Dialog", "First Name"))
        self.lblFirstName.setText(_translate("Dialog", "Peter"))
        self.lastNameLabel.setText(_translate("Dialog", "Last Name"))
        self.lblLastName.setText(_translate("Dialog", "Tan"))
        self.currentSalaryLabel.setText(_translate("Dialog", "Current Salary"))
        self.lblCurrentSalary.setText(_translate("Dialog", "20000"))
        self.currentPositionLabel.setText(_translate("Dialog", "Current Position"))
        self.newPositionLabel.setText(_translate("Dialog", "New Position"))
        self.lblCurrentPosition.setText(_translate("Dialog", "Placeholder Position"))
