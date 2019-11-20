from flask import Flask, request
import time
import datetime

app = Flask(__name__)
messages = [
    {'username': 'John', 'time': time.time(), 'text': 'Hello, MErry!'},
    {'username': 'Merry', 'time': time.time(), 'text': 'Hello, John!'},

]

password_storage = {
    'John': '123',
    'Marry': '321',
}


@app.route("/")
def hello_method():
    return "<h1>Hello, world</h1>"


@app.route("/status")
def hello2_method():
    date = datetime.datetime.now()
    return {
        'status': True,
        'date': date,
        'messages_count': len(messages),
        'users_count': len(password_storage)
    }


@app.route("/server_time")
def server_time_method():
    date = datetime.datetime.now()
    return {
        'date': date,
    }


@app.route("/change_password", methods={'POST'})
def change_password():
    """
    JSON {"username":str,"password":str,"new_password":str}
    username, password, new_password - строки
    :return: {'ok':bool}
    """
    username = request.json['username']
    password = request.json['password']
    new_password = request.json['new_password']

    if not isinstance(username, str) or len(username) == 0 or username not in password_storage:
        return {
            'ok': False,
            'error_message': 'Введите действующий ник для смены пароля'
        }

    if not isinstance(password, str) or len(password) == 0 or password_storage[username] != password:
        return {
            'ok': False,
            'error_message': 'Введите текущий пароль'
        }

    if not isinstance(new_password, str) or len(new_password) == 0 or password_storage[username] == new_password:
        return {
            'ok': False,
            'error_message': 'Введите НОВЫЙ пароль'
        }

    password_storage[username] = new_password
    return {'ok': True, 'message':f'Ваш новый пароль: {new_password}'}


def password_validation(pasw):
    if len(pasw) < 6:
        return False, 'Пароль должен быть длиннее 5 символов'
    if pasw.isdigit() or pasw.isalpha():
        return False, 'В пароле должны быть и буквы и цифры'
    return True, 'Ok'


@app.route("/register", methods={'POST'})
def user_register():
    """
    JSON {"username":str,"password":str}
    username, password - строки
    :return: {'ok':bool}
    """
    username = request.json['username']
    password = request.json['password']

    if not isinstance(username, str) or len(username) == 0 or username in password_storage:
        return {
            'ok': False,
            'error_message': 'Введите уникальный ник для регистрации'
        }

    pasw_valid = password_validation(password)

    if pasw_valid[0]:
        password_storage[username] = password
        return {'ok': True}
    else:
        return {
            'ok': False,
            'error_message': pasw_valid[1]
        }


@app.route("/send", methods={'POST'})
def send_method():
    """
    JSON {"username":str,"password":str,"text":str}
    username, password, text - строки
    :return: {'ok':bool}
    """
    # print(request)
    username = request.json['username']
    password = request.json['password']
    text = request.json['text']

    # Если ник первый раз встречается то добавляем его сразу
    if username not in password_storage:
        password_storage[username] = password

    if not isinstance(username, str) or len(username) == 0:
        return {
            'ok': False,
            'error_message': 'bad username'
        }

    if not isinstance(text, str) or len(text) == 0:
        return {
            'ok': False,
            'error_message': 'bad text',
        }
    # Если ник не соответствует паролю то фиг!
    if password_storage[username] != password:
        return {
            'ok': False,
            'error_message': 'Не верный пароль, смените пользователя или пароль!'
        }

    messages.append(
        {'username': username, 'time': time.time(), 'text': text})

    return {'ok': True}


@app.route("/messages")
def messages_method():
    """
    Param after - Отметка времени после которой нужны сообщения

    :return: {'messages':[
    {'username': str, 'time': str, 'text': str},
    ...
    ]}
    """
    after = float(request.args['after'])
    filtred_messages = [x for x in messages if x['time'] > after]

    return {'messages': filtred_messages}


app.run()
