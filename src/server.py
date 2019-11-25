from flask import Flask, request
# from peewee import *
from flask_peewee.db import *
import time
import datetime
# from utils import password_validation
import uuid
# from model import User, Message
# import utils



def password_validation(pasw):
    """
    passw - строка
    Проверяется на длинну и наличие цифр и букв
    :return: {'ok':bool}
    """
    if len(pasw) < 6:
        return False, 'Пароль должен быть длиннее 5 символов'
    if pasw.isdigit() or pasw.isalpha():
        return False, 'В пароле должны быть и буквы и цифры'
    return True, 'Ok'


app = Flask(__name__)
DEBUG = True
SECRET_KEY = 'ssshhhh'
# db = Database(app)

DATABASE = {
    'name': 'chat.db',
    'engine': 'peewee.SqliteDatabase',
}

class User(Model):
    name = CharField()
    password_hash = CharField(max_length=15, index=True)
    is_staff = BooleanField(default=False)

    class Meta:
        database = DATABASE  # модель будет использовать базу данных 'people.db'


# import bcrypt
# User.password_hash = bcrypt.hashpw('15072003'.encode('utf-8'), bcrypt.gensalt())
# bcrypt.checkpw('15072003'.encode('utf-8'), b'$2b$12$hBaNrCLZpZrNGQMb9cSjpuonpYyC0w24hcLqbb.3kg.NC.jqOr5si')

class Message(Model):
    username = ForeignKeyField(User, related_name='users', index=True)
    time = DateTimeField(default=datetime.datetime.now)
    body = TextField(index=False)
    destination = CharField(index=True) #  Может принимать направление ALL - для всех или имя пользователя

    class Meta:
        database = DATABASE['name']
        ordering = ('time',)


messages = [
    {'username': 'john', 'time': time.time(), 'text': 'Hello, MErry!', 'destination': 'all'},
    {'username': 'merry', 'time': time.time(), 'text': 'Hello, John!', 'destination': 'all'},
    {'username': 'nitr0', 'time': time.time(), 'text': 'Hello, John!', 'destination': 'all'},

]

# Пока тут будут храниться ключи пользователей которые прошли аунтификацию 'username' : 'secret_key'
key_stor = {

}

password_storage = {
    'john': '123',
    'marry': '321',
    'nitr0': '0147',
}


@app.route("/")
def hello_method():
    return "<h1>Hello, world</h1>"


@app.route("/status")
def hello2_method():
    date = datetime.datetime.now()
    # messages_count = Message.
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
        secret_key = key_generator()
        key_stor[username] = secret_key
        return {'ok': True, 'secret_key':secret_key}
    else:
        return {
            'ok': False,
            'message': 'Такого сочетания логина пароля не найдено'
        }


def key_generator():
    return uuid.uuid4().hex


@app.route("/users_list", methods = {'GET','POST'})
def users_list():
    """
    JSON {"key":str}
    username, password, text - строки
    :return: {'users':list}
    """
    key = request.json['key']
    username = get_by_value(key, key_stor)
    if not username:
        return {
            'ok': False,
            'message': 'Сначала пройдите регистрацию или авторизуйтесь'
        }

    ul = [x for x in key_stor.keys()]
    return {'users_online': ul}


@app.route("/send", methods={'POST'})
def send_method():
    """
    JSON {"username":str,"password":str,"text":str}
    username, password, text - строки
    :return: {'ok':bool}
    """

    key = request.json['key']
    text = request.json['text']
    destination = request.json['destination']
    print(key, text)
    username = get_by_value(key, key_stor)
    if not username:
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

    messages.append(
        {'username': username, 'time': time.time(), 'text': text, "destination":"all"})

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
    key = request.args['key']
    username = get_by_value(key, key_stor)
    if not username:
        return {'None': "Key not found, auth again please"}
    filtred_messages = [x for x in messages if (x['time'] > after) and x['destination'] in ['all', username]]

    return {'messages': filtred_messages, 'online_users':[x for x in key_stor.keys()]}


def get_by_value(value, dt):
    for key, val in dt.items():
        if val == value:
            return key
    return False

if __name__=='__main__':
    app.run()
