import requests
from datetime import datetime

# response = requests.get('http://127.0.0.1:5000/messages')
auth = False
username = ""
password = ""
print("Выберите нужную команду:")

def respons_pars(resp):
    if response.status_code == 200:
        jsn = response.json()
        if jsn['ok']:
            msg = {jsn.get('message', ' ')}
            print(f'Server: Вход разрешен {msg}')
            return True
        elif 'message' in jsn:
            print(f'Server: Ошибка отправки: {jsn["message"]}')
            return False
        else:
            print('Server: Unknown Send Message Error')
            return False
    else:
        print('Client: Error sent')
        return False
    return 0


while True:
    print("1 - для регистрации")
    print("2 - для авторизации")
    print("3 - для смены пароля")
    print("Остальное для выхода")

    ans = input(">> ")
    if ans in ['/exit', '/stop', '/quit']:
        print('Запрос на выход из чата')
        break
    username = input("Введите ваш ник >> ")
    password = input("Введите ваш пароль >> ")
    if ans == '1':
        response = requests.post(
            'http://127.0.0.1:5000/register',
            json={'username': username, 'password': password}
        )
        if respons_pars(response):
            auth=True
            break
    elif ans == '2':
        # авторизация
        response = requests.post(
            'http://127.0.0.1:5000/auth',
            json={'username': username, 'password': password}
        )
        if respons_pars(response):
            auth=True
            break
    elif ans == '3':
        new_password = input("Введите ваш НОВЫЙ пароль >> ")
        # сменd пароля
        response = requests.post(
            'http://127.0.0.1:5000/change_password',
            json={
                'username': username,
                'password': password,
                'new_password': new_password,
                }
        )
        if respons_pars(response):
            auth=True
            password = new_password
            break

if auth == True:
    while True:
        text = input("Введите сообщение >> ")
        if text == "/":
            print(
                "Доступные команды:\n/exit - для выхода\n/status - информация о сервере")
            continue
        if text in ['/exit', '/stop', '/quit']:
            print('Запрос на выход из чата')
            break

        if text == "/status":
            response = requests.get('http://127.0.0.1:5000/status')
            jsn = response.json()
            print(f'Текущее серверное время {jsn["date"]}')
            print(
                f'На сервере зарегистрировано пользователей: {jsn["users_count"]} !')
            print(
                f'За время существования сервера отправлено сообщений: {jsn["messages_count"]} !')
            continue

        if text.startswith("/user"):
            usr = text.split(" ")[1]
            response = requests.post(
                'http://127.0.0.1:5000/user_messages',
                json={
                    'username':usr
                })
            if response.status_code == 200:
                messages = response.json()["messages"]
                for m in messages:
                    print(str(datetime.fromtimestamp(m['time'])))
                    print(m['text'])
            else:
                print(f"Server: {response.status_code}")
            continue


        response = requests.post(
            'http://127.0.0.1:5000/send',
            json={'username': username, 'password': password, 'text': text}
        )

        if response.status_code == 200:
            jsn = response.json()
            if jsn['ok']:
                print('Server: Message sent')
            elif 'error_message' in jsn:
                print(f'Server: Ошибка отправки: {jsn["message"]}')
            else:
                print('Server: Unknown Send Message Error')
        else:
            print('Client: Error sent')
else:
    print('Авторизация не пройдена! ')
