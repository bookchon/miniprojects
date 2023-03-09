# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\StudyingPyQt\addressbook.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("NanumSquare")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(16, 24, 60, 12))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.txtName = QtWidgets.QLineEdit(self.groupBox)
        self.txtName.setGeometry(QtCore.QRect(80, 20, 281, 20))
        self.txtName.setAcceptDrops(True)
        self.txtName.setToolTipDuration(-1)
        self.txtName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtName.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.txtName.setText("")
        self.txtName.setFrame(False)
        self.txtName.setObjectName("txtName")
        self.txtPhone = QtWidgets.QLineEdit(self.groupBox)
        self.txtPhone.setGeometry(QtCore.QRect(80, 49, 281, 20))
        self.txtPhone.setAcceptDrops(True)
        self.txtPhone.setToolTipDuration(-1)
        self.txtPhone.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtPhone.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.txtPhone.setText("")
        self.txtPhone.setFrame(False)
        self.txtPhone.setObjectName("txtPhone")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(16, 53, 60, 12))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.txtEmail = QtWidgets.QLineEdit(self.groupBox)
        self.txtEmail.setGeometry(QtCore.QRect(80, 79, 281, 20))
        self.txtEmail.setAcceptDrops(True)
        self.txtEmail.setToolTipDuration(-1)
        self.txtEmail.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtEmail.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.txtEmail.setText("")
        self.txtEmail.setFrame(False)
        self.txtEmail.setObjectName("txtEmail")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(16, 83, 60, 12))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(16, 113, 60, 12))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.txtAddress = QtWidgets.QLineEdit(self.groupBox)
        self.txtAddress.setGeometry(QtCore.QRect(80, 109, 281, 20))
        self.txtAddress.setAcceptDrops(True)
        self.txtAddress.setToolTipDuration(-1)
        self.txtAddress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtAddress.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhLatinOnly)
        self.txtAddress.setText("")
        self.txtAddress.setFrame(False)
        self.txtAddress.setObjectName("txtAddress")
        self.btnNew = QtWidgets.QPushButton(self.groupBox)
        self.btnNew.setGeometry(QtCore.QRect(445, 107, 75, 23))
        self.btnNew.setObjectName("btnNew")
        self.btnSave = QtWidgets.QPushButton(self.groupBox)
        self.btnSave.setGeometry(QtCore.QRect(527, 107, 75, 23))
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout.addWidget(self.groupBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 621, 261))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tblAddress = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tblAddress.setObjectName("tblAddress")
        self.tblAddress.setColumnCount(0)
        self.tblAddress.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tblAddress)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.stbCurrent = QtWidgets.QStatusBar(MainWindow)
        self.stbCurrent.setObjectName("stbCurrent")
        MainWindow.setStatusBar(self.stbCurrent)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "정보입력"))
        self.label.setText(_translate("MainWindow", "이       름 :"))
        self.label_2.setText(_translate("MainWindow", "전화번호 :"))
        self.label_3.setText(_translate("MainWindow", "이  메  일 :"))
        self.label_7.setText(_translate("MainWindow", "주       소 :"))
        self.btnNew.setText(_translate("MainWindow", "신규"))
        self.btnSave.setText(_translate("MainWindow", "저장"))
