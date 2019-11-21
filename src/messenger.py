import datetime
import time
import threading

import requests
from PyQt5 import QtWidgets
import design


class MessengerApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.send)
        self.loginButton.clicked.connect(self.login)
        self.logoutButton.clicked.connect(self.login)
        thread = threading.Thread(target=self.receive)
        thread.start()

    key = "_"

    def login(self):
        username = self.loginEdit.text()
        password = self.passwordEdit.text()

        if not username or not password:
            return

        try:
            response = requests.post(
                'http://127.0.0.1:5000/auth',
                json={'username': username, 'password': password}
            )
        except:
            print('Connection error')
            return
        # if response.status_code == 200:

        jsn = response.json()
        msg = jsn.get("message", "")
        if msg:
            self.messagesBrowser.append(msg)
        self.key = jsn.get("secret_key", "")
        if self.key:
            self.secretKeyEdit.setText(self.key)
        return self.key

    def logout(self):
        self.key = "_"
        self.secretKeyEdit.setText("_")

    def send(self):
        if not self.key:
            return (False, "Сначала залогиньтесь")
        text = self.messageEdit.toPlainText()
        if not text:
            return

        try:
            requests.post(
                'http://127.0.0.1:5000/send',
                json={'key': self.key, 'text': text, "destination":'all'}
            )
        except:
            print('Connection error')

        self.messageEdit.setPlainText('')
        self.messageEdit.repaint()


    def receive(self):
        last_received = 0
        print(self.key)

        while True:
            if self.key == "_":
                time.sleep(2)
                continue
            response_user_list = requests.post(
                'http://127.0.0.1:5000/users_list',
                json={'key': self.key}
            )
            ul = ""
            if response_user_list.status_code == 200:
                ul = response_user_list.json().get('users_online', "")
                if ul:
                    self.usersList.clear()
                    self.usersList.addItems(ul)

            response = requests.get(
                'http://127.0.0.1:5000/messages',
                params={'after': last_received, 'key': self.key}
            )
            if response.status_code == 200:
                jsn = response.json()
                print(jsn)
                if 'None' in jsn:
                    self.messagesBrowser.append(jsn['None'])
                    time.sleep(2)
                    continue
                messages = jsn['messages']
                for message in messages:
                    username = message['username']
                    time_1 = datetime.datetime.fromtimestamp(message['time'])
                    time_str = time_1.strftime('%Y-%m-%d %H:%M:%S')
                    text = message['text']

                    self.messagesBrowser.append(f'{username} {time_str}')
                    self.messagesBrowser.append(text)
                    self.messagesBrowser.append('')
                    # self.messagesBrowser.repaint()

                    last_received = message['time']

            time.sleep(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MessengerApp()
    window.show()
    app.exec_()
