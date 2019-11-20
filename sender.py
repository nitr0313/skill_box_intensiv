import requests

# response = requests.get('http://127.0.0.1:5000/messages')
auth = False
print("Выберите нужную команду:")
while True:
    print("1 - для регистрации")
    print("2 - для авторизации")
    print("3 - для смены пароля")

    ans = input(">> ")
    username = input("Введите ваш ник >> ")
    password = input("Введите ваш пароль >> ")
    if ans == 1:
        # Регистрация на сервере
        pass
    elif ans == 2:
        # авторизация
        pass
    elif ans == 3:
        new_password = input("Введите ваш НОВЫЙ пароль >> ")
        # сменd пароля
        pass

if auth == True:
    while True:
        text = input("Введите сообщение >> ")
        if text == "/":
            print(
                "Доступные команды:\n/exit - для выхода\n/status - информация о сервере")
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

        response = requests.post(
            'http://127.0.0.1:5000/send',
            json={'username': username, 'password': password, 'text': text}
        )

        if response.status_code == 200:
            jsn = response.json()
            if jsn['ok']:
                print('Server: Message sent')
            elif 'error_message' in jsn:
                print(f'Server: Ошибка отправки: {jsn["error_message"]}')
            else:
                print('Server: Unknown Send Message Error')
        else:
            print('Client: Error sent')
else:
    print('Авторизация не пройдена! ')
