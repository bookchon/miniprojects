# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\StudyPython\cominfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 325)
        Form.setMaximumSize(QtCore.QSize(400, 350))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 141))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 52, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.lblCore = QtWidgets.QLabel(self.groupBox)
        self.lblCore.setGeometry(QtCore.QRect(100, 52, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.lblCore.setFont(font)
        self.lblCore.setObjectName("lblCore")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 82, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.lblMemory = QtWidgets.QLabel(self.groupBox)
        self.lblMemory.setGeometry(QtCore.QRect(100, 82, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.lblMemory.setFont(font)
        self.lblMemory.setObjectName("lblMemory")
        self.lblDisk = QtWidgets.QLabel(self.groupBox)
        self.lblDisk.setGeometry(QtCore.QRect(100, 112, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.lblDisk.setFont(font)
        self.lblDisk.setObjectName("lblDisk")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 22, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-weight: bold;")
        self.label.setObjectName("label")
        self.lblCPU = QtWidgets.QLabel(self.groupBox)
        self.lblCPU.setGeometry(QtCore.QRect(100, 22, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.lblCPU.setFont(font)
        self.lblCPU.setObjectName("lblCPU")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 112, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 157, 381, 111))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 52, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-weight: bold;")
        self.label_5.setObjectName("label_5")
        self.lblExtraNet = QtWidgets.QLabel(self.groupBox_2)
        self.lblExtraNet.setGeometry(QtCore.QRect(100, 52, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.lblExtraNet.setFont(font)
        self.lblExtraNet.setObjectName("lblExtraNet")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 82, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.lblNetstat = QtWidgets.QLabel(self.groupBox_2)
        self.lblNetstat.setGeometry(QtCore.QRect(100, 82, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.lblNetstat.setFont(font)
        self.lblNetstat.setObjectName("lblNetstat")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 22, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-weight: bold;")
        self.label_7.setObjectName("label_7")
        self.lblinnerNet = QtWidgets.QLabel(self.groupBox_2)
        self.lblinnerNet.setGeometry(QtCore.QRect(100, 22, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.lblinnerNet.setFont(font)
        self.lblinnerNet.setObjectName("lblinnerNet")
        self.btnRefresh = QtWidgets.QPushButton(Form)
        self.btnRefresh.setGeometry(QtCore.QRect(310, 280, 81, 31))
        self.btnRefresh.setObjectName("btnRefresh")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "내 컴퓨터 정보"))
        self.groupBox.setTitle(_translate("Form", "컴퓨터 정보"))
        self.label_2.setText(_translate("Form", "코어"))
        self.lblCore.setText(_translate("Form", "코어"))
        self.label_3.setText(_translate("Form", "메모리"))
        self.lblMemory.setText(_translate("Form", "메모리"))
        self.lblDisk.setText(_translate("Form", "디스크"))
        self.label.setText(_translate("Form", "CPU(속도)"))
        self.lblCPU.setText(_translate("Form", "CPU(속도)"))
        self.label_4.setText(_translate("Form", "디스크"))
        self.groupBox_2.setTitle(_translate("Form", "네트워크 정보"))
        self.label_5.setText(_translate("Form", "외부IP"))
        self.lblExtraNet.setText(_translate("Form", "외부아이피"))
        self.label_6.setText(_translate("Form", "전송상태"))
        self.lblNetstat.setText(_translate("Form", "전송상태"))
        self.label_7.setText(_translate("Form", "내부IP"))
        self.lblinnerNet.setText(_translate("Form", "내부아이피"))
        self.btnRefresh.setText(_translate("Form", "새로고침"))
