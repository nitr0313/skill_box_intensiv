import requests
import time
from datetime import datetime

# response = requests.get('http://127.0.0.1:5000/messages')

username = input("Введите ваш ник >> ")
last_received = 0
tab = "\t\t"
while True:
    response = requests.get(
        'http://127.0.0.1:5000/messages',
        params={'after': last_received}
    )

    if response.status_code == 200:
        messages = response.json()['messages']
        for mes in messages:
            print(
                f"{datetime.fromtimestamp(mes['time'])}\t{mes['username'].capitalize() if mes['username'] != username else 'Вы'}")
            print(
                f"{tab if mes['username'] == username else ''} {mes['text']} ")
            print()
            last_received = mes['time']
    else:
        print('Error sent')

    time.sleep(2)
