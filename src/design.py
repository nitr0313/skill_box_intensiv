# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 543)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 281, 31))
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
        self.loginEdit.setGeometry(QtCore.QRect(10, 80, 211, 20))
        self.loginEdit.setObjectName("loginEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(240, 80, 201, 20))
        self.passwordEdit.setObjectName("passwordEdit")
        self.messagesBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.messagesBrowser.setGeometry(QtCore.QRect(10, 170, 431, 291))
        self.messagesBrowser.setObjectName("messagesBrowser")
        self.messageEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messageEdit.setGeometry(QtCore.QRect(10, 470, 321, 51))
        self.messageEdit.setObjectName("messageEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(360, 470, 75, 51))
        self.sendButton.setObjectName("sendButton")
        self.serverUrlEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.serverUrlEdit.setGeometry(QtCore.QRect(10, 50, 431, 20))
        self.serverUrlEdit.setObjectName("serverUrlEdit")
        self.secretKeyEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.secretKeyEdit.setGeometry(QtCore.QRect(10, 140, 431, 20))
        self.secretKeyEdit.setObjectName("secretKeyEdit")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(10, 110, 211, 23))
        self.loginButton.setObjectName("loginButton")
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logoutButton.setGeometry(QtCore.QRect(240, 110, 201, 23))
        self.logoutButton.setObjectName("logoutButton")
        self.usersList = QtWidgets.QListWidget(self.centralwidget)
        self.usersList.setGeometry(QtCore.QRect(450, 50, 201, 471))
        self.usersList.setObjectName("usersList")
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
        self.secretKeyEdit.setPlaceholderText(_translate("MainWindow", "secretKey"))
        self.loginButton.setText(_translate("MainWindow", "Войти"))
        self.logoutButton.setText(_translate("MainWindow", "Выйти"))
