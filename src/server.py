from flask import Flask, request
import time
import datetime
from utils import password_validation
# import utils

app = Flask(__name__)
messages = [
    {'username': 'john', 'time': time.time(), 'text': 'Hello, MErry!'},
    {'username': 'merry', 'time': time.time(), 'text': 'Hello, John!'},

]

password_storage = {
    'john': '123',
    'marry': '321',
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
    date = datetime.datetime.now().strftime('%Y.%m.%d %H.%M.%S')
    return {
        'date': date,
    }


@app.route("/change_password", methods={'POST'})
def change_password_method():
    """
    JSON {"username":str,"password":str,"new_password":str}
    username, password, new_password - строки
    :return: {'ok':bool}
    """
    username = request.json['username'].lower()
    password = request.json['password']
    new_password = request.json['new_password']

    if not isinstance(username, str) or len(username) == 0 or username not in password_storage:
        return {
            'ok': False,
            'message': 'Введите действующий ник для смены пароля'
        }

    if not isinstance(password, str) or len(password) == 0 or password_storage[username] != password:
        return {
            'ok': False,
            'message': 'Введите текущий пароль'
        }

    pasw_valid = password_validation(new_password)

    if pasw_valid[0]:
        password_storage[username] = new_password
        return {'ok': True, 'message': f'Ваш новый пароль: {new_password}'}
    else:
        return {
            'ok': False,
            'message': pasw_valid[1]
        }

    return 0


@app.route("/register", methods={'POST'})
def user_register_method():
    """
    JSON {"username":str,"password":str}
    username, password - строки
    :return: {'ok':bool}
    """
    print('register')
    username = request.json['username'].lower()
    password = request.json['password']

    if not isinstance(username, str) or len(username) == 0 or username in password_storage:
        return {
            'ok': False,
            'message': 'Введите уникальный ник для регистрации'
        }

    pasw_valid = password_validation(password)

    if pasw_valid[0]:
        password_storage[username] = password
        return {'ok': True}
    else:
        return {
            'ok': False,
            'message': pasw_valid[1]
        }
    return 0


@app.route("/auth", methods={'POST'})
def user_auth_method():
    """
    JSON {"username":str,"password":str}
    username, password - строки
    :return: {'ok':bool}
    """
    username = request.json['username'].lower()
    password = request.json['password']

    if not isinstance(username, str) or len(username) == 0 or username not in password_storage:
        return {
            'ok': False,
            # Нет такого логина
            'message': 'Такого сочетания логина пароля не найдено'
        }

    if password_storage[username] == password:
        return {'ok': True}
    else:
        return {
            'ok': False,
            'message': 'Такого сочетания логина пароля не найдено'
        }


@app.route("/send", methods={'POST'})
def send_method():
    """
    JSON {"username":str,"password":str,"text":str}
    username, password, text - строки
    :return: {'ok':bool}
    """
    # print(request)
    username = request.json['username'].lower()
    password = request.json['password']
    text = request.json['text']

    # Если ник первый раз встречается то добавляем его сразу
    if username not in password_storage:
        return {
            'ok': False,
            'message': 'Сначала пройдите регистрацию или авторизуйтесь'
        }

    if not isinstance(username, str) or len(username) == 0:
        return {
            'ok': False,
            'message': 'bad username'
        }

    if not isinstance(text, str) or len(text) == 0:
        return {
            'ok': False,
            'message': 'Пустой текст',
        }
    # Если ник не соответствует паролю то фиг!
    if password_storage[username] != password:
        return {
            'ok': False,
            'message': 'Не верный пароль, смените пользователя или пароль!'
        }

    messages.append(
        {'username': username, 'time': time.time(), 'text': text})

    return {'ok': True}


@app.route("/user_messages", methods={"POST"})
def user_messages_method():
    """
    JSON {"username":str}
    Принимает ник и возвращает все сообщения этого пользователя
    :return: {'messages':[
    {'username': str, 'time': str, 'text': str},
    ...
    ]}
    """
    username = request.json['username'].lower()
    filtred_messages = [x for x in messages if x['username'] == username]

    return {'messages': filtred_messages}


@app.route("/messages")
def messages_method():
    """
    Param after - Отметка времени после которой нужны сообщения

    :return: {'messages':[
    {'username': str, 'time': str, 'text': str},
    ...
    ]}
    """
    # TODO Сделать выдачу сообщений только авторизованным рессиверам)
    after = float(request.args['after'])
    filtred_messages = [x for x in messages if x['time'] > after]

    return {'messages': filtred_messages}


if __name__ == '__main__':
    app.run()
