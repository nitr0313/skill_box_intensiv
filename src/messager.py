
from PyQt5 import QtWidgets
import design
import requests


class MessengerApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.send)

    def send(self):
        username = self.loginEdit.text()
        password = self.passwordEdit.text()
        text = self.plainTextEdit.toPlainText()
        if not username:
            return
        if not password:
            return
        if not text:
            return
            
        response = requests.post(
            'http://127.0.0.1:5000/send',
            json={'username': username, 'password': password, 'text': text}
        )
        if response.status_code == 200:
            print("good")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MessengerApp()
    window.show()
    app.exec_()
