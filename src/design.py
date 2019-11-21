# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 281, 31))
        self.label.setMinimumSize(QtCore.QSize(281, 0))
        self.label.setMaximumSize(QtCore.QSize(281, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loginEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.loginEdit.setGeometry(QtCore.QRect(20, 80, 171, 20))
        self.loginEdit.setObjectName("loginEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(220, 80, 201, 20))
        self.passwordEdit.setObjectName("passwordEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 120, 431, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 470, 321, 51))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(360, 470, 75, 51))
        self.sendButton.setObjectName("sendButton")
        self.serverUrlEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.serverUrlEdit.setGeometry(QtCore.QRect(120, 50, 161, 20))
        self.serverUrlEdit.setObjectName("serverUrlEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Super SkillBOX Chat Client"))
        self.loginEdit.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.sendButton.setText(_translate("MainWindow", "Отправить"))
        self.serverUrlEdit.setPlaceholderText(_translate("MainWindow", "server"))
